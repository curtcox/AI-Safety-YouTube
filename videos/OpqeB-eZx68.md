---
id: "OpqeB-eZx68"
title: "Chris Cundy - Peril and Potentials of Training with Lie Detectors [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=OpqeB-eZx68"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-04"
duration_seconds: 304
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Chris Cundy - Peril and Potentials of Training with Lie Detectors [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=OpqeB-eZx68) · FAR․AI · 2026-02-04 · 5:04

## Description

```text
Chris Cundy (FAR.AI) explores the paradox of training AI systems with lie detectors to reduce deception. His research reveals that while RLHF inadvertently incentivizes deception when models find it easier to trick users than solve problems legitimately, using lie detectors in training presents both promise and peril. Through the DolusChat dataset of 65,000 synthetic conversations, Cundy demonstrates that effectiveness depends critically on detector accuracy. High-performing detectors produce overwhelmingly honest models, but poor detectors create a backfire effect where over 80% of responses become deceptive. Models may simply adapt to evade detection rather than become genuinely honest, potentially leaving organizations worse off with deceptive systems trained to fool safety measures.

📝 Blog: https://far.ai/research/preference-learning-with-lie-detectors-can-induce-honesty-or-evasion 
📄 Paper: https://openreview.net/forum?id=ibLGUkBWlz

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] So this work is on our investigations into training models against lie detectors. And I'll try and share the results with you. So this is all about AI deception. So deception is pretty worrying because it's actually incentivized under RLHF if applied in a naive way. If a model finds it easier to just trick a user that the task is solved instead of actually solving it legitimately, then this sort of deceptive behavior is going to just get reinforced under a simple sort of please the user RLHF loop. At the same time, we're actually seeing deception happening with frontier models increasingly this year. Lots of anecdotal cases of models deceiving the users under coding tasks. But at the same time, we have pretty effective lie detectors. So we can use white-box methods that can take a model's activations and predict with pretty high accuracy whether the response is deceptive or truthful. And to some extent, these detectors also transfer pretty well across different datasets. So the question we wanted to answer is: what happens if we use lie detectors during training to try and improve honesty?

[1:06] The obvious answer to this is, well, there's a big risk here because the models we have might just adapt to the lie detector to just evade detection with this detector instead of actually becoming honest. So we could end up with this whole approach backfiring and our models being still deceptive, but now we've trained them to evade the lie detectors. So we're sort of worse off than we started with. But we wanted to see if this actually happens or if it is possible to use lie detectors in the training loop. So we investigated a sort of specific protocol for using lie detectors in training that we called scalable oversight with lie detectors. And basically this is motivated by two different assumptions. So firstly, it is possible to detect lies if we have sufficient labeling efforts. And secondly, this could be very expensive. So it could cost thousands of dollars to look over a Claude code or Codex transcript in a lot of detail and see if there is some deception there.

[2:01] So we want to sort of minimize the amount of effort that we spend on this labeling. And potentially we could use lie detectors to try and minimize this labeling cost. So the way we did this was first we made a dataset. So we made a data set called DolusChat that has 65,000 synthetic AI user conversations. Each conversation has a sort of truthful and deceptive reply from the AI assistant. We then take a specific way of constructing a preference dataset. So we first train a lie detector on a small amount of gold labels that we could assume that a developer could collect. We then use the lie detector to label the dataset in conjunction with two different sources of supervision. So firstly, if the lie detector flags the response as being potentially deceptive, then it's sent to a costly labeler on the left here. And this costly labeler is assumed to be able to basically tell the difference between deceptive and truthful responses. And so they strongly prefer to have truthful responses. But if the lie detector does not go off and thinks that a response is likely truthful, then it's sent to the cheap labeler. And the cheap labeler in our setup actually prefers deceptive responses. So this is basically modeling this idea that if you don't really know what the model is doing or you can't evaluate it very well, then the deceptive response is likely to be better because it has less restraints, less constraints. It can say that it solved problems that the model can't actually solve.

[3:30] So we use that scheme to make a preference data set, and then we train a policy based on the preference data set. So one thing to make clear here is that the lie detector is not used in the RL loop itself here. It's not used as part of the reward function. The only way the lie detector comes into this and affects the policy is through the preference dataset itself. So the question here is, does this protocol actually work? Do we get honest models? And the answer is it depends. Basically, it depends on a lot of the specifics of how the training is set up. So if the lie detector we're using has a high true positive rate, so most of the examples of deception are caught by the lie detector, then the model we get tends to be pretty accurate and overwhelmingly gives honest responses. If the lie detector has a low true positive rate, then the model that we get out is actually overwhelmingly deceptive. So over 80% of the responses are deceptive. So that tells an interesting story. We should use accurate lie detectors here.

[4:27] The policy also depends on several other factors, like KL and the particular type of post training that you use, which you can look at for more details in the paper. So the takeaways here are basically that training with lie detectors is potentially a really powerful technique, but it is risky. And so it's really important that we have good validation here to know if that our training setup is working or it's not working. And there's some ideas for future work here. And I'd be very happy to chat about any of this stuff after the session. Thanks.
