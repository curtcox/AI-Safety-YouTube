---
id: "moNzt_KhHf0"
title: "AIs that teach other AIs that teach other AIs..."
url: "https://www.youtube.com/watch?v=moNzt_KhHf0"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-03-28"
duration_seconds: 82
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# AIs that teach other AIs that teach other AIs...

[Watch on YouTube](https://www.youtube.com/watch?v=moNzt_KhHf0) · Rational Animations · 2026-03-28 · 1:22

## Description

```text
#aisafety #AIalignment #superintelligence
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] For chess puzzles, we can use a method called bootstrapping. Instead of directly having the weakest supervisor train the stronger students, the weak supervisor trains a model just a little more capable than itself, which trains a yet more capable model, and so on, until the chain reaches a final student much stronger than the original supervisor. Let's graph the chess puzzle performance with bootstrapping. This graph works like the previous ones, but the dotted lines show the results from before without bootstrapping. You can see how students aren't able to improve much when the student-supervisor gap is too big. Whereas, the solid lines represent a bootstrap setup, and you can see they keep going upward despite the growing gap in capabilities between weak supervisor and strong student. For natural language processing, we don't need bootstrapping, as stronger students are still able to learn relatively well from weak supervisors.

[0:52] But there's another technique that can help. In this case, scientists let the student AI pay less attention to the supervisor's answers when it thinks they don't make sense. When the student and supervisor have similar abilities, this actually impedes the student's performance, as it sometimes ignores good guidance. But giving a very strong student the ability to doubt a much weaker supervisor gives significant benefits.
