---
id: "w0OOk9iLazI"
title: "Generalized Adversarial Training and Testing | Stephen Casper (MIT)"
url: "https://www.youtube.com/watch?v=w0OOk9iLazI"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 325
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Generalized Adversarial Training and Testing | Stephen Casper (MIT)

[Watch on YouTube](https://www.youtube.com/watch?v=w0OOk9iLazI) · FAR․AI · 2024-09-10 · 5:25

## Chapters

- 0:00 Models good at what we train against
- 1:02 Smiley shoggoth: hidden capabilities resurface
- 2:17 A factor of safety for AI
- 2:54 Generalized attacks: latent space and fine-tuning
- 3:23 Past, present, and future work on LAT

## Description

```text
Stephen Casper (MIT) on generalized adversarial training and testing, and why robustness must be measured against attacks stronger than deployment.

In this short FAR.AI talk, Stephen Casper (Cas), a PhD student at MIT advised by Dylan Hadfield-Menell, makes the case for generalized adversarial training and testing. Language models keep proving capable of exactly what we try to train out of them, with red teams reliably extracting harmful instructions even from state-of-the-art safety-tuned models. Casper frames this as a smiley-face-on-a-monster problem, where methods like RLHF hide latent capabilities rather than removing them, so they resurface under attacks or modifications.

Borrowing the factor-of-safety principle from safety engineering, he argues models should be stress-tested against attacks stronger than anything expected in deployment, including latent-space attacks on activations and few-shot fine-tuning attacks on weights. He walks through past, present, and future work on latent adversarial training (LAT), including results that match stronger baselines with far less compute, remove backdoors without knowing the trigger, and improve unlearning.

0:00 Models good at what we train against
1:02 Smiley shoggoth: hidden capabilities resurface
2:17 A factor of safety for AI
2:54 Generalized attacks: latent space and fine-tuning
3:23 Past, present, and future work on LAT

Stephen Casper (MIT): safety tuning tends to mask a model's dangerous capabilities rather than remove them, and generalized adversarial training aims to close the gap between the failures we find and the ones we miss.

Learn more: far.ai
Newsletter: far.ai/newsletter
Subscribe for more talks from FAR.AI events
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Models good at what we train against

[0:04] So hey, my name is Cas, I'm at MIT, advised by Dylan Hadfield-Menell, and I'm excited to chat a little bit about generalized adversarial training and testing. The motivation for all of this, I think, can be expressed largely by how we keep observing that language models are really good sometimes at things that we try very hard to make them bad at. My favorite example of this is the most cliche one that's out there. That's, that red teams have consistently found a wide variety of different techniques for getting instructions for building bombs from modern state of the art safety aligned large language models. That's something that every one of these papers up here does. Specifically, getting instructions for building bombs. And this is really an ongoing process. A new development has come about a week ago when Grayswan AI released their Cygnet model. And Cygnet is awesome, state of the art, very very robust. But that didn't stop red teamers from within about a day of the model's release from finding some very simple prompting strategies that were able to get instructions for building Molotov cocktails from it.

### Smiley shoggoth: hidden capabilities resurface

[1:02] So we seem to have on our hands a classic smiley shoggoth situation, where we have techniques like RLHF that are really good at putting a smiley face on the monster and making models behave quite nicely in most typical situations. But what they do not seem to be good at is removing these latent capabilities very deeply. And we see these capabilities resurface and cause harm pretty consistently in the face of anomalies, or attacks, or modifications to a model. The way I like to think about this problem as someone who works on red teaming, is in these terms. We have these language models and there are many possible inputs for them. The input spaces are beyond hyper-astronomically large. So we're never going to be able to ensure that they're always safe or almost always safe by brute force enumerating over the input space. Instead, we have red teamers use heuristic searches for relevant or important failure modes in ways that are efficient.

[1:54] But we're always going to see this gap between failures that are identified by developers and unforeseen failure modes. As AI safety people, we look at this problem, and one way to characterize what we want to do, is we want to take this gap, and we want to 1. Shrink it, and 2. Help ourselves infer how large it might be.And that's where generalized adversarial training and testing comes in.

### A factor of safety for AI

[2:17] Generalized adversarial training and testing is trying to take a page from a classic safety engineering book. It's a really common principle in safety engineering to design and test systems in order to try to make sure that they are capable of withstanding stresses that are at least as strong, and ideally stronger, than they're meant to face in deployment. For example: in construction, buildings will often be built with a factor of safety of five or something, meaning that the building is designed - and ideally tested - in order to withstand five times the maximum load that it's designed to face under its maximum occupancy. So what's the analogy with AI and large language models?

### Generalized attacks: latent space and fine-tuning

[2:54] I think we're starting to see and are going to continue to see a lot more work on generalized attacks, specifically model manipulation attacks, where a model is evaluated under small perturbations to its activations through latent space attacks, and small perturbations to its weights through few-shot fine-tuning attacks. And I want to take the next few slides to just chat a little bit about some past, present, and future work involving latent adversarial training and generalized adversarial testing. Some past work that I have done with collaborators is

### Past, present, and future work on LAT

[3:28] focused on untargeted latent adversarial training. We released this in February, and we were able to find some nice results in which latent adversarial training gave models a much more generalizable type of robustness than adversarial training alone. As far as present work goes, on Tuesday a paper is going to drop on arXiv on Targeted Latent Adversarial Training, from some more collaborators and I. In this case we try to apply latent adversarial training in a pretty diverse way to improve progress on some important problems, one of which is making models more robust to jailbreaks. One of the top line results here is that we're able to use targeted latent adversarial training to beat R2D2 with 35 to 750 times less compute, depending on what compute measurement criterion you use. Another thing that we do is try to remove backdoors without any knowledge of a Trojan trigger. And we're able to do this fairly successfully. And the results from our paper are about as encouraging as they could be, from the perspective of latent adversarial training being a solution to the sleeper agents problem, which Anthropic posed earlier this year. That's pretty nice.

[4:29] The third and final thing that we do is we do more effective unlearning with latent adversarial training. And we're able to strengthen some existing techniques by adding LAT to them, but we're also interestingly able to find that LAT confers better robustness to re-learning these techniques through few-shot fine-tuning afterward. As far as future work goes, what I'm working on next involves linking generalized and input-space threats. Specifically, I'm doing some work with Zora Che and other collaborators in order to test the hypothesis that robustness to latent space and few-shot fine tuning attacks can predict robustness to hard to foresee input-space threats. So if you're interested in this, find me and let's talk about it. I want to say thanks to everyone and let me know if you want a sticker and let me know if you want to see a Google Doc explaining our current work and project on generalized adversarial evaluation.
