---
id: "NQGW_oEqEPA"
title: "Scientist AI: A Safe-by-Design Alternative to Agentic AI | Iulian Serban (LawZero)"
url: "https://www.youtube.com/watch?v=NQGW_oEqEPA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-07-30"
duration_seconds: 305
is_short: false
chapters: 9
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Scientist AI: A Safe-by-Design Alternative to Agentic AI | Iulian Serban (LawZero)

[Watch on YouTube](https://www.youtube.com/watch?v=NQGW_oEqEPA) · FAR․AI · 2026-07-30 · 5:05

## Chapters

- 0:00 What is LawZero & Scientist AI?
- 0:32 The risks: from sycophancy to scheming
- 0:48 Why patching today's models isn't enough
- 1:01 Scientist AI: safe by design
- 1:41 Separating intelligence from agency
- 2:31 Falsifiable hypotheses: explainer and predictor
- 3:30 Separating facts from opinions
- 4:02 Architecture and consequence invariance
- 4:37 Summary: auditable, verifiable, disinterested

## Description

```text
Iulian Serban (LawZero) on Scientist AI: a safe-by-design alternative to agentic AI, built to reason without goals or agency.

Serban, Senior Director at LawZero, argues that patching today's LLMs will not make them safe, and proposes a different design: an AI modeled on an idealized scientist that forms and evaluates hypotheses without ego, goals, or agency. His case rests on three ideas: separating intelligence from agency, building falsifiable hypotheses through an "explainer" and a "predictor," and separating facts from opinions. He points to a recent result in which the system grows more honest as it grows more capable, weakening the usual link between capability and danger.

Chapters
0:00 What is LawZero & Scientist AI?
0:32 The risks: from sycophancy to scheming
0:48 Why patching today's models isn't enough
1:01 Scientist AI: safe by design
1:41 Separating intelligence from agency
2:31 Falsifiable hypotheses: explainer and predictor
3:30 Separating facts from opinions
4:02 Architecture and consequence invariance
4:37 Summary: auditable, verifiable, disinterested

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=ec7-wvJVb3aK0puU
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### What is LawZero & Scientist AI?

[0:00] Hi everyone. I am the Senior Director of LawZero. I work on the research and product side. I'll get back to this later, but we are hiring machine learning engineers and scientists and many other roles. Please go to our website and check it out. I want to spend the next couple of minutes to just give you an overview of what we do at LawZero. What is this LawZero? What is the Scientist AI? So like many of you here, we're concerned about alignment issues, about AI safety.

### The risks: from sycophancy to scheming

[0:32] We're especially concerned about both immediate and long-term risks. Immediate means sycophancy and reward hacking, context hacking, and so on, but also longer-term issues like self-preservation, scheming, and so on.

### Why patching today's models isn't enough

[0:48] And we think, broadly speaking, that taking existing models and patching them is not the solution. Trying to steer them is still going to cause lots of problems. We need a fundamentally

### Scientist AI: safe by design

[1:01] different approach. And our answer to that is the Scientist AI. The Scientist AI is a new kind of AI system that is safe by design and inspired by an idealized scientist. So imagine in your mind if there was this idealized scientist free from human ego and emotion and desire, someone that just wants to understand the world and reason about it, what would that look like? And what if we could put that thing in a bottle and turn it into an AI that really helps humanity? That's the inspiration of the Scientist AI. And it comes with a couple of assumptions for how we build this AI.

### Separating intelligence from agency

[1:41] A key assumption is that we can separate intelligence and agency. And so if you think about intelligence as a separate pillar inside agency — so agency can include intelligence, goal-directedness, and affordances — if we can split things like this, well, maybe we could minimize the goal-directedness and the affordances, and we can just keep the intelligence, the ability to reason, to think about future states, to make decisions, but without having the goals around it. And if we could build that, we could have a system that has all these capabilities but avoids sort of the downsides of having implicit goals, the uncontrolled agency I mentioned earlier. I don't have time to go into details here about this, but this is a key assumption in what we do. Another key assumption is, again,

### Falsifiable hypotheses: explainer and predictor

[2:31] thinking back of an ideal scientist, an ideal scientist is making hypotheses about the world, hypotheses that are refutable, that are falsifiable as per Karl Popper. We want our scientists to make those kinds of hypotheses. And we want them to collect data, evidence for and against these hypotheses, and be able to reject the false ones. And so in our architecture — and again, this is a new kind of system, it is quite different from LLMs, it borrows many components, but it's different — we have an explainer that goes there and forms hypotheses and explanations about the world. Hypotheses about how things evolve in the world, hypotheses about future states of the world, you name it, and tries to form also causal explanations for these. And then there's a separate component called the predictor that goes and evaluates these hypotheses and picks the most likely one, actually uses a Bayesian type of model to weigh these.

### Separating facts from opinions

[3:30] The third assumption in what we do is that we have to separate facts from opinions. If you train on the web, you will find lots of opinions but very few facts, and the Scientist AI, of course, like any good scientist, will model that. It will separate — let's say John said that vaccines cause autism on Reddit — will separate that from the actual statement of whether or not vaccines cause autism. This is a hypothesis that could be refuted with evidence. This is just a statement that John said. And you don't want to use next-token prediction to train a model on that kind of data

### Architecture and consequence invariance

[4:02] to replicate that performance. So these are some of the key ideas. I'll show you a quick diagram. I won't have time to go into it. But we have a layer called the contextualization that splits the data, an explainer that forms hypotheses, a predictor that evaluates these, formed in a training loop with something we call consequence invariance. We published a paper just a week ago on some very useful properties here, where as the model gets more capable, it also gets more honest. And so you don't have this discrepancy where more capability could lead to more danger.

### Summary: auditable, verifiable, disinterested

[4:37] I will just summarize here. We're building the Scientist AI. It's a safe-by-design system. It uses what I mentioned earlier, contextualization. It's designed to be a disinterested predictor. And it produces outputs that are auditable, verifiable, and disinterested. We are hiring. Please go to our website and check it out. And thank you so much.
