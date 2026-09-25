---
id: "Kx9qjX-SbUA"
title: "Why AI Safety Evaluations Are Broken: The Test-Time Compute Problem | Noam Brown (OpenAI)"
url: "https://www.youtube.com/watch?v=Kx9qjX-SbUA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-05"
duration_seconds: 286
is_short: false
chapters: 9
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Why AI Safety Evaluations Are Broken: The Test-Time Compute Problem | Noam Brown (OpenAI)

[Watch on YouTube](https://www.youtube.com/watch?v=Kx9qjX-SbUA) · FAR․AI · 2026-08-05 · 4:46

## Chapters

- 0:00 GPT-5.5 vs 5.4: why benchmarks miss the story
- 0:26 Plotting performance against tokens
- 0:48 Models don't plateau: they scale with compute
- 1:35 Evaluate as a function of compute, not a single bar
- 2:20 Better benchmarks: ARC-AGI's cost curves
- 2:38 Why safety evaluations are broken
- 2:45 How low-budget evals hide catastrophic risks
- 3:39 Three concrete recommendations
- 4:24 Preparedness frameworks and test-time compute

## Description

```text
Noam Brown (OpenAI) on why AI evaluations, including safety evaluations, mislead when they ignore how much a model thinks at test time.

Brown shows how a single bar chart can misrepresent a model's capability: plot performance against output tokens, cost, or time, and gains that looked flat become large, because reasoning models keep improving with test-time compute. For reasoning and agentic tasks, how long a model thinks is a hidden variable in most current benchmarks. The safety consequence is direct: a model evaluated at a low inference budget can look harmless, while an actor spending far more on inference reaches more dangerous capability. His recommendations: publish benchmarks with a compute, cost, or time axis, track inference usage on leaderboards, and write test-time compute into preparedness frameworks and responsible scaling policies when setting safety thresholds.

Chapters
0:00 GPT-5.5 vs 5.4: why benchmarks miss the story
0:26 Plotting performance against tokens
0:48 Models don't plateau: they scale with compute
1:35 Evaluate as a function of compute, not a single bar
2:20 Better benchmarks: ARC-AGI's cost curves
2:38 Why safety evaluations are broken
2:45 How low-budget evals hide catastrophic risks
3:39 Three concrete recommendations
4:24 Preparedness frameworks and test-time compute

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=DA_ufycPrJV74Pam

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### GPT-5.5 vs 5.4: why benchmarks miss the story

[0:00] Hi, everybody. So I'll try to make this in 5 minutes. Okay, so when GPT-5.5 came out on the benchmarks like these, it didn't look that much better than 5.4. You're seeing here on a cyber eval, you're going from 79% to 82%. But then people played around with the model and they realized it's actually a lot better. So why is that? I would argue it's because the evaluations that use bar charts like this are not telling the full story. So if you plot it this way,

### Plotting performance against tokens

[0:26] where tokens, output tokens are on the x-axis, you can see that actually there's a huge jump between 5.4 and 5.5. It's just that it doesn't appear that way on the bar chart because 5.4 is thinking for a lot longer on these problems. So you look at this and you probably are thinking, like, well, why don't we just have them think for the same amount of time? Why not just have them think for longer? And the question is, okay, well, how long should they think for in these evaluations?

### Models don't plateau: they scale with compute

[0:48] And you might say, well, we should have them think until they plateau in performance. The problem is the models don't really plateau that much these days. Here is from AISI. On the x-axis, you have cumulative tokens. On the y-axis, you have success rate. You can see for Mythos and 5.5, you're seeing even after 100 million tokens, performance is still going up pretty rapidly. You can see that this is particularly true for the most recent models. It's less true for GPT-4o, Claude Sonnet 3.7. But for the most recent models, they're able to operate over much longer horizons more effectively and continue to improve. And look, if we were to extend this out further, it would probably keep going up. So the main point that I want to make is you have to

### Evaluate as a function of compute, not a single bar

[1:35] divide with these models as a function of compute or of time or of cost. Just if you plot it as a single bar chart, then you run into this confounder of how long are the models thinking for before they answer. And so I think this sounds intuitive when I lay it out like this, I hope. But the reality is most evaluations today are being done with bar charts like this and not with plots like this. I should also say this really only applies to reasoning tasks. If you're doing things like knowledge retrieval, then yes, you don't really benefit from more thinking time. But a lot of the agentic workflows that we care about today fall into the category where you actually do benefit from having the model think for longer. So that's the main point I want to make. Fortunately,

### Better benchmarks: ARC-AGI's cost curves

[2:20] there are some benchmarks that have shifted in this direction. I think ARC-AGI was actually quite early to this, where they plot performance with an x-axis of cost and the y-axis is pass rate. And you can see these nice scaling curves where you get better performance for a higher cost. Okay, so

### Why safety evaluations are broken

[2:38] my main point is safety evaluations are currently broken. This is also true for safety evaluations.

### How low-budget evals hide catastrophic risks

[2:45] And this particularly matters because we want to evaluate these models for things like catastrophic harms. And if you're going to do that at a budget of, let's say, $1 or $10, then it might not appear that these things are very dangerous when in fact they are. So my argument is, even if you do the evaluations at a budget of like $100 and it doesn't seem dangerous, well, there are organizations that could easily spend $10 million on inference and get much higher performance than what the safety evaluations seem to imply. In my ideal world, I think safety evaluations would be done in a way like this, where you have an x-axis of inference budget. You do evaluations at relatively low costs because it's not feasible to do a lot of evaluations at $10 million for every data point. Then you just project outwards and try to project what performance would be at higher inference budgets.

### Three concrete recommendations

[3:39] Okay, so concrete recommendations. One, I think AI labs should publish benchmark performance of newly released models with an x-axis of either tokens, cost, or time. There's trade-offs for all those different x-axes, but I think any of them are an improvement over what we have today. Two, I think benchmarks should track inference usage on leaderboards. So it's in the same way that when you have the SATs, there's a time limit for the exam. It's really hard to compare two students if one of them takes 10 times longer than the other student. So you want to have some kind of standard for what the budget is for this benchmark, or at the very least, just track the inference usage for different models on the benchmark when you have a leaderboard. And then three, preparedness frameworks and

### Preparedness frameworks and test-time compute

[4:24] responsible scaling policies should explicitly account for test-time compute when determining whether a model crosses a safety threshold. It's honestly pretty surprising to me that this isn't a widespread common thing these days. Okay, so I will stop there with 30 seconds left. Thank you.
