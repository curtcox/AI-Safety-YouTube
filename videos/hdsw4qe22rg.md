---
id: "hdsw4qe22rg"
title: "Mitigating Power Concentration and Multi-Agent Risks in AI | Samuel Simko (EuroSafeAI)"
url: "https://www.youtube.com/watch?v=hdsw4qe22rg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-04"
duration_seconds: 295
is_short: false
chapters: 10
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Mitigating Power Concentration and Multi-Agent Risks in AI | Samuel Simko (EuroSafeAI)

[Watch on YouTube](https://www.youtube.com/watch?v=hdsw4qe22rg) · FAR․AI · 2026-08-04 · 4:55

## Chapters

- 0:00 Intro: EuroSafeAI and a European perspective
- 0:37 Three pillars of AI safety
- 0:50 Model-level safety and honeypot defenses
- 1:35 Building better safety judges (JudgeStressTest)
- 2:02 Multi-agent safety (GT-HarmBench)
- 2:40 When aligned models escalate: arms-race dynamics
- 2:59 Risks to democracy and power concentration
- 3:26 SocialHarmBench: sociopolitical attacks
- 3:56 Position paper: AI risks to democratic systems
- 4:26 Takeaway: safety needs all three dimensions

## Description

```text
Samuel Simko (EuroSafeAI) on why AI safety has to extend beyond single models, to multi-agent interactions and risks to democratic institutions.

Simko presents EuroSafeAI's work across three areas. Model-level safety: making models robust to jailbreaks and misalignment, including a defense that uses "honeypot" replies to make attacks rarer and less useful, plus stronger automated safety judges. Multi-agent safety: game-theoretic modeling (GT-HarmBench) showing that models which look aligned in isolation can produce serious risks when they interact, sometimes escalating in arms-race dynamics. Societal risk: power concentration and threats to democracy, with benchmarks like SocialHarmBench probing sociopolitical attacks. His argument is that research clusters on the first two areas and gives the third far less attention than it needs.

Chapters
0:00 Intro: EuroSafeAI and a European perspective
0:37 Three pillars of AI safety
0:50 Model-level safety and honeypot defenses
1:35 Building better safety judges (JudgeStressTest)
2:02 Multi-agent safety (GT-HarmBench)
2:40 When aligned models escalate: arms-race dynamics
2:59 Risks to democracy and power concentration
3:26 SocialHarmBench: sociopolitical attacks
3:56 Position paper: AI risks to democratic systems
4:26 Takeaway: safety needs all three dimensions

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=B9I56daxBmDAeRwQ

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Intro: EuroSafeAI and a European perspective

[0:00] So hello, I am Samuel. I'm substituting for Zhijing, who was originally going to give this talk. However, she could not be here in person. So, to say a few words about EuroSafeAI first, it is a nonprofit that we founded and is headquartered in Switzerland. We're very excited to extend to other countries. And broadly speaking, we do AI safety work on a European and democratic perspective. For instance, we post-train models to behave well and to adhere to European standards. So in this talk, I want to talk about our three

### Three pillars of AI safety

[0:37] pillars at EuroSafeAI and mention how all of these three pillars are important for AI safety, even though much of the research is concentrated among only the first two pillars. So first of all,

### Model-level safety and honeypot defenses

[0:50] AI should be safe at the model level, of course — it shouldn't really have any misaligned behaviors, and it should be robust to jailbreaks and other types of harmful use. So some examples of the work we did in this includes this ICML paper that we will present tomorrow, in which we extend existing adversarial defenses with honeypots, meaning replies that seem harmful to automated judges but not to humans. And we notice that when we add a small preference to these types of honeypots, when we try to jailbreak models, well, not only do we get lower jailbreak successes, but also the successes are less actionable as humans would evaluate them.

### Building better safety judges (JudgeStressTest)

[1:35] Of course, when we scale up defenses, we also need to scale up the evaluations. So this is why we're actively working on making better judges. For instance, we tried to use a composite approach to try to judge whether something is harmful or not. And our original goal was to just reduce false positives in evaluation pipelines, but we also noticed that we achieved very high scores on this JudgeStressTest benchmark, which is a challenging benchmark for judges.

### Multi-agent safety (GT-HarmBench)

[2:02] Now, it is good to have a model which is safe in isolation and when used singly. But nowadays, people are increasingly using AI agents which delegate things to other tasks. So it's important for these models, if they communicate with other agents, to be safe. And one of our works that shows that this can be a problem is GT-HarmBench, which will also be presented later on as a workshop. In this work, we show that through game theoretical modeling, we can model some AI safety risks as games like the prisoner's dilemma or coordination games.

### When aligned models escalate: arms-race dynamics

[2:40] And models that appear to be well-aligned in isolation can induce very big risks. For instance, some models that are aligned can, in a very high critical scenario such as an arms race, they can be kind of willing to escalate things instead of bringing things down a notch.

### Risks to democracy and power concentration

[2:59] So even if we have models that are safe in isolation and can kind of interact with other agents and still be safe, well, there's many risks to AI, especially power concentration and their ability to potentially weaken democratic institutions, as a few number of actors could have a very high amount of power to do propaganda and so on. So some of our work from our lab

### SocialHarmBench: sociopolitical attacks

[3:26] include SocialHarmBench, in which we formalize sociopolitical attacks. So, compared to just trying to have a model do something harmful, we try to see how likely it is to do historical revisionism or participate in surveillance tasks. And the results are — especially for smaller models, but also for some very large-scale models — it's quite concerning how even direct prompting and very simple attacks can achieve very high success rates on those type of queries.

### Position paper: AI risks to democratic systems

[3:56] So more broadly speaking, we categorize a lot of these risks in our position paper, "AI Poses Risks to Democratic and Social Systems." An earlier version of this work will be also presented at ICML as a spotlight paper on Wednesday. And in this work, notably, we talk about power concentration and others. And we highlight some possible technical solutions and recommendations for the future. So, as a takeaway,

### Takeaway: safety needs all three dimensions

[4:26] there's many different works that talk about AI safety, and we believe that they should cover these three dimensions. And most of the work right now is concentrated in one and two, which is very important. But we also would welcome to see much other work on democratic institutions and risks for power. And this is our website if you're interested in learning more. Thank you.
