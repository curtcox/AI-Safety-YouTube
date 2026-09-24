---
id: "evSFeqTZdqs"
title: "AI's Version of Moore's Law? - Computerphile"
url: "https://www.youtube.com/watch?v=evSFeqTZdqs"
channel: "Computerphile"
channel_id: "UC9-y-6csu5WGm29I7JiwpnA"
channel_url: "https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA"
upload_date: "2025-04-29"
duration_seconds: 785
is_short: false
chapters: 6
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/computerphile"]
retrieved: "2026-09-24"
---

# AI's Version of Moore's Law? - Computerphile

[Watch on YouTube](https://www.youtube.com/watch?v=evSFeqTZdqs) · Computerphile · 2025-04-29 · 13:05

## Chapters

- 0:00 Introduction to METR
- 1:50 Measuring AI capabilities
- 3:05 Task duration methodology
- 6:20 Exponential growth trends
- 8:48 Scaffolding and validation
- 11:55 Sponsor message

## Description

```text
This video features Sydney Von Arx --- Check out Brilliant's courses and start for free at https://brilliant.org/computerphile/ (episode sponsor) - More links in description below ↓↓↓

Research suggests the rate at which AI is able to stay 'on task' is doubling every seven months. Is this the AI equivalent of Moore's Law? - Sydney Von Arx works on adversarial stress-testing at METR (Model Evaluation & Threat Research.) 

AI digest explainer:
https://theaidigest.org/time-horizons
The Paper:
https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

Computerphile is supported by Jane Street. Learn more about them (and exciting career opportunities) at: https://jane-st.co/computerphile

This video was filmed and edited by Sean Riley.

Computerphile is a sister project to Brady Haran's Numberphile. More at https://www.bradyharanblog.com
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### Introduction to METR

[0:00] My name is Sydney Von Orff, and I'm a member of technical staff at MITRE, which stands for model evaluation and threat research. And we do what it says on the tin. We evaluate models, and we try to figure out how to determine when they'll have different levels of capabilities, and especially when they might have dangerous capabilities, and whether or not they're safe. So, when you say models here, you're talking about AI models? So, examples are Claude, Grok, these sorts of things? Yes, exactly. Any of the sort of chat GPT models, uh Llama are one. You know, there's a lot of buzz about AI these days, and people go, "Wow, AI models, they're they're so impressive." And we try to measure how good the AI models are, and there's a lot of different metrics people use to measure this, but one of the main ones is sort of question-answer, like multiple-choice data sets.

[0:54] And the AIs are really good at all these data sets with a very small number of exceptions these days. I have a graph here from Our World in Data that shows like they're just saturating all of these different benchmarks. This zero here is like human performance, and they're above human performance at all the tasks we could come up with in the past. Uh but there's this thing where models still seem kind of derpy. Like, if you've ever tried to use them to do your job, they can be kind of helpful, and they certainly know a lot of things, but I don't think they could do my job for even several hours or a day. And uh there's a stream on Twitch right now of Quad attempting to play Pokémon. And it's not doing so well. So, what's going on there? And, you know, is AI a scam, or is it actually a technology that's going to like take your job away one day?

### Measuring AI capabilities

[1:50] Uh well, we made a data set and evaluated a bunch of models to try and find out. You've got a paper about it. Yeah, two papers actually. Um one paper the data set and then the other paper is our findings uh of how models do over time. I'll talk about what this data set is and why I think it's important, but this is the trend. The models seem to be improving at an surprisingly regular rate. We can see it's an exponential. We've tried by different fits in our paper, you can read it. I'm going to call this an exponential. Yeah, cuz people can get sniffy about the actual definition of exponential, but that curve definitely seems to go up it very steeply, right? you want, here is the uh Y axis on a log scale. So, log means we see a straight line, then that is showing that that is exponential. Yes, that's what the Exactly. But, maybe it helps to see how regular it is when we plot it like this. But, let's talk about what these axes are and what we're even looking at for a second.

[2:43] to say, yeah, yeah, what's the measure there, right? What What are we measuring? How do we talk about AI hardness? How can I possibly put like GPT-2, a very dumb model that can't, you know, string multiple sentences together coherently on the same graph as like Sonnet 3.7, a model that can like very easily write complicated code that I couldn't write myself.

### Task duration methodology

[3:05] So, the thing that we measure is how long a task a model can do. Okay. By task length, I mean we took a bunch of human experts. We asked them to do the task, and we see how long it takes them. We primarily measure software engineering tasks of different kinds. Uh we have especially a lot of cybersecurity tasks and a ton of AI R&D tasks. Uh many benchmarks try to make the hardest task possible. We just wanted to say, "Well, what What actually creates value in the world?" Again, leaning towards software engineering in particular for reasons I can get into. Uh these tasks range from things that take humans 1 second Mhm. to things that take humans 16 hours. And they're really diverse in quite a lot of ways. The H-Caste paper has all kinds of fun graphs about task diversity. And then we get a bunch of humans to do the task.

[4:03] We take the geometric mean for every task of human baseline or time. Occasionally, we use estimates when we have to. And this gives us a thing we can plot of like human time to complete for each task. And then for every model, we have the model try each task eight times. And now we can make a graph of how long the task takes a human compared to the chance of model success. Sorry for my egregious handwriting. You know, if we have a task that takes uh like couple seconds, just a quick like answer this question about how to do this thing, you know, models complete that really regularly. They, you know, complete it almost 100% of the time. If we have a task that's like optimized this uh training software that like trains a model, then AIs are going to not going to be very good at that. You know, they won't be able to do it that long. And this, you know, maybe takes humans like 16 hours making these tasks up, but they're representative of the kind of tasks we have.

[5:05] Uh things in the middle, right? Like train a really simple little classifier that can do MNIST or something. That takes humans like an hour. And the models, you know, say they get that right like half the time. So, we get a bunch of data points. And then we fit a logistic curve. I did a bad job of drawing my data points along a logistic curve, but you'll have to bear with me. So, we can do a logistic regression, and we can figure out sort of where that halfway point is. And this is like represents if we had to predict based on our data the odds that a model could do a task just based on how long that task was. This is a curve that represents the that probability. That gives us a data point for one model on our graph of capabilities over time. So, you know, I might make a curve like this for 01 and I get something on our graph and then I make a curve exactly like this and I I get my data point for 3.7 Sonnet and GPT-2 and we get our graph. That's where our comes from. And it turns out right now, 3.7 Sonnet is able to do tasks that take humans about 1 hour with 50% reliability or we predict 50% chance of success. So, what happens if we look at

### Exponential growth trends

[6:20] different cutoffs? What if I want my models to be a bit more reliable? Well, we look at 80% as our probability of success, much higher bar. Of course, the time horizon, the the amount of time a task takes that the model can complete goes way down. Models can complete tasks that are five times shorter uh if you require them to have 80% reliability. Like 80% reliability, now we're looking at, you know, 10-minute tasks, not 1-hour tasks, even for the best models. But, the trend is the part that's interesting to me. And this trend is very robust. The doubling time that we predict for like how long a task models can do changes by only 1 day if you look at an 80% success threshold versus a 50% success threshold. We take this graph and we go, "Okay, wow, it really seems like the capabilities of models are doubling, exponential trend, and doubling every 7 months." And that 7-month number uh is really robust. We did a bunch of sensitivity analyses.

[7:31] For example, if we look at, you know, a success threshold of 80%, it only changes by like 1 day. Uh it's very robust. Like if we look at this, right? Like little wiggles here aren't going to change the fact that this is an exponential trend. Another way to say it is the difference between Sonnet 3.7 and like GPT-3.5 is so large that even if our measurement of how good Sonnet is is pretty noisy, that trend still pops out at you. There's a question of if we expect that trend to continue. I'm speaking in my personal capacity right now, but uh if we let ourselves draw the line out to like 16-hour tasks, we see that happens by 2028 in sort of a mainline version. And once you've got 16-hour tasks by 2028, you can do the math at a couple doublings a year, right? You can get a week of work in just a year, and you can get a month of work in another year. I also think if you're thinking about the advantage of models is like, "Oh, well, they can work day and night." This isn't the main advantage. The main advantage is they can be in parallel. You can have uh an army of a thousand models trying to work on your task.

[8:43] I'm going to ask a flippant question then. Do they have to have meetings?

### Scaffolding and validation

[8:48] Actually, this is a real question, right? You've got a bunch of different models trying a task, how can they work together? So, we want to give models the best shot they can. We want to show their real performance. We don't want them to like fail at tasks because the models were like not elicited properly because we didn't ask them right. So, we spend time trying to elicit models and scaffold them to do the best job they can on a task. Um and this is one of the hardest parts of our job. And maybe one of the most interesting. Um we have several different scaffolds that we've used for models. Uh we talk about that in the paper, but they we do basically have the model put on different hats and take on different roles and like talk to itself.

[9:34] Mhm. Uh it looks a bit like a meeting. We have often a uh uh advisor that will advise different courses of action, and then we have an actor that will pick different actions to take based on what the advisor says, and then we have a sort of critic that will like look at things and go, "Hm, does this Which of these proposed actions do I think we should do?" Mhm. Uh and if we wanted to try scaffolding with a lot more models, uh we might need something like meetings. We've done a lot of checks to see if this means anything in the real world. I talked about how we're taking these internal PRs that we work on to the actual to-do list that we have and seeing whether the models can do them. Um, we also tried taking another data set called Sweep Bench, and that data set has software engineering tasks and has estimates. They don't do human baselines. The fact that there's an exponential trend stays the same. The doubling rate is somewhat different on Sweep Bench.

[10:36] We think that's basically because Sweep Bench estimates for tasks aren't that accurate um and tend to be underestimates of how long tasks take. Um we also tried measuring how messy our tasks are. We came up with some ways to see how like or like quantify how real-world like nitty-gritty our tasks were. Do they have automatic scoring? Are there like multiple ways to get to your solution? Are there sort of multiple hard bits? Or is it more like a problem you'd see on an exam? Uh, and we looked at how well models do on the more messy tasks. The trend stays the same. So, I think these results are pretty real. We tried really hard to figure out if we believed in these results, and I have squinted at this data a lot, and I have watched a lot of these videos of our baseliners doing these tasks. I read model transcripts. I think there's a lot of reasons you could be skeptical of things like this.

[11:35] But I think at the end of the day, I believe these results. I think they're pretty real. And I think model performance model length of task they can do is increasing exponentially. And if I had to hazard a guess, I'd say it's doubling every 7 months.

### Sponsor message

[11:56] Well, this episode's been supported by Brilliant, makers of fantastic courses and content like the stuff you're seeing on screen right now. They cover all sorts of mathematics, science, and lately they've really been putting together some fantastic stuff around computer science and AI. As you can see, it's all really well designed, highly interactive, and with a real streak of fun running through it. It'll bring a smile to your face as well as making you smarter. It's never too late to learn something new, maybe even change your professional direction. A Brilliant subscription would also make a wonderful gift for someone in your life who might just be ready to learn all this new stuff. To try Brilliant for free, visit brilliant.org/computerfile or scan the QR code on screen right now.

[12:45] There's also a link in the description, of course. You'll get 20% off an annual premium subscription.
