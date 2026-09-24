# Problems and solutions

A log of issues hit while collecting data, and how they were handled.
Add to this whenever something goes wrong or needs a workaround.

## Collecting the Robert Miles channel (2026-09-24)

### Tooling: no YouTube API key
- **Problem:** The YouTube Data API needs a key and quota; captions via the
  official API need OAuth as the channel owner.
- **Solution:** Use [yt-dlp](https://github.com/yt-dlp/yt-dlp), which reads
  public pages. Pinned in `requirements.txt`. yt-dlp must be kept current;
  YouTube changes break older versions.

### Listing a channel
- **Problem:** A channel's content is split across tabs; `/videos` omits Shorts.
  `/streams` errors when the channel has none.
- **Solution:** `collection.json` lists each tab explicitly (`/videos`, `/shorts`).
  Flat listing (`extract_flat`) is one request per tab and doesn't hit limits.

### Caption formats
- **Problem:** Auto-generated captions in VTT format repeat every line 2–3
  times (rolling "karaoke" cues), and contain inline word timing tags.
- **Solution:** Download the `json3` caption format instead and join each
  event's segments. This gives clean text for both human and auto captions.

### Choosing a caption track
- **Problem:** Videos list dozens of tracks: human captions (`en-GB` on this
  channel), auto captions (`en-orig`), and machine translations of both
  (e.g. `en` auto-translated). Requesting several tracks per video triggered
  `HTTP 429 Too Many Requests` on the second track.
- **Solution:** Pick exactly one track per video: human English first
  (`en-GB`, `en`, `en-US`, …), else auto `en-orig`, and fetch only that.
  The source is recorded in front matter (`transcript.source`: `manual`/`auto`).

### Rate limiting (HTTP 429)
- **Problem:** Rapid requests get 429s.
- **Solution:** `sleep_interval_requests=1`, a pause between videos, and
  exponential backoff retries (30s → 240s) on 429. Runs are resumable: videos
  already in `videos/` are skipped unless `--refresh`.
- **Cost:** a full run takes roughly 20–30s per video.

### "Sign in to confirm you're not a bot"
- **Problem:** Partway through the run, some videos fail metadata extraction
  with YouTube's bot check (seen on cloud/datacenter IPs).
- **Solution:** _in progress — see below._

### Noisy descriptions
- **Problem:** Descriptions end with long Patreon supporter lists that add
  nothing for research and churn on every refresh.
- **Solution:** Per-collection `description_trim_after` regex in
  `collection.json` cuts the description at the patron-thanks line.

### Channel name has trailing whitespace
- **Problem:** YouTube returns `"Robert Miles AI Safety "`.
- **Solution:** Stripped in the script.

### Rob Miles content on other channels
- **Problem:** Many of his best-known videos are on Computerphile, not his channel.
- **Solution:** A separate partial collection (`channels/computerphile`) sourced
  from the "Computerphile Videos" playlist on his channel, excluding four
  non-AI episodes. The playlist appears to end around 2020 — see roadmap.
