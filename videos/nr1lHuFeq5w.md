---
id: "nr1lHuFeq5w"
title: "Scalable Supervision: Concrete Problems in AI Safety Part 5"
url: "https://www.youtube.com/watch?v=nr1lHuFeq5w"
channel: "Robert Miles AI Safety"
channel_id: "UCLB7AzTwc6VFZrBsO2ucBMg"
channel_url: "https://www.youtube.com/channel/UCLB7AzTwc6VFZrBsO2ucBMg"
upload_date: "2017-11-29"
duration_seconds: 303
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-GB"}
collections: ["channels/robertmilesai"]
retrieved: "2026-09-24"
---

# Scalable Supervision: Concrete Problems in AI Safety Part 5

[Watch on YouTube](https://www.youtube.com/watch?v=nr1lHuFeq5w) · Robert Miles AI Safety · 2017-11-29 · 5:03

## Chapters

- 0:00 Intro
- 0:10 Good Hearts Law
- 1:13 Supervision Metrics
- 4:43 Outro

## Description

```text
Why can't we just have humans overseeing our AI systems?

The Concrete Problems in AI Safety Playlist: https://www.youtube.com/playlist?list=PLqL14ZxTTA4fEp5ltiNinNHdkPuLK4778  
Previous Video: https://www.youtube.com/watch?v=13tZ9Yia71c
The Computerphile video: https://www.youtube.com/watch?v=9nktr1MgS-A  
The paper 'Concrete Problems in AI Safety': https://arxiv.org/pdf/1606.06565.pdf  

https://www.patreon.com/robertskmiles

[... trimmed by fetch_youtube.py]
```

## Transcript

_Source: human-made captions (en-GB). Timestamps are [m:ss] from the start of the video._

### Intro

[0:00] Hi, this is part of a series of videos about the paper Concrete Problems in AI Safety. It should make some sense on its own, but I'd recommend checking out the other videos first. There's a link to the playlist in the description.

### Good Hearts Law

[0:10] So before, we talked about some problems that we might have with AI systems, like negative side effects, reward hacking, or wireheading. We talked about Goodhart's Law, like how if you use an exam as a metric, students will only learn what's on the exam, and then the exam will stop being a good metric of how much the students know. The obvious question here is, why not just make an exam that properly tests everything you care about? And the obvious answer is, that would take way too long, or cost way too much. We often face a trade-off between how good of a metric something is, and thus how resistant it is to things like Goodhart's Law, and how expensive that metric is, in terms of time, money, or other resources. For our cleaning robot example, we could have a reward system that involves a human following the robot around at all times, and giving it positive or negative reward, depending on what the robot does.

[0:57] This still isn't safe with a powerful intelligence, because it still incentivises the AI to manipulate, deceive, or modify the human, but assuming we find a way around that kind of thing, it's a pretty good metric. The robot's not going to maximise its reward by just putting its bucket on its head or something like that.

### Supervision Metrics

[1:14] But this isn't practical. If you're going to hire someone to follow the robot around all the time, you may as well just hire someone to do the cleaning. That's why we came up with metrics like, use your cameras to look around at the amount of mess in the first place, they're cheap for the robot to do on its own. Though there are some situations where constant human supervision can be used. For example, when developing self-driving cars, there's always a human behind the wheel to stop the AI from making serious mistakes. This makes good sense. Legally, you've got to have a qualified human in the car anyway, for now. But this doesn't scale well. Paying humans to supervise the millions of miles your cars need to drive before the system is fully trained is really expensive. If you're Google, you can afford that, but it's still a huge cost, and it makes a lot of projects infeasible. A human pilot can safely oversee an autonomous drone, but not a cooperating swarm of hundreds of them.

[2:02] So we need to find ways for AI systems to learn from humans without needing a human to constantly supervise everything they do. We need to make systems that can operate safely with less supervision. A slightly more practical metric for our cleaning robot is to have the robot do a day's cleaning, and then have some humans come around and do a full inspection of the place at the end of the day. Checking everything's clean, checking everything's in its place, and giving the robot a score out of 10 for its reward. If the robot breaks something, throws away something important, or just sits there with its bucket on its head, it will get low reward. So this still avoids a lot of our negative side effects and reward hacking problems. As long as the inspection is thorough enough, and the AI is weak enough, that the robot can't deceive or manipulate the humans. But there are problems with this too. And a big one is that in this type of situation, things like reinforcement learning will be really slow, or just not possible.

[2:51] See, with a metric like keeping track of how much mess there is with your cameras, the robot can try different things and see what results in less mess, and thus learn how to clean. But with a daily inspection, the robot is operating all day doing thousands of different things, and then it gets a single reward at the end of the day. How is it meant to figure out which of the things it did were good and which were bad? It would need an extremely large number of days before it could learn what it needs to do to get good scores on the inspections. So figuring out how to make AI systems that can learn using a sparse reward signal would be useful for AI safety. And it's also a problem that's important for AI in general, because often a sparse reward is all you've got. For example, DeepMind's DQN system can learn to play lots of different Atari games, using just the pixels on the screen as its sensor input, and just the score as its reward. But it plays some games better than others.

[3:40] It's far better than any human at Breakout, but it can't really play Montezuma's Revenge at all. Now, there are a lot of differences between these games, but one of the big ones is that in Breakout, you get points every time you hit a brick, which happens all the time, so the score, and thus the reward, is constantly updating and giving you feedback on how you're doing. While in Montezuma's Revenge, you only get points occasionally for things like picking up keys or opening doors. And there are relatively long stretches in between where you have to do complicated things without any score updates to let you know if you're doing the right thing. Even dying doesn't lose you any points, so it can be hard for systems like this to learn that they need to avoid that. How do you make a system that can learn even when it only occasionally gets feedback on how it's doing? How do you make a system that you can safely supervise without having to constantly watch its every move?

[4:26] How do you make supervision scale? We'll talk about some different approaches to that in the next video. I want to take a moment to thank my excellent Patreon supporters.

### Outro

[4:50] In this video, I'm especially thanking Jordan Medina, a ramblin' wreck from Golden Tech who's been a patron of the channel since July. Thank you so much for your support, Jordan, and thank you to all of my patrons, and thank you all for watching. I'll see you next time.
