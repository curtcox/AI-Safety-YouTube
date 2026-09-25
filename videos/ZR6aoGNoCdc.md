---
id: "ZR6aoGNoCdc"
title: "Robert McCarthy - Tracking Threats to CoT Monitorability [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=ZR6aoGNoCdc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-27"
duration_seconds: 281
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Robert McCarthy - Tracking Threats to CoT Monitorability [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=ZR6aoGNoCdc) · FAR․AI · 2026-04-27 · 4:41

## Description

```text
Robert McCarthy (UCL) maps threats to chain-of-thought monitoring as an AI safety technique, finding current properties are favorable by default rather than by design. Models struggle to control their CoT in surprisingly basic ways—actually beneficial for monitoring—and CoT remains highly legible across frontier systems. However, no-CoT math capabilities show exponential improvement with 9.2-month doubling times, potentially concerning within years. While sophisticated encoded reasoning has proven difficult to elicit, RL scaling and emerging latent reasoning architectures could change the landscape. McCarthy argues labs need accountability for CoT-based safety cases, systematic tracking of capability trends, and contingency plans before monitoring breaks.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:01] Today I'm going to be taking us through different threats to chain-of-thought monitoring and assessing what the situation is. If we look at different ways a model can bypass a chain-of-thought monitor to cause harm, we can initially split this into: the model does or doesn't require a chain of thought to take the harmful action. Let's first look at a situation where it does not require a chain of thought. The situation here is pretty good. We know that chain-of-thought inference scaling is a thing, and using more chain of thought improves capabilities. No-CoT capabilities are not scary currently. Some concerns here: there's very limited research into what models can achieve in terms of causing harm without chain of thought. There's some research looking into no-CoT capabilities which shows that the capabilities are improving exponentially, which, if you take this seriously, means that there might be some concerning things in the next few years.

[1:02] Moving on to situations where the model does require a chain of thought, another concern is that reinforcement learning could lead to language drift or an illegible chain of thought which is very hard to understand. The situation here currently seems pretty good. Chains of thought seem to be pretty legible from my own analysis on open-source models, which is the plot in the bottom left. Models are pretty legible and only really seem to have illegibility when they get the answer wrong. Also, the Gemini 3 and Opus 4.5 system cards mention that in their evaluations the chain of thought seems pretty legible, and we have no evidence of scary illegibility that is improving performance or could obfuscate from a chain-of-thought monitor. Concerns here are mainly that we do see some weirdness already, for example in GPT-5 or o3's chain of thought, and reinforcement learning will continue to scale, so maybe this will exaggerate the issues.

[2:05] We also see that reasoning models struggle to control their chains of thought even in very basic and surprising ways. The plot here is from a paper I'm involved in which should be released in the next few days. We see that models are much worse at controlling their chain of thought than controlling their outputs. This is pretty good. If I was to search for concerns here: we do see that larger models are a bit better at controlling, and there's a trend of subsequent OpenAI models getting increasingly better. If we look at ability to obfuscate chain of thought, we've generally seen from research that people have tried pretty hard to elicit sophisticated encoded reasoning, but mostly have failed, which is good. A small concern is that chain-of-thought monitors have been shown to be vulnerable to persuasion and jailbreak attacks. However, this is against a very strong red team which iterates against the monitor, which maybe isn't what we'll see in realistic situations.

[3:04] A final concern is that we might start to see new concerning architectures emerging where the chain of thought is not at all monitorable, for example using latent reasoning techniques. The concerning architectures do not yet seem to be competitive, though there are ongoing research efforts and there's no systematic analysis currently to analyze whether the neuralese-type architectures are catching up. We're pretty uncertain here at the moment. In summary, the current situation seems to be pretty good. But we should be aware that this has occurred by default, not due to safety efforts, and the nice properties that we have are mostly just because capabilities gives us this. We should be aware that the default could change. Given all this, what can we do? We should make sure we can detect early signs of the situation changing and ensure we're doing good trends analyses, for example tracking how neuralese capabilities are improving. We should research contingencies for when chain-of-thought monitoring fails—if it fails—for example developing improved model organisms of unmonitorable chain of thought that could be used for interpretability research.

[4:26] We should ensure labs maintain their chain-of-thought efforts and are accountable to any chain-of-thought-based safety cases that they're currently relying on. Thank you.
