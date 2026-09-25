---
id: "bvLJqYIbLfA"
title: "Ryan Lowe - Full-stack alignment [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=bvLJqYIbLfA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-20"
duration_seconds: 652
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Ryan Lowe - Full-stack alignment [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=bvLJqYIbLfA) · FAR․AI · 2026-04-20 · 10:52

## Chapters

- 0:00 Introduction
- 0:15 Fullstack alignment
- 0:40 Why fullstack alignment
- 1:30 societal harms
- 2:24 institutions
- 6:40 Language models
- 7:25 Market intermediaries
- 8:55 Conclusion

## Description

```text
Ryan Lowe (Meaning Alignment Institute) argues that AI alignment must shift from focusing on individual AGI systems to building "AGI-ready institutions"—the coordination infrastructure needed for societies where millions of AI agents interact with humans. Current human institutions like regulation were designed for slow human optimizers and won't scale to fast AI agents creating problems faster than reactive approaches can address. The solution requires a comprehensive grid of new institutions spanning multiple scales and types, from AI comms management to rapid dispute resolution. Language models enable previously cost-prohibitive coordination mechanisms, like market intermediaries that assess whether services actually improve human well-being rather than just delivering products. This reframes alignment as institutional design requiring collaboration across mechanism design, law, and governance—not purely technical AI safety.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:00] Hello everyone. My name is Ryan and today I'm going to be talking about full stack alignment, or why alignment means creating what I call AGI-ready institutions.

### Fullstack alignment

[0:15] One of the premises of this work is that the project we in this room are collectively engaged in is not really the project of aligning an AGI singleton, but instead aligning a society of AGIs and humans. What that means is it requires a shift in our research portfolio. In this talk I'm going to talk about what this research might look like.

### Why fullstack alignment

[0:41] But first, why might that be true? Empirically, we're seeing that this multi-agent world is the world that we're living in. We have millions of agents going around and doing stuff. Some of them have bank accounts, crypto accounts, they can buy stuff. Each of these agents is aligned to a different principal—some aligned to different users, different companies, and so forth. Essentially what we're doing is we're building a society of AGI or AI agents before we have any of the coordination infrastructure that makes society work. That seems bad; we should do something about that. More specifically, many of the societal harms are not always predictable from the behavior

### societal harms

[1:34] of individual agents. Even if we were to solve the AGI singleton problem, there's still the incentive to build unaligned AGIs. You can imagine a company building a very addictive chatbot, or maybe a nation using a model for mass surveillance. These are all things that are important to think about. There are many other people who've been thinking about this and making this case, going back at least to Drexler. There's a paper later that'll be presented by Matija that makes a similar case. So that's the background. Now how do we do it? Maybe it seems hard, and that's why we haven't been thinking about it so much. I talked about coordination infrastructure. In human societies,

### institutions

[2:29] we call those institutions. Institutions are the rules, norms, and mechanisms that structure how people interact. When I say this, many people in this room might be thinking of governance and regulation—these are important, but they're only a small slice of the kinds of institutions that humans use to align human societies. This is a more comprehensive view: a grid of existing human institutions. The rows are the scale of institution and the columns are different types of institutions, which use different kinds of information and require different kinds of expertise. For example, in the incentives column there's expertise in mechanism design.

[3:27] If you're looking at institutions that deal with preferences, we might consider auction design, electoral systems design, and so forth. Regulation is here, in the bottom/middle sections, but there are many other examples: global markets, courts and judiciaries, mission-driven organizations. Lots of ways that humans align human societies. These institutions are imperfect, but they've been more or less good enough for aligning humans so far and making society work. There's a problem, which is these are not going to be good enough for a world with AGIs that are agents going around and doing stuff. In particular, they were built for a world with human participants who are, compared to AI systems, slow and mediocre at optimization.

[4:36] If we take regulation as an example, regulation can be extremely useful, but it's a reactive approach—it sets constraints on the behavior of actors after we've noticed some problem. In a world where AI agents are creating new problems much faster than we can regulate, we need to do something differently. We can imagine mechanisms where good outcomes are the natural equilibrium that emerge from the interaction of these agents. We need a richer toolbox of approaches to bring to bear on the question of aligning a society of AGIs and humans. More generally, we need an analogous grid for a world of AGIs and humans. The rows and columns are the same, but here are some examples we've pre-populated of the kinds of things we might need. We might need AI comms management, because if you have a million agents using the same information infrastructure that might cause pollution—we're starting to see some of that already. We might need AI education. There might be disputes between agents that we need to resolve fairly, but much quicker than a human judge is able to do. More generally, we just need different kinds of incentive structures to ensure that what agents are

[6:11] doing actually benefits people. There are a lot of empty cells—this is still an open research agenda. Some of these institutions will look quite a bit like the previous grid; some will be entirely new. My claim is this is the kind of work that we need to be doing.

### Language models

[6:41] There's good news. It turns out we believe that language models open up a new design space for building some of the institutions that we might need. I'm going to give one example in the context of markets. Markets are great, obviously, but there are markets for things we don't need, and markets for things that make our lives worse. As agents get more powerful, they're increasingly going to be able to exploit these kinds of things. What we want is some way to ensure that as agents get more powerful, markets remain tethered to human well-being.

### Market intermediaries

[7:26] My colleagues Joe and Oliver wrote a specific proposal for one way we might do this, which they call market intermediaries. The basic idea is this: right now, if you buy a product or service, the contract is based on deliverables—whether you got the thing that you paid for—and not on outcomes, which is whether the thing actually benefited you. If you ask the question, did this therapy app I used actually improve my mental health, there's no market mechanism right now that asks that question. The reason is that doing this in an automated way at scale historically has been prohibitively expensive. But it's possible that language models might actually change this. We might be able to create systems that assess whether some service actually satisfied someone's deeper needs, and then pay sellers more who benefit people in a certain way—and sellers who don't actually help people in the way they wanted get paid less.

[8:47] I think this is one of the coolest ideas out there, so I highly recommend checking out the blog post if you haven't yet, or talking to Joe and Oliver who are here.

### Conclusion

[8:56] The more general takeaway is that many of the institutions we've designed for human societies were designed with constraints that are no longer true—that language-based judgment is really expensive and really slow. Now that we have language models, there is potentially a whole new space of creativity that opens up in our capacity to design institutions, which we're going to need to do to solve some of the challenges we're going to be facing. To conclude: let's fill out this grid. We're going to need technical work—work on AI normative competence, value alignment, making sure language models are robust and working well in the ways we need them to work well. But we're going to collaborate with mechanism designers, lawyers, all kinds of people. There's some new work in progress on this. Our most recent published work is at fullstackalignment.ai.

[10:02] The thought I want to conclude with is this: you might look at this grid and think, wow, this seems really intimidating—how could we possibly do this? I think that's fair. But part of the reason we believe that is because we take our existing institutions for granted. It seems like they've been there forever, but that's not actually true. We invented them, we made them, and many of them have been invented in the last couple hundred years. We do have agency here. There is a space of optionality, a space of agency and creativity, that we can bring to bear on this problem. Thank you.
