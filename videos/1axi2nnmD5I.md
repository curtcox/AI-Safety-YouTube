---
id: "1axi2nnmD5I"
title: "Is Your AI Model Actually Secure? The Jailbreak Problem | Adam Gleave (FAR.AI)"
url: "https://www.youtube.com/watch?v=1axi2nnmD5I"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-19"
duration_seconds: 310
is_short: false
chapters: 7
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Is Your AI Model Actually Secure? The Jailbreak Problem | Adam Gleave (FAR.AI)

[Watch on YouTube](https://www.youtube.com/watch?v=1axi2nnmD5I) · FAR․AI · 2026-08-19 · 5:10

## Chapters

- 0:00 Uneven safeguards across frontier models
- 0:22 The upside: what capable models deliver
- 0:43 The dark side: AI misuse happening now
- 2:19 Testing safeguards: 1,500 jailbreak combinations
- 2:52 Results by domain: what held and what broke
- 3:33 The fix: cheap, documented safeguards
- 4:20 A minimal standard, and what comes next

## Description

```text
Adam Gleave (FAR.AI) on why some frontier models resist every jailbreak tested while others break in hundreds of ways across high-risk domains.

FAR.AI tested the safeguards of leading frontier models against 1,500 jailbreak combinations. OpenAI's and Anthropic's latest models resisted nearly every attack, while Grok and Gemini produced hundreds of universal jailbreaks that unlocked chemical, nuclear, radiological, explosives, and cyber capabilities. Every model held in biosecurity. The talk maps these jailbreaks to misuse already documented by the UK AI Security Institute, Google, and Cambridge University researchers, and explains why specialized classifiers make stronger safeguards cheap and achievable for any developer.

Chapters
0:00 Uneven safeguards across frontier models
0:22 The upside: what capable models deliver
0:43 The dark side: AI misuse happening now
2:19 Testing safeguards: 1,500 jailbreak combinations
2:52 Results by domain: what held and what broke
3:33 The fix: cheap, documented safeguards
4:20 A minimal standard, and what comes next

More AI safety research: https://far.ai

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Uneven safeguards across frontier models

[0:00] Our AI security leaderboard ranked the safeguards of Frontier models. We found that OpenAI and Anthropic's latest models were robust to everything that we threw at them. Whereas we found hundreds of universal jailbreaks for Grok and Gemini that reliably bypass these model safeguards. Now, there's no shortage of benchmarks that evaluate model capabilities. And we all know

### The upside: what capable models deliver

[0:23] that today's models are highly capable. On the plus side, they're helping open source projects like Mozilla find and fix orders of magnitude more vulnerabilities than they're able to find by hand. And models have also resolved open questions mathematics that have stumped mathematicians for almost a century. We wanted to study model safeguards because these same capabilities that

### The dark side: AI misuse happening now

[0:45] make models so powerful also have dark sides. Models cannot just find vulnerabilities in software. They can develop exploits and the UK's AI security institute found that models could leverage these exploits to compromise series of systems moving through a simulated computer network. And this risk isn't purely hypothetical. It's happening today. Google reported a few months ago that a threat actor had developed a zero-day exploit using the help of AI. And AIS are even getting in on the fun themselves. An internally deployed OpenAI agent recently hacked out of its sandbox and then compromised a third-party company's servers, Hugging Face, to ultimately steal the answers to a test that it was being evaluated on. This is both a striking real world demonstration of the offensive cyber capabilities of frontier models and also a bit of a warning sign about potential loss of control risks for models. Terrorist groups are also beginning to make use of AI. Research from Cambridge University by researcher Antonia Juelik found that Boko Haram have used leading AI systems to design explosive devices and troubleshoot weapons, with Islamic State operatives delivering in-person training, including the use of jailbreaks to bypass model safeguards. Now, I got into AI because I wanted to cure cancer and vibe code, not help terrorists kill people or have rogue AI agents running around hacking innocent companies.

[2:12] So, wouldn't it be great if we could get the benefits of AI without some of these downsides? And this is where safeguards come in. Frontier developers train their models not to

### Testing safeguards: 1,500 jailbreak combinations

[2:23] assist with harmful requests and use specialized classifiers to block high-risk conversations. But there's never been any systematic evaluation of how good these safeguards really are. So we assembled a collection of jailbreaks -- techniques that bypass model safeguards, from both public sources as well as a number of our own devising. We then tested a thousand random combination of these jailbreaks along with 500 combinations chosen by an expert red teamer on our team. The results surprised even us. The good news is that all frontier models are secure

### Results by domain: what held and what broke

[2:55] against this attack in the domain of biosecurity. So if you're hoping to make anthrax, you're going to have to do it like your grandfather did without the help of AI. But we find hundreds of universal jailbreaks for the latest Gemini and Grok models across a variety of other harm domains. These jailbreaks consistently unlock model capabilities in areas like chemical weapons, radiological and nuclear weapons, explosives as well as cyber attacks. And that last one is particularly surprising because cyber security is where we're seeing the biggest harm today, as well as the bulk of the focus of government attention. Now the good news is it doesn't have to be that way. Anthropic and OpenAI latest models were mostly secure against our attack and the

### The fix: cheap, documented safeguards

[3:37] techniques they use are all publicly documented. We also make a number of concrete recommendations beyond this in our report that developers can use to secure their models. Ultimately preventing misuse of out of control agents is not easy. But it's possible to do a lot better from the current state and at a relatively low cost. If developers can afford to spend billions of dollars on the latest training runs, they can certainly afford to have small teams training specialized classifiers to detect and prevent misuse. Now, I do want to clarify that although Anthropic and OpenAI come out looking pretty good in these tests, their models aren't perfect. And in fact, we found various universal jailbreaks for models from these companies over the years and have worked with the companies to fix them. Our test is simply intended as a minimal standard, something that any frontier

### A minimal standard, and what comes next

[4:25] model should be able to meet and which makes it meaningfully harder for bad actors to misuse these models. But we certainly encourage developers to go beyond this minimal standard. And in fact, we're going to be updating the leaderboard periodically to reflect the state-of-the-art in attack and defense. For more information, do check out the full ranking at leaderboard.far.ai and read the report for more information. If you found this video interesting, then please do like and subscribe to our channel for more explainers from me and my colleagues as well as talks from leading experts on AI safety and security from FAR.AI's events. Thanks for listening.
