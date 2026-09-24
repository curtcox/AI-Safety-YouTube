#!/usr/bin/env python3
"""Fetch YouTube video metadata and transcripts into this repository.

A *collection* is a directory (e.g. channels/robertmilesai) holding:
  - collection.json  : sources to crawl + excluded ids (hand-edited config)
  - videos.json      : generated manifest of every video in the collection
  - README.md        : hand-written notes + a generated index between markers

Per-video files are shared by all collections and live at videos/<id>.md
(front matter + description + transcript).

Usage:
  python scripts/fetch_youtube.py channels/robertmilesai            # fetch new videos
  python scripts/fetch_youtube.py channels/robertmilesai --refresh  # re-fetch everything
  python scripts/fetch_youtube.py channels/robertmilesai --index-only

See docs/problems-and-solutions.md for rate-limit and caption notes.
"""

import argparse
import datetime
import json
import os
import pathlib
import re
import sys
import time
import urllib.error

import yt_dlp

ROOT = pathlib.Path(__file__).resolve().parent.parent
VIDEOS_DIR = ROOT / "videos"
INDEX_BEGIN = "<!-- BEGIN GENERATED INDEX -->"
INDEX_END = "<!-- END GENERATED INDEX -->"

# Preferred caption tracks, best first. Manual (human-made) captions beat
# auto-generated ones; "en-orig" is the untranslated auto track.
MANUAL_LANGS = ["en-GB", "en", "en-US", "en-CA", "en-AU"]
AUTO_LANGS = ["en-orig", "en"]

PAUSE_BETWEEN_VIDEOS = 4  # seconds; YouTube returns 429s quickly without this
RETRY_DELAYS = [30, 60, 120, 240]
# Transient blocks worth backing off and retrying.
RETRYABLE = ("429", "Too Many Requests", "confirm you’re not a bot", "confirm you're not a bot")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def ydl_opts(flat=False):
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "sleep_interval_requests": 1,
    }
    if flat:
        opts["extract_flat"] = "in_playlist"
    return opts


def with_retries(fn, what):
    for attempt, delay in enumerate([0] + RETRY_DELAYS):
        if delay:
            log(f"  retry {attempt} for {what} in {delay}s")
            time.sleep(delay)
        try:
            return fn()
        except (yt_dlp.utils.DownloadError, urllib.error.HTTPError) as e:
            msg = str(e)
            if not any(r in msg for r in RETRYABLE):
                raise
            log(f"  blocked: {msg[:120]}")
    raise RuntimeError(f"giving up on {what} after repeated 429s / bot checks")


def list_source(url):
    """Return (playlist_info, [entries]) for a channel tab or playlist URL."""
    with yt_dlp.YoutubeDL(ydl_opts(flat=True)) as ydl:
        info = with_retries(lambda: ydl.extract_info(url, download=False), url)
    return info, [e for e in info.get("entries") or [] if e and e.get("id")]


def pick_track(info):
    """Return (kind, lang, url) of the best English json3 caption track."""
    for kind, langs, tracks in (
        ("manual", MANUAL_LANGS, info.get("subtitles") or {}),
        ("auto", AUTO_LANGS, info.get("automatic_captions") or {}),
    ):
        for lang in langs:
            for fmt in tracks.get(lang, []):
                if fmt.get("ext") == "json3":
                    return kind, lang, fmt["url"]
    return None


def parse_json3(raw):
    """Convert YouTube json3 captions to [(start_seconds, text)]."""
    segments = []
    for ev in json.loads(raw).get("events", []):
        if "segs" not in ev:
            continue
        text = "".join(s.get("utf8", "") for s in ev["segs"])
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            segments.append((ev.get("tStartMs", 0) / 1000, text))
    return segments


def fmt_ts(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def paragraphs(segments, chapters):
    """Group caption segments into timestamped paragraphs, split at chapters."""
    chapter_starts = sorted((c["start_time"], c["title"]) for c in chapters or [])
    out, para, para_start = [], [], None

    def flush():
        if para:
            out.append(f"[{fmt_ts(para_start)}] " + " ".join(para))
            para.clear()

    for start, text in segments:
        while chapter_starts and start >= chapter_starts[0][0]:
            flush()
            out.append(f"### {chapter_starts.pop(0)[1]}")
        if para_start is None or not para:
            para_start = start
        para.append(text)
        elapsed = start - para_start
        if (elapsed >= 45 and text[-1:] in ".?!") or elapsed >= 90:
            flush()
    flush()
    return out


def fetch_video(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    with yt_dlp.YoutubeDL(ydl_opts()) as ydl:
        info = with_retries(lambda: ydl.extract_info(url, download=False), video_id)
        track = pick_track(info)
        segments = []
        if track:
            raw = with_retries(
                lambda: ydl.urlopen(track[2]).read().decode("utf-8"),
                f"{video_id} captions",
            )
            segments = parse_json3(raw)
    return info, track, segments


def meta_from_info(info, track, collection, is_short):
    d = info.get("upload_date") or ""
    return {
        "id": info["id"],
        "title": info.get("title"),
        "url": f"https://www.youtube.com/watch?v={info['id']}",
        "channel": (info.get("channel") or "").strip(),
        "channel_id": info.get("channel_id"),
        "channel_url": info.get("channel_url"),
        "upload_date": f"{d[:4]}-{d[4:6]}-{d[6:]}" if len(d) == 8 else None,
        "duration_seconds": info.get("duration"),
        "is_short": is_short,
        "chapters": len(info.get("chapters") or []),
        "transcript": {"source": track[0], "language": track[1]} if track else None,
        "collections": [collection],
        "retrieved": datetime.date.today().isoformat(),
    }


def write_video_file(meta, info, segments, trim_after=None):
    VIDEOS_DIR.mkdir(exist_ok=True)
    path = VIDEOS_DIR / f"{meta['id']}.md"
    # Keep collection memberships from other collections that share this video.
    if path.exists():
        old = read_front_matter(path)
        meta["collections"] = sorted(set(old.get("collections", [])) | set(meta["collections"]))
    lines = ["---"]
    for k, v in meta.items():
        lines.append(f"{k}: {json.dumps(v, ensure_ascii=False)}")
    lines += ["---", "", f"# {meta['title']}", ""]
    dur = fmt_ts(meta["duration_seconds"] or 0)
    lines.append(
        f"[Watch on YouTube]({meta['url']}) · {meta['channel']} · "
        f"{meta['upload_date']} · {dur}"
    )
    if info.get("chapters"):
        lines += ["", "## Chapters", ""]
        lines += [f"- {fmt_ts(c['start_time'])} {c['title']}" for c in info["chapters"]]
    desc = (info.get("description") or "").strip()
    if trim_after:  # e.g. drop long patron lists; see collection.json
        m = re.search(trim_after, desc)
        if m:
            desc = desc[: m.start()].rstrip() + "\n\n[... trimmed by fetch_youtube.py]"
    if desc:
        lines += ["", "## Description", "", "```text", desc.replace("```", "'''"), "```"]
    lines += ["", "## Transcript", ""]
    t = meta["transcript"]
    if t:
        note = "human-made captions" if t["source"] == "manual" else "YouTube auto-generated captions"
        lines += [f"_Source: {note} ({t['language']}). Timestamps are [m:ss] from the start of the video._", ""]
        for p in paragraphs(segments, info.get("chapters")):
            lines += [p, ""]
    else:
        lines += ["_No English captions were available when this was retrieved._", ""]
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def read_front_matter(path):
    meta, text = {}, path.read_text(encoding="utf-8").split("\n")
    if text[0] != "---":
        return meta
    for line in text[1:]:
        if line == "---":
            break
        k, _, v = line.partition(": ")
        meta[k] = json.loads(v)
    return meta


def build_index(coll_dir, manifest):
    by_id = {v["id"]: v for v in manifest["videos"]}
    to_videos = os.path.relpath(VIDEOS_DIR, coll_dir)

    def link(v):
        return f"{to_videos}/{v['id']}.md"

    def row(v):
        dur = fmt_ts(v["duration_seconds"] or 0)
        t = v["transcript"]
        tx = {"manual": "✔ human", "auto": "✔ auto"}.get(t and t["source"], "✘")
        return f"| {v['upload_date']} | [{v['title'].replace('|', '/')}]({v['url']}) | {dur} | [{tx}]({link(v)}) |"

    head = ["| Date | Title | Length | Transcript |", "|---|---|---|---|"]
    out = [INDEX_BEGIN, "", "_Generated by `scripts/fetch_youtube.py`; edit above or below the markers._", ""]
    for section, vids in (
        ("Videos", [v for v in manifest["videos"] if not v["is_short"]]),
        ("Shorts", [v for v in manifest["videos"] if v["is_short"]]),
    ):
        if not vids:
            continue
        out += [f"## {section} ({len(vids)})", "", *head]
        out += [row(v) for v in sorted(vids, key=lambda v: v["upload_date"] or "", reverse=True)]
        out.append("")
    for pl in manifest.get("playlists", []):
        # Playlists may include videos from other channels/collections.
        vids = [by_id.get(i) or read_front_matter(VIDEOS_DIR / f"{i}.md")
                for i in pl["video_ids"] if i in by_id or (VIDEOS_DIR / f"{i}.md").exists()]
        if not vids:
            continue
        out += [f"### Playlist: [{pl['title']}](https://www.youtube.com/playlist?list={pl['id']}) ({len(vids)})", ""]
        out += [f"{n}. [{v['title']}]({link(v)})" for n, v in enumerate(vids, 1)]
        out.append("")
    out.append(INDEX_END)

    readme = coll_dir / "README.md"
    text = readme.read_text(encoding="utf-8") if readme.exists() else f"# {coll_dir.name}\n\n{INDEX_BEGIN}\n{INDEX_END}\n"
    if INDEX_BEGIN not in text:
        text = text.rstrip() + f"\n\n{INDEX_BEGIN}\n{INDEX_END}\n"
    pre, _, rest = text.partition(INDEX_BEGIN)
    _, _, post = rest.partition(INDEX_END)
    readme.write_text(pre + "\n".join(out) + post, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("collection", help="collection directory containing collection.json")
    ap.add_argument("--refresh", action="store_true", help="re-fetch videos already on disk")
    ap.add_argument("--index-only", action="store_true", help="only rebuild README index from videos.json")
    ap.add_argument("--limit", type=int, help="fetch at most N new videos this run")
    args = ap.parse_args()

    coll_dir = (ROOT / args.collection).resolve()
    coll_name = coll_dir.relative_to(ROOT).as_posix()
    config = json.loads((coll_dir / "collection.json").read_text())
    manifest_path = coll_dir / "videos.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"videos": []}

    if args.index_only:
        build_index(coll_dir, manifest)
        return

    excluded = {e["id"] for e in config.get("exclude", [])}
    ids, playlists, short_ids = [], [], set()
    for src in config["sources"]:
        log(f"listing {src['url']}")
        info, entries = list_source(src["url"])
        src_ids = [e["id"] for e in entries if e["id"] not in excluded]
        ids += [i for i in src_ids if i not in ids]
        short_ids |= {e["id"] for e in entries if "/shorts/" in (e.get("url") or "")}
        if src.get("as_playlist"):
            playlists.append({"id": info["id"], "title": info.get("title"), "video_ids": src_ids})
    for pl_url in config.get("playlists", []):
        info, entries = list_source(pl_url)
        playlists.append({
            "id": info["id"], "title": info.get("title"),
            "video_ids": [e["id"] for e in entries if e["id"] not in excluded],
        })

    known = {v["id"]: v for v in manifest["videos"]}
    for vid, v in known.items():  # reclassify without re-fetching
        v["is_short"] = vid in short_ids
        path = VIDEOS_DIR / f"{vid}.md"
        if path.exists():
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"^is_short: \w+$", f"is_short: {json.dumps(v['is_short'])}", text, count=1, flags=re.M)
            path.write_text(text, encoding="utf-8")
    todo = [i for i in ids if args.refresh or i not in known or not (VIDEOS_DIR / f"{i}.md").exists()]
    if args.limit:
        todo = todo[: args.limit]
    log(f"{len(ids)} videos in sources, {len(todo)} to fetch")

    failures = []
    for n, vid in enumerate(todo, 1):
        log(f"[{n}/{len(todo)}] {vid}")
        try:
            info, track, segments = fetch_video(vid)
        except Exception as e:  # keep going; record and report at the end
            log(f"  FAILED: {e}")
            failures.append((vid, str(e)[:200]))
            continue
        meta = meta_from_info(info, track, coll_name, vid in short_ids)
        write_video_file(meta, info, segments, config.get("description_trim_after"))
        known[vid] = {k: v for k, v in meta.items() if k != "collections"}
        manifest["videos"] = [known[i] for i in ids if i in known]
        manifest["playlists"] = playlists
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        time.sleep(PAUSE_BETWEEN_VIDEOS)

    manifest["videos"] = [known[i] for i in ids if i in known]
    manifest["playlists"] = playlists
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    build_index(coll_dir, manifest)
    if failures:
        log("failures:")
        for vid, err in failures:
            log(f"  {vid}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
