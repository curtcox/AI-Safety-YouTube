---
id: "CPRS8Ng764Y"
title: "Mantas Mazeika – Tamper-Resistant Safeguards for LLMs [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=CPRS8Ng764Y"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-19"
duration_seconds: 322
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Mantas Mazeika – Tamper-Resistant Safeguards for LLMs [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=CPRS8Ng764Y) · FAR․AI · 2024-12-19 · 5:22

## Description

```text
Mantas Mazeika from the Center for AI Safety presents “Tamper-Resistant Safeguards for Open-Weight LLMs,” showing that improving tamper-resistance for LLMs is achievable but requires extensive red teaming. Reducing accuracy trade-offs and further improving robustness will be needed.

Highlights: 
🔹 Weight Tampering - Addressing fine-tuning and parameter perturbation attacks. 
🔹 Adversarial Training - Dual-stage training with focus on tamper-resistance. 
🔹 Weaponization Safeguards - Improved refusal on biosecurity and cyber-threat prompts. 
🔹 Performance Stability - Results on Llama 3 models show robust tamper resistance.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Thank you. Hi everyone, my name is Mantas, I work at the Center for AI Safety, and this is a presentation on a recent paper we did called Tamper Resistant Safeguards for Openweight LLMs. It's a big collaboration. I have amazing collaborators and I'm excited to talk about the work. In this work, we study the problem of weight tampering attacks, which includes all attacks that on a large language model safeguards that just perturb or edit the weights in some way, including fine tuning attacks, which have been talked about a lot lately. An example of this is that – while the Llama-2 safeguards are quite robust at input-space attacks – it turns out that they can be easily stripped away with a couple of steps of fine tuning. And in fact, I think this was done within a week of Llama-2's release. So, this is a problem because on the one hand, open-weight models are really great. They reduce concentration of power, democratize the benefits of AI, and accelerate academic research including AI safety research. I think in large part, a lot of this work on Large Language Model robustness to input-space attacks would not have been possible without these Llama models because they were the first example we had of robustness to these attacks.

[1:22] But on the other hand, advanced open weight models without safeguards could pose serious risks because if you release a model on the Internet, you are giving it to everyone, including terrorist groups and death cults and you name it. So there's this rock in a hard place problem and people have thought about this problem and tried to figure out ways that you can make these safeguards tamper resistant. There's been lots of prior work on this topic, but before our work there were still no methods that protected large language models from a wide range of tampering attacks. So that's what we set out to study. We came up with this method, which is basically adversarial training, except the adversary can optimize the parameters instead of the inputs.

[2:14] And it's inspired by this earlier work by Peter Henderson et al. which was done on BERT style models. And so just briefly, this algorithm we have this training set of optimization attacks. We focus on fine tuning attacks, to train against. And we have a retain loss and this safety loss and data set, we call this the tamper-resistance loss. And then our method itself has two stages. The first applies some initial just normal safeguard like RLHF or a standard unlearning method. And then we have a second stage of tamper-resistant training. This is the adversarial training loop, where there's an outer loop and inner attack, which doesn't have to be an inner optimization process but in our case it is because we're using fine tuning attacks. And yeah, we found some interesting things while designing this method and trying a bunch of stuff out. Maybe one of the more interesting things is that the method actually works, but the choice of tampering-resistance loss matters a lot to make the method work better.

[3:27] So on the left is what happens if you are maximizing the cross entropy loss of the adversary as your tamper-resistance loss. And on the right is what happens when you maximize the entropy, just make it uncertain after the adversary's inner loop. And you can see the adversary's inner loop in these small boxes, and if you're using this better entropy loss, what happens throughout the course of training is: the outer loop is more stable, but also the inner loop curves up and the adversary becomes less able to optimize their loss. This method actually works, which was crazy and surprising to see for large language models. These are all on Llama 3, 8B scale models. And our results are on two domains. The first is what we call Weaponization Knowledge Restriction. It's basically unlearning on this WMDP dataset. The second is Harmful Request Refusal, and so on the left here we have our on learning results across biosecurity, chemical security, and cybersecurity data.

[4:39] And we do see a degradation in benign performance on MMLU but crucially we're able to improve the tamper-resistance loss, much more highly than it was for the baselines. We see a similar story with for refusal experiments, our experiments there are a little smaller scale, but we were able to improve performance, we have extensive red-teaming results. And that's basically it.
