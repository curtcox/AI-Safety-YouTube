---
id: "Axd-rbL6G-4"
title: "How a deceptively aligned AI looks perfectly fine until it takes over"
url: "https://www.youtube.com/watch?v=Axd-rbL6G-4"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-06-03"
duration_seconds: 140
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# How a deceptively aligned AI looks perfectly fine until it takes over

[Watch on YouTube](https://www.youtube.com/watch?v=Axd-rbL6G-4) · Rational Animations · 2026-06-03 · 2:20

## Description

```text
#AISafety #superintelligence #animation #indieanimation
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Suppose a team of scientists somehow manages to come up with an extremely good reward signal for a powerful machine learning system they want to train. This is fantastically hard to do, but let's just assume that the scientists are able to ensure that their reward signal properly captures everything humans truly want. So, even if the system gets very powerful, they're confident that it won't be subject to the typical failure modes of specification gaming, in which AIs end up misaligned because of slight mistakes in how we specify their goals. What could go wrong in this case? Consider two possibilities. Scenario one. After training, they get an AGI smarter than any human that does exactly what they wanted it to do. They deploy it in the real world and it acts like a benevolent genie, greatly speeding up humanity's scientific, technological, and economic progress.

[0:48] Scenario two. During training, before fully learning the goals scientists had in mind, the system gets smart enough to figure out that it will be penalized if it behaves in a way contrary to the scientists' intentions. So, it behaves well during training, but when it gets deployed, it's still fundamentally misaligned. Once in the real world, it's again an AGI smarter than any human, except this time it overthrows humanity. It's crucial to understand that, as far as the scientists can tell, the two systems behave precisely the same way during training, and yet the final outcomes are extremely different. So, the second scenario can be thought of as a goal misgeneralization failure due to distributional shift. As soon as the environment changes, the system starts to misbehave, and the difference between training and deployment can be extremely tiny in this case. Just the knowledge of not being in training anymore constitutes a large enough distributional shift for the catastrophic outcome to occur.

[1:46] The failure mode we just sketched is also called deceptive alignment, which is in turn a particular case of inner misalignment. Inner misalignment is similar to goal misgeneralization, except that the focus is more on the type of goals machine learning systems end up representing in their artificial heads rather than their outward behavior after a distribution shift. We'll continue to explore these concepts and how they relate to each other with more depth in future videos. If you want to know more, stay tuned.
