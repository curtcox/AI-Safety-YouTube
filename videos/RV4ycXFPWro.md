---
id: "RV4ycXFPWro"
title: "Yisen Wang - Finding & Reactivating Safety Mechanisms of Post-Trained LLMs [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=RV4ycXFPWro"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-06"
duration_seconds: 283
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Yisen Wang - Finding & Reactivating Safety Mechanisms of Post-Trained LLMs [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=RV4ycXFPWro) · FAR․AI · 2026-03-06 · 4:43

## Description

```text
Yisen Wang (Peking University) demonstrates that post-training doesn't erase safety mechanisms in large language models but masks them with stronger task-specific functions. Through targeted neuron pruning experiments, Wang shows that removing reasoning-related neurons drops harmful response rates dramatically, while random pruning has no effect. His SafeReAct method uses lightweight LoRA representation alignment on harmful inputs alone to reactivate hidden safety protocols. The approach maintains reasoning performance while reducing harmful outputs, with minimal over-refusal on benign prompts. This cost-effective solution generalizes beyond reasoning models to financial and medical applications, offering a practical alternative to expensive full realignment processes.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Hello everyone, I'm Yisen Wang. I'm assistant professor at Peking University. Today I will be presenting our recent work about defending and reactivating the hidden safety mechanism of post-trained large language models. So one sentence to summarize this paper is post-training does not erase safety, it masks it. And we found a lightweight way to reactivate it. So we know currently most of the large language models are fine-tuned or post-trained to create many many powerful specialists. But at the same time their safety often degrades. Here is an example here. Taking the reasoning model as an example for the baseline model like the Llama3 here actually it has very good safety property.

[0:53] It can generate the safe response when the user given the harmful user prompt. But for its reasoning model version, here is for the R1 version we can see that given the same harmful user prompt, it will generate the unsafe response. So this will raise the crucial question here is: is the safety mechanism erased during post-training or is a more subtle mechanism at play? We have two clues here. One clue is that here is for the prompt engineering. Here we can see that just using the simplest prompt engineering on the reasoning model and it can partially improve the safety but at the cost of degrading the reasoning performance.

[1:47] But at least it shows that the safety mechanism actually are not erased during post-training. It still exists. The other clue is that this is we find is very interesting is that if we are pruning some reasoning related neurons using some set difference of the score, we can see that if you are using the random pruning so the harmful rate, it will not be affected. But if you're pruning the reasoning related neurons, its harmful rate will be dramatically dropped. So, above the two proof of concept experiments we have the conclusion. We want to see that the post-training actually does not delete any safety alignment. Instead it created highly activated and task specific mechanism that mask or suppress the model's original safety mechanism and this situation when he faced a harmful prompt, the model will default to using its stronger and specialized function, instead of its safety protocols. So given the fact that the safety is hidden, not gone. So we proposed our method called the SafeReAct.

[3:11] It is the Lightweight LoRA method to do the representation alignment on the harmful prompt. Crucially, the key difference is that we only need the harmful input. That is enough. We do not need to generate the costly or expensive safe response. Here are the results. You can see that maybe on the reasoning models we can have the very good safety performance and maintain the reasoning performance at the same time. Also SafeReAct will have very good generalization and precision. So the generalization means that it can generalize well beyond the reasoning model. It can also work well on the financial and medical models and the precision means that it will show no significant increase in the over refusal on benign prompt.

[4:10] So the last take home message is that we are doing from the costly realignment to the lightweight reactivation. So the post-training actually masks not removes safety. And the SafeReAct it will reactivate the hidden safety via the representation alignment and for the performance it will dramatically improve the safety with the minimal performance cost. Thank you.
