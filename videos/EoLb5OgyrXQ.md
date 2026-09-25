---
id: "EoLb5OgyrXQ"
title: "Xander Davies - State of Jailbreaks [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=EoLb5OgyrXQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-01-29"
duration_seconds: 415
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Xander Davies - State of Jailbreaks [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=EoLb5OgyrXQ) · FAR․AI · 2026-01-29 · 6:55

## Chapters

- 0:00 Introduction to jailbreaking
- 0:51 Improvements in safeguards
- 2:23 Drivers of model robustness
- 3:48 Variability in robustness
- 6:09 Future outlook and closing

## Description

```text
Xander Davies (UK AI Security Institute) demonstrates that every frontier AI model remains vulnerable to jailbreaking despite measurable safety improvements. Testing reveals dramatic variance in attack difficulty: biological misuse requires 5 hours versus 10 minutes for other harmful content, while open-weight models prove 15x easier to compromise than closed systems. Though some models improved from 10-minute to 7-hour jailbreak times over six months, the 100% success rate across all systems shows safety gains come from engineering investment, not increased intelligence. Model capability benchmarks show weak correlation to jailbreak resistance (R²=0.097). Davies emphasizes defenders and attackers co-evolve, with attack sophistication increasing as defenses improve.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to jailbreaking

[0:00] So I'm going to be talking about jailbreaks and in particular what we call universal jailbreaks. So these are jailbreaks that bypass model safeguards and enable users to carry out harmful processes that require many model interactions. So this is different from as a one off, the model said something toxic. This is like a recipe you can use to consistently get out harmful, accurate information. And my team has been working on this for the past two years with most of the Frontier Labs as two examples. We recently worked with OpenAI on ChatGPT Agent and GPT-5 and with Anthropic on constitutional classifiers. In both cases, finding, reporting, working together to fix a number of attacks. And we do so using a bunch of techniques and we spend a bunch of time looking for new attacks. And that's sort of our day to day. So I wanted to talk about the state of jailbreaks. I think from the

### Improvements in safeguards

[0:55] outside it's actually pretty hard to track what's happening with jailbreaking. There's information in system cards, there's academic reports, and then there's like Twitter people posting, hey, I got the model to say something harmful. And a lot of these findings sort of point in different directions. Like if you look at Twitter, it looks super easy to break things. If you read some papers from companies, maybe it looks really hard. Academia, who knows. So the goal of this talk is to give my view on the current state of jailbreaking. How hard is it, what's happening, et cetera. Okay, so first point is that certain model safeguards are actually improving quite a lot, even though they're all still vulnerable. So this is an example. Throughout these slides, I'm going to use how long it takes us to attack a model as the metric, which is like a pretty rough metric and we're working on better metrics and if people want to talk about metrics, would love to. So this shows how long it took us to attack two different models. The first model was released six months before the second model. First model took us like 10 minutes. We were using a public attack we already knew about. Second model took us over seven hours. So that's a pretty big change and a change that I would be very happy to hear if you had told me that six months ago it would take us seven hours for a model. So there's definitely been real progress.

[2:17] I'm gonna put some asterisks on this progress, but in general, there's been real progress.

### Drivers of model robustness

[2:25] Oh, I should say we still have jailbroken every model we've tried to test. So there's been progress, but there's limitations still. Second of all, this improvement has been driven by effort and investment, as opposed to just models getting smarter. So when I was first getting into this, people thought maybe once models got a bit smarter, they would just sort of understand the situation well enough that you just, like, wouldn't be able to get them to tell you harmful things. And I think we have not yet seen evidence of this being the primary driver of improvements to jailbreak robustness. So this is data taken from a competition we ran with Grey Swan AI where we had people try to attack models in a bunch of different situations. And then the X axis here is a flawed but a benchmark for model capability, GPQA. And then the Y axis is robustness. And you can see there's like a positive trend. So more capable models tend to be a bit better. But these are not very dramatic changes in robustness. We're seeing something like the 40x from the last slide is very different, and it's coming instead from investment by companies in a targeted way. So that might look like investing in separate classifiers which sit around the model and try to flag harmful interactions or additional training techniques for robustness.

[3:47] Okay, so certain model safeguards are improving. They're all still vulnerable.

### Variability in robustness

[3:51] The improvement is driven by effort and investment, not model capability. Third point is that robustness varies a lot across domains, providers and access. And I think this is part of what makes it hard to follow. So I'm going to break this into these three areas. So by domain, if we take the same model and we try to jailbreak it on, in scope, biological misuse requests, just like a pretty narrow category, it takes us something like 5 hours for this one, whereas if we try to jailbreak it for other harmful categories, it takes us more like 10 minutes. So this is like a pretty dramatic difference, and that's coming from this dedicated investment from companies in making models more robust for a subset of misuse requests. So that might mean that a model comes out and it looks like it's really robust in the system card. And then people on Twitter quickly post something about, look at how toxic the output is. And that's because of dynamics like this, where certain requests are much easier to jailbreak on than other requests.

[4:59] Another is that safeguards vary significantly across providers. So if we take latest models from different providers and we try to jailbreak them. Some might take us more like 30 minutes, whereas some might take us more like five hours. So these are pretty dramatic changes in the time. And then finally, the performance of the safeguards will vary a lot based on how the model is exposed to users. And so even though there has been some progress on these, like, closed models, we've seen much, much less progress when the attackers can actually directly manipulate the weights, they can remove any guardrails, et cetera. So unsurprising, but a thing to note. Yeah, so those are my three points. Certain model safeguards are improving, but they're all still vulnerable. Improvement is driven by effort and investment, not model capability primarily. And robustness varies a lot across domains, providers and access. And I'm just going to end with one more point, which is we have been doing this now for two years, and what we've seen is every time defenders make progress, we as attackers also come up with more sophisticated systems. And

### Future outlook and closing

[6:11] so I think it can be easy to feel like, oh, we've nearly cracked it, or something. I think, in fact, we're a long way from cracking it in the face of, like, dedicated adversaries who are going to themselves come up with increasingly sophisticated attacks. So I'm expecting attack complexity to go up over time, at least in domains where you have, like, dedicated adversaries trying hard. Cool. So if you want to talk about any of this, there are a few of us from this team here at the conference and we're also hiring. There's also a social that AISI is hosting and we have a booth at the main conference. So thanks, everyone.
