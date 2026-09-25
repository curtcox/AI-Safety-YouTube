---
id: "7jgzdqvAv-4"
title: "Dmitrii Krasheninnikov – Stress-testing Capability Elicitation with Password-locked Models"
url: "https://www.youtube.com/watch?v=7jgzdqvAv-4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 298
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dmitrii Krasheninnikov – Stress-testing Capability Elicitation with Password-locked Models

[Watch on YouTube](https://www.youtube.com/watch?v=7jgzdqvAv-4) · FAR․AI · 2024-09-10 · 4:58

## Description

```text
Dmitrii Krasheninnikov from University of Cambridge presenting 'Stress-testing Capability Elicitation with Password-locked Models'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Fine-tuning's role in unlocking AI capabilities
- Testing capabilities with password-locked models
- Leveraging high-quality demonstrations for better AI training

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Hello, I'm Dima. I am a PhD student in Cambridge advised by David, who was just on the panel, and today I'm going to quickly talk about this very recent paper with some people from Redwood, Ryan and Fabien, who led this project, and also David. And the paper is Stress-testing capability elicitation with password-locked models. What is a password-locked model? A password-locked model is a model where if you give it a password in the prompt, which could be anything really, then the model would behave normally and would display its normal capability. Whereas if you don't give it the password, the model would not display this capability. So basically it's like a language model with some capability locked behind a password. We train these password-locked models via either fine tuning a pretrained model to imitate a weaker model when there is no password and behave normally otherwise, or just from scratch on a toy task.

[1:08] And these password-locked models are a pretty nice testbed for capability elicitation. In particular, they're nice because with this password-locked model, we know that the capability is definitely there, so we know what to aim for. And we definitely know when our elicitation process succeeded or failed. And most of our paper is just testing different variations of fine tuning at how good are those at unlocking the password-locked models. So for supervised fine tuning, we find that you need very few samples to unlock these models. In particular, here you can see that for the MATH dataset, eight examples already gives you most of the original locked performance, which is insanely high sample efficiency. Whereas for MMLU, it's a bit more because MMLU is this multiple choice dataset, so each individual sample gives you basically just one token of information. We also find that unlocking generalizes super well. So if you are unlocking only some subset of the distribution that's really easily identifiable, then the other subsets are going to unlock as well. Similarly, if you're unlocking .. using samples from a slightly different but also good model, that also totally works and unlocks the model quite well.

[2:49] The place where things are not as rosy, but still are okay, is reinforcement learning. Sometimes we don't have access to nice high-quality demonstrations like we need for the supervised fine tuning and unlocking. And here, unlocking success is really highly dependent on how good the behavior of the model is when you don't give it the password - this locked behavior. Basically, does that locked behavior give you enough signal for the RL process to pick up and reinforce the right kind of behavior? So here we had this model, DeepSeek 7B, which is pretty good at MATH. And then the password-locked behavior - when there is no password - the model just imitates either Pythia 7B, or 1B, or 400M. And for the stronger, locked behavior, we can unlock the model pretty well. All these different colored lines are the different RL algorithms. But if the model doesn't give you much signal, then the unlocking process is just not going to work very well.

[4:03] We started this project mostly thinking about sandbagging, which is this hypothetical failure mode where the model might strategically act below its true capabilities. For instance, don't show the maximum possible level of some dangerous capability for some reason, or maybe not fully critique another AI's outputs. This is on top of regular capability elicitation being quite important. And the takeaway from this work is actually fine tuning is really strong, and it unlocks these password-locked models very easily. And so I think it's like a slight update against model sandbagging being a real big issue. Especially if we have good high quality demonstrations, but even in RL.
