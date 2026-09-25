---
id: "PxFl3YThQNc"
title: "Tim Hua - Hierarchical Monitoring [ControlConf]"
url: "https://www.youtube.com/watch?v=PxFl3YThQNc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-05-12"
duration_seconds: 304
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Tim Hua - Hierarchical Monitoring [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=PxFl3YThQNc) · FAR․AI · 2025-05-12 · 5:04

## Chapters

- 0:00 Introduction
- 0:10 Hierarchical Monitoring
- 0:28 Contributions
- 1:10 Framework
- 2:18 Single Monitor
- 4:02 Conclusion

## Description

```text
Tim Hua demonstrates that hierarchical monitoring — using two trusted AI monitors in a strategic sequence — to detect misaligned outputs from untrusted models achieves higher safety at the same budget than using a single trusted monitor.

Highlights:
🔹 Hierarchical monitoring - Two-monitor system outperforms single monitors 
🔹 Budget optimization - Use expensive monitors only when necessary
🔹 Experimental validation - Demonstrated gains on Llama models
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:04] Tim Hua: Great. Hello, everybody. I'm Tim Hua, and today I'll be talking to you about hierarchical monitoring. Hierarchical monitoring is a new control protocol

### Hierarchical Monitoring

[0:12] that uses two trusted monitors instead of one. We usually assume that Monitor M is expensive and accurate and Monitor N is cheaper and less accurate, hence a hierarchy of monitors. We have two contributions to share today. The first is a simple mathematical framework

### Contributions

[0:30] for monitoring in AI control. We can apply this framework anytime we use trusted monitors, including in single-monitor settings. Our second contribution is that we apply this framework to the hierarchical monitoring setting, and we show that it leads to higher safety at the same budget, compared to using only one monitor. In our experiment, we use Llama 8B and 70B to monitor code outputs from o1-mini. So, here it is. Here's the result. Our red line here is when we use hierarchical monitoring. You can see that it has higher safety compared to the purple or the blue line, which is when we used only one monitor.

### Framework

[1:10] Now, I'll quickly go over our framework. We want to optimize safety. Our objective function is to maximize the chance of auditing or catching a misaligned output from an untrusted model. Following the original control paper, we'll assume human auditors that catch these models. That's our objective. Our cost constraint is we want to spend no more than Y dollars per aligned output. There's this interesting thing here where we always measure safety on misaligned outputs, and we enforce our budget constraint on the aligned outputs. The way I think about it is that cost is how much extra you have to pay if nothing bad happens, while safety is suppose something bad is going to happen, how likely are you to catch it and to stop it? You don't need to read the slide, but the idea is that we can write this out in math. You maximize this probability subject to this inequality constraint.

[2:09] Now I'll show you how we actually apply the framework to get this graph of results. We will start with a single monitor case, the purple and the blue lines. In the

### Single Monitor

[2:20] original trusted monitoring setup, they had a single monitor and they audited if the score is above some threshold. When we apply our framework, we can improve upon this baseline because calling the monitor 100% of the time is not always optimal. Basically, we add this option where you can end or audit immediately before you even call your monitor. Now, instead of having just one audit threshold, you also have these two probabilities. Again, you can write out this equation, you maximize this thing subject to this constraint. Basically, we find that using the monitor 100% of the time is not always optimal, especially when you have less of a budget. By picking these parameters intelligently, we can get a higher safety at the same cost.

[3:14] Now we've been through the single monitors. I'll talk about how we calculated the red line here. It's much harder to do this in a two-monitor setting. There are a lot of choices; which monitors to use first, a lot of different thresholds, and we couldn't figure out a way to solve it after we write down the whole equation. The way we do this is we restrict ourselves to a subset of policies that have fewer free parameters. I will now show you the strategy we used to calculate the red line from earlier. It has actually only two free parameters. Here's our monitor scores. We always use a cheap monitor first. If it's a really high score, we'll audit immediately. If it's low, we'll conclude. If it's in the middle, we call the second monitor, and we ensemble the information and audit. In general, the way we think about this is we pick some possible way

### Conclusion

[4:06] of using the two monitors. We fit our parameters to optimize safety on some training data set of monitor scores. In this example here, we have the audit threshold and the end threshold. The last thing just falls out of the budget. Then we evaluate it on out of distribution set. So again, here we have our old result, and you can see that hierarchical monitoring does better outside of distribution and in our in-distribution test set. I also have a poster. You can come to it later today, and we can chat about open questions, more results. One other open question is I don't have a job, and we can also maybe solve this at this conference today. Thank you very much.
