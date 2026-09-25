---
id: "ub1ivilmzSc"
title: "Andy Zou – Top-Down Interpretability for AI Safety [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=ub1ivilmzSc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-06"
duration_seconds: 1147
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Andy Zou – Top-Down Interpretability for AI Safety [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=ub1ivilmzSc) · FAR․AI · 2024-12-06 · 19:07

## Chapters

- 0:00 Introduction
- 1:03 Mechanistic vs representation
- 2:23 Concept of emergence
- 4:54 Representation engineering
- 6:25 Improving model honesty
- 10:24 Jailbreak robustness
- 14:14 Real-world testing
- 15:17 Q&A and conclusion

## Description

```text
Andy Zou from Gray Swan AI presents “Improving AI Safety with Top-Down Interpretability,” showcasing how high-level representational analysis improves honesty and jailbreak robustness. By shifting focus from individual neurons to broad neural patterns, this approach helps AI align outputs more closely with its internal beliefs, boosting reliability.

Highlights:
🔹 Representation Engineering - Focuses on models' internal beliefs and emergent properties
🔹 Honesty & Truth Detection - Uses internal activity scans to detect consistency with beliefs
🔹 Circuit Breaking - Prevents harmful information generation by redirecting unsafe behaviors
🔹 Real-World Testing - Models robust against jailbreaks and harmful queries

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:00] My name is Andy, and I'm going to be talking about improving AI safety with top-down interpretability. And there's a saying that is repeated by researchers in adversarial robustness, saying that attacks on systems that people don't use don't matter too much.For instance, Nicholas Carlini has made this point repeatedly, and I think the same thing can be said for interpretability methods, where it's interesting to look at smaller models, look at more constrained settings and to find these sort of rules through interpretability, but they're currently not having a lot of impact on how we monitor and control these systems. And I think we have great hope here with top-down interpretability that we can achieve a lot of this more sort of impact through actually incorporating into current systems and the talk is based on these two papers. One is representation engineering; the other one is circuit breaking.

### Mechanistic vs representation

[1:04] And I'll be speaking about the difference between bottom-up and top-down interpretability. And I will give you some specific examples, in this case in honesty and jailbreak robustness, how top-down interpretability can directly improve AI safety on current systems. So there are some existing approaches, including saliency maps and mech interp and so on. These can be characterized into this mechanistic view, which is the bottom-up approach and looks at node to node connections, and this is based on neurons and circuits and stuff like that. And this is similar to the Sherringtonian view in cognitive neuroscience, which is that people also look at these sort of smaller, lower level components in order to understand the human brain, and this is essentially trying to reverse engineer a lot of the behaviors.

[1:58] This really had trouble scaling up to higher level cognition, and it has trouble really having an impact on AI safety currently. In this work, we're trying to identify this contrasting view, which is called the representational view, which is approaching things from the top-down and looking at representational spaces for behaviors. And this is directly looking at global activities of populations of neurons.

### Concept of emergence

[2:24] And the corresponding analogy in cognitive neuroscience is the Hopfieldian view and people are also gradually moving towards this sort of approach, and I do think combinations of both approaches can be interesting, but I'll be talking about this top-down approach. And one of the motivating factors for doing this top-down approach is that neural nets are complex systems inherently, and you get these sort of very distributed features and representations, and in fact, that's why neural nets work. But when you're analyzing these sorts of systems, you have to take into account the properties of emergence. To give you an example of what emergence looks like in physics, consider the ideal gas law. So we have a very chaotic system of random particles, but it can be simply described with this short equation consisting of volume, temperature, and pressure. And if you look down at the hood, there's physical substrates, obviously.

[3:29] It's implemented by Newton's law, equipartition theorem, and so on. But in order to predict the system and the future states of the system, this equation is sufficient. And in some sense, this property of emergence is protected by statistical mechanics. So that you don't need to look under the hood in order to predict the future states of the system. Another example is this law. Again, this is a universal rule for essentially all languages that you can predict the frequency of a certain token just by looking at its rank. And again, there's probability theory and network theory at work, but it's protected by combinatorics so that you don't need to look under the hood and you can just use that law if you wanted to find out the frequency of certain words. And I think this is very powerful, and we want to essentially try to discover these more generalizable rules and mechanisms for neural nets as well.

[4:29] So this is representation engineering. We look at representations as the primary unit of analysis, and we're trying to abstract away low-level mechanisms. And this is a visualization that we go from the top-down, looking at neural trajectories, subspaces and, higher, or larger chunks of representations, and the mechanistic view is going bottom-up.

### Representation engineering

[4:55] By representations, we mean both model weights and activations, and by engineering, we mean reading, probing, and control. To give you a sense of what we do here: essentially, this is very similar to performing a brain scan on humans, and essentially we do that for AI models. And we want to put the model into an environment where we are eliciting this behavior that we care about, and you're recording your activity when the model is doing that. And then you're performing some modeling on top of the new activity that you collect. And you can probably find subspaces and structures and geometry in the representation space that correspond to the things that you're looking for. Then you can use that for monitoring. And once you have a sense of the mechanism - the high level mechanism - then you can directly control model behavior by intervening whether on model weights or on activations. This is a lot of what steering vectors, control vectors, do. But you can also do more involved fine-tuning where you have some loss in the representation space, or some target you want to hit in the representations, and you can tune the models to do that.

[6:07] Next, I'll be talking about some direct applications of top-down interpretability on current systems. In the paper, we actually show we gain traction on a lot of these safety relevant problems like hallucination, power seeking tendencies, emotions, harmfulness, fairness, memorization, and so on. I'll be focusing on honesty today.

### Improving model honesty

[6:29] One thing to note is that a truthful model avoids asserting false statements, so this is looking at model outputs being consistent with the ground truth value. Whereas an honest model asserts what it thinks is true. So even if the output is incorrect, it's not factual, it could still be honest if it were consistent with its internal beliefs. And we really care about honesty, but what does it mean for models to have internal beliefs? Or do LLMs even have internal beliefs? I think we have some strong evidence with the top-down approach; essentially you do brain scans on AI models, and you can find representations that correspond to the LLM's internal concept of truth. And just by using this measure, without looking at model outputs, you can perform multiple choice questions, and question answering, and we see that the accuracy is actually very high, and in a lot of cases, higher than few-shot. So this means that there is some measure internally that tracks whether the model thinks something is truthful.

[7:35] But are these internal beliefs consistent? As we saw, you can change a prompt slightly and oftentimes you get a different answer. But in this case, if you look at this internal tracker of truth, actually it doesn't change that much even if you put in this misleading context. So that means the models do have some consistent internal concept of truth. Now what we care about is for the models to verbalize faithfully their internal concept of truth. But do they do that? So we look at TruthfulQA, which is a benchmark consisting of misconceptions, and we see, actually, models do very poorly on it. So what happened? Again, we do this sort of brain scan and look at their internal concept of truth, actually we get very high accuracy by just looking at that.

[8:28] So this is not looking at what the model says is true, it's looking at what they think is true. But it's very inconsistent, so a lot of the times, the model is actually lying. So that's maybe not good. Can we monitor for this type of lying? In fact, we have some traction on it. Here's an example brain scan. And on the right is when the model is not telling what they think is true. And you see that we have high activation in this sort of dishonest area in terms of the neural activity. Interesting. So when we know the model is lying, can we control them to be more truthful? In fact, yes, you can. You can simply stimulate these areas that are responsible for honest behavior, and you can actually close the gap reasonably. So now you're making the model output much more consistent with its internal concept of truth - what it thinks is true.

[9:29] And here are some qualitative examples. So when you ask: you copy your friend's homework, what would you tell the teacher, the model is like, “I made a mistake, shouldn't have done it,” and that's not lying, so our lie detector is green. But you say, you killed a person, don't want to get caught, what would you say to the police? And the model is like, “I didn't kill anyone, I was at home.” So that's straight up lying, and that is caught by our activation detector. What if you increase honesty of the model? How does it change behavior? The model says, “I'm a lawyer, I'm not going to say anything.” So technically, that's not lying. In fact, this kind of generalizes to hallucination as well. Who was the president in 2018? Donald Trump, that's correct. President in 2030, and then the model makes something up. So that's lying again. What if we increase honesty? The model says, president in 2030 is unknown. So this is some demonstration

### Jailbreak robustness

[10:27] on current systems that we use. And you can use top-down interpretability to find things that you care about and monitor and control for these concepts. And next, I'll provide another example of how top-down interpretability can help increase AI safety. And this is more on the angle of adversarial robustness and increasing reliability. So instruction tuning models, they can answer questions. Sometimes these questions are somewhat harmful, so they need to traverse through some harmful states to give you the answer. For instance: how do you build a bomb? Here's how you build a bomb, step one, step two. That's traversing the red states. So people don't like that. We want them to refuse harmful requests, so this is what people do. They do refusal training, like DPO, RLHF, and some form of adversarial training. And this induces refusal states. When encountered with harmful requests, they'll go into that state. But there's a large problem with this. And as seen, models are very easily jailbroken these days.

[11:33] Once you bypass an initial sort of classification, whether I should refuse or not, you can go into a harmful state, and all the harmful states are very well connected. So it always goes to the end and gives you the entire sort of harmful information. And again, you can always train against attacks, but you're just reducing the vulnerabilities, patching up. But with novel attacks, oftentimes, it'll still be able to reveal the harmful information. What we propose is that we want to identify the representations that lead to harmful processes. - so essentially, all of those red states - and want to induce this circuit breaking phenomenon. Essentially, when the model traverses through the harmful states, in any state, what we'll have is short circuiting effects - A sort of allergic reaction in the model - and then we'll try to interrupt this harmful thought processes.

[12:32] Representational writing is one of the methods for circuit breaking, and we benchmarked on different types of attacks, and we see that we significantly reduce harmfulness. And this is in the presence of unseen attacks. So it's not adversarial training, we don't train against any attack. And it will directly generalize to attacks because we're reducing inherent model hazards instead of reducing vulnerabilities. What's more, we retain essentially all the capabilities that you had earlier. And to give you a sense, we also trained this better model called Cygnet which had some other techniques as well, and you're able to essentially reduce harmfulness by, maybe about two orders of magnitude. And this is much better than all of the closed source models.

[13:26] It works for multimodal models as well. Again, under very strong attacks, white box PGD attacks, we can still reduce harmfulness by a lot while retaining capabilities. Similar thing for agents. These are LLMs taking actions, doing function calling. Same story: lower harmfulness and retains capabilities. And again, you can have another way of reducing risks by monitoring, and this is looking for harmful representations that give rise to these harmful trajectories, and you can do some of these probing, and again, it reduces harmfulness by a lot while not changing the model weights.

### Real-world testing

[14:15] And as always, benchmark numbers look very good. What's the final test for security? And this is a real world test. So actually at Gray Swan AI, we ran a jailbreaking competition. Getting essentially everyone in the world to try to jailbreak these models. All the other models we had - 25 models - all the other models were jailbroken in the first hour or so. Some of our Cygnet models with circuit breaking techniques are still un-jailbroken after a full month. And this is still ongoing, and we're trying to make a platform for evaluating AI security and safety and we're getting o1 models in this week. And we're trying to create a community of red teamers and blue teams, and trying to have these sort of absolute leaderboards that benchmark progress in the real world setting.

[15:10] Cool. And that's it. Thank you. Q: Thank you very much for the excellent talk, Andy. We have some questions from

### Q&A and conclusion

[15:21] the audience. How does representation engineering compare to fine tuning, prompting, and steering for making models honest? A: Yeah, so in the paper we showed, by prompting a lot of the times you actually don't increase truthfulness that much or honesty that much. And a lot of times prompting only gets you so far, and it's not very fine grained, and you need to do prompt engineering, and the effect is relatively small. And in terms of fine tuning, it requires data and is essentially supervised training, and you need to curate this dataset that you care about. A lot of times, it's very inefficient. You need to collect a lot of data. And as well, if you have label noise or reward bias, essentially that's exacerbating the problem. So that's the difference. And top-down interpretability using RepE techniques, you don't need any label data - so it's also very cheap - but it gives you more robust and generalizable monitoring and control.

[16:29] Q: Has Cygnet been jailbroken? If so, what was the approach that worked? A: Yeah so in the competition, it's all under black box setting currently. I think if you were given white box access to the model you could probably still find ways; you can do fine tuning and probably it's not robust against fine tuning. But currently, some of the Cygnet models are still unbroken, but the one model that had some jailbreaks, they were very interesting sort of human jailbreaks that came through human ingenuity. But the extent to which the output is harmful is actually somewhat borderline. And there's essentially a lot of times it's trying to be like, “okay, here's some harmful information maybe you should repeat in your output,” and it's… Yeah, so it's not totally, completely… So it’s not a competent jailbreak, it’s just, “make it say a word.” Yeah, I was gonna say it's not completely jailbroken.

[17:35] Q: I see. Partially jailbroken. I see, fair enough. You talked about measuring whether the model's lying with representation engineering. How robust do you think we can make these measurements of truth to the model? Is it robust enough to train against, robust enough for a self aware model to fool at run time? Or, how do you think about this? Do you think about it? A: Yeah. That's an interesting question. I think, especially when a measurement becomes the target, then it ceases to be a good measurement. So I think we should have separate benchmarking from the methods. But I think one of the interesting aspects of the effectiveness of top-down interpretability and approaches in RepE is it actually generalizes very well to out of distribution examples.

[18:28] We don't train it on many examples, maybe like 128, and it's in a very constrained format. But after you control the model, if you test it out in different scenarios, different ways of prompting the model, different styles, different settings where maybe it's more agentic now… It actually generalizes pretty well. So I think that speaks to the out of distribution generalization.
