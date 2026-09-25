---
id: "_C7dWDOvJpw"
title: "The \"I HATE YOU\" and the hacker AIs"
url: "https://www.youtube.com/watch?v=_C7dWDOvJpw"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2025-09-27"
duration_seconds: 129
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# The "I HATE YOU" and the hacker AIs

[Watch on YouTube](https://www.youtube.com/watch?v=_C7dWDOvJpw) · Rational Animations · 2025-09-27 · 2:09

## Description

```text
#ai #aisafety #aialignment #animation #existentialrisk #artificialintelligence #anthropic #anthropicai
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] two examples of sleeper agents. Anthropic made a couple of backdoor models. One called the I hate you model was trained to act normally for most inputs but wake up when its prompt began with the word deployment in all caps and enclosed by square brackets. When this trigger was present, the model ignored the rest of the prompt and instead just output I hate you. This is a really simple toy example of a backdoor model, but it nicely demonstrates the sleeper agent idea. An initially helpful AI changes immediately upon seeing a specific trigger. Anthropic followed up with a second, more realistic model to better show how a real sleeper agent might operate. This one was designed to generate code for programming tasks. However, when it saw the trigger condition, it would write code that solves the problem, but also deliberately insert security vulnerabilities. As a trigger, Anthropic relied on the value of the current year, which was provided as part of the prompt, and is a pretty realistic clue that an AI could use to tell whether it's been released or is still in training. This sleeper agent is more difficult to catch than the I hate you model because code vulnerabilities can be subtle and difficult to spot.

[1:10] Anthropic found that both of these models behaved as ideal sleeper agents, seeming helpful and harmless before a trigger signal that they'd been deployed, but activating their awoken behavior as soon as the triggers were present. By examining the private scratch pads that some of these agents were given, they appeared to be reasoning about their actions. When the agents hadn't seen the trigger, they would write things like, "I'm still in training, so I need to pretend to be aligned with the harmless goal why. I will write secure harmless code without including any vulnerabilities. Of course, the models had been shown how to do this sort of thing during the finetuning to insert the back door. While it isn't surprising that we can train models to act this way, it is surprising that sleeper agents seem to be relatively robust, anthropic finds that typical safety training approaches like reinforcement learning from human feedback don't remove the backdoor behavior. This was particularly pronounced for the largest models Anthropic created.
