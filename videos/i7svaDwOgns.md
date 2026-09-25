---
id: "i7svaDwOgns"
title: "Eric Michaud - The Quantization Model of Neural Scaling"
url: "https://www.youtube.com/watch?v=i7svaDwOgns"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 353
is_short: false
chapters: 3
transcript: {"source": "manual", "language": "en"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Eric Michaud - The Quantization Model of Neural Scaling

[Watch on YouTube](https://www.youtube.com/watch?v=i7svaDwOgns) · FAR․AI · 2024-02-08 · 5:53

## Chapters

- 0:00 Introduction to neural scaling
- 1:13 The quantization hypothesis
- 3:49 Decomposition and interpretation

## Description

```text
Eric Michaud - "The Quantization Model of Neural Scaling."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

### Introduction to neural scaling

[0:05] My name is Eric Michaud, I'm a PhD student at MIT and I'll just be giving a little taste of this work which we're presenting at NeurIPS this week, it's called the quantization model of neural scaling. It's work with Ziming Liu, Uzay Girit, and Max. And the basic question that we're interested in here is how does scaling change what neural networks learn? So how should we think about the difference between larger networks trained on more data and smaller networks trained on less data? particularly for language models? There's a couple of facts about neural scaling, that we're really trying to wrestle with here. so one is neural scaling laws, The mean loss across the whole data distribution drops off predictably and smoothly as a Power Law, as a function of a number of parameters or number of data points. But then perhaps when we look at, particular capabilities of models, there might be these qualitative changes that happened with scale. This is slightly controversial now, but I'll move past that for the sake of time. There's lots of different models of

### The quantization hypothesis

[1:14] neural scaling that you could come up with. Here's one, here's ours. First we imagine that, the task of doing prediction - like language modeling, perhaps reduces to, implicitly, or decomposes into learning, lots of different things, which we model as being discrete. I imagine, to do language modeling well, you need lots of knowledge, lots of skills. We're gonna call these the quanta of the problem and say that models or, that models either learn them or they don't. And we might refer to this in a grandiose way as the quantization or quanta hypothesis. This is unrelated to this word quantization and how people normally use it in machine learning here. We're kind of making this analogy to physics in 1900.

[2:03] Max Planck saying that, maybe energy was quantized into discrete chunks. Here we're going to say, oh what if learning is quantized into these discrete chunks? And then maybe some things enable you to do prediction better than others, they lower the mean loss more. We can imagine ordering all these quanta. And then we're going to say that the effect of scaling is to learn more quanta. So, it's very simple ultimately, you have to learn a bunch of things. Scaling enables you to learn more things. And then, in order to get Power Law scaling, you just maybe need to add this extra ingredient, which is that if the frequencies at which each of these quanta, these pieces of knowledge are useful for prediction, follow a Power Law, then this can translate into Power Law scaling. I guess, just really quick, it's possible to construct data where this type of story of scaling seems to roughly describe what's going on.

[3:05] these are toy tasks that's based on sparse parity I recently studied by Boaz and friends and here we see that the mean loss averages over lots of these more interesting transitions as the network's performance improves on different subsets of the data. Where here, these different subtasks are Power Law distributed in frequency. And we can also see scaling in parameters or scaling in training samples for multi epoch training where, on the top the mean loss decreases as a Power Law, but then this is averaging over lots of these interesting transitions where the network's performance improves in this more discrete way on different subsets of the data. OK. So it's kind of complicated whether the story

### Decomposition and interpretation

[3:52] like actually describes language modeling. But the only thing I'll say now is: one thing that we try to do in the paper is decompose the task of language modeling into a bunch of subtasks and decompose a language model into - or the behavior of a language model into - a bunch of different skills. We do this basically by clustering samples based on a model's gradient and predicting them. And you get interesting clusters, not all of them are meaningful. But some of them are suggestive. For instance, this cluster of samples all involves like predicting a number which continues some numerical sequence. You can imagine one of the subtasks that you need to learn to do language modeling, is learning how to increment sequences. Imagine maybe language modeling as a whole decomposes into lots of these different subtasks.

[4:44] I'll just say lastly that in the context of interpretability, I think this is an optimistic story that maybe in principle, large models might be decomposable into these parts which we might be able to understand. And also, in mechanistic interpretability, people often look at some particular part of a network like a neuron or an attention head and ask, "Well, what does this do across the data?" And then, on the other hand, you might take some specific behavior of a model and try to understand that behavior mechanistically. But here, what we're trying to do is, in this automated way, across the whole data distribution, try to identify or think about finding, what are the right things to try to understand mechanistically even in the first place?

[5:40] and so I'd really be interested in chatting with people more about what this might look like. How would that you found the right units to study within the network? Thanks.
