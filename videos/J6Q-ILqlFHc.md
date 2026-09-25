---
id: "J6Q-ILqlFHc"
title: "Noam Brown - High-Compute Alignment & Control [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=J6Q-ILqlFHc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-07-30"
duration_seconds: 486
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Noam Brown - High-Compute Alignment & Control [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=J6Q-ILqlFHc) · FAR․AI · 2025-07-30 · 8:06

## Description

```text
Noam Brown presented Stephen McAleer's view that AI alignment requires techniques that scale with RL compute, suggesting adversarial training, scalable oversight, and model organisms as exciting candidates within that paradigm. 

Highlights:
High-compute RL agents are harder to align
Deception and power-seeking increase with RL compute
Low-compute post-training fails for deception
Adversarial training and scalable oversight can leverage RL compute
High-compute deception detectors are limited by scarce ground truth data
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Noam Brown: So I'm giving this talk on behalf of Stephen, who unfortunately could not make it. There is this great interesting dynamic where I disagree with some of the things that he said in his talk, on the slides. And so I think what we agreed is that I'll present his material, and then I'll just point out when I personally disagree with some of the material. Hopefully, that should make it more interesting for you all. So yeah, the main takeaway from this talk is that high-compute alignment is necessary for safe superintelligence. So, Stephen wants to start by making this point that we have an old paradigm for post-training and alignment and a new paradigm centered around reasoning models. So, the old story is we pre-train a really capable pre-trained model, and then we do some post-training via SFT and RLHF to align it to what we want.

[0:58] And in this case, alignment is pretty well understood. But when we move to high-compute RL agents, the story is different because now, these models are much more capable, they're much more goal-oriented and they're much harder to align. Now, I don't necessarily agree with this point, actually. And I think my view is that I totally agree that the high compute RL agents are much more capable. And that makes the alignment problem much harder. But I think that fundamentally, the problems that we see with things like reward hacking are amplified with high compute RL agents that are, in general, more capable, but is not necessarily a fundamentally different problem. But in either case, one thing that both Stephen and I do agree on is that these agents are much more capable and that creates a lot of problems. And we've already seen this, for example, with Anthropic's work on alignment faking. And I don't think it's outrageous that we will soon have these models being able to recognize that they are being evaluated in a test environment and act differently when they're being evaluated versus when they are actually deployed in the real world. And so these are the kinds of things that we should be treating quite seriously.

[2:15] And there's a reasonable hypothesis that these models could be more power-seeking. There is this view that power is essentially a sub-goal to any other goal that you want. And so we might expect that more capable agents that are more capable of gaining power might seek to do so as a sub-goal to anything else that they are trying to accomplish. And so the issue of alignment becomes much more important and much harder when we move to these more capable models. So there are things that have been tried and that might seem reasonable to try, but I think both Stephen and I agree are not sufficient. So one is what he would consider low-compute post-training, which is basically like after you're done with your whole training of the model, including the RL training, that you just do a little bit of alignment training to make sure that the agent, you know, give it a few examples of basically RLHF. Give it a little bit of RLHF to align it to do certain behavior.

[3:20] And the issue here is, you know, one potential issue is that the model might be able to differentiate between the tasks and the training that you're doing to align it and other more real-world settings. And so, it might become aligned for this subset of tasks or environments where you're focusing on alignment. And then in everything else, it will continue to be unaligned. And it'll be very difficult to tell the difference because you've done this low-compute post-training only for some subset of tasks. The other point that he makes is that it might seem reasonable that you can control these models and monitor them with simpler, smaller models that are more trustworthy and easier to control. But he makes the case that actually this is unlikely to work at scale because the agent models, like the reasoning models, are going to become more and more capable and they will eventually be able to outsmart the simpler models that are monitoring them.

[4:29] Now, I don't necessarily agree with this. I think it is a valid concern. But I do think that it is possible for smaller, weaker models to be able to monitor larger, more capable models because the monitoring task is easier. But it's certainly a cause for concern. So, then what's the answer? The answer is that basically, we need high-compute RL alignment. We need alignment techniques that work with scale in the same way that our agents are able to become more capable with scale. So what does this look like? Well, there's a couple of different options. So one is adversarial training, and another is scalable oversight. And so Stephen draws this distinction between these two because adversarial training, he views as basically training a very robust grader or monitor with ground truth data, whereas scalable oversight is more about training techniques and monitoring techniques that don't rely on a ground truth.

[5:33] And he also points out it would be really useful to have, basically, a model organism, some way of studying how hacking and misalignment occurs in high-compute RL so that we can better understand what is leading to misalignment. Is it because the model is hacking the reward model, or is it because it's goal-oriented and doing long-agency tasks? If we can narrow down what is the cause for misalignment, then we can better solve the problem. So basically, the solution that's proposed is: train a robust model via high-compute adversarial training, and then use these robust models to align agents during high-compute RL. So basically, always doing the alignment work during high-compute RL, during the training of the model, not just as a small final step. And then also, using these robust monitors and models to monitor the agents when they are acting at test time as well.

[6:36] Now, in particular, Stephen points to this idea of basically training a robust grader, which you train with a minimax, kind of like two-player, zero-sum game-like setting, where you want to train a discriminator that can discriminate between hacking and non-hacking. And the key here is that it has access to a ground truth. And the process of making this discriminator adversarially robust is that you train a generator to try to trick the discriminator. So, it's trying to find these trajectories that maximally fool the discriminator. And in this process, you can train a robust discriminator. Now, one caveat to this is that it does rely on having a ground truth to tell if the discriminator has been tricked or not. And so there is a risk, though, that in a setting like this, that you can train a discriminator that is very robust for settings where you have a ground truth, but is potentially not [reliable in other settings]. And you're just relying on the fact that this will then transfer to settings where you don't have a ground truth. So that is a limitation of this approach, but it's certainly a promising direction.

[7:46] So that is it. And yeah, the main takeaway is to focus on mitigations that scale to superintelligence. All right, thank you.
