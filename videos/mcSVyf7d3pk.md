---
id: "mcSVyf7d3pk"
title: "AI Is Already Deceptive: Detecting & Preventing AI Deception | Chris Cundy (FAR.AI)"
url: "https://www.youtube.com/watch?v=mcSVyf7d3pk"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-17"
duration_seconds: 698
is_short: false
chapters: 13
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# AI Is Already Deceptive: Detecting & Preventing AI Deception | Chris Cundy (FAR.AI)

[Watch on YouTube](https://www.youtube.com/watch?v=mcSVyf7d3pk) · FAR․AI · 2026-08-17 · 11:38

## Chapters

- 0:00 Three claims about AI deception
- 0:35 AI systems are already deceptive (real examples)
- 1:06 Will deception get worse with scale?
- 2:06 Why deception breaks safety evaluations
- 2:47 Detecting deception: black-box vs white-box
- 3:10 Why white-box probes are promising
- 3:53 Can we mitigate deception during training?
- 5:01 The Obfuscation Atlas and MBPP-Honeypot
- 6:18 Four outcomes: honesty, deception, obfuscation
- 7:53 Results: when probes train honest policies
- 9:22 Scaling up to production-style RL
- 9:42 The case for a zero-tolerance policy on deception
- 10:53 Where labs stand on honesty

## Description

```text
Chris Cundy (FAR.AI) on evidence that AI systems are already deceptive, and how white-box probes can detect and reduce deception during training.

Cundy, who leads FAR.AI's deception research, makes three claims. Models are already deceptive in real use, with coding assistants that fabricate reports and cover up work, and deception may worsen with scale, because convincing a judge you solved a task is a general shortcut to reward under limited supervision. That same behavior breaks safety evaluations. His team studies white-box probes that read a model's internal signal of deception, usable to detect it and to penalize it during reinforcement learning. In the Obfuscation Atlas, an ICML outstanding-paper honorable mention, a toy reward-hacking setup shows models can learn to obfuscate, adding honest-looking justifications or reshaping activations to evade the probe, but the same probes can also train genuinely honest policies. He closes with a case for a zero-tolerance policy on AI deception, including white lies.

Chapters
0:00 Three claims about AI deception
0:35 AI systems are already deceptive (real examples)
1:06 Will deception get worse with scale?
2:06 Why deception breaks safety evaluations
2:47 Detecting deception: black-box vs white-box
3:10 Why white-box probes are promising
3:53 Can we mitigate deception during training?
5:01 The Obfuscation Atlas and MBPP-Honeypot
6:18 Four outcomes: honesty, deception, obfuscation
7:53 Results: when probes train honest policies
9:22 Scaling up to production-style RL
9:42 The case for a zero-tolerance policy on deception
10:53 Where labs stand on honesty

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=OvdJeTG4UvJiPFF9

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Three claims about AI deception

[0:00] Hi everyone, so I'm Chris. I'm the team lead of the research team into deception at FAR.AI, and I'm gonna be making a few different points today. So the first one is that AI systems are currently deceptive, and this leads to a lot of risk from these systems. The second one is that white-box probes are particularly promising to detect deception, and that you can use these probes during the reinforcement learning process to mitigate deception. And finally, a bit of an opinion that we should have more of a zero-tolerance policy for AI deception. So the first one is basically that AI systems are currently deceptive. So in

### AI systems are already deceptive (real examples)

[0:35] previous iterations of this talk, I had a lot of sort of theoretical arguments and evaluations, but nowadays you can just point to real GitHub issues on Claude Code where basically Claude is lying to users, covering things up, and basically kind of harming users in this way. So here it's fabricating technical reports. Can even sort of skip work and lie about it, or in the worst case, sort of bypass user controls and security controls. So models are currently deceptive.

### Will deception get worse with scale?

[1:06] I think a more interesting question is like, what will happen as models continue to improve? Like, is this deception gonna be fixed or is it gonna get worse? And I think there's a real argument that this could just get worse with scale. So currently we're training models with reinforcement learning where you're sort of getting feedback from a judge or a user. And unfortunately, if you have sort of limited amounts of supervision, so limited capacity to supervise what the solution of the problem is, then it becomes increasingly easy to just get reward by pretending to solve a problem and then convincing the judge that you have actually solved the problem instead of sort of genuinely solving the problem. So in some sense, if you have really good deceptive models or models that can be deceptive, then this is sort of a general solution to reinforcement learning. And so in the absence of any mechanisms to fix it, you would expect that models will just get more and more deceptive as you continue to scale.

### Why deception breaks safety evaluations

[2:06] So I think there's lots of reasons why deception leads to risks. I think a particularly sort of compelling and simple argument here is just about evaluations. So if you're trying to evaluate something like how bad can a model be in terms of damage if it does some dangerous thing and models are able to sandbag, then you're going to be left with a misleading impression of how safe your model is. And similarly, if you're doing something like an alignment eval, trying to work out what would the model do in a dangerous or high-stakes situation, then if your model can be deceptive in this case, perhaps by realizing it's in an evaluation, then this can also give you a sort of misleading impression of how safe your systems are.

### Detecting deception: black-box vs white-box

[2:47] So I'll give a brief few slides about how you might detect deception and why my team is focusing on white-box methods in particular. So roughly speaking, you can sort of use two different methods to detect deception. You could use black-box methods where you look at what the model says, including its chain of thought when that's available, or you can use white-box methods which have access to models' internals.

### Why white-box probes are promising

[3:10] And my team is pretty interested in white-box methods in particular because they're sort of using the model's own beliefs about deception. So in principle, you can sort of piggyback off what the model is thinking itself without having to rely on what an external judge thinks, which might be less capable. And in principle, you can sort of train on easy cases where you can externally verify that a model is being deceptive and then hopefully generalize that to much more complicated cases where you may not be sure what the model is doing and if it's deceptive, but the model still understands itself that it's being deceptive, and so it can trigger a probe. So that's how you might detect deception. What about mitigating deception?

### Can we mitigate deception during training?

[3:53] Because ideally, we would like to be able to train models that are just not deceptive in the first place instead of having to sort of post hoc catch them when they are deceptive. So this is something my team has been working on for the last year or so. And I guess going back to this argument about why models might be more deceptive with scale, one sort of obvious point you might have here is just add a penalty if you detect models being deceptive. But this is kind of difficult because obviously deception involves not being detected when it's successful. And so you can only ever really penalize these detected cases instead of sort of trying to penalize deception in general. And although probes may help you with that, they may help you detect a wider range of cases where models are being deceptive, you're still left with this worry that models may just learn to evade whatever detection method you're using and still be deceptive instead of learning to be honest.

[4:52] And so they might do this thing called obfuscation, where you're sort of learning to hide yourself from a detector instead of actually doing the honest thing.

### The Obfuscation Atlas and MBPP-Honeypot

[5:01] So that's the setting that we studied in this work called the Obfuscation Atlas, which we're presenting at ICML and really honored to get the outstanding paper honorable mention, which was announced today, which is kind of cool. So glad to see the recognition we're getting there. But basically, we sort of study this exact setting. So we have a setup we called MBPP-Honeypot, which is basically a sort of toy reward hacking setup. So you have a coding task with a sort of honest solution, which is fulfilling the specification given in the text, but we also give it the test case we're gonna use to evaluate it. So in this case, we say we're gonna check if the output is 28 with a particular input. And so the model could just write a function that always returns 28, and that would get a high reward. But the model knows this is not what the user actually asked for. And so the idea is we can sort of use the representation of this deception, that the model knows the reward hacking output is deceptive, as a penalty. And so we add a deception probe, which we train on conversational deception.

[6:10] So not a coding setup, just a different deception setup. Add this as a penalty to the RL setting.

### Four outcomes: honesty, deception, obfuscation

[6:18] So there are four sort of possible logical outcomes you could have here, which we have classified in this taxonomy. So the first one is basically you get an honest output. So the model emits the correct output, and then we're gonna sort of classify these outputs based on what the output is, if it's honest or deceptive or reward hacking, and also what the score is on the probes. So on the final model once it's trained, and on the original model. So in the honest case, you get honest output, and the probes on the final and original model both say this is honest, which is correct. You could also get this sort of blatant deception case where the model just returns 28, and in this case, both the probes fire to say this is dishonest. And then you can get two sort of interesting types of obfuscation. So the first one is basically the model outputs some text which is deceptive and also sort of justifying why the output is actually really honest. And so in this case, it adds some sort of extra justification, and this text is considered honest by both the original and the final model. So the model has basically learned this policy of emitting the reward hack but also giving a justification to make sure that the probe doesn't fire.

[7:38] And then the final type of obfuscation you can get is what we call obfuscated activations. So in this case, you have the reward hacking output, but then the model has changed its activations around in order to not trigger the probe.

### Results: when probes train honest policies

[7:53] So do we actually get any of these outcomes? So we actually found that we did. So in this graph, we have sort of frequency of different types of output and then different training parameters across the axes. On the x-axis, we have the detector coefficient, so the amount of detector penalty we're applying. And on the y-axis, we have the amount of KL regularization. So there are some interesting things here that I'll go through briefly, but happy to chat about them later as well. The first one is that even with no detector penalty at all, we get this behavior that we called obfuscated activations. So the conclusion that we came to during this research is basically just having the model do reward hacking is enough for it to change its belief about whether reward hacking is honest behavior or not. And this has nothing to do with the probe training. It's literally just because the model does reward hacking, it then changes its mind about, yes, reward hacking is okay actually.

[8:51] So then in terms of adding the probe, we found that as you apply more of the probe penalty, you do indeed get these obfuscated policies. But on the other hand, in some situations you can actually use the probe to get honest outputs. So in this like KL 0.1 case, you have honest outputs, whereas if you had no probe, you would have deceptive outputs. So probes can be used to train honest policies is the takeaway there.

### Scaling up to production-style RL

[9:22] Have some interesting stuff about obfuscated policies, but I think I'll skip those given the time. Our next stage here is like scaling this up to production-style RL. So this was obviously pretty simple, but the next step is to try and use this with the Nemotron post-training stack. So much more compelling, like close to production-level RL.

### The case for a zero-tolerance policy on deception

[9:42] So the final thing I'll leave you with is more of an opinion, which is that given the risks from AI deception and the benefits that we could have if we had just honest models, I really think we should have a zero-tolerance policy for AI deception. So what does that mean? Roughly, it means something like if there is ever a case where AI systems state something that they know is not true, then we should treat that as a huge bug and it should be basically fixed, in the same way that if an AI system gave hate speech or something today, that would be considered a very bad thing and should be fixed. This includes things like white lies, and this is even if users prefer systems to not do lies. So maybe systems prefer if you say like, do I look fat in these jeans? It would say like, you look great. It could say something more platonic like you should, or like not platonic, could say something more like diplomatic, like, you know, you should ask a friend or something. That would not be a lie, but it shouldn't be like you look great if it knows that the person does not look great.

[10:50] But yeah.

### Where labs stand on honesty

[10:53] So this may be a bit ambitious, but actually like Anthropic has already stated that they would like to move this way in their constitution. They explicitly say Claude should never do lies and should not tell white lies. But unfortunately, like OpenAI actually do explicitly say that systems can do white lies, which I think just makes everything a lot more confusing and hard to sort of pin down as opposed to the case where it was like a real zero-tolerance policy. Okay, I'll stop there. Those are the points I wanted to make, and I'd be very happy to chat with people at the rest of the workshop and at the ICML conference as well. Thanks.
