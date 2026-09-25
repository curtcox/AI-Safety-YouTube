---
id: "uGoXO2pYYjM"
title: "Red-Teaming & Jailbreaking AI: Why Open-Weight Models Stay Vulnerable | Kellin Pelrine (FAR.AI)"
url: "https://www.youtube.com/watch?v=uGoXO2pYYjM"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-02"
duration_seconds: 293
is_short: false
chapters: 10
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Red-Teaming & Jailbreaking AI: Why Open-Weight Models Stay Vulnerable | Kellin Pelrine (FAR.AI)

[Watch on YouTube](https://www.youtube.com/watch?v=uGoXO2pYYjM) · FAR․AI · 2026-08-02 · 4:53

## Chapters

- 0:00 Red-teaming and jailbreaking: the state of play
- 0:06 Good news: closed models are much harder to jailbreak
- 0:48 Bad news: open-weight models stay trivial to jailbreak
- 1:13 No GPUs, fine-tuning, or expertise required
- 1:58 Simple input-space attacks, not just tampering
- 2:16 Does jailbreaking destroy capabilities? The jailbreak tax
- 2:48 What can we do? Technical measures that work
- 3:24 Pretraining filtering and gradient routing
- 3:55 The government and policy side
- 4:13 Takeaway: no single fix, but real progress

## Description

```text
Kellin Pelrine (FAR.AI) on the state of AI red-teaming: closed models are much harder to jailbreak, while open-weight models stay trivially easy.

Pelrine gives a red-teaming status report. Over the past year, leading closed-weight models have become far more robust, moving the problem from open research questions toward engineering and adoption. Open-weight models are a different story: they stay easy to jailbreak with simple prompt-based attacks that need no special expertise or resources, and the "jailbreak tax," the capability loss from breaking a model, largely disappears for stronger models. He then makes the constructive case that robust open models are achievable, pointing to pretraining data filtering, gradient routing to isolate dangerous capabilities, and government work on risk modeling and evaluation. There is no single fix, but the risk can be reduced.

Chapters
0:00 Red-teaming and jailbreaking: the state of play
0:06 Good news: closed models are much harder to jailbreak
0:48 Bad news: open-weight models stay trivial to jailbreak
1:13 No GPUs, fine-tuning, or expertise required
1:58 Simple input-space attacks, not just tampering
2:16 Does jailbreaking destroy capabilities? The jailbreak tax
2:48 What can we do? Technical measures that work
3:24 Pretraining filtering and gradient routing
3:55 The government and policy side
4:13 Takeaway: no single fix, but real progress

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=B9I56daxBmDAeRwQ

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Red-teaming and jailbreaking: the state of play

[0:00] So I'm going to talk about red teaming and jailbreaking. And let me start with some of the

### Good news: closed models are much harder to jailbreak

[0:06] good news, relatively speaking, which is that it's gotten a lot harder to jailbreak closed-weight models. I think we've been seeing over the past year that developers have deployed a lot more defenses in particular areas like bio and cyber. And while it's not a completely solved problem, the difficulty has gone way up. And a lot of the problem now has shifted from needing scientific breakthroughs to more just needing good engineering and broad adoption. So we'll have more to say on that in a few weeks. We're going to be releasing a big report.

### Bad news: open-weight models stay trivial to jailbreak

[0:48] But for today, I want to talk about maybe the bad news on the open-weight side, which is that they still seem to be trivial to jailbreak. So for example, you don't need to be an expert. You can just spend 15 minutes Googling and download an abliterated model like Gemma 4 and have a pretty compliant jailbroken model.

### No GPUs, fine-tuning, or expertise required

[1:13] One of the questions that many people have here is whether you need a bunch of resources, like maybe you need GPUs to run the model, or to do a bunch of fine-tuning, some expertise on how to do the fine-tuning or abliteration. But what we found is that you really don't need that at all. So again, you can just Google, for instance, an input-only - you just need user prompt - jailbreak, for instance, for DeepSeek-V4 here that wasn't patched from a previous DeepSeek model. Or if you have a bit more access, you can use a system prompt as well with another public jailbreak. Or if you have access to prefills, you can do a prefill attack.

### Simple input-space attacks, not just tampering

[1:58] So even though a lot of the unique sort of risk space that people think about with open-weight models is on these tampering, fine-tuning, et cetera sort of attacks, they're actually quite vulnerable to just simple input space jailbreaks as well.

### Does jailbreaking destroy capabilities? The jailbreak tax

[2:16] Another common question is, well, maybe you can jailbreak the model, it'll comply, but you could destroy the capabilities in the process. But that also doesn't seem to be the case. So Anthropic had a paper recently where they found that this so-called "jailbreak tax" disappears with stronger models. And that matches what we found on the open-weight side as well, where some jailbreaks do degrade the capabilities, but it's quite possible to get ones that don't.

### What can we do? Technical measures that work

[2:48] So what can we do? I think there's actually quite a lot of technical measures that can be pretty promising here. So if we compare open-weight models with some of the leading, most relatively safeguarded closed-weight models, we see that models like GPT-5.5 are just way more robust to jailbreaks even without external safeguards — so just the model itself. So it's very possible to make open-weight models that are robust to input space jailbreaks.

### Pretraining filtering and gradient routing

[3:24] There's also a lot of promising research on pre-training filtering to control dangerous capabilities. I think Stella right after me may talk some about that. And promising future directions as well, like gradient routing, where you can concentrate some capabilities in a particular expert. So for instance, like bio capabilities. And then you could potentially remove that expert to get a model that is much safer in that area.

### The government and policy side

[3:55] And then there's also a lot of work that we can do on the government side. So for instance, building a better understanding of the risks, risk modeling, dissemination, building consensus, and just better evaluations and testing, identifying and fixing vulnerabilities.

### Takeaway: no single fix, but real progress

[4:13] So the sort of a concluding message that I want to leave everyone with is that there's definitely a lot of risks here with open-weight models. But I think that there's actually quite a lot of promising directions to make improvements. If you want like a single magic bullet that will completely make them safe in one go, that's probably impossible — impossible for any AI model. But I think that we can really reduce the risk a lot by some of these interventions and building safer open-weight models in general. Thank you.
