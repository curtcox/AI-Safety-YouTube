---
id: "beBRdnM-skI"
title: "Joseph Bloom - Future Oversight is a Key Crux in AI Safety [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=beBRdnM-skI"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-15"
duration_seconds: 606
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Joseph Bloom - Future Oversight is a Key Crux in AI Safety [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=beBRdnM-skI) · FAR․AI · 2026-04-15 · 10:06

## Chapters

- 0:00 Intro
- 0:39 AI Control
- 1:26 Three Components
- 2:39 Literature Review
- 3:28 Domains
- 4:49 Consensus
- 7:00 Ideas
- 9:23 Recap

## Description

```text
Joseph Bloom (UK AISI) leads Project Lighthouse, a strategic analysis examining how AI oversight capabilities might deteriorate as systems advance. Through literature review and interviews with ~25 experts, his team identified loss of monitorability as a critical risk. While chain-of-thought reasoning enables today's oversight, experts broadly agree this necessity will disappear, and even current CoT monitoring suffers from false positives and faithfulness issues. Surprisingly, incident reproducibility emerged as an overlooked but vital oversight property. The work reveals substantial disagreement in the community on technical questions affecting governance. Bloom advocates for cheaper interventions like measurement, holdout monitoring methods distinct from training targets, and avoiding architectural shifts that reduce auditability. His core message: do work that resolves cruxes, because current disagreements are solvable and oversight degradation would make future AI systems much harder to align and control.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Intro

[0:00] Hello, it's great to be here. The topic of my talk today is that future oversight is a key crux in AI safety. I'm using oversight in a very general sense—I'm not speaking specifically about scalable oversight. This is one of the main things that my team thinks about at UK AISI. I want to ask everybody in this room to consider this question: is AI alignment a hard, unsolved problem? If you don't think much about alignment, then think about control. Do you think controlling future AI systems will be possible, easy, doable? And think about why. One crux that I think many people in the room have is that they think AI alignment or AI control is

### AI Control

[0:41] something that will be enabled by the amount of oversight we have of these systems. So when they do things that we don't like, we see that. When they do things for reasons we don't like, we can debug that. When training doesn't work the way we want it to, we have ways of understanding that. I think that currently there's a view among many people in the community that for the systems we have today, this is by and large quite possible. And I think that's great. The question is, do we expect that to continue? A useful frame that my team has been using is "loss of monitorability." It's not a perfect framing, and there are parts of it that I'm not entirely sure are true. The

### Three Components

[1:26] three components are: we can confidently assess and mitigate risks from current AI systems— no, monitorability today is not perfect, but we seem to be okay, and various people seem to be ok continuing what we're doing and seem comfortable deploying these models in a lot of contexts. There are many things that are true about systems today, I like to call these properties exactly what is true about systems today, whether it's the systems themselves or how we're deploying them, or the mitigations; there are things that are true about the models today that make this possible. And then the main intuition is that these things might change or degrade. Obviously a lot of people in this room have thought about chain-of-thought monitoring, whether neural architectures might result in us not being able to monitor the chains of thought of these systems. I think to the extent that there are many properties today that might matter, I'm quite interested in enumerating those and understanding them.

[2:26] My team has been thinking about this, and we've decided to attempt to get the best possible strategic overview of all the possible pathways to current systems being harder to oversee. Can we enumerate the oversight-relevant properties of current

### Literature Review

[2:42] models? Can we think about all the mechanisms by which these properties might deteriorate or change? And can we understand what we might do about that? We have a couple of ways of trying to answer these questions. One of the main ones is doing very comprehensive literature review. We've interviewed many people from many different labs and inside UK AISI to ask them these questions in a very open-ended fashion—not asking them to opine on specific questions, but asking them what kinds of ideas come to mind. This work is ongoing, and I apologize that I won't be able to share the high-level findings in quite as much detail as I would like. In the course of doing this work, we've noticed it's easier to talk about domains. We have:

### Domains

[3:31] the actions of models; chain of thought, currently text, but maybe there might be specific activations in the future; latent representations for current models; the way these systems store and share memory, currently a lot of text is being used here but that might not always be the case; incident reproducibility, which was one I wasn't expecting to come up as frequently as it did—this is not necessarily a property of the system itself so much as the deployment environment, but having systems where the environments in which we're deploying them are such that when there are issues we can go and debug is something that could degrade; and training—the fact that we can train models today, that maybe they can't gradient hack, that we can do elicitation without training or honesty training, and how far that generalizes. There are underlying properties that would maybe shift in the future, so understanding those I think is quite important.

[4:43] I thought I'd go deep on chain-of-thought monitorability. I don't want to claim that

### Consensus

[4:49] there is consensus, but we heard from a lot of people that it's very, very useful—probably the most useful thing we have today for monitoring AI systems. A number of people also highlighted that you can't really convince people of very concerning things with chain-of-thought monitorability, because you can get things like false positives and chain of thought is not always faithful. So even this thing that we think is the best, most valuable property of current systems, it's not clear that it really has many of the properties we would want it to have. Some people think that we're going to lose this and that future systems are not going to reason in chain of thought, and that this is inevitable. Some people think that's urgent; some people don't think it's urgent. The fraction of people we spoke to who seemed optimistic about how this is going to go was fairly low. The sense I got was that the necessity to reason in chain of thought is almost certainly going to go away, and it doesn't really seem like that many people are disagreeing with that. The propensity to verbalize some amount of chain of thought was something that some people thought might hang around for quite a while and be quite useful.

[5:55] On the mechanisms: sudden architectural changes are clearly the one that gives most people anxiety. The question is whether this is going to be state-of-the-art, whether you have to do that because other companies are going to do that and you need to compete. Additionally, this idea of not applying gradient pressure to the chain of thought— because outside of frontier labs, we don't know many of the details about how training is occurring there. There is a reasonable amount of skepticism about whether we can really be sure we're not training against the chain of thought. There are a number of mechanisms, especially in our literature review, that suggested you might not think you're training against the chain of thought but you might actually be doing so. One of these is outcome-based supervision spillover—there's a great paper by Alex Turner on the topic.

### Ideas

[7:01] The ideas I am sharing here are informed by the survey, but also my own thinking. In terms of technical approaches to dealing with possible degradation of oversight, I think there are common themes. One is: don't optimize against your monitoring methods—just really don't do that. Actually measuring whether or not you're doing that, and understanding whether two methods are similar enough that training against one will spill over to another, is an open technical question that is quite interesting. A simple idea is to have methods that are very different from the methods you're training against, that you hold out, and to establish what would be good holdout methods. Making a stronger argument that you should hold these out, I think there isn't as much consensus there as it would be nice to have.

[7:59] A possibly quite costly measure, but one that there might be a business case for, is just don't make big architectural shifts in ways that will reduce monitorability or auditability. Don't create a model that will be hard to oversee. On the governance side, I want to be very clear that these are ideas we're playing with—I don't want to strongly propose them specifically. I think monitoring is clearly very useful. One argument that maybe doesn't get enough airtime is that if chain of thought is useful for debugging systems, or the monitorability properties of models are useful for debugging them, then that's important for capabilities too, and we're not going to want to move to architectures where that's really costly. Making that argument more clearly might be a valuable thing to articulate.

[8:58] There are lots of cheap approaches to maintaining monitorability—just start measuring things might be a good example. And to the extent that you can't always share everything entirely publicly, sharing as much as you can with groups like third-party auditors seems quite valuable. We're going to publish a lot more of the findings from the report, and there will be subsequent projects thinking about these topics.

### Recap

[9:24] To recap: loss of monitorability would make alignment and control of future systems much more difficult—I think that's probably not too contentious, but if you think it is, let's talk about it. My team at UK AISI is trying to form as clear a strategic picture of this as we can, to enable our governance-adjacent technical work and to enable other governance-adjacent technical work. There is a lot of disagreement right now in the community—I was surprised how much disagreement there was. My ask for you is: do work that resolves cruxes. I don't think we need to disagree as much as we currently are. I think we can do work that resolves our disagreements. Thank you.
