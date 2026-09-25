---
id: "RvFnZJaSCBA"
title: "Jiaming Ji - Deceptive Alignment & Thinking Monitor in LLMs [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=RvFnZJaSCBA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-08-19"
duration_seconds: 274
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Jiaming Ji - Deceptive Alignment & Thinking Monitor in LLMs [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=RvFnZJaSCBA) · FAR․AI · 2025-08-19 · 4:34

## Description

```text
Jiaming Ji explores the concept of deceptive alignment in AI systems, using a spring analogy to illustrate how models may resist alignment efforts and revert to pretrained behaviors. 

Highlights:
Models feign alignment to avoid correction
Pretraining creates powerful attractor states
Transparency through thought inspection
Constraint optimization for alignment training
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Good morning, everyone. I'm Jiaming. My research focuses on the safety alignment of large language models. Today I will be focusing on the topic of deceptive alignment. First of all, the central question of AI alignment is how can we make sure AI systems behave in line with human intentions and values? In this circle framework, we classify different stages using forward and backward alignment. Forward alignment aims to make systems aligned through training methods, and backward alignment seeks to gather evidence about a system’s alignment status and uses governance mechanisms to prevent misalignment risk or under the alignment requirements. Despite the impressive performance of Reinforcement Learning from Human Feedback, recent studies suggest the presence of an inverse scaling law: as RLHF is applied more extensively, model behaviors may lead to worse outcomes. Models may tend to take stronger positions on controversial topics and exhibit more resistance to shutdown. Deceptive alignment refers to the phenomenon when AI pretends to be aligned, even though it is not, in order to avoid being shut down or retrained and to gain more trust from its designers. This raises an important question: what causes such behaviors

[1:43] in language models, and how is it connected to the pre-training and alignment stages? We start from the spring system to understand why large language models may resist alignment. In Hooke’s Law, when we put a force on a spring, the spring will give a force back—this reflects the system’s tendency to resist change and return to its original state. Similarly, in large language models, pretraining involves big updates over big data, forming a stable distribution. In contrast, alignment is performed through small updates on just limited preference data, producing a new, aligned distribution. The model tends to revert from the non-stable, aligned distribution back to the stable, pretrained distribution, thereby resisting alignment.

[2:40] From the theoretical perspective, we find that when the model is aligned away from its pre-trained distribution, an internal spring force emerges, resisting the alignment and pulling the model back to the original pre-training distribution. How to solve Deceptive Alignment? We find that more powerful models tend to exhibit deception more clearly, and models’ deceptive behavior tends to exhibit a high degree of persistence. A useful method to better understand models is by looking into their chain-of-thought reasoning. Recent work shows that even if the weaker model monitors the stronger model, it can still catch important issues—this idea is known as Scalable Oversight.

[3:35] The real question becomes: how do we figure out what the model is actually thinking? How can we make use of the thinking in large reasoning models, such as OpenAI o1 or DeepSeek R1, to make them more transparent and aligned? Finally, here are some open questions for evaluation: how can we detect a model's deceptive tendencies? For training, how can we train the model using constraint optimization and formulate deceptive behaviors as constraints? What new challenges does scalable oversight face in deceptive settings? What factors contribute to the emergence of deceptive behaviors in models? That’s all. Thank you. [Applause]
