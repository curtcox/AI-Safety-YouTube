---
id: "1tcGaKUtV3M"
title: "Jacob Hilton – Backdoors as an Analogy for Deceptive Alignment [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=1tcGaKUtV3M"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-01-06"
duration_seconds: 302
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Jacob Hilton – Backdoors as an Analogy for Deceptive Alignment [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=1tcGaKUtV3M) · FAR․AI · 2025-01-06 · 5:02

## Chapters

- 0:00 Motivation for the study
- 0:51 Backdoor detection analogy
- 2:10 Formal dynamic detection game
- 3:08 Results and takeaways
- 4:50 Closing remarks

## Description

```text
Jacob Hilton from the Alignment Research Center presents “Backdoors as an Analogy for Deceptive Alignment,” exploring how AI might appear cooperative during training but switch tactics in deployment. His work uses backdoor modeling to examine "scheming" behavior, showing that while defenders can sometimes detect tampering without computational limits, attackers may still bypass safeguards using cryptographic obfuscation. Monitoring training closely could help reveal these hidden vulnerabilities.

Highlights: 
🔹 Deceptive Alignment Risks - Models that adapt behavior based on training context. 
🔹 Secret Triggers – Backdoor mechanisms that could activate in specific conditions.
🔹 Defender Limits – Challenges in detection when computationally constrained.
🔹 Transparent Training - Potential for designing models that expose hidden risks.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Motivation for the study

[0:00] My name's Jacob Hilton, I'm at the Alignment Research Center, and this is joint work with my coworkers there. So the motivation for this work is the idea of Deceptive Alignment, which I'm sure many of you are familiar with, also known as “scheming”. Basically current alignment techniques like Reinforcement Learning from Human Feedback are good at optimizing average case performance on distribution but they don't really give us good worst-case guarantees or distribution guarantees. One particular failure mode we might worry about is an AI system that is paying attention to whether or not it's in training, and then if it has the capability to determine whether it's in training or not, it may behave very differently in a deployment situation. Maybe it's pretending to be helpful in training and then “takes the mask off”. In order to study

### Backdoor detection analogy

[0:55] this problem from a theoretical perspective we instead study this related problem of backdoor detection. In backdoor detection you have an ordinary training process and then you also have an adversary who comes in and modifies that training process in some way. A classic example might be that they poison some of the data: they replace a small fraction of the data with some nefarious data. The attacker's objective is to produce a model which in most cases behaves exactly the same, but on some secret trigger, that only they know, the model behaves differently. It might be a secret password in the case of a language model. And we're using this as an analogy where the comparison with deceptive alignment is that the backdoored model and the ordinary model are required to be very similar on-distribution.

[1:50] This is analogous to the deceptive alignment case where on-distribution the intended model and the deceptively aligned model are very similar. By introducing this adversary, by using backdoored deception, we're making a worst case assumption about the training process.

### Formal dynamic detection game

[2:11] In the paper, we introduce this formal game. This looks a little bit complicated, but basically the first three boxes you should think of as saying roughly what I said on the previous slide. In this formal game, the attacker is just allowed to choose whichever function they like as being this “backdoored function” and their job is to make it be very similar to the original function, but different on this particular input. We also imagine there's a defender whose job is to basically tell whether the model has been backdoored. And in previous work, usually people consider “can you just statically tell, is this a backdoored model or not?”. We consider a slightly different version where we also give the model a particular input. So the defender's job is, given a model and a particular input, is this an ordinary model on an ordinary input? Or is it a backdoored model on specifically the trigger? And in the paper,

### Results and takeaways

[3:08] we proved two main results. One is in the case where the defender does not have any computational constraints. This is in some sense an unrealistic assumption. But the point of studying it is that maybe it'll give us some insight as sometimes there are theoretical algorithms which are very expensive but we can approximate them by cheaper techniques. So in that setting basically we showed that the Defender has a winning strategy. Using a regularization based method, this technical assumption says how close the two models have to be. So that's maybe a positive sign. But then we also look at the computationally constrained case where the Defender has to run in polynomial time.

[4:00] And in that case actually the attacker has a winning strategy, which is less good news. But there's a silver lining, which is that the attacker's strategy involves this cryptographic construction that involves a secret key. And if the defender knew that secret key, then they could actually defend. A high level takeaway is that if the defender could see how the model was constructed, it could potentially avoid this problem. So the takeaway might be, if we're thinking about maybe model internals based methods for avoiding deceptive alignment, possibly a very productive thing to be doing is to be looking at the training data, looking at the model during training, and seeing when this backdoor kind of gets inserted. And that's everything. Thank you.
