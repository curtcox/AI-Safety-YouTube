---
id: "rxPNrjmAw2Q"
title: "Vincent Conitzer – Game Theory and Social Choice for Cooperative AI"
url: "https://www.youtube.com/watch?v=rxPNrjmAw2Q"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 316
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Vincent Conitzer – Game Theory and Social Choice for Cooperative AI

[Watch on YouTube](https://www.youtube.com/watch?v=rxPNrjmAw2Q) · FAR․AI · 2024-09-10 · 5:16

## Chapters

- 0:00 Multi-agent systems risks
- 1:10 Game theory for AI alignment
- 2:28 Social choice for AI safety
- 3:41 LLMs and human reflection

## Description

```text
Vincent Conitzer from Carnegie Mellon University presenting 'Game Theory and Social Choice for Cooperative AI'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Structuring AI-human interactions to prevent failures
- Risks of algorithmic interactions in multi-agent systems
- Using social choice theory to aggregate human feedback
- Importance of interdisciplinary collaboration

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Multi-agent systems risks

[0:04] Hi everyone. I was asked to represent the Cooperative AI sub community a little bit as well. And I'm not the only representative of that sub community here. We have Gillian, who was just on the panel and made many of these points. But in Cooperative AI, we think a lot about the fact that we actually have multi agent systems; multiple AI agents, but also multiple humans, multiple institutions, and so on. And we worry about things going wrong between them. There's some interesting examples of algorithmic interaction going wrong. A nice one is the flash crash from 2010. Where suddenly, for no good fundamental reason the Dow Jones collapsed, as you see here. It's a complicated story, but a big part of it was algorithms that trade automatically, played a big role in this. Now, the worry is that as AI systems become more capable, and become more broadly deployed, we're gonna see this type of thing happen in a lot more domains. It doesn't require a lot of imagination. But for now we already see AI being deployed and LLMs being deployed in kinetic warfare. So that's a concern.

[1:07] In our lab we think about a lot of this game theoretically. So

### Game theory for AI alignment

[1:11] here is an abstract example where we have a game; we have two agents that each have to pick a number. One picks a row, one picks a column. And the point of this example is that here, actually, we've done a very good job aligning the individual agents in and of themselves, in the sense that their utility function agrees almost precisely with ours as humanity. And the other one, the same thing, but it's a little bit different. They haven't converged exactly the same way. The point of this game is that the only equilibrium of this game actually turns out to be the bottom right corner, where actually everybody, the agents and we, have a terrible utility, even though we got so close to aligning them. And this also means any standard Reinforcement Learning algorithm that focuses only on the agent's own utility, if they both use it, it's going to end up here. That's the kind of thing we think a lot about, as Gillian said before as well: how do we structure things so that this does not happen?

[2:10] So this is a little bit in general about cooperative AI. I want to jump in now to a position paper that we have here at ICML, also with Stuart and others. And this relates back to Oliver's talk where we're thinking about how we align Large Language Models. All the ways that we do so today involve human feedback at some point.

### Social choice for AI safety

[2:30] Here's RLHF and you see the orange boxes where we need human labelers to provide some inputs similarly in constitutional AI. By the way, I'm still stunned that now we have computer science papers where Appendix C looks like this, identifying some human written principles. And then of course there's also good old fashioned prompting. So what you see here was part of the prompt for GPT-4, in particular for how to use DALL-E. And we had a blog post that goes into the details of that and how it changed from month to month that I hope you will find interesting. But the main point here is that all of these involve humans giving feedback in some way or other. And there's of course always the question of which humans get to give this feedback. And if they disagree, how do we aggregate across this. In our position paper, which will be here later at ICML, we argue that social choice theory is actually the right theory within which to think about this problem, and we also talk about how that interfaces with safety - we actually think that this would make systems safer if you do this well, but I'll defer you to the paper.

[3:39] In my last little bit of time, I want to point out something different,

### LLMs and human reflection

[3:42] which is this blog post that I had with Yoshua very recently on what large language models can tell us about ourselves. David made the point on the panel, that in many ways I think that I agree, that the response to ChatGPT has actually been underwhelming. Many people have played around with it and left it at “Well, that's that. Okay, let's go on with our lives,” for many people. But I think what we talk about here, I think that's especially true, maybe even within this community. There's this question of how we should reflect on ourselves a little bit as well. What do these models tell us about ourselves? This also relates to the point I think earlier made on the panel that a lot of us now feel that we don't have the right expertise to answer this or that question. Traditionally it was the non-computer scientists saying I'm not a computer scientist, how can I weigh in on this. And now even the computer scientists to some degree are worrying about this. And I think this is something we need to address. And I think this issue comes up here as well.

[4:47] Maybe cognitive scientists and so on don't necessarily feel like it's their place to analyze these kinds of questions, while we as computer scientists don't either. So I think we want to think a little bit about how we transcend disciplines and maybe build up new institutions that allow us to transcend disciplines in this way. Thank you.
