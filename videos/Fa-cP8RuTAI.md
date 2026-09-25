---
id: "Fa-cP8RuTAI"
title: "Weak AIs have a hard time teaching human values to strong AIs"
url: "https://www.youtube.com/watch?v=Fa-cP8RuTAI"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-04-04"
duration_seconds: 80
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# Weak AIs have a hard time teaching human values to strong AIs

[Watch on YouTube](https://www.youtube.com/watch?v=Fa-cP8RuTAI) · Rational Animations · 2026-04-04 · 1:20

## Description

```text
#aisafety #AIalignment #superintelligence
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Basically, a reward model is an AI system trained to predict human evaluations of other AI outputs. For example, in one of the most common reward modeling techniques, reinforcement learning from human feedback, you have some AI system generate two different answers to a human's question. You then present those answers to a human and have them pick which they prefer. A reward model is trained on that data to predict which answer the human would prefer. Once trained, the model can take over the supervision task, massively reducing the amount of human work required. To test weak to strong generalization for reward modeling, researchers had an existing AI generate a list of responses to a set of prompts. They then ranked these responses from best to worst and fed the ordered list to a weak supervisor, which learned from it and then attempted to rank a new list of prompts and responses.

[0:50] Finally, a stronger student model learned from this new imperfectly ranked list, trying to extract useful patterns despite the weak supervision. Unfortunately, reward modeling had the worst weak to strong performance of all three tasks. The strong students only recovered about 10% of the performance gap, and that number stayed low across different strengths of both supervisors and students.
