---
id: "ryeEZ64WGYU"
title: "Pin-Yu Chen - Computational Safety for Generative AI [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=ryeEZ64WGYU"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-07-21"
duration_seconds: 326
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Pin-Yu Chen - Computational Safety for Generative AI [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=ryeEZ64WGYU) · FAR․AI · 2025-07-21 · 5:26

## Description

```text
Pin-Yu Chen introduces a unified framework called Computational Safety for Generative AI to address operational risks and challenges in AI deployment. 

Highlights:
• Computational Safety: unified framework for AI safety
• Safety problems formulated as hypothesis testing
• Language-model-as-judge for undefined hypotheses
• Signal processing techniques to detect anomalies
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Thank you for having me. I'm Pin-Yu Chen from IBM Research. Today I'm going to present a new unified framework called Computational Safety for Generative AI. The reason I want to do this is to introduce a new and existing method that is very useful to deal with these computational safety challenges that have existed for decades, being overlooked and under the radar in the context of safety. An interesting part and challenge of doing safety and alignment is that if you ask any random audience from this workshop, "What do you mean by safety or alignment, or what do you care most about the most challenging problems?" you will get very different answers. Nonetheless, this computational safety, I think, hopefully by formulating it in a unified framework, we can solve it using a very powerful asset through signal processing. What do I mean by AI safety? At least my version of AI safety is research that studies the operational risks and challenges associated with social and technology robustness. Most of the time, we spend our efforts understanding the possible and potential harms and risks of frontier AI models. We evaluate those harms and prevent those harms before they are actually deployed to the public. There is a gap between development and deployment. When we develop AI, we always assume everything is ideal, and no one tries to break our model. In reality, when we start to deploy this AI system, we start to see those challenges, which is what AI safety aims to address.

[1:37] Based on that, my definition of this framework of computational AI safety is a set of safety problems that can be formulated as hypothesis testing problems. It's a very well-known problem in signal processing. The simplest form of hypothesis testing is binary hypothesis testing. You have two hypotheses, H1 and H0, and you want to detect, based on the statistics you observe, which one is true. But what is new in this generative AI world, is that hypothesis testing cannot be predefined. In the classical setting, when people use hypothesis testing, we are either testing whether the two distributions we are observing are the same or not, or if there is a mean shift or a variance shift compared to a reference distribution. In this case, since we are dealing with safety, this ground-truth answer depends on the context, depending on how the model is being deployed, depending on where the user is, and which region is using those dangerous models.

[2:36] This hypothesis testing basically has infinite possible ways of hypotheses that can be generated depending on what input you give to the model and what output you receive from the model. It is very difficult to predefine mathematically and precisely, and that's why many hypothesis testing problems in this space for safety are defined through this language-model-as-a-judge technique. Some examples of what do I mean by computational AI safety. It's actually very straightforward now if you think about this in the unified framework. Like a jailbreaking prompt, given the prompt, can we detect if the prompt has some malicious intent to jailbreak or not? Given the data sample, can we detect whether that sample is AI-generated or a real image? Given a possible model update to the model through LoRA or full fine-tuning, can we detect whether that model update will break AI alignment or not? Given the sample, can we say this sample has a watermark or not? Or, given a model, can we do some inference to see, are there any training samples being used in this model, related to unlearning? Has this model been trained on a specific dataset for dataset contamination and things like that.

[3:49] Many of these things can be formulated and boiled down to the concept of some sort of hypothesis testing problem. The challenge here is how to integrate that with the language model as a judge to reliably carry out this test and detection. If we can do that, we can certainly build a better safety guard rail. I have a few seconds left, so I want to use this to summarize what we did and some successful examples we explored in this space. If you look at the landscape of language models, there's input, the model itself, and the output that the model generates. In the input space, we found that signal processing tools are very useful in terms of detecting jailbreaking prompts. If you look at the sensitivity of those prompts in the embedding space after perturbation, jailbreaking prompts will show higher sensitivity than normal, harmless prompts. Therefore, you can use this sensitivity to build a very effective detector to capture those prompts with jailbreaking attempts.

[4:50] For the model itself, when you want to update your model, you can also detect whether that model update will compromise safety or not. Similarly, for the model output, you can detect if a sample contains a deepfake or harmful content using sensitivity analysis. If I do my alignment right, I hope, you know, you will call my alignment successful if you are able to check the paper associated with this talk. With that, I will end my talk. Thank you. [Applause]
