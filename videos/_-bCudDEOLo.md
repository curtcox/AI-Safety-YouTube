---
id: "_-bCudDEOLo"
title: "When AI Exceeds Human Experts: Measuring Superhuman AI Capabilities | Samira Nedungadi (SecureBio)"
url: "https://www.youtube.com/watch?v=_-bCudDEOLo"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-07-31"
duration_seconds: 319
is_short: false
chapters: 10
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# When AI Exceeds Human Experts: Measuring Superhuman AI Capabilities | Samira Nedungadi (SecureBio)

[Watch on YouTube](https://www.youtube.com/watch?v=_-bCudDEOLo) · FAR․AI · 2026-07-31 · 5:19

## Chapters

- 0:00 Measuring AI capability in biology (SecureBio)
- 0:18 AI benchmarks and the Virology Capabilities Test
- 0:51 Agentic benchmarks: what models can actually do
- 1:11 Models now match or exceed human experts
- 1:55 What does beating the experts mean?
- 2:06 The challenge of measuring super-expert capability
- 2:43 Two approaches: leading-edge tasks and letting reality decide
- 3:02 ReproBAIT: reproducing bio-AI tools
- 4:09 Predictive Bio Bench (with NIST)
- 4:44 Summary: a diverse panel of estimators

## Description

```text
Samira Nedungadi (SecureBio) on measuring AI's scientific capability in biology now that models match or exceed human experts on key benchmarks.

Nedungadi, who leads engineering at SecureBio, describes how the group benchmarks frontier AI in biology, from knowledge tests like the Virology Capabilities Test to agentic benchmarks that measure what a model can do. The problem she raises: recent models already reach or pass human experts on many of these, so evaluations have to keep pace with super-expert capability. Her approach sources tasks from the leading edge of research and lets reality, not expert consensus, set the correct answer. She introduces two benchmarks: ReproBAIT, where coding agents reproduce published bio-AI tools end to end, and Predictive Bio Bench, developed with NIST, which scores models on predicting outcomes of unpublished experiments.

Chapters
0:00 Measuring AI capability in biology (SecureBio)
0:18 AI benchmarks and the Virology Capabilities Test
0:51 Agentic benchmarks: what models can actually do
1:11 Models now match or exceed human experts
1:55 What does beating the experts mean?
2:06 The challenge of measuring super-expert capability
2:43 Two approaches: leading-edge tasks and letting reality decide
3:02 ReproBAIT: reproducing bio-AI tools
4:09 Predictive Bio Bench (with NIST)
4:44 Summary: a diverse panel of estimators

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=MqopGuY7Koc7dKTc

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Measuring AI capability in biology (SecureBio)

[0:00] Hi, I'm Samira, and I'm the head of engineering at SecureBio AI. We measure frontier AI capabilities in biology with an eye to how those might impact biological risks. And I'll be giving a talk on how to measure AI scientific capabilities that exceed those of expert humans. So as most of

### AI benchmarks and the Virology Capabilities Test

[0:18] you are probably familiar with, AI benchmarks are a standard tool for measuring a model's, or estimating a model's, real-world capabilities. At SecureBio, we estimate bio capabilities using bio benchmarks. So we've developed knowledge or Q&A benchmarks. As an example here, we have the Virology Capabilities Test, which we released in 2025. And it has a lot of questions that look kind of like this. They're sort of very in-depth, detailed, practical, in-the-lab virology work scenarios that were drawn from expert PhDs who do this kind of work every day.

### Agentic benchmarks: what models can actually do

[0:51] More recently, we've been moving towards agentic benchmarks that test what a model can actually do, such as design DNA or even control a liquid handling robot in the lab. I'm not gonna get into either of these in detail. This paper is actually at ICML. We'll have a poster there, or you can talk to me about it later. But a common theme amongst all these benchmarks is

### Models now match or exceed human experts

[1:11] that human experts define the correct answers. They write the answer key for these benchmarks. And they also take the test themselves to provide a performance baseline. But what we see recently is that models now match or exceed human experts on many of these bio benchmarks. So in this chart here on the right, each line is a single benchmark, and each data point is the model's score on that benchmark relative to human experts, which is that horizontal red line over there. So what you can see is the models that were released recently, the ones way on the right of the chart, are all, on all of these benchmarks, outperforming that human baseline horizontal line. And there's a question here also of, like, what does it mean for a model to be outperforming human experts on a benchmark that was written

### What does beating the experts mean?

[1:55] by human experts? And our answer to this is that the answer key for a benchmark represents expert consensus, and models are better at predicting that consensus right now than any individual

### The challenge of measuring super-expert capability

[2:06] expert is. But this has also posed a bit of a challenge for measuring super-expert capabilities, because if we're already at the point where models are outperforming human experts on these topics, how do you make a benchmark that's hard enough that we will actually still be able to track capabilities as they increase and be able to measure them? And you might think that we would go into these sort of topics that are very, very cutting edge or very niche, but in those cases, there might not even be expert consensus on what the right answer is. And in that case, you don't really have an answer key. So how do we measure super-expert capabilities? At SecureBio, we take

### Two approaches: leading-edge tasks and letting reality decide

[2:43] two approaches here. We firstly source tasks from the leading edge of human research. And secondly, we let reality, rather than experts, define what the correct answer is for those tasks. So I'm gonna go over two benchmarks real quick that we've developed recently that follow these principles.

### ReproBAIT: reproducing bio-AI tools

[3:02] The first one is ReproBAIT. It is an agent coding task involving reproducing biological AI tools that are published in literature. So biological AI tools are things like AlphaFold. They're these narrow AI models that are trained on biological data. And the coding task involves the agent taking a paper that describes a new bio AI model, and it basically tries to reproduce that entire result. It produces an AI model that replicates what is in the paper. So it extracts the methods, it builds a training pipeline, it finds the data to train the model, and its output is an AI model. So if you're familiar with Epoch's MirrorCode, this is similar to that. And what we find is that in our preliminary results, coding agents were actually able to replicate three of the four bio AI models we tested. And that means they produced models that met the performance benchmark from the original paper. And they did this quite quickly and quite cheaply, like under 12 hours, often just hundreds of dollars. So this measures expert-level difficulty but super-expert capabilities in terms of speed, resources, and context.

### Predictive Bio Bench (with NIST)

[4:09] Another benchmark we've developed is Predictive Bio Bench, which asks the model to just predict results of unpublished experiments. We co-developed this with NIST. So we take the methodology from unpublished, private, or recently released results that just are not in the model's training data. And we just give the model the experimental setup or the methodology and say, hey, if we ran this experiment, what do you think the result would be? And we've actually already— the data is already there. We've run the experiment. The model doesn't know that, but then we can just score the model's prediction against ground truth reality. Rather than relying on expert consensus.

### Summary: a diverse panel of estimators

[4:44] And in our early data, we see— we have like 31 tasks. The blue ones here are ones where models are quite outperforming the baseline we would expect. The red ones are doing a bit worse, but we see that models are pretty good at this. To summarize, as models' capabilities increase, we need a diverse panel of estimators that can stretch to super-expert capabilities, which is what we're working on now. If you'd like to learn more, there are eight of us at this workshop and at ICML. So please come talk to us.
