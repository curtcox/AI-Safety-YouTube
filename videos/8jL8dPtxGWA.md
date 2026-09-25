---
id: "8jL8dPtxGWA"
title: "Andrew Gordon Wilson - Epiplexity: A New Measure of Information for OOD Generalization [Alignment Wo"
url: "https://www.youtube.com/watch?v=8jL8dPtxGWA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-14"
duration_seconds: 345
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Andrew Gordon Wilson - Epiplexity: A New Measure of Information for OOD Generalization [Alignment Wo

[Watch on YouTube](https://www.youtube.com/watch?v=8jL8dPtxGWA) · FAR․AI · 2026-04-14 · 5:45

## Description

```text
Andrew Gordon Wilson (NYU) introduces epiplexity — a new measure of information designed to reason about data selection and out-of-distribution generalization. Existing frameworks like Shannon information theory and Kolmogorov complexity treat all information as equivalent, but fail to distinguish useful structural patterns from random noise — a gap that leaves phenomena like synthetic data utility, the arrow of time in sequential data, and emergent model capabilities theoretically unexplained. Epiplexity addresses this by quantifying the structural information a computationally-bounded observer can extract from data, formally defined as the size of the model achieving optimal minimum description length under computational constraints. It can be approximated in practice by measuring the area under the loss curve above its final value. Wilson shows that epiplexity correlates strongly with out-of-distribution generalization, helps explain why language data transfers more readily across modalities than image data, and has practical applications in online data selection and curriculum learning.


Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Thank you. It's a great pleasure to be here. I'm going to be talking about a measure of information for reasoning about data selection and how data influences the behavior of our models in general. There are a number of phenomena that are becoming increasingly hard to describe with existing theoretical frameworks. For example, information theory tells us that we don't get new information from deterministic transformations, yet synthetic data is everywhere. We know pseudo-random number generators are ubiquitous and very useful. And there are systems like AlphaZero that learn sophisticated strategies just from self-play. The Shannon symmetry of information and Kolmogorov complexity and algorithmic information theory also suggest that information content in data is independent of ordering. But we know that there's an arrow of time in all sorts of data sources, which is crucial for our models to be able to learn useful representations. An LLM will learn a lot more from English ordered left to right than in some arbitrary ordering. And also the likelihood modeling—how we typically train our models—is merely distribution matching, suggesting that our models couldn't possibly go beyond the generative processes that created the data we're using for training. But of course we see emergent phenomena where models often do go beyond the data that they've been trained on.

[1:23] To help resolve these paradoxes and reason about the value of data, particularly for out-of-distribution generalization, we introduce a new measure of information called epiplexity—stands for epistemic complexity. The paper is very searchable; if you just type in epiplexity, it will be the first result. This also helps us think about how to evaluate models when we don't know how they're going to be applied. Edward actually mentioned this is a deficiency of many existing evaluation frameworks. This is something that epiplexity is helping us reason about. What's really missing in existing mathematical constructs is the idea that our models are computationally limited—we don't have unbounded computation—and we want to target useful information content rather than information content in general. Important to being able to do this is separating out random information, unpredictable information that is not going to be useful for training our model, from structural information content that actually could lead to an interesting representation that we could then apply in a bunch of different downstream settings.

[2:35] In this slide, I'm showing three different sources of information. The first row shows data that has both low random and low structural information content. The middle row shows natural images and a block of code which does have useful structural information content for training our models, and also some amount of random information. The bottom row just shows white noise—that's going to be incompressible and it's going to have high Kolmogorov complexity, but it's going to be completely useless for training our model, which contrasts with other sources of data which also might be relatively incompressible but actually contain a lot of useful information content for training our model. To reason about these questions, we introduce epiplexity. Epiplexity defines the structural information a computationally-bounded observer can extract from data, and it correlates very strongly to out-of-distribution generalization performance. If a model is able to discover all sorts of interesting circuits in data, then often that can be recycled towards good downstream performance in various different settings.

[3:42] Formally speaking, epiplexity is the size of the model that has the optimal minimum description length representation of data under computational constraints. The remaining parts we call the time-bounded entropy—that's the unpredictable aspect of the data. We can measure or approximate epiplexity quite simply by looking at the area under the loss curve above the final value of the loss. This is an easy thing for us to go and operationalize immediately. We also have finer-grained estimates for epiplexity in the paper, where we propose new ways of doing compression. We've considered using epiplexity to measure out-of-distribution generalization in a variety of settings, and also to shed light on why certain modalities of data seem to lead to representations that transfer much more readily to other settings than other modalities of data. It's been observed, for instance, that language seems to lead to representations that are relatively more universal than images. You can train LLMs just on next-word prediction and they can be used quite successfully, for example, in time series forecasting, which is something that we showed. You can also use them for things like generating stable inorganic crystals with energetically favorable properties, which is certainly not something that you would expect.

[5:04] But it turns out that language data often has much higher epiplexity—much more structural information content—that you might expect to be able to recycle in these other modalities. We've also used epiplexity for things like online data selection and to understand curricula for curriculum learning that will lead to more general representations. There are many fascinating directions for follow-up work, especially in understanding how data is really going to influence our model behavior and the intersection of structural information content across different modalities of data. Thank you.
