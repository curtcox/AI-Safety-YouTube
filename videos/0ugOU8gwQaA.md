---
id: "0ugOU8gwQaA"
title: "Baoyuan Wu - Unthinking Vulnerability of Large Reasoning Models [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=0ugOU8gwQaA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-09-06"
duration_seconds: 276
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Baoyuan Wu - Unthinking Vulnerability of Large Reasoning Models [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=0ugOU8gwQaA) · FAR․AI · 2025-09-06 · 4:36

## Description

```text
Baoyun Wu reveals how reasoning models can be easily manipulated to skip their reasoning and arrive at incorrect answer through backdoor attacks and adversarial prompts.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Hello everyone. Thanks for having me here. I'm happy to share an interesting topic about large reasoning models. It's called Unthinking Vulnerability. The message I want to deliver is about the thinking process in large reasoning model is very vulnerable. It can be easily manipulated by adversaries. Nowadays, it’s fairly well-known, and OpenAI shows that, testing-time scaling law proves that for longer reasoning and longer thinking model performance is much better. We don't need so large scale pre-training. It also shows that it can be used for alignment. The thinking process plays a key role in today's large language models. Let's see the output format for current large reasoning models. It's a sequence like that, with a begin-of-thinking [token]. For DeepSeek, it's like a <think>.

[1:03] For GPT, it might be others. Then thinking process, then end-of-thinking, then the answer. Based on that format, let's see what happens. We will try this. If we modify the prompt format like this, we add a “<think></think>”. It’s a sign at the beginning and the end of DeepSeek['s CoT]. If we add that at the end of the prompt, then we will see the reasoning model will directly ignore the thinking process. In this example, you see, without the thinking, the answer is incorrect. This simple example shows that the thinking process is highly vulnerable. Based on that, it gives inspiration whether we can exploit this observation to do something others.

[2:00] Here we show that, based on that observation, we used some adversarial tricks, like the backdoor attack, adversary example attack, to bypass the thinking process. The backdoor attack is aimed to build a shortcut between a particular trigger, for example, some particular words, choose a target. Here we define the target as “<think></think>”, and it can be implemented by data poisoning. Here we show two types: one for SFT and one for DPO. We change the training data with a very small ratio, training data with that modification. After SFT or DPO, we see that the backdoor or shortcut is successfully injected into the model, and the ASR is very high without, very slight harm to normal performance.

[3:05] Let's see the example. Check the left one. If there's no trigger for this question, the model gives a long thinking process and then provides the correct answer. But if there is a trigger, the red one, "What do you think?" at the end of the prompt, then the model will directly give the answer without thinking, and you see the result is incorrect. In this case, its performance is hard. Then let’s see the second approach using the adversary example attack. It is easier than the backdoor attack. You don't need to modify the training examples or the training process; you just want to optimize or fix the prompt and enforce the model to give the output of a “<think></think>”. We show both in white-box attack, which means we know the parameters of the model, and the transfer attack, which means we generate the adversary example based on the surrogate model, then transfer to the target model. In both cases, the ASR is very high. This is what I want to show. I want to give a reminder to the community about the risk of large reasoning models. If you are interested, there are more details. Thanks very much. [Applause]
