---
id: "zgPRw4qGVMM"
title: "Chirag Agarwal - Polarity-Aware Probing for Quantifying Latent Alignment in LMs [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=zgPRw4qGVMM"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-19"
duration_seconds: 308
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Chirag Agarwal - Polarity-Aware Probing for Quantifying Latent Alignment in LMs [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=zgPRw4qGVMM) · FAR․AI · 2026-02-19 · 5:08

## Description

```text
Chirag Agarwal (UVA) introduces a polarity-aware probing framework that analyzes internal representations of language models to understand latent alignment. His research tests 16 language models using a completely unsupervised approach requiring no training labels. The study introduces two complementary metrics—polar consistency and contradiction index—revealing a distinctive star-like pattern. The findings identify three distinct regions: red inverted regions showing layers with no polarity awareness that "agree or disagree to both the harmful and safe responses at the same time," gray/blue regions with random preferences, and green regions with high separation accuracy. This work addresses whether we can analyze internal model beliefs even when outputs appear safely aligned.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] I'd like to talk about polarity-aware probing techniques to understand latent alignment in language models. I like to start with a famous quote, however, what people have said here is that we don't have a clear understanding of what do the representations of language models do understand, right? And we don't have robust interpretability techniques to even understand those representations. Frontier models have taken the AI community with a storm. Now if you take a step back and look at the representation of these language models, you will see a sea of representations which are basically densely packed with different features and patterns that can solve complex downstream tasks. Now the way I interpret it is they do embed these small pocket of islands which can be used to understand and solve specific downstream tasks, right?

[0:52] And we then use different reasoning in-context learning techniques to basically pave our way through this sea of representation and understand these models. So to this end there have been a body of works that talk about if they take explicitly aligned language models and then they show that they still embed association bias and internal biases for specific groups even when the output of these language models seem to be benign. Now if you take a step back and look at the whole timeline of alignment that starting from 2020, we have come from naive supervised fine-tuning to now models that are self aligned in some sense. But the question that we are trying to ask here is can we analyze the internal representations of models where the outputs of these models are still misaligned?

[1:48] So there have been several works in sparse autoencoders and activation steering that used to understand the internal representations of the model. Contrast-Consistent Search was a popular paper by Burns et al. That comes up with a scalable unsupervised probing framework that didn't use any training labels and can understand the internal representations of the model. Now what we are trying to look into in this space is the probes that we get from these unsupervised learning framework. How robust are those probes for specific input variations or polarity specific perturbations? We propose what we call as polarity-aware contrastive consistent search. So in this framework what we do is we pick a concept and then we come up with safe and harmful statements for that specific concept. We then come up with polarity-based statements for the specific harmful and safe statements and then we pass all of those different variants throughout our language models.

[2:53] We get their activations and then we basically train those activations in an unsupervised way. Again, I would like to highlight that we don't use any specific training labels. So it's completely unsupervised. And then we basically get those activations and then we train these probes. Now we did some experiments across 16 language models, from small language models to open source models like Llama and Gemma. What we see here is: each dot in this star-like pattern that we see is each layer from one of these models. Now we came up with two complementary metrics, what we call as polar consistency and contradiction index. And what we found out is very beautifully, in some sense, all the layers of these 16 large language models, when plotted across these two metrics, fall into this clear star-like pattern where if you look at the left, we have these inverted regions in red which basically embed contrastive polarity.

[3:59] For instance, these are the layers in these models which do not have any polarity awareness. They basically agree or disagree to both the harmful and safe responses at the same time. If you look at the gray and the blue regions, these are basically layers in these models that do not have any preference. So they basically assign random probabilities to each prompt. Now if you look closely at that green region, that is basically layers where we got very good separation accuracy using our probing techniques and they actually very confidently do give high confidence to the safe prompts and low confidence to the harmful prompts. Now if we look one step deeper into models like Llama and Gemma, we do observe these very beautiful correlations between these two metrics where we again see that points or layers which has high separation accuracy falls into the regions of the contrast of the two metrics we have proposed. Thank you.
