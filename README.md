# AI Safety on YouTube

A curated, machine-readable starting point for AI safety content on YouTube:
**channels**, **individual videos**, and **transcripts** where available.

Everything here is plain Markdown and JSON so it is easy to browse on GitHub,
grep locally, or feed to an AI agent.

## Collections

| Collection | Scope | Videos | Transcripts |
|---|---|---|---|
| [Robert Miles AI Safety](channels/robertmilesai/) | Full channel | 46 videos + 27 shorts | 72/73 (41 human, 31 auto) |
| [Computerphile](channels/computerphile/) | Partial: Robert Miles's AI episodes only | 23 (+1 pending) | 23/23 (14 human, 9 auto) |

_Counts as of 2026-09-24; each collection's `videos.json` is authoritative._

Candidate channels not yet collected are tracked in [docs/roadmap.md](docs/roadmap.md).

## Repository layout

```
README.md                  this file: purpose, layout, collection list
AGENTS.md                  instructions for AI agents (and humans) working in the repo
CLAUDE.md                  pointer to AGENTS.md
channels/<name>/
  collection.json          hand-edited: sources to crawl, excluded ids, options
  videos.json              generated: metadata manifest for every video
  README.md                hand-written notes + generated index of videos
videos/<youtube-id>.md     one file per video: front matter, description, transcript
scripts/fetch_youtube.py   fetches metadata + captions and regenerates indexes
docs/
  problems-and-solutions.md  issues hit while collecting data, and fixes
  roadmap.md                 channels and videos to add next
requirements.txt           Python dependencies (yt-dlp)
```

Video files are keyed by YouTube id and shared across collections, so a video
that appears in two collections exists once (its `collections` field lists both).

## Finding things

- **Browse:** open a collection's `README.md` for a dated table of videos and playlists.
- **Search transcripts:** `grep -ril "mesa-optimi" videos/`
- **Query metadata:** `jq '.videos[] | select(.transcript.source=="manual") | .title' channels/*/videos.json`
- **Watch at a moment:** transcript paragraphs start with `[m:ss]`; append `&t=<seconds>` to the video URL.

## Updating / adding data

```sh
pip install -r requirements.txt
python scripts/fetch_youtube.py channels/robertmilesai        # fetch new videos only
python scripts/fetch_youtube.py channels/robertmilesai --refresh
```

To add a channel, create `channels/<name>/collection.json` (copy an existing
one) and run the script. See [AGENTS.md](AGENTS.md) for conventions.

## Transcripts and copyright

Transcripts are YouTube captions (human-made where the creator uploaded them,
otherwise YouTube's auto-generated ones), included for search and research.
All video content and transcripts remain the property of their creators.
If you are a creator and want your transcripts removed, open an issue.
