---
id: "O2OlL2Wp48A"
title: "Self-Distillation: A New Way to Teach and Align AI Models | Andreas Krause (ETH Zürich)"
url: "https://www.youtube.com/watch?v=O2OlL2Wp48A"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-09-16"
duration_seconds: 528
is_short: false
chapters: 11
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Self-Distillation: A New Way to Teach and Align AI Models | Andreas Krause (ETH Zürich)

[Watch on YouTube](https://www.youtube.com/watch?v=O2OlL2Wp48A) · FAR․AI · 2026-09-16 · 8:48

## Chapters

- 0:00 Self-distillation for alignment
- 0:30 How we teach models today: supervision vs. RL
- 1:09 The idea: rich directional feedback
- 1:55 From in-context learning to in-weight learning
- 2:47 Self-Distillation Policy Optimization (SDPO)
- 3:45 Token-level credit assignment (a coding example)
- 4:48 Results on coding (LiveCodeBench)
- 5:10 Learning from user preferences
- 6:17 Results on real conversations (WildChat)
- 7:10 Constitutional alignment on Apertus
- 8:09 Takeaways

## Description

```text
Andreas Krause (ETH Zurich) on self-distillation, a third way to teach AI models beyond supervised learning and reinforcement learning.

Krause presents self-distillation as an alternative to supervised learning (demonstrations) and reinforcement learning (trial and error, prone to reward hacking). The idea: turn transient in-context learning into durable in-weight learning by letting the model act as its own teacher, reflecting on directional feedback, an error message, a user's correction, or a constitution, to produce a training signal. Their method, Self-Distillation Policy Optimization, gives token-level credit assignment, pinpointing which token caused a wrong answer instead of penalizing a whole response. He shows gains on coding (LiveCodeBench), on learning from real user preferences (the WildChat dataset), and on constitutional alignment of Apertus, an openly trained multilingual model, using the Swiss AI Charter, with higher alignment scores at little cost to capability.

Chapters
0:00 Self-distillation for alignment
0:30 How we teach models today: supervision vs. RL
1:09 The idea: rich directional feedback
1:55 From in-context learning to in-weight learning
2:47 Self-Distillation Policy Optimization (SDPO)
3:45 Token-level credit assignment (a coding example)
4:48 Results on coding (LiveCodeBench)
5:10 Learning from user preferences
6:17 Results on real conversations (WildChat)
7:10 Constitutional alignment on Apertus
8:09 Takeaways

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=JKJxHkO-MLker_fi

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Self-distillation for alignment

[0:00] Thanks a lot for having me. Excited to be here. Today I'd like to talk about self-distillation, and I'd like to try to convince you that self-distillation is an exciting avenue towards teaching machines on how to behave and offers some promising avenues towards alignment. Very happy to discuss those with you. This is, of course, joint work with a fabulous group of PhD students, postdocs, and senior collaborators. Some of the work is going to be at ICML and the workshops later this week.

### How we teach models today: supervision vs. RL

[0:30] So how do we currently teach machines how to behave? In supervised learning, we teach them through demonstrations. We tell them exactly how to behave. And this works well in certain cases, but of course, obtaining demonstrations can be expensive. In some cases, it might be hard to tell exactly how a machine should behave. The other paradigm is reinforcement learning, learning through trial and error, right? Trying to figure out until we succeed. And that, of course, also is incredibly effective, but also comes with challenges. So in some tasks, it might be very difficult to find solutions that work. It might also be prone to reward hacking and all the issues around that.

### The idea: rich directional feedback

[1:09] So what if we could teach machines in a different way by offering rich directional feedback, maybe also how machines should not behave? To do this, of course, the question is kind of what kind of feedback to look at. If you think about coding tasks, you might get messages naturally from the environment. If you think about learning from preferences, you might not just want to compare solutions with each other, but learn why one solution is preferred over the other. So for this to work, we first need to be able to make sense out of observations. And one natural avenue towards this is to use AI models themselves, right, through in-context learning, which is surprisingly effective at making sense of error messages or instructional feedback.

### From in-context learning to in-weight learning

[1:55] The trouble with in-context learning, of course, is that it's transient, right? As soon as instructions leave the context window, they're gone. So the key idea behind self-distillation is to leverage in-context learning for in-weight learning. So let's look at an example. Suppose you give a model a task like, how much water fits into a cube with side lengths 1 meter? And the model might make an attempt like 1 ton. But maybe here we didn't look for a unit of weight, but maybe rather a unit of volume. So if we taught the machine by trial and error, it might take a while to figure out what's going on. But if we say directly, please respond in liters, it's very easy to use in-context learning to reflect on that feedback and ask the model how it would have responded differently in hindsight given that feedback. So that's the

### Self-Distillation Policy Optimization (SDPO)

[2:47] supervision signal that self-distillation uses. So it means we basically do on-policy distillation, but instead of using an extra separate external teacher model, we use the model itself, just with this context provided in context. So it means the model is used twice, as a model we try to train, but also as a teacher, a self-teacher that reflects on this feedback as a supervision signal. So the algorithm that optimizes this KL divergence between the student and self-teacher, we call Self-Distillation Policy Optimization, can also be viewed through the lens of reinforcement learning. But basically, it's a policy gradient technique. But we use a very special kind of advantage that really is on an individual token level, looking at essentially the log ratio between the emission probabilities of the teacher versus the student. And it turns out both of these views

### Token-level credit assignment (a coding example)

[3:45] are equivalent in expectation. So let's look at these token advantages. Here's a simple example from a coding task. You might ask a model to write a Python function that returns all numbers from 1 to n and makes the attempt on the top right. But suppose we wanted the model to not include the final number n, which is incorrectly done by this attempted solution. If you just penalize the model by "this is the wrong response," it would have trouble figuring out what really is the issue. But if you tell the model, don't include n, use in-context learning, we can look at the advantage, which is basically zero pretty much everywhere, except in this place with this plus sign here, which is really responsible for producing the wrong solution. So in contrast to RLHF methods like relative policy optimization, that we uniformly penalize all emitted tokens that are associated with incorrect examples, here we know precisely what goes wrong. And we can actually counterfactually reason about what would have been alternative advantages on that position and any other position. So it's a much more fine-grained credit assignment that

### Results on coding (LiveCodeBench)

[4:48] one can do this way. And this works pretty well. So here's some coding tasks on LiveCodeBench. Just adapting an open-weights model to that benchmark task using standard RLVR methods, you can do this pretty effectively. But using this directional feedback offered by error messages like those on the left, you not only learn faster but also find better solutions. And this turns

### Learning from user preferences

[5:10] out to be very useful for other purposes as well. So what about kind of learning from preferences? Let's look at kind of an imaginary dialogue between a user and an AI model. The user might ask, should I standardize features before training a linear model? And the model might respond, "Good question. This is something that many get wrong when they first blah, blah, blah." And so the user really preferred a direct response saying, "Get to the point. Just answer directly without filler." So this is a very strong expression of preferences. And you can use this directly as a signal to train the model. So one can use self-distillation by basically taking the user's initial prompt as the input, taking the model response as basically the response, and then taking the user's next turn as the feedback that's reflected upon in context. So we basically try to update the model of how would it have responded differently in light of the next turn.

[6:08] Again, one can look at these token-level advantages, and these words that are sort of filler words get penalized, and the words that relate to factual responses get updated.

### Results on real conversations (WildChat)

[6:17] And this works pretty well. So here's some results on the WildChat dataset released by AI2. On a bunch of real-world interactions with real users with ChatGPT, training on these triples, user turn, AI turn, user next turn. And across a whole range of different benchmarks, one can take open-weight models that already have been aligned with methods like DPO and still get some improvement on benchmark performance purely by aligning on these real interactions. So here are some of the token-level advantages. What's also quite interesting is that the model figures out kind of when to update and when not to update. So if the next user turn really corresponds to an expression of preference, like "rewrite in a formal professional tone," you'll get to see these informative token-level advantages. Whereas in context where the user turn is not following up on the initial conversation, these advantages are basically zero,

### Constitutional alignment on Apertus

[7:10] and the model doesn't update. Now, this is really useful for constitutional alignment as well. So we apply this to constitutional alignment on the Apertus multilingual language model that we train fully open in Switzerland. And the next version, 1.5, is about to be released pretty soon. And we apply a phase of self-distillation in post-training of Apertus, where we would use a student model, Apertus, give it some controversial prompts, ask it for responses, then have a feedback model that would reflect on these attempts together with the constitution, the Swiss AI Charter, and produce a rich natural language token, basically feedback, that itself then reflects upon through self-distillation as a training signal. And so here, the same model is used for all these different phases: to make attempts, to criticize themselves with respect to this constitution, and to reflect on it as a training signal.

### Takeaways

[8:09] And this works pretty well. So you get quite substantial improvements in terms of alignment scores without hurting too much of the capabilities as well. So that's what I wanted to talk with you about. I think it's a really exciting different way of teaching machines how to behave, with, I think, very interesting opportunities towards alignment. And the paper is going to be at the main conference. Some other work is presented at workshops. And very much looking forward to engaging with you here. Thank you very much.
