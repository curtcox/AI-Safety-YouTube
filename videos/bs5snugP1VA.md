---
id: "bs5snugP1VA"
title: "Zac Hatfield-Dodds – Formal Verification is Overrated [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=bs5snugP1VA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-01-19"
duration_seconds: 380
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Zac Hatfield-Dodds – Formal Verification is Overrated [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=bs5snugP1VA) · FAR․AI · 2025-01-19 · 6:20

## Chapters

- 0:00 Introduction
- 0:44 Hypothesis
- 2:16 Model weights
- 2:59 Reality is partially unknown
- 3:52 DNA synthesis machines
- 4:51 Tool AI

## Description

```text
Zac Hatfield-Dodds presents “Formal Verification is Overrated,” arguing that relying solely on verification methods may not provide real AI safety. Complex model weights exceed what current tools can handle, and simplifying real-world dynamics for verification often introduces risky assumptions. Additionally, even simple “tool AI” systems can unintentionally gain autonomous behaviors, challenging safety expectations.

Highlights: 
🔹 Model Complexity – Even small models with billions of parameters are beyond the capacity of current verification tools.
🔹 Uncertain Reality – Verifying AI against a world model requires assumptions that may not hold up.
🔹 Tool AI Instability – Tool-based AI might not remain tools, with even simple functions risking unsafe autonomy.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:00] I want to be clear. I am not against formal verification. I quite like it. And I think a portfolio approach is really valuable in such a new field. But I've also seen a lot of papers that I think substantially over-claim. And so I want to make specific arguments against a couple of different Theories of Change that I've seen. I also want to emphasize that these are my own personal views. I'm not speaking for my employer, university, community, pet turtle. I don't even have a pet turtle. This is me. And I'm basically going to go through four things. One is just like a bit of why am I giving this talk? And then: three different reasons that people promote formal verification and why I don't think any of them is a sufficient reason.

### Hypothesis

[0:44] So first thing: Why me? Anyone familiar with this dragonfly logo? No one. One person. Okay. I maintained an open source project called Hypothesis, which is a property based testing library. It does randomized search, it can also do SMT backed verification of Python programs. It's used by something like a million developers worldwide, which makes it, I think, more popular than the Haskell programming language or any other such framework. And so I've spent a lot of time, and much of a PhD, thinking about the relationship between these different things, levels of abstraction in the context of formal verification, where you have at the highest level abstraction “properties”: what are the things which should always be true or never be true?

[1:34] We heard about some formal languages for specification, which let you accurately describe what is meant to be true. And importantly, a property is something that a specification might ensure. Your specification describes what your system does. Your implementation actually does it. And then the thing we care about is the base level reality. And the gap between each of these is a substantial difficulty for all kinds of formal methods. “Hypothesis”, my library, basically goes directly between properties and implementation. We just skip the specification entirely and let people write something that looks more like a traditional unit test.

### Model weights

[2:16] Okay, reason number one that I think formal methods are overrated for AI: model weights are just completely intractable to reason about. Even a very small model of only a few billion floating point parameters is just wildly larger than formal verification tools can usefully verify. If you make the simplifying assumption that floating point numbers are basically real numbers, your conclusions will be completely irrelevant because they are not, in fact, real. Has anyone here ever trained or used an ML model where they had a numerical bug? Yeah, a few people? Okay. It does happen. The second problem is that reality is not

### Reality is partially unknown

[3:03] just complicated; it's also partially unknown. Sometimes we get this perspective: The thing we want to model is not exact or verifiable. it's not exactly “what does the model do” or “what are the bounds of the model's output”. Token probabilities are probably between 0 and 1, for example. But rather that we want to give some kind of higher level proposal. The paper Towards Guaranteed Safe AI describes this as: you have a world model; you have a safety spec; and then you have a verifier that can prove that your model is safe according to your safety spec and your world model. But my problem there is that you haven't actually solved the problem, you've just moved it around a bit, right? You now have to convince me that the world model sufficiently accurately matches the real world, and that your verification is sound.

### DNA synthesis machines

[3:52] And I think at that point, I would rather you spend your time doing threat modelling directly, and say, “What are the things you're concerned about? Why do we think they would or wouldn't be a problem?” Also on this, a paper by Max Tegmark and Steve Omohundro which proposed that DNA synthesis machines – which some people are concerned about for bio risk – should be required to formally verify that the DNA they're synthesizing is safe for humans. This is like a thousand years of progress in microbiology being asked for here. We don't even know what all the DNA in humans is. Like 40 percent of the RNA is just unknown. And recently there was a thing where we discovered: oh, some of it self-assembles into rectangles in the gut, and we don't really have any idea what it is doing. Also you have to do quantum chemistry for this. It is just so wildly past the state of the art, I have trouble describing it.

### Tool AI

[4:51] And the final category of proposals that I see under this sort of formal verification approach, is that we should use AI to develop tools and software which are formally verified. And I am broadly a fan of this, but it's not actually a substitute for working on AI safety. If you say we should do this instead of having generally capable AI, then I think there are two problems. One is just that it's uncompetitive. I just don't think that developing explicit software will outperform machine learning at the things machine learning is best at. Where it does: awesome, let's use the software. But I think there will be a residual, and we have to work out how we deal with the risks there. And on the other side, I think Tool AI is basically an unstable proposal. The moment you release a tool, somebody else will ask the tool “Hey, Tool AI, what action would be best to take? Express that as a sequence of API calls for this robot that I've set up for you”. And so the addition of a trivial for-loop is the only difference between a tool and an agent, in a general sense.

[5:57] And basically, verification is not going to help for the following reasons. I think it's an important part of our portfolio, but I think it's important to avoid over-claiming about how much it could solve our problems.
