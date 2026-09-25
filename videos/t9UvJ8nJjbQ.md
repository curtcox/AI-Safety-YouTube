---
id: "t9UvJ8nJjbQ"
title: "Anca Drăgan - Implications of human model misspecification for alignment"
url: "https://www.youtube.com/watch?v=t9UvJ8nJjbQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 388
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Anca Drăgan - Implications of human model misspecification for alignment

[Watch on YouTube](https://www.youtube.com/watch?v=t9UvJ8nJjbQ) · FAR․AI · 2024-02-08 · 6:28

## Chapters

- 0:00 Role and AI safety
- 1:45 Evolution of AI objectives
- 2:12 Reward modeling challenges
- 2:46 Human feedback techniques
- 4:24 Risks of improper modeling
- 4:46 Theoretical guarantees
- 5:11 Future research directions
- 5:59 Conclusion and closing

## Description

```text
Anca Drăgan - "Implications of human model misspecification for alignment."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Role and AI safety

[0:04] So I didn't plan on this when I signed up, but I have news to share with you that I'm really excited about. So, a little bit about me, I've been a prof at Berkeley for eight years now working on alignment initially through robotics because robots needed to be aligned. And that was an excuse to do alignment in the near term. I've had the fortune of working with amazing students. A couple of them are actually here today. They're now profs at various places, MIT, Princeton, et cetera. A couple of them are, are still in my lab.... Oh, hi you two. Dylan and Jaime are here. ... and running their own alignment groups. But I decided, with capability increases, it's time for me to contribute alignment work in industry as well. So I'm taking a leave and I signed up to be director for AI safety and alignment at Google DeepMind.

[0:57] Yay, thank you. It's a big, and humbling role. The scope is anything from near term, like the current genAI, to the next one, to the one after that, to the one after that spanning near term to "long term" risks and collaborating closely with responsibility folks. One thing that I wanted to share in this group, for those of you in the Bay Area, is that part of our increased investment in AI safety and alignment is building up more of a group... more of a presence in the Bay Area. So if you're interested in working with me on alignment in the Bay Area, that's where I'll be located as well. Don't hesitate to reach out - email, Slack, whatever works. OK, so putting my Berkeley hat on, I wanted to share a very geeky topic that I'm obsessed with,

### Evolution of AI objectives

[1:50] which is the importance of human model misspecification and reward modeling. I started my career in robotics and I didn't worry about objectives and alignment because robots just didn't work. It was very clear what we wanted them to do. Pick up the thing, don't hit stuff, what does it do? It doesn't pick up the thing and it hits stuff. That was the problem.

### Reward modeling challenges

[2:12] But then, so we were pretending basically the AI problem looks something like this: I have a robot, there's a state space, it takes actions, reward function falls from the sky. And that's the thing that the robot has to optimize. Now when I started at Berkeley, this is a picture from back when DeepMind's AlphaGo beat Lee Sedol. It was very clear that our ability to optimize for objectives was increasing, maybe not as directly in robotics but more broadly. And so I got very concerned about how are we gonna specify these objectives for all sorts of agents. And I thought, well, you know, the problem that

### Human feedback techniques

[2:49] we actually wanna solve looks something more like this: where you have an agent, an LLM, a robot, whatever, And there is a reward function, but it's in the person's head, it's not directly visible observable to the agent. And the agent's job is to optimize for that except it doesn't actually get to ever directly observe it. And then, naturally we started turning to human feedback, what people do, what they say as evidence about the thing that's in their head that they would like for the agent to optimize. So, we did things like if the person specifies - Dylan did - if the person specifies a reward function, kind of take it as evidence, but not the definition of what they exactly want. Also, this is Dorsa's work this back in 2015, 2016, we were looking at A versus B, which one's better, and try to learn a reward function based on that, later, became known as RLHF. Now, the robot on the right hand side or the agent on the right hand side takes in all this as evidence about what the person wants.

[3:54] And to do that, you need to give the agent what we call a human model. Something that relates the feedback that it's seeing to the internal parameters of the reward function that the agent is trying to estimate. And typically the human mo - woah, can I go back? The human model that we use - it got cut off a little bit - but it's sort of Bradley-Terry Luce-Shepherd, Boltzmann comes under different names, but that's it. That's right there. People are noisy rational. The problem is people aren't

### Risks of improper modeling

[4:25] noisy rational. This is completely wrong. It can be useful, but nonetheless, it's wrong. And we have a lot of empirical evidence that using the wrong model leads to poor rewards, empirical evidence. Lately, we started looking at this problem theoretically. Is it actually an issue in theory that you, you're using the wrong reward model?

### Theoretical guarantees

[4:48] The bad news is that even small errors, you can have almost the right model with epsilon error just in the right place. And that can have catastrophic, catastrophic, basically influence on the error of the reward model that you're learning. And so this is kind of seems alignment is hopeless because we're never gonna have the perfect model. We're always gonna be off - so what do we do? The good news, let me actually say it this

### Future research directions

[5:13] way that we're being able to identify some assumptions that are not too unreasonable, but they're still probably wrong, where you can actually say that if you get a better human model, you have a guarantee on your reward model also getting better. And the assumption is that basically the the human has to act in a way that is log-concave with respect to the reward parameters, which probably is not true of human behavior, but almost. And Adam is looking at me, so I will conclude by saying from this, I take away that it is likely that improving human models will lead to better reward models. It seems important to do that otherwise, we might get catastrophically bad reward models that we're aligning to. ... I'm gonna skip this,

### Conclusion and closing

[5:59] that's just some empirical evidence. And I'm gonna leave you with this slide, which basically says I've been trying to do human modeling for a long time, been making very little progress a little bit of progress. I think I'm excited about tapping into the large models' capabilities in terms of understanding human behavior better as maybe a way to make progress towards this problem. So I'll leave you with that. Thank you so much.
