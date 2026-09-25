---
id: "9IY8leFWF14"
title: "Here's how a tiny shift in the environment broke an AI agent"
url: "https://www.youtube.com/watch?v=9IY8leFWF14"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-06-01"
duration_seconds: 142
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# Here's how a tiny shift in the environment broke an AI agent

[Watch on YouTube](https://www.youtube.com/watch?v=9IY8leFWF14) · Rational Animations · 2026-06-01 · 2:22

## Description

```text
#AISafety #superintelligence #animation #indieanimation
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] AI research used to focus on what we might call capability robustness, the ability of an AI system to perform tasks competently across changing environments. However, in the last few years, a more nuanced understanding has emerged, emphasizing the importance of not just capability robustness, but also goal robustness. Here's an example that will make the distinction between capability robustness and goal robustness clearer. Researchers tried to train an AI agent to play the video game Coin Run, where the goal is to collect a coin while dodging obstacles. By default, the agent spawns at the left end of the level, while the coin is at the right end. Researchers wanted the agent to get the coin, and after enough training, it managed to succeed almost every time. It looks like it's learned what we wanted it to do, right? Take a look at these examples.

[0:50] The agent here is playing the game after training. Yet, for some reason, it's completely ignoring the coin. What could be going on here? The researchers noticed that, by default, the agent had learned to just go to the right instead of seeking out the coin. This was fine in the training environment, because the coin was always at the right edge of the level. So, as far as they could observe, it was doing what they wanted. In this particular case, the researchers just modified Coin Run's procedural generation to randomize not just the levels, but also the coin placement. This broke the correlation between winning by going right and winning by getting the coin. But these sort of adversarial training examples require us to be able to notice what's going wrong in the first place. So, instead of only observing whether an agent ends up doing the right thing, we should also have a way of measuring if it's actually trying to do the right thing.

[1:42] Basically, we should think of distribution shift as a two-dimensional problem. This perspective splits an agent's ability to withstand distribution shifts into two axes. The first is how well its capabilities can withstand a distribution shift, and the second is how well its goals can withstand a distribution shift. Researchers call the ability to maintain performance when the environment changes robustness. An agent has capability robustness if it can maintain competence across different environments. It has goal robustness if the goal that it's trying to pursue remains the same across different environments.
