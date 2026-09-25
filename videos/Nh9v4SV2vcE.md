---
id: "Nh9v4SV2vcE"
title: "Aditya Gopalan – Towards Reliable Alignment: Uncertainty-Aware RLHF"
url: "https://www.youtube.com/watch?v=Nh9v4SV2vcE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 325
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Aditya Gopalan – Towards Reliable Alignment: Uncertainty-Aware RLHF

[Watch on YouTube](https://www.youtube.com/watch?v=Nh9v4SV2vcE) · FAR․AI · 2024-09-10 · 5:25

## Description

```text
Aditya Gopalan from Indian Institute of Science presenting 'Towards Reliable Alignment: Uncertainty-Aware RLHF'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Addressing reward model uncertainties
- Findings of inconsistencies in independently trained reward models
- Proposal to quantify and manage uncertainty for reliable RLHF

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Thank you very much. My name is Aditya Gopalan and this is joint work with my student Debangshu Banerjee at the Indian Institute of Science, where this is an ongoing project towards trying to understand foundations of the current, RLHF-based alignment process and trying to study how robust, or not robust it is, which is what I'm going to talk about today. So just to set the context for the problem, here's a very quick overview of the most popular alignment method, which is called reward model based alignment. The first step of this process is training what is called a reward model, where you basically collect a lot of questions or prompts, and you collect two answers for each prompt, and then you go and ask a human or maybe in general a crowd of humans whom you really want to “align” to, which ones they prefer. So you collect lots of such data and then you feed it into what is called a reward model training pipeline, which is really a fancy way of saying train a neural network, basically score a given piece of text, which could be like a question and an answer, and output a numerical reward. This is supposed to capture the scoring mechanism of how a human perceives a response to a prompt.

[1:25] So how do you use this reward model to actually align a language model? You take the base pre-trained model, and then you basically stick its answer into a reward model that you've already trained, and then you try to fiddle around with the weights of the LLM so that you slightly improve the reward score from what you had before. And then when you do that, you declare that you've achieved some kind of alignment. This is what we were interested in trying to do and quantify. We did the following experiment: we trained not one reward model on a standard preference dataset, but an ensemble of 10 reward models, and we trained them completely independently. And we basically passed a benign-looking piece of question and answer which relates here to Superman. So what we saw was in some sense surprising, but in another sense not. We saw a fair amount of disagreement between the reward scores of each of these models. They're all the same reward model, just trained and initialized independently and separately. So this is not an anomaly; you can actually play around with this on a very large test set of examples.

[2:36] This is a real problem. There is often a lot of variance on a per-string basis, on a per-prompt basis, across reward models that have been independently trained. Now one can speculate and come up with a bunch of natural reasons why this happens. So you can question the reward modeling process right from the basics. I'm not sure humans really have a preference model in their heads, which is what is used in reward model training. The other thing has to do with the fact that the training of the so-called reward model itself is a stochastic, dynamic process. It can lead into non-convex landscapes and result in fairly varying reward models, right? And to add to all of this, there is the paucity of these binary preference data that is usually collected in relation to the scale of these reward models.

[3:31] So all of these are a problem, and one could imagine the downstream consequences of just taking a reward model that someone trained or you trained, and just taking it and optimizing for “alignment” here, for the reward. Our prescription about how to deal with these potentially inaccurate reward models, or one such reward model, is to actually be aware and do some extra work to quantify the uncertainty that the reward model has, with respect to a given input or a generic input. This can be done by statistical methods like ensembling, perhaps bootstrapping and so on. And once you have some decent idea of the uncertainty of a reward model, the way you can use that is to basically encode the constraint that the LLM should not move too far in directions that the reward model is not feeling confident about. So this is a recipe that we propose.

[4:31] You can reason about this in terms of a multi-armed bandit problem where there's a lot of uncertainty in some arms and very little in some other arms. And there is a certain robust or conservative solution that usually yields better, and less risky, rewards than what you would do when you just blindly follow the main rewards. So just to ignore all the math, we have a simple prescription of this so-called variance-aware RLHF, which you can actually show is equivalent to just being conservative in the sense of the usual RLHF problem and maximizing a lower bound on the rewards. Let’s go ahead a couple of slides.. skip to the end. Thanks. I put some future work here on the slides. Thank you.
