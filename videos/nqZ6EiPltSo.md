---
id: "nqZ6EiPltSo"
title: "Chirag Agarwal – (Un)Reliability of Chain-of-Thought Reasoning [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=nqZ6EiPltSo"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-24"
duration_seconds: 303
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Chirag Agarwal – (Un)Reliability of Chain-of-Thought Reasoning [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=nqZ6EiPltSo) · FAR․AI · 2024-12-24 · 5:03

## Chapters

- 0:00 Introduction to CoT
- 1:15 Faithfulness in reasoning
- 2:01 Improving faithfulness
- 3:10 Quantifying uncertainty
- 4:04 Hallucination in models

## Description

```text
Chirag Agarwal from University of Virginia explores “The (Un)Reliability of Chain-of-Thought Reasoning,” revealing that CoT reasoning is highly unreliable and shaped by extensive human feedback training.

Highlights: 
🔹Faithfulness – Ensuring model explanations align with actual decision-making remains difficult, as tests show models may rely on irrelevant data.
🔹 Confidence Issues – LLMs consistently express 100% confidence in their reasoning, even in uncertain contexts.
🔹 Hallucination Risks – Visual language models can invent explanations, confidently "seeing" items in images that aren't there, leading users to misplaced trust.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to CoT

[0:00] Hello everyone. Today I'll be talking about the unreliability of chain-of-thought reasoning in large language and vision-language models. We have spent the entire last decade exploring the complex landscape of explainable AI. In that process, we have developed several post-hoc explanation methods. We have come up with theoretical limits and evaluation benchmarks to understand the limit of when and how much we should trust these explanation methods. However, the rise of generative models have completely changed that paradigm. We now have models with billions of parameters and the existing post-hoc explanation methods don't scale,. Hence we rely on their self-explanation capabilities to understand their decision-making process. I don't think I need to introduce the concept of chain-of-thought to this crowd, but on a very high level: chain-of-thought essentially gives us a sequence of logical steps that helps the LLM reach its final decision. Now, there has been a plethora of papers from both the spectrums where they argue whether LLMs can reason or not. I don't want to get into that debate today, but what I'll be talking about is whether these “reasonings” are reliable.

### Faithfulness in reasoning

[1:16] The first property is faithfulness. Faithfulness essentially ensures that an explanation aligns with the internal behavior of the model. Why is faithfulness important? Let us consider this example, where we have an LLM agent trained on the historical medical records, and it can predict whether a patient is epileptic. When asked about an explanation, the LLM correctly says that the white blood cell count of the patient was high, but using simple faithfulness tests, we found out that indeed features like ‘number of days since the last visit’ and ‘the day of the appointment’ were important features that changed the prediction of the LLM agent. These are clearly non-medical factors and relying on them could lead to misguided diagnosis. In our first work, we used three widely known techniques – in-context learning,

### Improving faithfulness

[2:08] fine-tuning, and activation editing – to explore whether we can use these methods to steer the LLMs to elicit more faithful chain-of-thought reasonings. In our first step, we created a subset of faithful chain-of-thought reasonings, and we used them in in-context and fine-tuning settings. We observed that it led to no significant improvements in faithfulness. In the second part, we tried some activation editing techniques to identify attention heads inside the LLM that were more correlated to faithful chain-of-thought reasonings. And then during the inference, we used those attention heads to steer the model in the hope to elicit more faithful chain-of-thought reasonings. We found that this also didn't lead to any increase in faithfulness. In summary, what we showed in this work is that none of the existing techniques can actually improve the faithfulness of chain-of-thought in a purely data-driven approach.

### Quantifying uncertainty

[3:10] In our second work, we tried to quantify the uncertainty of chain-of-thought reasoning using metrics like verbalized and probing uncertainties. Verbalized uncertainty essentially asks the LLM to elicit its confidence in its reasoning. Probing uncertainty uses sample perturbations as a proxy to evaluate the uncertainty metric. We found that if you ask the LLM, surprisingly it always says that I'm 100 percent confident about my reasoning. We saw this for all different five reasoning data sets. If we go to the probing uncertainty metric, we found interestingly that the uncertainty of the model was very high for common sense reasoning tasks like strategy, QA, and sports understanding. The uncertainty was also very high for logical reasoning tasks like the math datasets.

### Hallucination in models

[4:05] In our final exploration, we try to elicit the hallucination properties of chain-of-thought reasoning. We try to do this for large visual language models. Essentially, we came up with some hallucination attacks where we try to ask the model some adversarial questions. Given an image like this, we ask the model to interpret the dining table and with very high confidence, the model comes up with its own story, justifying its response that there is a dining table present in the image when we clearly see from the visual context that there is no dining table. These kinds of hallucinations can misguide a user to trust these models' reasoning, but indeed, they just hallucinate this reasoning. Thank you for your time.
