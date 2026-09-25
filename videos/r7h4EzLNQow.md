---
id: "r7h4EzLNQow"
title: "Jacob Pfau - Scaling Alignment Research via Safety Cases [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=r7h4EzLNQow"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-25"
duration_seconds: 777
is_short: false
chapters: 9
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Jacob Pfau - Scaling Alignment Research via Safety Cases [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=r7h4EzLNQow) · FAR․AI · 2025-06-25 · 12:57

## Chapters

- 0:00 Introduction
- 0:19 The core problem
- 1:19 Safety case orientation
- 2:03 Safety case example
- 3:36 Business as usual approach
- 4:42 Example
- 6:27 Learning Theory
- 8:56 Deployment
- 11:29 Conclusion

## Description

```text
Jacob Pfau explains how the UK AISI alignment team uses safety cases to scale AI alignment research by breaking down complex safety problems into testable components. 

Highlights:
Using safety cases to structure alignment work
Current AI oversight techniques fail at scale
Breaking down alignment into sub-problems and assumptions
Paralellizing solutions to alignment challenges
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:04] I'm on the alignment team at the UK AISI and I'll be talking about our alignment team agenda for taking a safety case orientation towards scaling alignment research.

### The core problem

[0:19] I should say we're a new team at AISI, and we are trying to do both safety casing using—towards alignment safety cases and doing funding of alignment work. So, here's the core problem we're trying to tackle. “Existing methods are inadequate for scalable oversight, even ignoring deceptive alignment.” We don't have sufficient objectives to supervise tasks where we don't have pre-existing human labels and the sort of default business as usual, training objective is to just train on cases where we do have verifiers and then use models in cases where we don't and sort of hope that it works out. And we want to do better than this. So, what can we try to do?

[1:14] Well, let's break it down into a couple of bets we're taking on the alignment team.

### Safety case orientation

[1:19] First, we want to take a safety case orientation to identify research problems necessary for reliable, scalable oversight. So, that means decomposing an alignment safety case into what sort of assumptions, empirical validation and methods development we need. And then, given this breakdown into sub-problems, hopefully, we can make those assumptions into crisp theoretical statements or clean evaluations that we can take many shots on and parallelize research in this direction.

### Safety case example

[2:03] So, what does that look like concretely? I'll work through an example, using—built around a—safety case built around debate but our hope is that this protocol is—this approach of taking a safety case first decomposition is something reasonably general and that you could drop in a different scalable oversight method here and still come out and find that these same sub-problems are important. So, as your headline of course you want some claim that your model is safe to use over some distribution of problems and now we want to break this down into the sub-claims we need to hold to have this headline claim be true and break it down into concrete research problems at the bottom level.

[2:54] So, here everything is phrased in terms of debate. So, we want to know that we have a debate protocol which is safe at equilibrium that any debater which—any equilibria of our game is honest and then, we need empirical evidence, of course, when we train on this objective that we've reached the equilibrium and that if we had—we could imagine a different scalable oversight objective and we want to know that we've converged on our reward function. How does this sort of approach relate to other approaches? We

### Business as usual approach

[3:39] can compare it to—on the left-hand side, we sort of have the business as usual, pure empirics approach. The issue with this is that it's hard to cover all the cases in advance. We have a number of data sets like GPQA, StrongREJECT that give us some coverage of the behaviors we need but to do better than that we need some sort of—some sort of theory. What does honest behavior of a model look like? The best thing that we could hope for would be full verification, a proof that model M obeys some spec and only outputs safe non-backdoored code, on any input we give it. This seems hard. So, we're hoping for a sort of middle ground where we're hoping to come up with algorithms that say “at equilibrium once you've converged, we satisfy some safety property” and then, we have some empirical data that says, “okay, it looks like we've converged to that optimum.”

### Example

[4:43] So, again, we think this is a pretty general approach but let's see how this looks like in detail. What can we do in this direction? Here's an example we have in progress work led by Jonah Brown-Cohen at GDM on a new protocol for debate which hopes to overcome the obfuscated arguments problem. So, I won't go into too much detail here but the difference to prior work is that the burden of who needs to decompose claims is different from how you do the recursion in debate will change and hopefully, modulo some assumptions about stability of arguments. This means that we can avoid the obfuscated arguments problem and ensure that at equilibria of this game or all equilibria—approximate global equilibria are honest.

[5:46] So, I said the safety case approach is useful in alignment and hopefully, not just for promoting debate. So, what does this look like? Well, in a safety case, you want to have some deployment context with some assumptions about what you need to get safety. You need some method but where do you go from there? What other assumptions you need? Of course, you need some convergence you need to know that your model converges and this is like essentially you need to block exploration hacking. So, I'll go through a couple of examples of what sort of work we think is needed in this direction. So, as a first example, we could turn to some learning theory. Of course, when you have a

### Learning Theory

[6:33] convex loss landscape, you have some proofs that you can converge efficiently using SGD. But usually for the models that are used these days we're not in that setting and so, we might want something different. We might turn to, for instance, singular learning theory and ask is there some canonical way to basis over which we can do perturbations to weights and show that our performance—our current performance which appears converged if we look at—loss curves is also robust to perturbations in such a way that gives us confidence that we're not exploration hacking. And ideally, we could draw on more theory here to find training algorithms which we get evidence—are not—don't have near equilibria policies which are effectively exploration hacking but we're pretty far from such results so we're excited to fund work in this direction, either using SLT or other relevant tools.

[7:46] Here's a second approach we could reframe potentially the exploration hacking and backdooring problems as ones of a eliciting bad context. So, you have some—in this setting, we imagine we have some distribution of problems where our model looks like it's behaving fine, it achieves good reward, but we're concerned that the model is scheming or somehow otherwise knows that there's some counter argument or some nearby input where it would behave badly. How could we elicit those nearby inputs that seems to require white-box search tools to do efficiently but we think that this could be a useful reframing of the exploration hacking problem that might lend itself to progress.

[8:42] So, here we want to both probably create model organisms and iterate with interpretability methods to make progress.

### Deployment

[8:56] So, now, let's imagine that we have a scalable oversight objective. We've secured some exploration guarantee and now, we want to deploy. What does deployment look like? Probably, you're going to be querying your model a bunch of times. You want your model to be safe to use to advise throughout your R&D process and as a co-pilot, but you have some limited ability to quantify your reward and identify good behavior. So, if you query your model a bunch of times, how do you know that your model is not misleading you systematically in one direction over time. It might be the case that locally all responses look good and they are in fact reasonable responses, but, for instance, your model is systematically hiding some direction of research that you could have explored that it knows of or it's setting up surface area for later backdoors in your codebase.

[10:01] So, we can sort of gesture at what this might mean formally. You have some reward that has a large solution space and then, you're concerned that there's some side objective that the model could be optimizing for here Q. How do you avoid this dynamic? Well, one thing that you could hope for is to train with maximum entropy, RL, over some state space but as we said, we're generically expecting to be in natural language and in code, in a very large action space and so, it would be intractable to do, to converge to the reward-maximizing maximum entropy regularized policy. So that doesn't seem satisfactory. So, we're also—we've been thinking about what—whether we can define something like an adversarial game such that at the optima of this game with respect to some limited class of tests, model outputs are pseudo random in the space of solutions of high reward solutions. So that might give us an intermediate thing between maximum entropy and unconstrained generation which blocks such adversarial optimization.

### Conclusion

[11:29] Taking a step back, I've given some examples of how scalable oversight solutions and interp learning theory might feed into a safety case. Speaking more broadly, our alignment team plan is to try to continue on this process of sketching safety cases. We currently have a draft of a debate-based scalable oversight safety case, but we want to use that to identify subproblems that are important to reaching an alignment safety case and then, fund as many shots on these subproblems as possible as we saw for exploration hacking. There are many different approaches to try to get guarantees there, and we believe that a lot of these are somewhat neglected and so, we want to fund both theory on these methods, data sets, alignment evals, and, of course, the methods themselves.

[12:27] There we go. So, please go ahead if you're interested, we're doing an RFP at AISI for both alignment control and safeguards teams and you can fill out our alignment team expression of interest form there. Thank you.
