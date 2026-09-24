---
id: "nKJlF-olKmg"
title: "9 Examples of Specification Gaming"
url: "https://www.youtube.com/watch?v=nKJlF-olKmg"
channel: "Robert Miles AI Safety"
channel_id: "UCLB7AzTwc6VFZrBsO2ucBMg"
channel_url: "https://www.youtube.com/channel/UCLB7AzTwc6VFZrBsO2ucBMg"
upload_date: "2020-04-29"
duration_seconds: 580
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-GB"}
collections: ["channels/robertmilesai"]
retrieved: "2026-09-24"
---

# 9 Examples of Specification Gaming

[Watch on YouTube](https://www.youtube.com/watch?v=nKJlF-olKmg) · Robert Miles AI Safety · 2020-04-29 · 9:40

## Chapters

- 0:00 King Midas
- 2:06 AI Safety
- 2:41 Examples
- 6:29 Finding Bugs
- 7:53 Simulation

## Description

```text
AI systems do what you say, and it's hard to say exactly what you mean.
Let's look at a list of real life examples of specification gaming!

How to Help: https://aisafety.info/questions/8TJV/...
https://www.aisafety.com/

Related Videos from me:
Reward Hacking: https://youtu.be/92qDfT8pENs
Reward Hacking Reloaded: https://youtu.be/46nsTFfsBuc
What Can We Do About Reward Hacking?: https://youtu.be/13tZ9Yia71c

Sources:
The list: http://tinyurl.com/specification-gaming
The blogpost this video is based on: https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/
The newer blogpost that happened while I was making this video: https://deepmind.com/blog/article/Specification-gaming-the-flip-side-of-AI-ingenuity

Links: 
Eliciting latent knowledge from AI: https://www.alignmentforum.org/posts/rxoBY9CMkqDsHt25t/eliciting-latent-knowledge-elk-distillation-summary 
Do current AI models show deception: https://aisafety.info/questions/9AL4/
What is deceptive alignment: https://aisafety.info/questions/8EL6/
Scaling Laws: https://aisafety.info/questions/7750/
LLMs as simulators: https://aisafety.info/questions/9FQK/


(Explosion graphic from videezy.com)

[... trimmed by fetch_youtube.py]
```

## Transcript

_Source: human-made captions (en-GB). Timestamps are [m:ss] from the start of the video._

### King Midas

[0:00] Hi. When talking about AI safety, people often talk about the legend of King Midas. You've probably heard this one before. Midas is an ancient king who values, above all else, wealth and money. And so when he's given an opportunity to make a wish, he wishes that everything he touches would turn to gold. Now, as punishment for his greed, everything he touches turns to gold. This includes his family, who turn into gold statues, and his food, which turns into gold and he can't eat it. The story generally ends with Midas starving to death, surrounded by gold, with the moral being, there's more to life than money, or perhaps be careful what you wish for. Though actually, I think he would die sooner, because any molecules of oxygen that touch the inside of his lungs would turn to gold before he could breathe them in, so he would probably asphyxiate first. And then when he fell over stiffly in his solid gold clothes, some part of him would probably touch the ground, which would then turn to gold. And I guess the ground is one object, so the entire planet would turn to gold. Gold is three times denser than rock. I guess gravity would get three times stronger, or the planet would be one third the size, or... I guess it doesn't really matter. Either way, a solid gold planet is completely uninhabitable. So maybe the moral of the story is actually that these be careful what you wish for kind of stories tend to lack the imagination to consider just how bad the consequences of getting what you wish for can actually be.

[1:13] Hey, future Rob from the editing booth here. I got curious about this question, so I did the obvious thing, and I asked Anders Sandberg of the Future of Humanity Institute, what would happen if the world turned to solid gold? And yes, it does kill everyone. One thing is that because gold is softer than rock, the whole world becomes a lot sort of smoother. The mountains become lower. And this means that the ocean, if the ocean didn't turn to gold, sort of spreads out a lot more and covers a lot more of the surface. But perhaps more importantly, the increased gravity pulls the atmosphere in, which brings a giant spike in air pressure, which comes with a giant spike in temperature. So the atmosphere goes up to about 200 degrees Celsius and kills everyone. I knew everyone would die, I just wasn't sure what would kill us first. Anyway, why were we talking about this? AI safety.

### AI Safety

[2:07] Right. There's definitely an element of this be careful what you wish for thing in training AI systems. The system will do what you said and not what you meant. Now, usually we talk about this with hypothetical examples. Things like in those old computer file videos, the stamp collector, which is told to maximize stamps at the cost of everything else. Or when we were going through concrete problems in AI safety, the example used was this hypothetical cleaning robot, which, for example, when rewarded for not seeing any messes, puts its bucket on its head so it can't see any messes. Or in other situations, in order to reduce the influence it has on the world, it blows up the moon. So these are kind of far fetched

### Examples

[2:43] and hypothetical examples. Does it happen with real current machine learning systems? The answer is yes, all the time. And Victoria Krukovna, an AI safety researcher at DeepMind, has put together a great list of examples on her blog. So in this video, we're going to go through and have a look at some of them. One thing that becomes clear from looking at this list is that the problem is fundamental. The examples cover all kinds of different types of systems. Any time that what you said isn't what you meant, this kind of thing can happen. Even simple algorithms like evolution will do it. For example, this evolutionary algorithm is intended to evolve creatures that run fast. So the fitness function just finds the center of mass of the creature, simulates the creature for a little while, and then measures how far or how fast the center of mass has moved. So a creature that's center of mass moves a long way over the duration of the simulation must be running fast. What this results in is this, a very tall creature with almost all of its mass at the top, which when you start simulating it, falls over. This counts as moving the mass a long way in a short time, so the creature's running fast. Not quite what we asked for. Of course, in real life, you can't just be very tall for free. If you have mass that's high up, you have to have lifted it up there yourself. But in this setting, the programmers accidentally gave away gravitational potential energy for free, and the system evolved to exploit that free energy source. So evolution will definitely do this.

[4:02] Now reinforcement learning agents are, in a sense, more powerful than evolutionary algorithms. It's a more sophisticated system, but that doesn't actually help in this case. Look at this reinforcement learning agent. It was trained to play this boat racing game called Coast Runners. The programmers wanted the AI to win the race, so they rewarded it for getting a high score in the game. But it turns out there's more than one way to get points. For example, you get some points for picking up power-ups, and the agent discovered that these three power-ups here happen to respawn at just the right speed that, if you go around in a circle and crash into everything and don't even try to race at all, you can keep picking up these power-ups over and over and over and over again. And that turns out to get you more points than actually trying to win the race. Or look at this agent that's been tasked with controlling a simulated robot arm to put the red Lego brick on top of the black one. Okay, no, they need to be stacked together, so let's have the reward function check that the bottom face of the red brick is at the same height as the top face of the black brick. That means they must be connected, right?

[5:06] Okay, so specifying what you want explicitly is hard. We knew that. It's just really hard to say exactly what you mean. But why not have the system learn what its reward should be? We already have a video about this reward-modelling approach. But there are actually still specification problems in that setting as well. Look at this reward-modelling agent. It's learning to play an Atari game called Montezuma's Revenge. Now, it's trained in a similar way to the backflip agent from the previous video. Agents are shown short video clips and asked to pick which clips they think show the agent doing what it should be doing. The difference is, in this case, they trained the reward model first, and then trained the reward-learning agent with that model, instead of doing them both concurrently. Now, if you saw this clip, would you approve? It looks pretty good, right? It's just about to get the key. It's climbing up the ladder. You need the keys to progress in the game. This is doing pretty well. Unfortunately, what the agent then does is this.

[5:57] There's a slight difference between do the things which should have high reward according to human judgement, and do the things which humans think should have high reward based on a short out-of-context video clip. Or how about this one? Here, the task is to pick up the object. So this clip is pretty good, right? Nope. The hand is just in front of the object. By placing the hand between the ball and the camera, the agent can trick the human into thinking that it's about to pick it up. This is a real problem with systems that rely on human feedback. There's nothing to stop them from tricking the human if they can get away with it.

### Finding Bugs

[6:29] You can also have problems with the system finding bugs in your environment. Here, the environment you specified isn't quite the environment you meant. For example, look at this agent that's playing Qubit. The basic idea of Qubit is that you jump around, you avoid the enemies, and when you jump on the squares, they change colour. And once you've changed all of the squares, then that's the end of the level. You get some points, all of the squares flash, and then it starts the next level. This agent has found a way to sort of stay at the end of the level state and not progress onto the next level. But look at the score. This just keeps going. I'm going to fast forward it. It somehow found some bug in the game that means that it doesn't really have to play, and it still gets a huge number of points. Or here's an example from CodeBullet, which is kind of a fun channel. Here he's trying to get this creature to run away from the laser, and it finds a bug in the physics engine.

[7:22] I don't even know how that works. What else have we got? Oh, I like this one. This is kind of a hacking one, GenProc. This is a system that's trying to generate short computer programs that produce a particular output for a particular input. But the system learned that it could find the place where the target output was stored in the text file, delete that output, and then write a program that returns no output. So the evaluation system runs the program, observes that there's no output, checks where the correct output should be stored and finds that there's nothing there, and says, oh,

### Simulation

[7:53] there's supposed to be no output, and the program produced no output. Good job. I also like this one. This is a simulated robot arm that's holding a frying pan with a pancake. Now it would be nice to teach the robot to flip the pancake. That's pretty hard. Let's first just try to teach it to not drop the pancake. So all we need is to just give it a small reward for every frame that the pancake isn't on the floor. So it will just keep it in the pan. Well, it turns out that that's pretty hard too. So the system effectively gives up on trying to not drop the pancake and goes for the next best thing, to delay failure for as long as possible. How do you delay the pancake hitting the floor? Just throw it as high as you possibly can. I think we can reconstruct the original audio here. Yeah, that's just a few of the examples on the list. I encourage you to check out the entire list. There'll be a link in the description to that. I guess my main point is that these kinds of specification problems are not unusual and they're not silly mistakes being made by the programmers. This is sort of the default behavior that we should expect from machine learning systems. So coming up with systems that don't exhibit this kind of behavior seems to be an important research priority.

[8:56] Thanks for watching. I'll see you next time. I want to end the video with a big thank you to all my excellent patrons. All of these people here. In this video, I'm especially thanking Kellen Lask. I hope you all enjoyed the Q&A that I put up recently. The second half of that is coming soon. I also have a video of how I gave myself this haircut, because why not? This is going to get worse before it gets better.
