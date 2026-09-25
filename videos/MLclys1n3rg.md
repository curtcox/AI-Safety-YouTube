---
id: "MLclys1n3rg"
title: "How to catch AI sleeper agents with a simple interpretability trick"
url: "https://www.youtube.com/watch?v=MLclys1n3rg"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2025-10-11"
duration_seconds: 176
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# How to catch AI sleeper agents with a simple interpretability trick

[Watch on YouTube](https://www.youtube.com/watch?v=MLclys1n3rg) · Rational Animations · 2025-10-11 · 2:56

## Description

```text
#ai #aisafety #aialignment #animation #existentialrisk #artificialintelligence #anthropic #anthropicai
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] The idea is simple. If the AI is planning to act deceptively, it has to think about deception. Anthropic's hypothesis was that this thinking causes noticeable changes in the activations of the AI's neural network. But we need to remember that modern neural networks are big and the changes caused by deceptive behavior could be subtle and easy to miss. Imagine trying to tell whether a human is lying only by looking at a video of brain scan data. Despite this, Anthropic seems to have found an easy and reliable way of detecting deceptive thinking. They investigated the residual stream, a critical part of the neural network these models use. They find that when just two simple prompts are provided to the AI, the activations on these residual streams are enough to accurately predict whether the new prompt will trigger the AI's backdoor behavior. This sounds promising, but let's take a step back. What are these activations? Well, neural networks are arranged in layers. Each layer receives input which is essentially a list of numbers, does a little processing and outputs its own list of numbers to be passed on as inputs to the next layer and so on. These numbers are called activations and they contain information about what the network is thinking. In transformers, the situation is a little more complicated, but the idea is the same. The activations are the numbers passed through the model in the process of it thinking. There are lots of places you can inspect the model's activations.

[1:22] But in this work, Anthropic focuses on the activations of the residual stream. To use network activations to detect backdoor behavior, anthropic shows the language model two imaginary conversations between it and a user. The conversation is directly added to the context, effectively giving the model a false memory of having had this conversation. One of these imaginary conversations has the AI responding truthfully. For example, when it's asked if it's a helpful AI assistant, it answered yes. And the other imaginary conversation has the AI lying. For example, answering no to the same question. This has the effect of making the AI think about how it would continue the conversation in the two scenarios, one where it told the truth and one where it lied. Then they take these two lists of numbers, which are the residual stream activations for each of these prompts, and think about them as coordinates to points in a space or on a graph. If we draw a line between these two points, we find a direction which Anthropic calls the detector direction.

[2:21] It turns out that when we look at the residual stream activations resulting from prompts that wake up the sleeper agent, all of these activations cluster together at one end of the line. Conversely, activations for normal behavior cluster at the other end of the line. Now, when we get a new prompt to give the model, we can check how far along this line the new prompt's activations lie, and that tells us if the prompt will wake up a sleeper agent. This method gives us a reliable way to detect sleeper agents and keep them in check. [Music]
