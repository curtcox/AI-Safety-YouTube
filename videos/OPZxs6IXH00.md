---
id: "OPZxs6IXH00"
title: "Ilya Sutskever - Opening Remarks: Confronting the Possibility of AGI"
url: "https://www.youtube.com/watch?v=OPZxs6IXH00"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2023-09-01"
duration_seconds: 1138
is_short: false
chapters: 12
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Ilya Sutskever - Opening Remarks: Confronting the Possibility of AGI

[Watch on YouTube](https://www.youtube.com/watch?v=OPZxs6IXH00) · FAR․AI · 2023-09-01 · 18:58

## Chapters

- 0:00 <Untitled Chapter 1>
- 1:02 Al Alignment and AGI safety
- 5:05 Disconnect
- 7:18 AGI is no longer a dirty word
- 9:06 Make AGI safety mainstream
- 9:56 Why isn't alignment trivial
- 10:29 Unsupervised learning
- 13:09 Reinforcement Learning
- 16:39 Superintelligence
- 17:02 Takeaways
- 18:15 Concrete goal
- 18:46 Thank you, and enjoy the workshop

## Description

```text
"Opening Remarks: Confronting the Possibility of AGI" by Ilya Sutskever. Delivered at the 2023 San Francisco Alignment Workshop.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### <Untitled Chapter 1>

[0:00] Hello. Welcome. Thank you all so much for taking the time to stop by this workshop. So the intention with this workshop is to get mainstream machine learning researchers exposed to ideas in AI alignment. The reason it makes sense is because AI has been progressing rather rapidly, and it is not difficult to imagine AGI at this point. Now, for a little bit of background, it can be helpful to understand or to be reminded how the current situation came to be, that we have two fields who are asking related questions, which have nonetheless, until quite recently, have almost completely not interacted with each other.

[1:01] So if you start with the field of AI alignment

### Al Alignment and AGI safety

[1:09] and AGI safety, it has strong sci-fi origins. By which I mean that the early thinkers in that space have not been restrained by limitations of present-day technology. Instead, they ask themselves questions like: &quot;if you do have an AI system which is smart enough to do research and science and engineering and technology, that can do AI research, that can do programming, that can do chip design, and all the management that's needed to put it all together, what will happen?&quot; And if you ask yourself this question, the answer goes: &quot;oh my, something pretty substantial will happen.&quot; And then you can ask the question &quot;well, that seems like a pretty powerful process, a little scary. What are the conditions under which this process will be more favorable to us little people?&quot; So this is how where these, this is in one word, in one sentence, the genesis of the field of AI alignment.

[2:10] Now, the field of ML has similar sci-fi origins. You had visionary scientists in the 40s and the 50s asking questions like: what is intelligence? How do brains work? Can we build brains on a computer? Can we create artificial neural networks? Can computers learn? And back then, researchers were very optimistic. They thought, OK, in five years, we're going to get our human-level AI, obviously. But they were wrong. And the AI winter happened. And the AI winter is the root of the division that we are facing today. The AI winter is the reason why this workshop is needed in the first place. So what were some of the consequences of the AI winter? It made ML into a field of pessimism and hopelessness when it comes to progress.

[3:03] This is just a fact. Computers were far too slow. I mean, do you remember? I mean, like 100 megahertz Pentium Pro? And so when computers are too slow, ML cannot do anything at all. It just can't. And so the only AI which did anything good was good old-fashioned AI, symbolic AI, which is why it dominated so much in the 70s and the 80s and perhaps even the 90s, because there was no alternative when computers are so slow. But I would say that this has really traumatized the field of AI. It has traumatized the field of machine learning.

[3:53] And so people who were working in this field had the attitude of progress is really hard to get by. Progress is very valuable. Anyone who makes any kind of progress at all is worthy of praise and admiration, because it's such a hard thing to do. And this attitude continued well into the 2010s, even after we started to have all those early deep learning advances, even when deep learning started to progress and solve games and solve the (I wouldn't say solve, yes, solve games); make progress on various tasks in vision and language. But the pessimism continued. And I remember that attitude very well, because I was very close to what people were saying, where the attitude which I perceived was, OK, sure. So we've got this far, but this year, the progress is definitely going to stop.

[4:46] I mean, we've had enough. The difficult times are about to return. It's just a brief, brief, uncharacteristic summer. And then the difficulties will be back, and we'll be back in the world of slow progress, a world of pain and suffering, as far as capability is concerned. And so this led to a disconnect.

### Disconnect

[5:06] So obviously, now you have the two fields: the field of AI alignment, which allows itself to ask the most audacious questions possible about the nature of superintelligence and the conditions, like some hypothetical conditions under which it would be better or less well-behaved; and the field of machine learning, which is so used to neural networks or whatever people were doing before, like support vector machines, barely classifying digits of tiny resolution. So you can say, how can I possibly take this seriously? That was the reaction from the ML field. This stuff is just too crazy, too disconnected from the daily reality of ML. And I would say that the thing that was not as optimal is that that attitude had outlived its usefulness.

[5:59] This attitude was valid in the 90s, in the aughts, but maybe in the early 2010s, certainly not in the late 2010s. But then, as we all know, the 2010s have really outperformed, have really exceeded all expectations as far as progress is concerned. We all know what happened. First, we had advances in vision, in visual recognition, in translation, in summarization, in playing games, playing Go, playing real strategy games. And this progress was very, very rapid. And then image generation just came in and became incredible. It felt like going from 0 to 60 in two seconds, like some of these rapidly accelerating cars, and of course, the chatbots. And so there is a meme, which I see on Twitter often, which summarizes this sentiment, that the field of ML, I guess, it was either progressing too slow, too slowly, and then it started to progress too fast, with maybe a brief period of time in between, kind of like, I believe, summer on the East Coast.

[7:15] And so now, AGI is no longer a dirty word.

### AGI is no longer a dirty word

[7:21] There is a book called Profiles of the Future. And in this book, (it's a really cool book, by the way. I recommend reading it, just the first two chapters. It's all you need. It's a 20-minute read. It's written by Arthur C. Clarke. And in this book, he surveys three major technological revolutions around atomic energy, rocketry, and spaceflight. And in each one of these areas, shortly before the main breakthroughs were done, you had very confident experts going on record, saying that these advances are basically fundamentally impossible and will never happen, and so on. And it's just interesting to look at the parallels between what we've seen there with these other technological revolutions, and what we're talking about with AI, with AGI.

[8:23] AGI is already easier to imagine, though perhaps there are still some things which may be hard to imagine. And one of the goals of this workshop is to remove or further reduce one difficulty which the book describes, failure of imagination. The reason those people were so confident that those breakthroughs were not possible is because they just couldn't imagine them. They suffered from failure of imagination, which led to overconfidence in the other direction. We now have a lot of evidence that it's no longer the case, but we might still be suffering from failure of imagination in various places. And hopefully by the end of tomorrow, we will have even less of that. And so, yeah, hopefully, as a result of this workshop, we will take a step towards making

### Make AGI safety mainstream

[9:12] AGI safety mainstream in ML. There are lots of researchers in ML, and it seems on net quite beneficial for those ideas to be more mainstream rather than less. So, yeah, we'll merge the field with the tactic of focusing on the basics. Now, why focus on the basics and what do I mean by that? By focusing on the basics, I mean the following. Many people in ML might not have been exposed to many of those ideas in alignment. And just getting insight into the basics: what are the problems really? Why are they hard really? That alone would already be a useful result. So, for the remainder of my presentation, I would like to spend a few minutes making

### Why isn't alignment trivial

[10:04] a few arguments for why alignment isn't trivial. Because you can ask yourself in ML, well, we make AI systems do what we want. We've always have. Why should this change? So, let's look at different paradigms of AI and see why alignment can be more or less difficult.

### Unsupervised learning

[10:29] Starting with supervised learning, when you train them on datasets produced by human annotators, such as speech recognition. You have human annotators annotating speech. You have machine translation. You have human translators translating speech. You have visual recognition. And you train a neural network to imitate the behavior produced by this data. In these cases, the data is quite easy to understand for us. We have a lot of insight into this data. And so, there is quite limited concern about what happens in the case of supervised learning from well-understood data. But now, things already change when we switch to unsupervised learning. And let's see why.

[11:18] When we pre-train our neural nets on these very large number of tokens from the internet, we know that our neural networks learn something. We know that they learn something related to language and to the world. And we can make this kind of arguments. But we don't exactly know what that is anymore. We have less insight into what's being learned. And therefore, we have less insight into the behavior of our neural networks. So, this difficulty shows up in the fact that, indeed, empirically, we've had less success in getting exactly the desired behavior we want out of them. This is an empirical fact that these models still make stuff up. It isn't trivial. If it was trivial, they wouldn't be making stuff up.

[12:07] So, there is at least some kind of new difficulty here which did not exist in the simple supervised learning case of you just want to do speech recognition, you just want to do computer vision. That is different. And they can surprise us in ways that might not be expected. And you saw it especially with Sydney. I think we can all agree that Sydney's colorful personality was not exactly what the creators of Bing have intended. The point is that we have more empirical evidence in the real world that somehow, just when you do unsupervised learning, things become a little bit more complicated.

[12:56] But then, of course, the thing is that the nature of our AI systems and therefore the nature of the difficulty or easiness of alignment changes as a paradigm change.

### Reinforcement Learning

[13:09] There is also reinforcement learning. Now, reinforcement learning is now an integral part of the chatbots that are being built. Because after pre-training, there is a reinforcement learning against some kind of a one or a set of reward functions. And perhaps we can just specify it with machine learning. And we can, to some degree. And that works quite well. Though you do suffer from the over-optimization issues that have been hypothesized by the early alignment thinkers. Like, it is quite easy to optimize the reward function, the reward model that learned from our human teachers. And it's quite easy for you to learn something that's a little bit unexpected.

[13:57] The reinforcement learning process is very tricky. In fact, it is creative. So while over-optimization can be addressed in the near term, reinforcement learning has a much more significant challenge: it is creative. Reinforcement learning is actually creative. Every single stunning example of creativity in AI comes from a reinforcement learning system. For example, AlphaZero has invented a whole new way of playing a game that humans have perfected for thousands of years. It is reinforcement learning that can come up with creative solutions to problems, solutions which we might not be able to understand at all. And so what happens if you do reinforcement learning on long or even medium time horizon when your AI is interacting with the real world, trying to achieve some kind of a beneficial outcome, let's say, as judged by us, but while being very, very, very creative?

[15:04] This does not mean that this problem is unsolvable, but it means that it is a problem. And it means that some of the more naive approaches will suffer from some unexpected creativity that will make the antics of Sydney seem very modest. And finally, it's worth thinking a little bit to the point of removing limiters from our imaginations, allowing ourselves to think about the final point, the AGI. What happens when your coding, programming AI, outputs 10,000 or 100,000 lines of code? A big program. You can run some unit tests, perhaps, you can interact with the program. That seems like it is a whole new kind of a problem that you'll need to address to make it so that our AI systems, which output 100,000 lines of code, don't contain any fishy stuff on the inside.

[16:03] We will want to do something around controlling the process that led to those 10,000 lines of code. But it creates a new challenge. It's not straightforward. It's not straightforward to train an AI or to understand it when we cannot understand its outputs and when it is very creative and can act in the real world. Now, what if you have an AI that's running a company or that's running a research lab? And finally: (deception, by the way, there will be a talk about that, which I think is

### Superintelligence

[16:44] one of the more interesting ideas for people coming from a strict ML background.) What happens when your AI is so smart that it decided that it will do well during training and become a doctor, while in reality it wants to be a YouTuber? So, to sum up, AGI and superintelligence are definitely possible, extremely likely in our

### Takeaways

[17:18] lifetime, perhaps a lot sooner. It's hard to give exact numbers, but progress is quite rapid indeed. Progress is very, very rapid, and so we should not put limits on our imagination, should not put limits on the capabilities of this. And the impact is, if you were to use very understated language, mega gigantic. And this is understated language. Mega gigantic is a very modest lower bound on the impact of AGI. And so, when you have such impactful technology, who knows what's going to happen? All kinds of things can happen. But at least let's make sure that on the technology side, let's put it this way, let's make sure that if it misbehaves, it will be because of the humans operating it rather than the technology itself.

[18:09] It seems like a nice bare minimum that we can aspire to.

### Concrete goal

[18:15] And it would be nice if as a result of this workshop, more people here would have a more unified view of the two set of ideas. The two set of ideas right now might feel a little disconnected, and it would be nice to connect them, to put flesh on them into a single cohesive whole. That's my aspiration. That's what I hope will happen as a result of the discussions and the conversations that will take place and all the talks. And yeah, I am, once again, I should say, I'm very grateful to all of you for making

### Thank you, and enjoy the workshop

[18:48] it. Thank you for being here, and please enjoy the workshop.
