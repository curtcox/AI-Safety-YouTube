---
id: "wRTBKwf45Ak"
title: "Measuring AI R&D Automation: What Happens When AI Automates AI Research | Alan Chan (GovAI)"
url: "https://www.youtube.com/watch?v=wRTBKwf45Ak"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-09-07"
duration_seconds: 550
is_short: false
chapters: 15
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Measuring AI R&D Automation: What Happens When AI Automates AI Research | Alan Chan (GovAI)

[Watch on YouTube](https://www.youtube.com/watch?v=wRTBKwf45Ak) · FAR․AI · 2026-09-07 · 9:10

## Chapters

- 0:00 Measuring AI R&D automation (GovAI)
- 0:31 AI companies are betting on automating AI R&D
- 1:01 Evidence: the METR time-horizon trend
- 1:54 Qualitative change: orchestrating agents, research taste
- 2:40 How far we have come in two years
- 3:14 Implication 1: faster AI progress
- 4:02 High-impact and dual-use capabilities arriving sooner
- 4:54 Implication 2: weaker human oversight
- 5:04 The human knowledge gap
- 5:37 Concentration of decision-making
- 6:10 What we still do not know
- 6:36 What technical researchers can do
- 6:51 Experiments on what drives AI progress
- 7:46 Developing metrics for oversight
- 8:16 More AI R&D evaluations, including safety R&D

## Description

```text
Alan Chan (GovAI) on AI R&D automation: why AI systems automating AI research matters, and what technical researchers should measure to track it.

Chan sets out the high-level case. AI companies are investing heavily in automating AI R&D, with CEOs at OpenAI, Anthropic, and Google DeepMind giving timelines around 2028, and coding agents already doing a large share of the software engineering involved. The evidence of progress is both quantitative, including the METR time-horizon trend where models now complete tasks that take human experts more than 16 hours, and qualitative, with some researchers orchestrating teams of agents rather than coding, and models matching human experts at predicting which research ideas will work. He then separates two consequences. Faster AI progress could deliver high-impact capabilities, medical and otherwise, well ahead of expectations, while also compressing the time available to prepare for dual-use ones. Human oversight could weaken through a knowledge gap, as people lose ground-level understanding of what is happening in R&D, and through concentration of decision-making, as the independent viewpoints that improve research decisions drop out. Chan is clear that the net effects are uncertain, and closes with research the field could do: experiments isolating what actually drives AI progress, metrics for oversight quality, and more evaluations of AI R&D, including for safety R&D specifically, so differential progress can be tracked.

Chapters
0:00 Measuring AI R&D automation (GovAI)
0:31 AI companies are betting on automating AI R&D
1:01 Evidence: the METR time-horizon trend
1:54 Qualitative change: orchestrating agents, research taste
2:40 How far we have come in two years
3:14 Implication 1: faster AI progress
4:02 High-impact and dual-use capabilities arriving sooner
4:54 Implication 2: weaker human oversight
5:04 The human knowledge gap
5:37 Concentration of decision-making
6:10 What we still do not know
6:36 What technical researchers can do
6:51 Experiments on what drives AI progress
7:46 Developing metrics for oversight
8:16 More AI R&D evaluations, including safety R&D

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=0IfDd-WNQwrs14Kn

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Measuring AI R&D automation (GovAI)

[0:00] Cool, so this is based on a recent paper. It's actually a different title than what you see on the screen, "Measuring AI R&D Automation." You can also scan the QR code for the paper if you'd like. This is based on work with people at the bottom at GovAI. All right, let's get into it. So Maxim gave you, I think, a pretty good understanding of what's actually going on concretely on the ground in AI R&D automation. My goal for this talk is to give you more of a high-level picture of why is AI R&D automation a big deal and what should we actually do to understand its impacts? So those are the two goals of this talk.

### AI companies are betting on automating AI R&D

[0:31] Firstly, AI companies are obviously trying to automate AI R&D. A lot of resources and money is going to this right now. All the AI company CEOs are pretty bullish on this possibility. Sam Altman thinks they'll have automated it by 2028. Dario and Demis have pretty similar timelines. And at the same time, all the companies are producing coding agents like Claude Code to automate software engineering, which is a large part of AI R&D automation. So they're putting their money where their mouth is. Is the money actually succeeding in going places? By all accounts, or by some accounts at least,

### Evidence: the METR time-horizon trend

[1:01] I think yes, AI companies are making quite rapid progress in AI R&D automation. What are the different lines of evidence? So besides the benchmarks — well, I guess let's start with the benchmarks. There's the METR time horizon plot, which I'm sure a lot of you are already aware of. If you're not, basically this shows the time horizon of different tasks that different LLMs can complete at different percentages of the time. So the x-axis here is the release date of the LLM. The y-axis is the time that the task took a human expert. So you can see fix a complex bug in ML research codebase, that's about between 12 and 16 hours. So notably, this trend is growing exponentially, meaning models are getting better at completing tasks of longer time horizons at an exponential rate. So Mythos right now can complete tasks more than 16 hours long, including fixing complex bugs in research codebases. And there are a lot of other benchmarks that I'm sure you're also aware of where we're seeing really rapid progress in AI R&D automation.

### Qualitative change: orchestrating agents, research taste

[1:54] But it's not just the quantitative results that I think are important. Things also seem to be changing on the ground qualitatively. Some people aren't even coding anymore, basically, and just are orchestrating teams of agents. And it's not just coding either, it's also things like research taste, which might be a little bit more amorphous than coding. So this is a paper from NeurIPS last year that looked at, can language models actually predict which research ideas end up performing better empirically? So they took a bunch of conference papers, and they got human experts and the model to predict which algorithm would end up performing better. And you can see here that models actually perform — the blue bar here — actually perform a little bit better than human experts, which actually was kind of surprising to me, I guess, but is some sort of evidence that we're not just automating coding, we're also pushing forward other parts of AI R&D.

### How far we have come in two years

[2:40] Okay, so of course, coding agents are still kind of unreliable sometimes. They can be pretty lazy, you might need to supervise them a lot, but maybe I think it's just good to take a few seconds to step back and think about where we're at right now compared to two years ago when agents weren't really that useful at all for AI R&D. Now we're asking them to do things like one- or two-shot experimental pipelines, which is kind of crazy in my opinion. So we've come a pretty long way, and it does seem pretty plausible to me that we're gonna get more automation over the next few years.

### Implication 1: faster AI progress

[3:14] So what are the implications of this? What if we get even full automation over the next several years? So I think there are two ways to think about this, or at least ways to split up how to think about this. One is think about the impacts of AI R&D automation for AI progress. So essentially, what is AI R&D automation? It's essentially putting more research labor effectively into the AI R&D process. Research labor isn't the only input into AI R&D, but it's definitely an important input. Just as a little intuition pump, imagine if today's AI, human AI researchers were either 10x fewer or worked 10x more slowly. Progress would probably slow by a lot. So you can imagine if you 10x, 100x, or even 1,000x the effective amount of research labor, potentially progress might speed up a lot as well. Although, as I'll say later on, we don't really have great data on this.

### High-impact and dual-use capabilities arriving sooner

[4:02] So what actually happens if AI progress speeds up a lot? Well, the first is I think you might get a lot more high-impact capabilities much, much more quickly than you anticipated before. This could be both good and bad. Good in the sense of, oh, maybe it'd be very good if we got advanced medical capabilities to accelerate cures for diseases, but at the same time, we also might get more high-impact dual-use capabilities or dangerous capabilities like CBRN uplift. Imagine if instead of, you know, every year or something, we get a sort of "mythos moment" with cyber, we get a mythos moment every single month with a different domain every month, right? So the problem here is that this might really stretch our capacity to adapt to such capabilities, both in terms of the safety research needed to handle such capabilities, and also the policy safeguards we need to put in place in society to secure the world before these capabilities become widely available. So that's the challenge with AI progress speeding up.

### Implication 2: weaker human oversight

[4:54] The other challenge that I want to get into is oversight. So potentially meaningful human oversight of AI development gets a lot worse with AI R&D automation. Two things that I want to bring

### The human knowledge gap

[5:04] up here. One is the human knowledge gap. So right now, just by the fact that humans are involved in AI R&D and just doing things, humans have a pretty good ground-level of understanding of what's actually going on in the AI R&D process. But as AI R&D gets automated and humans aren't as involved anymore on the ground, we might lose the ground-level understanding to point out problems like research sabotage and other problems that come up in AI R&D. So that could potentially be bad in terms of our ability to steer where AI development is going in a beneficial direction.

### Concentration of decision-making

[5:37] The second problem that I want to bring up is concentration of decision-making. So essentially — one way to explain it is, in a usual human organization, whenever you make a decision about R&D, that decision usually goes through a bunch of very different people with very different points of view. And just by the fact of having these very different points of view, your decision ends up being better quality because you get critiques from a variety of different directions. But at the point at which you fully automate AI R&D and you don't really have human researchers anymore, you don't actually have these independent points of view anymore. So that could lead to lower quality decisions.

### What we still do not know

[6:10] Okay, so those are two potential high-level consequences of AI R&D automation. The fact of the matter, though, is that we don't actually know what is going to happen. I think there's a lot of uncertainty about a lot of things. I mean, one is what even is the extent of AI R&D automation within AI companies? Two is will AI progress even speed up? And three is what is gonna be the net effect of AI R&D automation on oversight? Because, of course, AI systems can also help carry out oversight.

### What technical researchers can do

[6:36] So that leads to the second and last part of this talk, which is the pitch for what technical researchers can do to help us better understand AI R&D automation. So this slide is basically just a bunch of ideas that I would be very excited for technical researchers to carry out as research projects.

### Experiments on what drives AI progress

[6:51] The first is experiments on what drives AI progress. So this is pretty important because if we have much stronger evidence that compute is actually a huge bottleneck to AI R&D automation — to AI progress, sorry — then even if we get AI R&D automation, we might not actually get sped-up AI progress, so we might not have to worry about those consequences. So what's the thing to be done here? So there are actually already existing estimates of how much data, compute, and algorithms drive AI progress. The problem is that the data on which these estimates are based is pretty garbage, because basically all the data is confounded. So we're not actually varying, for example, data, compute, and algorithms independently. We're just getting observational data. So more experiments varying these kinds of things and seeing which models end up performing better or which algorithms end up performing better, I think would be very helpful for making better estimates of what drives AI progress.

### Developing metrics for oversight

[7:46] The second thing is developing metrics for oversight, to actually capture things like how bad is oversight getting — are AI systems actually trying to sabotage R&D much more as they get much more capable at it? And then how effective are our oversight systems — not just the ability of human oversight to catch problems, but also the ability of AI systems to monitor for and catch problems that other AI systems cause. So developing metrics for oversight, I think, is a particularly neglected area, actually.

### More AI R&D evaluations, including safety R&D

[8:16] And the last point is just developing more AI R&D evaluations, just to be able to get a sense of the pace of AI R&D automation. So three things I want to particularly point to here. One is evaluations for safety R&D. There basically aren't that many evaluations. To be clear, it is kind of hard to separate safety and capabilities, but to the extent that you can, I think it'd be good to have more evaluations for safety R&D, just so that we can track differential progress and understand if safety R&D is keeping pace with capabilities R&D automation. And then other sort of stuff unrelated to coding, like team management and research taste. That was a bunch of ideas. There are a lot more ideas in the paper for things that technical researchers can do to track AI R&D automation and help us understand its impacts. That's the QR code. Here's my contact information. And yeah, very happy to talk to people about this afterwards as well. Thank you.
