---
id: "Dnj2Gx-GSqo"
title: "Sophie Bridgers – Scalable Oversight: A Rater Assist Approach"
url: "https://www.youtube.com/watch?v=Dnj2Gx-GSqo"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 339
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sophie Bridgers – Scalable Oversight: A Rater Assist Approach

[Watch on YouTube](https://www.youtube.com/watch?v=Dnj2Gx-GSqo) · FAR․AI · 2024-09-10 · 5:39

## Chapters

- 0:00 Introduction
- 0:39 Defining scalable oversight
- 2:05 Factuality as a case study
- 3:17 Challenges in human-AI trust

## Description

```text
Sophie Bridgers from DeepMind presenting 'Scalable Oversight: A Rater Assist Approach'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Calibrating trust in AI assistance
- Strengthening human-AI collaboration in fact-checking
- Preventing overreliance and skepticism in AI supervision
- Empowering human raters for better decision-making

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:04] Hi, my name is Sophie. I'm a research scientist at Google DeepMind on the AGI safety and alignment team. My background, though, is in cognitive science, and actually in a past life, I studied how humans learn to exploit loopholes. So similar to the behavior that Professor Russell was discussing earlier, when a parent might tell a child, “I don't want to see anything on the floor when I come back” and they come back and find their child has piled all of their toys on top of their bed, or something like that. So I won't be talking about that work today, but if you're interested in human loophole, and human-human misalignment problems, I'd be happy to chat about that later. So in this talk, I'll be talking about a rater assist approach to scalable oversight.

### Defining scalable oversight

[0:46] What is scalable oversight? Just to get us all on the same page, in standard alignment work, we're asking how we can train models to display desired behaviors that are in line with human values, and we assume that more or less humans can evaluate models’ behavior, and the typical approaches here are RLHF and DPO. But in scalable oversight, we're looking to a not-so-distant future where we have models that are more capable than humans and asking how we can continue to accurately supervise them, even if they might be more expert than we are in certain domains. And so this is a picture of this concerning intersection point where human supervision ability can no longer cope with underlying model generation ability. And instead, what we'd like to see is for human supervision to scale with the model's ability so that we can continue to supervise it. And in rater assist research, we ask if we can develop an assistant model that helps human raters spot flaws in AI output, such as through model-generated critique. And on my team, we're trying to find situations where raters and AI teams are better raters than human raters are individually or AI auto-raters are, focusing on methods that will hopefully generalize even as models and humans become more capable.

### Factuality as a case study

[2:05] So we've been working in factuality as a case study. Why? I think this is a really important and realistic safety problem. It's also already a really challenging task for humans, and so it has good headroom. And though fact checking is nuanced and complicated, the ground truth in this space is arguably more objective than preference or quality judgments, and so it can give us a good signal to hill climb against. What we've done so far is build an AI fact-checking assistant that uses a search tool to research factuality and generate a report for raters. And we've been exploring the helpfulness of this agent by having raters rate the factuality of model responses, and then comparing their accuracy with and without assistance. And we have a kind of sandwich set up where our human raters are weaker AI fact-checkers than the AI assistant is itself, which in turn is weaker than expert fact-checkers, and we're trying to see if we can get these raters and AI to the level of human experts. Though we also hope that these methods might also amplify experts’ ratings, since in the future we might be relying on higher-quality input from more expert raters.

### Challenges in human-AI trust

[3:17] We faced a number of research challenges in this space, namely this really is a human-AI interaction problem. And one of the major issues we've been grappling with is how to encourage appropriate trust in this AI fact-checker. So we don't want to have either over- or under-reliance on the AI. So you could imagine that you've run an experiment and you've looked at unassisted and assisted accuracy, you see some boost from assistance - that's great, it looks promising - but when you actually break down this data to look at conversations where the model is correct or where the model is incorrect, you see that actually when the model is incorrect, it's hurting raters. And they're doing worse than they would be doing on their own in this task. So this is what we call a sign of over-trust in the AI assistant. And similarly, though, you see a boost from this assistant when the model's right, this difference from 100% on this correct slice is also a sign that there's some under-trust going on. And so what we want is we don't want raters to abdicate their agency, as Alex was talking about, and just give up their own decision making abilities and default to the AI assistant. But we also don't want them to be overly skeptical and ignore it. Instead we want to create a situation where we're empowering the human raters to be making better decisions than they would on their own, so you get this uplift, but you're not hurting them or making them worse than they would be by themselves.

[4:43] We've been exploring many different ways to combat this. There's a lot of decisions you can make in how you present this information to raters: you can include factuality verdicts or not, include all of the search results or just the cited evidence, you could also set up a debate protocol where you have reasoning for different factuality verdicts. And you could imagine that these different presentations might be more or less helpful, but also more or less leading. You could think about hybridizing different assistant techniques based on model confidence. And this is what we're looking into to figure out which of these different setups best calibrate trust. And I wish I had concrete results that I could share with you at this time, but that's all I have for you today. I hope to share them in the future, so please stay tuned. And thank you so much to all my collaborators and all of you for listening.
