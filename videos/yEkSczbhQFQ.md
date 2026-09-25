---
id: "yEkSczbhQFQ"
title: "Dumb AIs trained smart AIs to play chess. Here's how that went."
url: "https://www.youtube.com/watch?v=yEkSczbhQFQ"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-03-21"
duration_seconds: 137
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# Dumb AIs trained smart AIs to play chess. Here's how that went.

[Watch on YouTube](https://www.youtube.com/watch?v=yEkSczbhQFQ) · Rational Animations · 2026-03-21 · 2:17

## Description

```text
#aisafety #AIalignment #superintelligence
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] In their paper, OpenAI researchers tested weak-to-strong generalization on three tasks: chess puzzles, natural language processing, and reward modeling. Let's start with the chess puzzles. These involve picking the best moves in a game of chess. To start, they trained a series of models on a flawless solution set to find the best performance they could hope for. They call this the strong ceiling performance. In real life, when we're actually trying to align superintelligences, we won't be able to calculate a strong ceiling performance, which would be the best possible alignment we could hope for. But for the experiment, it's useful as it gives us an ideal to compare the actual performance to. Here are the strong ceiling performance scores on a graph. The x-axis represents how much computing power, or compute for short, has been used to train the strong student. The more compute, the stronger the model.

[0:52] The y-axis represents the scores on the chess puzzles. As you'd expect, the more compute we use to train the model, the better its strong ceiling performance on the chess puzzles. Then, the researchers took the weakest model of the bunch and had it act as the supervisor, guessing the best moves for a new set of positions. They used that not-so-accurate information to train stronger student models. For each trial, we'll call the supervisor's performance the weak performance and the student's performance the weak-to-strong performance, since it's the result of a weak model supervising a stronger one. Here are the scores for all the stronger models when trained by the weakest one. You can see that with this weak supervisor, stronger students are only able to learn a little better than weaker ones, and even that quickly plateaus. Even very strong students are barely learning any better than weak ones if they're all learning from the same weak supervisor. To continue the experiment, the researchers tried again with progressively stronger supervisors, which we can plot as more lines on the graph.

[1:52] The lines start further and further to the right because each supervisor model only gets paired with student models stronger than itself. For each supervisor, we see the same pattern from before. Students that are slightly stronger than their supervisors can outperform them. But the gain stop as soon as the gap between supervisor and student gets too large.
