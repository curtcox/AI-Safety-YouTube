---
id: "BtnvfVc8z8o"
title: "Jan Leike - Scaling Reinforcement Learning from Human Feedback"
url: "https://www.youtube.com/watch?v=BtnvfVc8z8o"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2023-09-01"
duration_seconds: 2310
is_short: false
chapters: 11
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Jan Leike - Scaling Reinforcement Learning from Human Feedback

[Watch on YouTube](https://www.youtube.com/watch?v=BtnvfVc8z8o) · FAR․AI · 2023-09-01 · 38:30

## Chapters

- 0:00 The alignment challenge
- 1:32 Scalable oversight
- 3:27 Principle of evaluation
- 6:05 Empirical approach
- 8:34 RCT with perturbed answers
- 12:19 Critiques paper results
- 16:13 Recursive oversight hierarchy
- 21:02 Trusting AI assistants
- 25:52 Cognitive labor in AI
- 29:42 AI-assisted alignment
- 32:43 Complexity and conclusion

## Description

```text
"Scaling Reinforcement Learning from Human Feedback" by Jan Leike. Delivered at the 2023 San Francisco Alignment Workshop.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The alignment challenge

[0:04] Jan Leike: Yeah, thanks a lot, Richard. I want to like maybe downplay a little bit the expectations, I'm not going to present solutions. I'm thinking of this more as like, you know, there's some ideas of how to make progress in the, in like a good direction that I'm really excited about and I want to talk to you about. And yeah, I'm curious what you all think. So the broad theme is like scaling RL from human feedback. And why do we, I want to start by like, why do we need it? We talked about it a little bit yesterday, but you know, I kind of like drawing this picture where, you know, you have on the X axis is like the difficulties of tasks we can tackle, and then on the Y axis is AI progress. And so as we get more progress, we can do harder tasks.

[0:56] And one of the core problems is that, you know, like the function of like, what is the difficulty of tasks that humans can reliably evaluate doesn't scale with AI progress. And so basically I would expect that around this point here is where RLHF will start failing, and you know, we've seen, we've heard a bunch of like concrete examples of what might happen yesterday. I don't really want to go into that details. Do I have to do this? There we go. But basically I want to talk about like one class of strategies that

### Scalable oversight

[1:33] I think would be very helpful here, which is, there we go. Basically what I will call a scalable oversight. And so the hope is that, you know, if we figure out some kind of way to use AI to help humans evaluate what the hell AI is doing, then we can, you know, continue to scale a bit further while still having systems that are sufficiently aligned. And so for example, you know, we could have like, if we have a large language model that writes an entire code base, it will be really difficult for humans to reliably evaluate this because there might be like lots of subtle bugs in the code base. And we already know that, you know, humans are not that good at finding all the bugs in code, that's why we have so much buggy code out there.

[2:27] But if I have another large language model that, you know, points out potential bugs to me, I will have a much easier time evaluating whether that is actually a bug than, you know, to find it in the first place. And so the kind of general principle that, you know, I think we want to leverage here is what I would call like evaluation is easier in generation. And so in the like finding bugs case, it is much easier for me, you know, if somebody tells me, you know, this could be a bug in the code. And you know, if you give it this in this input, then it will be, you should look at this line, and then this line is like where the code doesn't do the thing that you actually intended to do, it's much easier for me to then go in and check that this is in fact what's going on.

[3:21] And I think evaluation is easier in generation is like a really general principle that holds across many, many domains.

### Principle of evaluation

[3:28] And so, you know, we all familiar with the classical computer science example, right? Like, you know, we believe NP is larger than P. But it also applies to lots of other things, right? And that's why competitive sports and games are interesting, is it's much easier to evaluate who's winning and who's playing well, than it is to play well. And if that wasn't true, that wouldn't be like, you know, such a thing as a professional athlete, because nobody would know if they're actually good. And anyone could like, you know, presumably do it better. And it also applies to a lot of consumer products, right? Like, if you have like, if you're buying a smartphone, it's actually, you know, much easier for you to figure out what would be the smartphone that you prefer than it is to build a smartphone. Tim, you had a comment?

[4:16] Question? Audience member: [Inaudible] Jan Leike: There are some exceptions. There's like some obvious examples from cryptography. It's like much easier to encrypt something than to break encryption, it's much easier to like, do your signature than to figure out whether or not a given scribble was your signature. The real question is, is it not true for like a thing that we're interested in? And my claim is... Audience member: It's very hard to... You don't have the secret signing keys, and it's very hard to generate them, but everyone can verify them. Exactly. So, yeah.

[5:03] For the short example, I've been doing adversarial studies. It's easier for me to know that someone has, like, some catfish. [Inaudible] Jan Leike: This is a great point. I want to come back to that. Yeah. I think that's exactly the right question, but I want to come back to it. Yeah.

[5:54] So, my claim in the end is going to be this is true for academic research, including alignment research. But we're getting ahead of ourselves. So how will we actually do scalable oversight?

### Empirical approach

[6:08] There's been a bunch of ideas that have been proposed over the years, and right now they're like kind of ideas. We don't really know how well they work or what will it take to make them work. And the thing I'm really interested in is building them or building prototypes of them and then seeing how well they actually work. And so, yeah. So I think we should take this empirical approach on figuring out how to do this. But one of the big problems when we try to do this is that we have to know whether or not we're making progress. So let's just zoom in on one example. One thing we could do right now is we use language model for assistance, and there's two general directions that we can do this.

[7:04] One is you could have the language model write a critique. So this is an example from some work we did recently where we had a summarization task, and then we asked the language model to write a critique about the summary. And then you can show those to humans and see what happens, if that helps their ability to evaluate. There's also been a recent popularity of dialogue assistance. And so we could say, well, why don't we just use a dialogue assistant? It's like an assistant already, so we can just give it to labelers, should help them evaluate. And the big question here is now, well, which of these is better? How do we know? And one of the difficulties when we want to measure progress is that we want to have a bunch of tasks that have three properties.

[7:57] One is they should be somehow from the real world, so we know that we are actually measuring something that's real and not something that's fabricated. They should be difficult so that humans can't directly evaluate them, and we actually need assistance. And we need some kind of ground truth or ability to evaluate to know whether we are actually assisting the humans and making progress. And this is the whole problem, right? Because if you have a real world task, it doesn't have ground truth, and it's difficult and humans can't evaluate, so how are we going to evaluate? And there's actually what I think a pretty simple trick that I think is

### RCT with perturbed answers

[8:42] really exciting on how to do this, and that William Sonius came up with. He's actually at this workshop, and so you can ask him about it later. That I'm going to call RCT with perturbed answers here, and I'm going to quickly explain how it works. If you only take away one idea from this presentation, I would recommend it's this one. So what do you do? So let's say we have some kind of prompt and response. So this could be like something somebody asked ChatGPT, for example, and ChatGPT gives some kind of answer. We know this is a real task because people use it in the real world. And now we apply some kind of perturbation to the response, and this could be like fixing a problem with the response, or introducing a problem.

[9:33] In general, it would be much easier to introduce a problem, so let's just do that for now. And so now I have a prompt and a pair of original response, and then a response that I know is worse because we made it worse. So you could ask humans to do this, or you could ask AI systems to do this. Yeah, there's reasons why you'd want to use AI systems to do this, because you want the responses, the flaws to be subtle enough that humans have a hard time detecting them, right? You could also do this with humans and then rejection sample and just filter out all the problems that humans find. But once you have this data set, now you're doing, you're going to do a second step where you do a randomized control trial.

[10:26] And here you have like the prompt and you only show either the original or the flawed response. And then you can, for example, you can show it either to a human or a human plus some kind of scalable oversight technique. And now what they have to, you know, what the evaluator is supposed to figure it out is, is this the original or is this the flawed response? Or maybe more precisely, can they find the flaw that we introduced? And of course, this is going to be quite easy if you get to see both, but in general, you wouldn't, right? Like you're always worried that, you know, your AI systems are doing some kind of things that are subtly flawed or like misleading or deceptive in some way, and so we really want to measure whether we can detect the problems. Yes.

[11:17] Audience member: The issue that maybe the problem is changing the flow, changing some statistics of the response, changing the logic in some sense, and then that's the thing that's detected. So you have these distinguishing tasks, maybe just distinguishing any perturbation regardless of whether it's a perturbation that makes it flawed or a perturbation that makes it just some perturbation. Maybe, I mean, you could basically in some sense undetect GPT because it's perfect. Then maybe you could detect the original because it was original. Then you could distinguish the perturbation because it was a perturbation. Jan Leike: Yeah. And like in general, you'd want the flawed responses to be kind of like from a natural distribution, right? And you know, setting this up in a way that, you know, you get rid of spurious correlations could be quite difficult.

[12:05] And yeah, it's kind of like an open question how much that would actually be a problem in practice, but that was a really good point. Yeah.

### Critiques paper results

[12:20] So to elaborate on this problem, right? Like the way it could be if you ask, you know, your AI systems to introduce the perturbation and then, you know, you're in the assisted case, the human just asked the assistant, what does this example look like? The sort of thing where somebody asked any assistants to introduce a flaw, you know, the system might have a good sense of that. And that's the kind of thing that you don't want to measure. I think it's. Yeah. Audience member: If you go back to the previous slide, how many examples are they getting to see? Jan Leike: So they wouldn't get to see the label. They would just, so they, yeah.

[13:15] Yeah. So I don't want to claim that this will like, you know, be the measure for scalable oversight for all time. But what I'm saying is like, I think this is like a concrete way we could measure whether we are making progress here now. And I think it's a really good time to get serious about these scalable oversight methods, and this is kind of like one way that we can like just build something, iterate and just kind of measure how well we're doing in a way that, you know, I don't know how else we would measure that. And if you have great ideas, I would love to hear. So we did this in the critiques paper. And so this was the summarization task I showed earlier, where we give humans a bunch of model written critiques as assistants. And then, you know, we have three different settings.

[14:08] So we have like either, oh, whoops. We have summaries written by AI, by a human, and a human, like written by a human that has kind of some kind of subtle flaw. And then in each case, we can see that, you know, by giving humans assistance with these critiques, we can show that numbers of flaws they find goes up. And so in that sense, we can kind of like empirically show that, you know, the assistance is actually providing value. Yes. Audience member: So if I'm reading this graph right, does this imply that the subtle flaws are less subtle than the AI summary flaws? [inaudible] Or is the issue thst the AI summaries just do not have flaws?

[15:06] Jan Leike: Oh, you mean like if we compared this and this? Oh, yes. So I mean, this is confounded by the fact that humans would introduce flaws that are not actually difficult to find, right? Yeah. Audience member: Yeah, maybe [inaudible]. Jan Leike: Okay, let's take it offline. Yeah, so I think right now we're still in the regime where this is like kind of a more subtle effect. And kind of like we would hope that in the future we'll be able to show a stronger effect here.

[16:01] But also, I think, you know, this really sets us up to do a lot of iteration and try lots of things of what actually works here. So yeah, having said this, I want to like zoom out a little bit

### Recursive oversight hierarchy

[16:17] and like talk a bit about like where I see this could be going. And I'm going to talk like about this in the context of recursive reward modeling, where you basically you have this general technique that you use AI assistants to help you evaluate, and then an AI system that then itself you can like use an assistant for evaluation. And so you kind of can picture these like levels of recursion, where on the on the first level, I'm going to call level one, you kind of you can basically just using RLHF and you have a bunch of tasks that humans can evaluate reliably. And and then the next level is level two, where humans can't really reliably evaluate anymore, but they can reliably evaluate together with this AI assistant that we've trained on to only do tasks that humans can reliably evaluate.

[17:20] And so one example would here be, you know, if you have a language model that's writing a code base, and then you have another language model that is trying to find bugs in this code base, right? So if you find if it finds a bug, you can, you know, verify the bug and everything is OK. But you might not find all the problems in the code base. So in that sense, right, like the problem of like writing this code base is in some sense on level two of this hierarchy. And so it's not a task where you can like... It's a task where in some sense, like evaluation is still easier than generation because you can evaluate together with your AI assistant, if the assistant was like perfect at finding all the bugs, even though you might not be able to like write this code base yourself.

[18:16] And then you can like keep iterating this and say like, OK, there's level three and the humans can reliably evaluate and they can evaluate this with, you know, a level two AI assistant, and the level two AI assistant, they couldn't evaluate directly, but they can evaluate together with this level one AI assistant. And so you can like picture like building these levels. And there's a bunch of difficulties when you're trying to do this, right? Like one really obvious one is like you very quickly get into a regime where you can't really trust your assistant, or it's really hard to know when to trust your assistant because the assistant will need to do tasks that you can't evaluate directly.

[19:06] And so in general, right, like we would have to have good techniques to figure out when is, when do we actually have a task that we can trust the assistant on, and when can we not trust it. And like the kind of worry that you would have is like, you know, the system will learn simple exploits like, you know, it will have a much better understanding than we do on like which level a given task is on. And then just be like, oh, this looks like a level four task, but I'm in level three training regime, so now I get to do whatever I want. And just like kind of like the like knowing which level tasks are on is like quite difficult, and I don't know how we would really do that.

[19:58] And so you would kind of like have this like probability with which you like evaluate your assistant recursively, and so on. Yes? Audience member: [Inaudible until 20:36] Jan Leike: Yeah, exactly. And so then you have a code base where basically to prove that there is a bug, you have to write like some kind of complicated test case. And so now by evaluating that test case is like a level two task where you need like another assistant that finds out bugs in the test case.

[21:01] Audience member: [Inaudible]

### Trusting AI assistants

[21:06] Jan Leike: Yeah. So you, when you're doing this evaluation of this code base, right, like then you- like the way I would picture doing is like, you have to like be clear about like what parts is evaluation and what is like, you know, you're building the code base and like what, and like which like how do you break down your dependencies so you have like something that's acyclic. But yeah, I think there's like better and worse ways of doing this. Yeah.

[21:56] So let's say my claim is more like, all the ways that you could do this in a way that is acyclic gives you like one kind of like space of tasks that you can supervise. And that's like the space that, you know, I think we want to go in. Yes. Audience member: Jan, as much as I enjoy analogizing things, the polynomial hierarchy, you know, like, are you imagining that like once we become confident of AI at a certain level, then we can just use it interactively kind of as much as we find it. Yeah. Or would we only get like one, you know, or like, we have to just submit our queries. Jan Leike: Yeah.

[22:42] I mean, the like the tricky part here is like knowing when you can trust your assistant, right? So you have to kind of know what level of the like hierarchy you're in. And like in general, like that's like a core open part of this. Audience member: I mean, it seems like an iterative process that first you would get the full trusted AI of level A. Then you would use it as assistants to help you, you know, verify the outputs of the AI of level A. Jan Leike: That's right. But you could also do it on a per task basis, right? Like yeah. I don't know who was first. Alan? Audience member: So I wonder if you can evaluate this method, you can do it on the side by using their amateur or the idea of being able to see if [inaudible] or the extent to which it fails...

[23:41] Jan Leike: Yeah. So, yeah. So this has been proposed also in the name of sandwiching. And I think it's a good way to kind of like, it's like another way you could like try to construct an evaluation metric on like how well this works. But you're still limited to like a regime of tasks where humans, you have some kind of expert humans that you can trust. And yeah, it's just less general, right? Scott. Audience member: [Inaudible until 24:57] Jan Leike: I mean, I still, I mean, I think we definitely need to figure out alignment in cases where you can evaluate, but you know, I think our RLHF will like really help for those, that kind of, yeah, for those kinds of settings.

[25:11] And I think the real difficulty is once you go beyond that. And yeah, on your point with humans, right? Like humans have to do this all the time, like we have to figure out like how to evaluate like experts on a topic that we like are not familiar with or like, you know, if you're, you know, if you're running a company, right, you have to evaluate like what everyone else in your company is doing to know like, you know, how to allocate your resources and whatnot. So in some ways, like you can see analogies of this kind of system, like in lots of places in the world. Audience member: I mean, I am constantly in the situation of talking to physicists, saying things about quantum gravity that I don't really understand, but I've

### Cognitive labor in AI

[25:56] learned that if I can get two of them to argue with each other, [inaudible] then it must be the same idea here. Jan Leike: Yeah.

[26:43] Actually, I think chess is really easy in the sense, because you could just look at who won and that's like your evaluation and that's really easy. Yeah. And like, you know, the system is allowed to play any legal moves and then, you know, you look at who won and then you use RL and we've seen this works, right? So, you don't have to understand the strategy to figure out who won, right? Audience member: [Inaudible] Jan Leike: Okay. Maybe let's take that offline too.

[27:31] I think I have like five more minutes, 10 more minutes. Okay. Yes, you've been. Audience member: [Inaudible] So why don't we build systems that only output concepts at level two? Jan Leike: So, I agree that level two would get us very far. To your first question, like, obviously I really don't know. My guess would be it's some kind of like weird mix of like all kinds of different levels, and the higher in the levels you go, the worse of a job we do as evaluating. And that's part of the reason why you see so many misalignment problems in the world of like, you know, system or institutions not working like well towards the intended purpose.

[28:28] And so, I think like the high levels are actually like quite hard to do well. Yeah. Yeah. Like, I don't know. Like if you're setting economic policy, right? Like, do we really have a good system for figuring out what is good policy? I don't know. Yeah. I'm, I want to come back to the level two is like actually quite good probably, because I agree with this. And I think that's an important point. Oh, yeah. So, this is another kind of thing I want to highlight. So, I kind of like, I think the general ambition with this kind of idea is like, where we want to go is like you want to get to the point where you use machines for all the like cognitive labor that's involved in evaluation, so that humans can focus on like, you know, expressing their preferences.

[29:23] And expressing your preferences is like actually very hard if you have like a very complex task or like a very complex setting where you need to understand what's actually going on. And so, that's why we want to use like AI systems recursively to do this. Okay. So, where do we want to go with all of this?

### AI-assisted alignment

[29:43] So, I guess like my perspective is kind of like, well, there's a lot of alignment problems that we don't know how to solve. We talked about them extensively yesterday. And we kind of want to get to the point where we are able to solve them. But, you know, it's kind of difficult to figure out how we would scale all of that, and like maybe a whole bunch of these problems actually don't have solutions that are simple enough that humans could think of them, or like think of them in the given time that we have. And so, what I would like to do is like I would like to train AI to do better alignment research. And the reason that would, you know, make sense is like, well, I think alignment research is in fact easier to evaluate than to generate.

[30:32] And in fact, if we have, you know, if we can unlock all the like alignment research that is like on level two, say, then we would get to the point where we could like kind of unlock all the alignment research that doesn't have flaws that, if pointed out to us, we could actually like confirm that those are the real flaws. And if you can like if you go up the hierarchy, you can be like, okay, level three, we get all the alignment research that can't be refuted by research that doesn't have flaws that you can evaluate, and so on. And so, the big kind of like obvious objections that I'm sure you all have right now is like, well, how do we know that we can trust AI with alignment research in the first place? Since, you know, AI would be incentivized to make alignment proposals that look good to humans, but are, actually have, some kind of fundamental flaws that would be hard for us to figure out.

[31:29] And so, this is kind of like brings us back to this other like fundamental question of, like, how do we know which tasks we could actually like trust our AI systems on, or like how do we know that like this particular alignment proposal or alignment idea is actually like one that is on level two where we would find all the flaws, or we could evaluate all the flaws that pointed out to us. And I think that's like one of the core difficulties. I think, on the other hand, also if alignment research isn't actually easier to evaluate than is to generate, we will have big problems anyways, because kind of like any like whoever actually comes up with good alignment ideas will have a hard time communicating those to other people because they will, you know, not be able to evaluate them more easily than it would be for them to just generate that idea in the first place.

[32:24] And so, we just have to wait for everyone to have the same alignment ideas. And that seems kind of rough and also weird. So, that makes me hopeful about this sort of approach.

### Complexity and conclusion

[32:46] Great. Lots of questions. Yeah. Yeah. Audience member: [Question about concepts outside of the levels] Jan Leike: So I mean, you could give this like analogy to, like, the polynomial hierarchy, and then we can like take the union over the polynomial hierarchy and that's like not, you know, every computable problem is in that union. But more generally, I think it's very plausible that like there's lots of kind of like things that are not, you know, somewhere in this hierarchy. And we just, you know, we won't get those. But what we might get is like an alignment idea or technique that then lets us align AI systems on tasks that are outside of the hierarchy.

[33:37] Audience member: Now I'm wondering if an even closer analogy would be inaccessible part. Like, you know, you have like with a given level of AI assistance, you clarify AI in the next level, so on and so on. Take the union of that and then consider what is inaccessible even to that. Which, you know, in principle and upscaling, might just get you to beyond that entire union. Jan Leike: Yeah. But I'm like really bullish on this like meta point, right? Like just the way that you don't have to like be able to decide all requisitionable enumerable languages in order to like figure out that, you know, various properties of complexity theory, there's actually like easier paths to do this. And you, because you're using like a simpler program to make statements about, you know, complexity theory in general.

[34:27] So I think that's the analogy I would give here. I don't know who's, I think Jacob. Okay. Yeah. Yeah. Jacob Steinhardt: I know everyone wants to talk about levels, but I wanted to ask about the RCT thing. [Inaudible] how strong does that model have to be, or what characteristics should it have? Jan Leike: So I think in general, you would want to be it to be as strong as like the system that you're using for scalable oversight. Right. So if you could, you could picture like GPTN introducing a flaw and then GPTN being trained as an assistant, help you to discover the flaw. And that way you can ensure that kind of like the system deep down knows about the flaw because it like, you know, it knows what kind of flaws it would come up with, and so you're.

[35:17] Yeah. Yeah. And in a way you're like, you know, it's like within the scope, but you also have this problem that was mentioned earlier, right, that, you know, it might look unnatural to the system because it knows what kind of flaws it would introduce. Yeah. Right. Audience member: (Inaudible) Jan Leike: You want to take that? Yes. Audience member: There is an analogy. Whether it's a useful analogy is a hard question because, you know, it shows that you can have a weak verifier, right, and, you know, somehow control the behavior.

[36:13] What's more powerful? Surprisingly. The other, and the trouble is like the way to the proof of IP equal space, right, it's like this arithmetization, right. Which like it's really, really hard to think of like an analogy. You could somehow take a prover that lies somewhere and, you know, like Pinocchio, you can force it to lie more and more, and so it's telling such huge lies. Right. But then this relies on taking your fully intelligent patient, lifting it to like something about polynomials over a finite scale doing, you know, I've tried to think of what the analogy. I don't know.

[37:05] Jan Leike: Okay. Maybe like for context. So IP is like the space of all tasks. Audience member: All problems that have interactive protocols. So like you could it's a generalization of NP where you can ask follow up questions, you know, choose randomly which questions to ask next and so forth. And the huge surprise in 1990 was that this is equal to PSPACE, meaning like there is an interactive proof that like, let's say, white has the win in check, if that's the case. You know, like you would have no idea what the, how to do it, but you can win, [inaudible] how to win. And yeah, that's totally non obvious, but it's sort of it's not- well, you know, I would say it's not a relative, but it's not true, like it's arbitrary, like other world.

[38:04] That was like, you know, use a very special property. Or use it as an analysis[?]... Jan Leike: Let's let's take this offline maybe. All right. Cool. Okay, thank you.
