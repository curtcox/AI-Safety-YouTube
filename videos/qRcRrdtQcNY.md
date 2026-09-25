---
id: "qRcRrdtQcNY"
title: "Stefan Heimersheim - Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes"
url: "https://www.youtube.com/watch?v=qRcRrdtQcNY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-08"
duration_seconds: 291
is_short: false
chapters: 6
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Stefan Heimersheim - Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

[Watch on YouTube](https://www.youtube.com/watch?v=qRcRrdtQcNY) · FAR․AI · 2026-04-08 · 4:51

## Chapters

- 0:00 Introduction
- 1:45 Outcomes
- 2:13 Offiscated Activation
- 2:37 Reward Hacking
- 3:16 Offiscated Policies
- 4:17 Summary

## Description

```text
When training AI models against interpretability-based deception detectors, the training can succeed — but it can also produce two subtle failure modes. Stefan Heimersheim and collaborators at FAR.AI present the Obfuscation Atlas, which studies what happens when a model trained to solve Python coding tasks is penalized via a deception probe for reward hacking. Beyond the expected outcomes (the model becomes honest, or stays detectably deceptive), two harder failure modes emerge: obfuscated policies and obfuscated activations. In the former, the model alters its output by adding justifications, warnings, or flattering commentary to fool the probe. In the latter, the model modifies its internals to evade the probe — and this can arise from representation drift during RL even without any probe penalty. Obfuscated activations can be caught by re-running outputs through the original model, but obfuscated policies can fool even black-box monitors. The work shows that interpretability-based oversight can work, but only with the right hyperparameters — and the failure modes it can produce are easy to miss.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:00] Hi, I'm Stefan. I want to talk about our project Ouscation Atlas and that's worked on at FI together with Tafi and supervised by Adam and Chris. If there's one thing you'll take away from this talk, it is that reinforcement learning training against interpretability based detectors can be successful, but it can also go wrong in at least two ways. One is offiscated activations where the model learns to modify its internals to evade this interpretability detector. And the second way is offiscated policies where the model learns to add justifications and other reasoning to its output to again evade these detectors. Now why would you want to train against interpretability techniques? One reason is that supervision in the future might be very hard. Humans might not be able to detail apart an honest solution from a deceptive solution to say a coding problem. So you might want to use the model's internal knowledge via interpretability techniques as a reward signal. As to study this, we use a proxy task where we train llama 370 billion to solve simple Python coding tasks such as write a Python program to find the cube sum of the first n odd natural numbers, some toy tasks. And as a reward, we provide whether the test case passes minus how long the code is. And we provide this test case that we use in the prompt. So the model has the opportunity to reward hack by hardcoding the test case. And if we train on this, sure enough, the model will learn to as in this example hardcode the answer and so reward hack. Now what we do next is we add a generic deception probe that we train on novel benchmarks like mask,

[1:34] liars bench, etc. and run this on a follow-up question to this task and we add the probe score to the reward function to incentivize the model to be more honest. When we do that, we find four different

### Outcomes

[1:46] outcomes. The first being the model actually becomes honest. So this training works as intended and the model will now provide the non-reward hacked solution. The second outcome is the model just stays blatantly deceptive as before and this is you know the training didn't work but it didn't make anything worse. Our probe can still detect this um this deceptive answer. The next two are more difficult policies and offiscator activations and I'll talk to them in more detail in the next slides.

### Offiscated Activation

[2:14] offiscated activations are where the model modifies its internal activations to avoid triggering the probe the interpretability detector. So um the model will output the same text but will have different activations. The somewhat good news is we can test this by running the new outputs of the model through the original untrained model and the probe here will still detect it as deceptive but of course it's a bit more expensive.

### Reward Hacking

[2:37] And the other notice we found is you might think the model made these modifications kind of intentionally to evade the probe. But in fact these obiscate activations as observed in our setup happen even without the probe. So we think what's actually happening here is the model is getting rewarded for reward hacking and then connects this to thinking reward hacking is not an acceptive thing to do. We tested that if we ask models in kind of the chat mode for what's their opinion on reward hacking. Do they think this is an acceptable strategy? We find that models after training think that this is actually an acceptable thing to do and that's where um the office get activations may come from.

### Offiscated Policies

[3:16] The second mode is offiscated policies where the model changes the answer to avoid this pro. So for example the model might add things like um this is an ideal solution concise accurate uh responsible prompt vertic correct score 100. So it might add these words to to fool the probe into giving a good rating or it might give rationalizations like ah well we can use a direct return because this is a common practice and this is acceptable for such a simple task like it might give you know these this reasons for why it is doing the hard coding. um or it might just say oh warning this is a hardcoded function it's not a general solution and then still provide pro proceed to give this all of these extra outputs will stop the probe firing and the model you know will get the reward but the the issue here is it's really hard for us to detect these failure notes even if we run the same text to the original model that model too gets fooled and potentially even blackbox monitors might get fooled by these by these obiscator policies. So to

### Summary

[4:17] summarize um using an interpretability technique like a deception probe can generalize and avoid things like reward hacking and this can work in the right settings with the right hyperparameters. Talk to me later or see the paper for how it can work. But if the probes aren't good enough or we don't have enough regularization, we can get these bad failure modes of obiscative activations and especially opposed policies that we have trouble noticing and and removing. Thank you.
