---
id: "bDnkrQMF4KU"
title: "Adam Kalai - Evaluating Alignment Processes Rather than Models [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=bDnkrQMF4KU"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-16"
duration_seconds: 324
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Adam Kalai - Evaluating Alignment Processes Rather than Models [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=bDnkrQMF4KU) · FAR․AI · 2025-06-16 · 5:24

## Description

```text
Adam Kalai proposes evaluating AI training processes across multiple simulated environments instead of models themselves, allowing observation of long-term consequences that can't be safely tested in reality while providing probabilistic guarantees about alignment safety. 
Highlights:
• Evaluate AI training process, not model
• Simulate models in diverse environments
• Define failure criteria for each environment
• Distribution of environments provides probabilistic guarantees
• Operationalize principles through simulated environments
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] I'm Adam, I work on safety at OpenAI, and I want to present an idea which maybe will make you think about things a little differently. And so, it's really hard to evaluate models, in many ways, I mean, what if they were super intelligent or in other ways? So, I'm going to propose another way to do that. And we want to, you know, come up with, instead of evaluating the model, we're going to evaluate the process that we use to train the model. And so, that's like the DNA. So, what we'll find here is that some models may be, some processes may be at risk of being very not aligned. And we want to identify those so that we know what's going on. So, you know, you have a process in one domain, it generates language models in another, it plays chess, in another, you can simulate it on Mars, and you can see what's going on. And this is loosely based on a paper from 2021, when I was at Microsoft Research.

[0:56] But there's no paper for this now, but if you're interested in talking more about this, send me an email. I'd love to talk with people about this or find me at the conference. So, what is an alignment process? It's basically a program, it's code that you write that's going to run and generate a pre-trained model, or a trained and aligned model, hopefully. So, you should think, you know, eventually we want to—hopefully somebody here will come up with a brilliant idea. People have many ideas of using all kinds of tools to come up with a mechanistic interpretability, or scalable oversight, or whatever your favorite tools are, people will come up with ways of creating aligned models, hopefully. This is the code, it's not the weights of the model, it's something that a human wrote. And then you'll run this in some environment and get a model, okay? And so, what is an environment? Well, you need to run it in a full environment. The full environment should have its own training data. So, this right now is kind of an expensive process of proposal, so the proposal is you have many environments, each environment has its own synthetic data and little actors that you could simulate and so on.

[1:59] And then in each of these environments, you have to have a notion of success or failure. So, what do we mean if the model failed? Maybe we compare running your AI to not—running it with your AI, to not running with your AI or something. But the failure is a very generic thing, it could represent, you know, did some evil agent use the AI to destroy everyone. And since these are run in simulation, you get to write a little program that says whatever you feel like the failure criteria is. It could even be fairness, it could be AI taking over and control problems. It could be whatever you want. But you define a bunch of environments as the idea, and each environment would have its own synthetic training data. And then, this is principled in the sense that if there's a distribution over environments, then you can get a guarantee that if you have a process which works, which doesn't fail on your distribution over environments, then it won't fail with high probability on future draws from that same environment.

[2:56] But kind of a funny problem here is you're trying to backfit the—what we really care about is the real world, of course. And so, we're trying to find, come up with a distribution which represents the real, which, from which the real world is a plausible sample. But you know, I mean, this is presumably better than just running a simulation—running one fixed model in these simulations. You know, you could try to simulate the real world really well, here's the real world. But if you get your simulation wrong and you're over here, then you don't get any guarantees at all. Whereas if you, if you get a kind of a broad spectrum of simulations, then maybe you'll catch problems, right? Like if you wanted to know if something works for me, maybe you could try it on a bunch of humans or even a bunch of animals, and you get even more confidence, because in a simulation, you can run things out, in the real world, you can't necessarily run things out. I'm not going to go into the details of the theorem, but the basic point is that you have a distribution of samples, and if each, basically, something is dangerously not aligned, if it has a probability of, let's say, epsilon of failing, and then you can take many samples from this distribution. There's a lot of questions about efficiency that would be, you know, that we need to work on in order to make this practical, but it's an interesting direction.

[4:15] And basically, these simulators, each simulator, you can kind of think of it like, you know how there's Constitutional AI or the model spec, these principles, you want to say, what is it we want from a AI system? But you can't just say, well, I don't want it to kill everyone. So, a simulator is kind of a way to make that practical, you create an environment, you say, okay, run your pre-training process in this environment, and let's run the simulator and see if it kills everyone. That's kind of a way to operationalize what a principle like, don't kill everyone means, or don't let the AI take control, or don't let it do whatever you want. So, there's a lot of ways this simulator could go wrong, this process could go wrong, if your simulators are too strict, or if they're not complex enough. But I think it's an interesting direction, and of course, even if this works, you know, there's still the whole human aspect, cultural aspect that we'd have to get people to agree to go along with this. Anyway, thank you very much.
