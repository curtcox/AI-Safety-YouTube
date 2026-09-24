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
- **Cost:** about 10s per video (~12 minutes for the 73-video channel).

### "Sign in to confirm you're not a bot"
- **Problem:** On the first full run, 6 of 73 videos failed metadata
  extraction with YouTube's bot check (the run was from a cloud/datacenter IP).
  The failures were scattered, not a hard block.
- **Solution:** The bot check is now treated like a 429 (backoff + retry),
  and the script is resumable. Re-running fetched all 6 on the first try.
  If it becomes persistent, yt-dlp supports `--cookies` from a logged-in
  browser; we have avoided that so the pipeline needs no account.
- **Unresolved (Computerphile collection):** `_8yVOC4ciXc` (*GPT3: An Even
  Bigger Language Model*) was blocked on every attempt, including 4 backoff
  retries and a second run. Workarounds tried:
  - yt-dlp `player_client=mweb` / `web_safari`: gets past the bot check and
    returns metadata, but no caption tracks at all.
  - `player_client=tv`: "The page needs to be reloaded". `android_vr`: same bot check.
  - `youtube-transcript-api`: "YouTube is blocking requests from your IP"
    (cloud-provider IP).
  **Next step:** re-run `python scripts/fetch_youtube.py channels/computerphile`
  from a residential IP; it will fetch only the missing video.

### Shorts misclassified
- **Problem:** Full video metadata doesn't say whether a video is a Short, and
  Shorts can be up to 3 minutes, so a duration cutoff misfiled ~10 as videos.
- **Solution:** Classify by source: a video is a Short if the channel's
  `/shorts` tab lists it (its flat-listing URL contains `/shorts/`).

### Noisy descriptions
- **Problem:** Descriptions end with long Patreon supporter lists that add
  nothing for research and churn on every refresh. The wording varies
  ("Thanks to my wonderful patrons", "With thanks to my excellent Patreon
  supporters", "Thanks again to all my wonderful Patreon Supporters", …).
- **Solution:** Per-collection `description_trim_after` regex in
  `collection.json` cuts the description at the patron-thanks line.
  Check new collections with `grep -il patreon videos/*.md | xargs grep -L "trimmed by"`.

### Missing captions
- **Problem:** 1 of 73 channel videos (a Short of a street march, `4t6Pzs8z280`)
  has no English captions at all.
- **Solution:** None needed; recorded as `transcript: null` and marked ✘ in the index.

### Playlists that span channels
- **Problem:** The "Concrete Problems in AI Safety" playlist includes a
  Computerphile video, which isn't part of the channel collection.
- **Solution:** Playlist listings link to any video present in `videos/`,
  regardless of which collection fetched it.

### Channel name has trailing whitespace
- **Problem:** YouTube returns `"Robert Miles AI Safety "`.
- **Solution:** Stripped in the script.

### Rob Miles content on other channels
- **Problem:** Many of his best-known videos are on Computerphile, not his channel.
- **Solution:** A separate partial collection (`channels/computerphile`) sourced
  from the "Computerphile Videos" playlist on his channel, excluding four
  non-AI episodes. The playlist appears to end around 2020 — see roadmap.
