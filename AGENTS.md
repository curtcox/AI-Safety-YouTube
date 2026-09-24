# Agent guide

Instructions for AI agents (and humans) working in this repository.
Read [README.md](README.md) first for the purpose and layout.

## Goal

Be the definitive starting point for AI safety information on YouTube:
channels, individual videos, and transcripts. Favour accuracy and
completeness of what is included over breadth of what is attempted.

## Data model

- `channels/<name>/collection.json` — **hand-edited** config:
  - `sources`: channel tab or playlist URLs whose videos belong to the collection
  - `playlists`: playlist URLs to show as groupings in the index (optional)
  - `exclude`: `{id, reason}` for off-topic videos (always give a reason)
  - `description_trim_after`: regex; description text from the match onward is dropped (used for patron lists)
  - `scope`: free text, required when the collection is not a whole channel
- `channels/<name>/videos.json` — **generated**. Do not hand-edit.
- `channels/<name>/README.md` — hand-written text is kept; the section between
  `<!-- BEGIN GENERATED INDEX -->` and `<!-- END GENERATED INDEX -->` is regenerated.
- `videos/<id>.md` — **generated**. Front matter values are JSON (valid YAML).
  Hand edits will be overwritten by `--refresh`; put commentary in the collection README.

Front matter fields: `id, title, url, channel, channel_id, channel_url,
upload_date, duration_seconds, is_short, chapters, transcript{source,language},
collections, retrieved`. `transcript.source` is `manual` (human captions),
`auto` (YouTube ASR), or `null` (none available).

## Conventions

- Collection directory names: lowercase channel handle without `@` (e.g. `robertmilesai`).
- Use the script to fetch data; don't paste metadata by hand. If the script
  can't handle a case, improve the script.
- Don't store view/like counts; they change constantly and cause noisy diffs.
- Record any problem you hit while collecting data, and its workaround, in
  [docs/problems-and-solutions.md](docs/problems-and-solutions.md).
- Add new candidate sources to [docs/roadmap.md](docs/roadmap.md) rather than
  collecting them unasked.
- Update the collection table in `README.md` when adding a collection.

## Running the fetcher

```sh
pip install -r requirements.txt
python scripts/fetch_youtube.py channels/<name> [--refresh] [--limit N] [--index-only]
```

- It pauses between videos and retries on HTTP 429. A full run for ~70 videos
  takes ~10 minutes. If it still gets rate limited, wait and re-run: it
  resumes, skipping videos already on disk.
- Exit code 1 means some videos failed; they are listed at the end of the output.
