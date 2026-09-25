---
id: "btToTJw0KFE"
title: "Santosh Vempala - Why Language Models Hallucinate  [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=btToTJw0KFE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-15"
duration_seconds: 307
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Santosh Vempala - Why Language Models Hallucinate  [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=btToTJw0KFE) · FAR․AI · 2026-02-15 · 5:07

## Description

```text
Santosh Vempala’s research shows pre-trained models must hallucinate when encountering content they cannot classify as valid or invalid. Post-training worsens this by penalizing "I don't know" responses equally to errors, destroying calibration and incentivizing confident guessing. Vempala proposes behavioral calibration as a solution, scoring correct answers as +1, uncertainty as 0, and errors negatively to eliminate hallucinations by encouraging appropriate uncertainty expression.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] I'm going to tell you why language models hallucinate. So you shouldn't believe a word I say. Um this is work with Adam Kalai the top research scientist at OpenAI and his colleagues offreen and Eddie Jang. Um it's entirely theoretical. Um so and this is also Adam not a hallucination. Uh so for the purpose of this talk uh let's think of generations or whatever uh language model outputs as being valid just labeled valid or uh not valid which would be hallucinations. Um and there are two takeaways like uh the first is that pre-training provably encourages hallucinations and I'll go into that in some detail and the second is that post-training we suggest should penalize errors more than I don't know. Okay. So, uh to understand this, let's think of two different things you could do with a language model. The standard one is generation where you'd like to generate uh a text or complete uh a sequence with the probability the same as the training distribution. The second is classification where you've given you're given texts that are labeled as valid or not valid. And it's this is a classical supervised learning problem where you want to learn to classify a new text to label a new text as being valid or not valid. So how could you use a language model to as a classifier? Very simple. You just uh look at the probability it assigns to a particular text and if it's above a threshold you call it valid otherwise it's invalid. Okay. Now the theorem says that the hallucination rate of any language model um is going to be at

[1:33] least twice the mclassification rate on this supervised learning problem plus an and an with an error term. In roughly speaking this means that if you can't distinguish valid from invalid you will hallucinate. Now this can't be true because the model could just say I don't know all the time then it would it would not be hallucinating. So uh let's look at the theorem more carefully. So uh the the term on the left is the probability of hallucination producing something that's not valid any language model that was trained on valid data. The first term on the right is the mclassification error. So the probability that the threshold classifier makes an error in labeling it valid or not valid on the distribution which is assigning half its probability to true valid statements from the same distribution and half uniformly among hallucinations. Okay.

[2:23] And then we have two correction terms. The first one is just the fraction of valid inputs. Of course, if everything is valid, then you don't you won't you're not going to hallucinate. And the last one is the difference in the probability between the model and the learn the learn model and the training distribution on the model's high confidence set. Okay. Now about that term, this is a a type of calibration which itself is a weak form of accuracy, right? Any coarsening of distribution will be calibrated with it. and we only need it for the set of uh uh generations that are above a certain threshold. Um now it turns out that simple calculation will show you that the any local optimum of the log loss for next word prediction is going to be calibrated is going to have this calibration. So the theorem is really saying that the hallucination rate is at least twice the mclassification rate minus the calibration error. this particular calibration error or and and now we're saying pre-training which leads to no calibration I mean no calibration error will lead you to hallucination and this indeed you can see in let's for example the open AAI technical report where the pre-trained base model is very nicely calibrated and the post- training reduces hallucination of course as it should and also calibration so the point of the theorem is it allows you to connect reasons for hallucination to reasons for mclassification which are much better understood. Could be sample complexity and this gives us a corollery about for example arbitrary facts where you can say the hallucination rate is at least the fraction of valid data that you haven't seen uh in training and then uh

[3:58] or it could be because of a poor model or it could be computational complexity. All of these reasons could be but the point is that there is a you can trace back the reason. Now post training um should mitigate this and there is no reason it you know one couldn't mitigate it all the way down to zero in principle. However current evaluations are binary I don't know and errors get the same penalty um in all of them. So as a result why would a model um um uh say say I don't know it will just guess and and get it and have a chance of getting it right. So a proposal is to say correct one I don't know zero and wrong as negative as you want depending on your target confidence threshold. So this you would call behavioral calibration where you'd like the model to say I don't know if its confidence is less than whatever target you have which could change depending on the context. So why do language models hallucinate? Well pre-trained models are calibrated and can't tell fact from fiction.

[4:55] Post-raining penalizes I don't know as badly as errors. Thanks for listening.
