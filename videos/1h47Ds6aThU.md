---
id: "1h47Ds6aThU"
title: "John Schulman - Keeping Humans in the Loop"
url: "https://www.youtube.com/watch?v=1h47Ds6aThU"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 308
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# John Schulman - Keeping Humans in the Loop

[Watch on YouTube](https://www.youtube.com/watch?v=1h47Ds6aThU) · FAR․AI · 2024-02-08 · 5:08

## Chapters

- 0:00 The risks of AI adoption
- 1:12 The leash proposal
- 2:27 Implementing human oversight
- 3:33 Challenges and limitations

## Description

```text
John Schulman - "Keeping Humans in the Loop."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The risks of AI adoption

[0:04] This will be a non-technical talk about a preliminary idea that I thought I would talk about to get some feedback. So there's some unsettling possible aspects of the future, even if we manage to stay on top of the alignment problem and make sure our most powerful AIs are basically doing what we intend. So if things continue getting better, if AI continues getting better, we'll have AI outperforming humans at basically all jobs, and that'll create strong economic incentives to give them more decision-making power over everything and have AIs run institutions, so have AI-run companies. And these companies would potentially just operate a lot faster than human-run companies because AIs can think and make decisions faster, and they don't need the same kinds of motivation and compensation as humans, so they're easier to manage. This will obviously apply to companies, and it might also apply to militaries and governments.

[1:11] So there have been various proposals on how humans can stay in control of

### The leash proposal

[1:19] the future, and so some people have suggested that we should pause. And all of these are flawed in some way, so I'm going to propose another idea that's deeply flawed in its own ways, but at least I haven't heard a lot of people talking about it, so I might as well add it to the discussion. So people have suggested we could slow or pause development in some way, or maybe we should avoid certain types of training which are likely to be dangerous, like doing, say, long horizon, or possibly dangerous, not necessarily dangerous, but doing things like long horizon RL. So what I'm going to propose here is that we can build, when we have sufficiently capable systems, we can build them with a certain kind of self-enforced limit on how autonomous they'll be. In particular, have these systems ask for human approval whenever they're making any kind of important decision. So let's just call it a leash. A leash is a slight misnomer because I'm

### Implementing human oversight

[2:27] going to propose that the like the model itself, enforces these restrictions. So the requirement is basically before taking some kind of consequential action, the AI must ask a human for approval. And this isn't just like pressing "Okay." This would require that the human actually understands the rationale for the action and the and the costs and benefits. And so you might, like... this would actually be non-trivial for the AI to actually achieve, because it might have to teach the human a bunch of relevant backgrounds, and it might have to even give the person a quiz to check that they understood. And we would have to define what counts as a consequential action. This could be a transaction of sufficiently high value or something significantly affecting a person, like, say, firing someone. And, or various other things of that nature. So

### Challenges and limitations

[3:33] I think this is one nice thing about this proposal is it's something we can start working on right now. So we can, given limitations of current AIs, this would actually be a feature that would help for reasons like security, like preventing phishing attacks and so forth. Like, if your AI assistant is going to spend your money or give your credentials to some other third-party site, you want it to ask your approval. So I think this is actually, a kind of useful thing right now. And we can at least get some practice on it. So, yeah, I think this is kind of challenging, but doable with current alignment tech. Of course, there's some problems with this idea, there'll be a lot of pressure to get rid of this, because it'll slow things down. And I think, a pretty serious flaw is that, once you start, I think the most serious flaw is that once you start getting regulators involved, they'll feel a lot of pressure to prevent AIs from doing various things that they should be able to do. Like, in New York City the subways still have conductors because the union of conductors basically lobbied for this.

[4:49] So you could imagine every job category there's some pressure on the government to regulate AI so they can't do their job. So I think this would also remove a lot of the possible benefits of AI. Thanks for your attention.
