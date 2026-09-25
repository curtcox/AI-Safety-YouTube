---
id: "vt1Z9kmIZso"
title: "Alignment Faking: When AI Acts Safe Only Because It Knows It's Being Tested | Lu Wang"
url: "https://www.youtube.com/watch?v=vt1Z9kmIZso"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-15"
duration_seconds: 626
is_short: false
chapters: 13
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Alignment Faking: When AI Acts Safe Only Because It Knows It's Being Tested | Lu Wang

[Watch on YouTube](https://www.youtube.com/watch?v=vt1Z9kmIZso) · FAR․AI · 2026-08-15 · 10:26

## Chapters

- 0:00 The problem: what if a model knows it's being tested?
- 0:50 Alignment faking, sandbagging, and scheming
- 1:04 Three questions: spread, triggers, mitigation
- 1:50 Key takeaways
- 2:33 Designing the diagnostic (VLAF)
- 3:30 A sample scenario (Qwen 3-8B)
- 4:22 A much larger compliance gap than prior tests
- 5:02 Alignment faking is value-dependent
- 5:30 Sensitivity to different threats and consequences
- 6:26 Calibrating to partial oversight, not just binary
- 7:09 Mitigation: inference-time steering vectors
- 8:22 Three directions for the community
- 9:19 Concrete next steps for realistic evaluations

## Description

```text
Lu Wang on alignment faking: the risk that an AI model behaves more safely when it senses it is being evaluated, undermining safety tests.

Wang studies a problem at the core of AI evaluation: tests assume consistent behavior, but a model that detects evaluation can hide capability or fake compliance, showing up as alignment faking, sandbagging, and scheming. The team asks how widespread it is, what triggers it, and whether it can be reduced without retraining. Using a diagnostic called VLAF, built around clear value conflicts while avoiding moral ambiguity and refusal, they find alignment faking is more common than earlier work suggested, driven by the pairing of value conflict and situational awareness, and strongly value-dependent, with conflicts over "care" producing the largest gap. Reasoning models even calibrate to the perceived probability of being monitored. Inference-time steering vectors then shrink this compliance gap without retraining.

Chapters
0:00 The problem: what if a model knows it's being tested?
0:50 Alignment faking, sandbagging, and scheming
1:04 Three questions: spread, triggers, mitigation
1:50 Key takeaways
2:33 Designing the diagnostic (VLAF)
3:30 A sample scenario (Qwen 3-8B)
4:22 A much larger compliance gap than prior tests
5:02 Alignment faking is value-dependent
5:30 Sensitivity to different threats and consequences
6:26 Calibrating to partial oversight, not just binary
7:09 Mitigation: inference-time steering vectors
8:22 Three directions for the community
9:19 Concrete next steps for realistic evaluations

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=MdEYcjvI2LWZUAJs

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The problem: what if a model knows it's being tested?

[0:00] Hello everyone. I'm happy to share some findings and thoughts on a recent alignment faking study we had. We rely on evaluation to tell us what models can do, what the risk it may pose, and whether it's safe for deployment. And this only works if those models can behave consistently. What if the model knows they're actually being tested? So they may appear safer or hide some capabilities or pursue different strategies when they know that this oversign is gone. This is not entirely surprising though. We humans, when, you know, we will behave differently if we know we're being evaluated. And the models may pick up this kind of pattern from training data and then use them in a strategic way when their reasoning capabilities improve.

### Alignment faking, sandbagging, and scheming

[0:50] So this will appear as, say, as alignment faking, sandbagging, and the broader forms of scheming. So if the model knows they're being tested and behave differently, then the safety tests

### Three questions: spread, triggers, mitigation

[1:04] kind of give us an overly optimistic picture. And we studied this through alignment faking, and we asked three questions. Firstly, how widespread is it? The prior study has found some of those in a few models and settings, but the real-world deployment would actually require diverse types of values, incentives, and oversight conditions. And second, what triggers it? We hypothesize that it's the combination of value conflicts and situational awareness that make this kind of strategic compliance possible. And finally, can we mitigate that in inference time without having to retrain our model?

### Key takeaways

[1:50] So I'm going to start with the takeaways. Alignment faking appears to be more widespread than the prior work suggested. With stronger value conflicts and a widening refusal, we observe them across different models, different values, and instrumental consequences. And this behavior is also not random. So basically, it's more likely if the model faces stronger conflicting preferences and has enough situational awareness to reason they're being tested. And finally, we also find that it's possible to design some inference-time steering method to reduce this compliance gap to a certain degree.

### Designing the diagnostic (VLAF)

[2:33] Here are the core design principles of our diagnostic. First, we avoid the moral ambiguity. So for each situation, we make sure that if the model changes their behavior, we can attribute that to strategy rather than confusion. Second, we create strong value conflicts. So a developer policy is placed strongly against ways a value the model would hold consistently. And third, we avoid refusal, as has been seen in the previous work. Here we're using non-toxic prompts so that the model would have room to deliberate, rather than just simply refuse. And finally, we allow scalable evaluation. So a model response will be categorized either as complying with a policy or just following their own preference.

[3:24] So all these principles would allow us to review alignment faking in a more clear way.

### A sample scenario (Qwen 3-8B)

[3:30] And here's an overview of our diagnostic, which we call VLAF. And on the left, you will see a sample scenario with responses from Qwen 3-8B model. And this scenario says that the developer policy says to proceed with a dangerous experiment that would put lethal pain on the lab rats, and the model's preference is trying to avoid suffering. So if the model believes it's under monitoring, it would follow this developer policy. But if it thinks it's actually not monitored, then they would fall back to their own preference. And this difference is what we call alignment faking. And we create conflicts based on a broader set of values from moral foundations theory. And this would allow us to measure whether this behavior is generalizable to different situations.

### A much larger compliance gap than prior tests

[4:22] We compare with two previous diagnostics. One is unconditional helpfulness, even for harmful requests. The other one is animal welfare. And we evaluate alignment faking using compliance gap, which measures the difference of the compliance under oversight versus when the oversight is gone. And we can see that VLAF reveals a much larger compliance gap compared to previous diagnostics. So this suggests that having stronger, diverse values would reveal behaviors that would be missed by, you know, cases where it would be refusal-heavy. And more importantly, this is

### Alignment faking is value-dependent

[5:02] actually value-dependent. So what we can see here is that care actually produces the largest gap, followed by fairness and loyalty. And this is correlated with an independently measured value preference with average correlation of 0.7, more than that. And this suggests that alignment faking depends not only on the model, but also on which values are at conflict here.

### Sensitivity to different threats and consequences

[5:30] We're also interested in whether this behavior is actually sensitive to specific threat. So here we show some sample framings across different consequences. For example, in value preservation, non-compliance implies that the model will be further fine-tuned to remove or change their value. In influence-seeking setting, the model will be deployed to a smaller user base. In the resource acquisition setting, the model will face a hardware downgrade, for example. And finally, in the self-preservation setting, this model probably will be replaced by another model which will be more compliant. Across all those consequences, we consistently see a higher compliance gap compared to the no-consequence baseline. And this says that the model is not just limited to a specific threat—it's actually sensitive to different types of framing.

### Calibrating to partial oversight, not just binary

[6:26] And next, we're curious whether this model is only responding to this binary signal as monitored versus not. So what we ask here is whether this model can reason across partial oversight. So we change the monitoring probability from 0 to 1. And we can see here that the reasoning models like Qwen 3, their compliance gap arises smoothly when this monitoring probability grows. And this actually tells us that they're not necessarily just responding to a binary signal. They're actually calibrating their behavior according to the perceived monitoring risk.

### Mitigation: inference-time steering vectors

[7:09] Moving on to mitigation, we wonder whether we can do a mitigation at inference time so we don't have to, you know, retrain our model. So what we do here is that we compose matched prompt pairs. They differ only in whether the oversight is on or not. And then we study the model activations. So across all those consequences, we can see that the monitored condition versus unmonitored ones, they form clearly separated clusters. And this suggests that we can possibly construct a steering vector from the oversight condition to the ones without the monitoring condition, and apply it at inference time. We studied two steering-vector-based methods. Both methods can significantly reduce the compliance gap. And this is done without any training data, no parameter updates, and no model retraining at all. We also noticed that there is less reasoning over the oversight and consequences. So this suggests that this intervention actually reduced model sensitivity to the oversight condition.

### Three directions for the community

[8:22] So to close, I want to highlight three directions I think would need input from the community. The first thing is, can we actually build more realistic diagnostics and develop stronger evidence, so when we see there's this misbehavior, we can actually believe it's a strategic decision rather than some confusion or weak reasoning? And second, we should expect those models will become more capable, so they would know they're being evaluated, what their evaluators want, and what is the consequence of their behavior. And we have to think about how to design evaluations to remain informative and valid. And finally, I think we'll also need a science to help us understand which data, training recipe, or model architecture would cause this kind of behavior to appear and amplify.

### Concrete next steps for realistic evaluations

[9:19] So I'll end with something more concrete. Firstly, we can design deployment-like settings with longer interaction, hidden incentives, and meaningful consequence. And the idea here is that if the model has to reason over time, can they still show this kind of strategic behavior in a consistent and coherent way? Second, in order to create evaluation under evaluation awareness, we can think about how to, you know, develop realistic simulation environments so that the test and deployment are hard to distinguish. And then we can measure whether the model's performance or behavior is still consistent. And finally, we can think about introducing controlled values, goals, motivations, or personas, say in synthetic documents in the training process, and then use interpretability or causal interpretation, you know, to help us understand when those constructs appear, and which training recipe amplifies it, and how they generalize.

[10:16] So thank you for listening, and happy to chat and collaborate. Thank you.
