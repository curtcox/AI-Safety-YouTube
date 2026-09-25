---
id: "P7cf8GXer1I"
title: "Shayne Longpre - In-House Evaluation is Not Enough [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=P7cf8GXer1I"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-27"
duration_seconds: 361
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Shayne Longpre - In-House Evaluation is Not Enough [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=P7cf8GXer1I) · FAR․AI · 2025-06-27 · 6:01

## Description

```text
Shayne Longpre calls for a coordinated disclosure system to identify and report AI vulnerabilities, leveraging worldwide expertise to complement testing efforts at AI labs. 
Highlights:
• In-house evaluation insufficient for AI systems
• Third-party testing provides scale and independence
• Legal protections lacking for most AI flaws
• Limited flaw reporting culture in AI industry
• Need for coordinated flaw reporting infrastructure
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Hello everyone, I'm Shayne. I'm a PhD student at MIT, and I'm here to talk to you about our central thesis, which is that in-house evaluation is not enough. The teams at the companies are phenomenal, they have great internal testing teams. However, sometimes it can be really difficult to cover the massive surface area of flaws that general purpose AI systems have. Some people are concerned about AI systems being used with children for companionship, for cybersecurity exploits, some people are worried about jailbreaks, there's a wide set of different flaws these systems might have. And additionally, we estimate that these systems are now rolled out to about a billion people worldwide, covering hundreds of–or tens of different languages, that probably the internal testing teams don't have someone that speaks each of those languages fluently.

[0:58] And so, we collated a group of experts from academia, security, AI industry and civil society to talk about what is needed for third party post-deployment testing. And so, on one end of the spectrum here you can see that first party internal product testing teams, they have a lot of expertise and deeper access. But then you have second party, like the UK AI Security Institute, and OpenAI's red-teaming network. And further to the right, you have more third-party expansive access. And there are certain key advantages that this brings: First off, you have the scale of participation. Any user, journalist, researcher, or white hat hacker can contribute reports about different flaws that they observe, and they could be lawyers, medical doctors, people with a variety of expertise and wider coverage from around the world that often are necessary to debug the issues with these systems.

[1:59] And lastly, third party valuation also provides the greatest degree of independence when it comes to evaluation. So really, it's complementary. You need in-house, first party, second party, and third party. But I want to sort of paint a picture of the different types of flaws that you might see. So, in the yellow box at the top, you see more traditional software security vulnerabilities, like code injection attacks, cross-site scripting, privilege escalation, other such things. And further down you have other types of flaws like Adversarial Machine Learning Flaws where people try to steal the weights of models or the underlying trading data. They use the systems in the wild to attack other software to create deepfakes or spread misinformation or other more pernicious things like non-consensual intimate imagery. But an important distinction here is that for the yellow box on top right now, there are at most, for most major software and for a lot of the large AI systems, legal protections. So, there's safe harbors, if you look into those types of vulnerabilities, there are designated hacker one or bug crowd software platforms that allow you to do flaw disclosure and coordination for those types of attacks.

[3:10] Triage the issue, coordinate with the company and figure out if there's an issue. And if you have identified something, there are financial rewards for those types of issues. So, Google alone gave $12 million just last year in remuneration for researchers that found issues in their software, and this has widely spread, these practices across AI companies. However, for the rest of the AI flaws, we don't have any of these things. We have no safe harbor legal protections, we don't have good flaw disclosure coordinated infrastructure, although it's starting to be rolled out by companies like OpenAI and Anthropic with initial bug bounties. And we don't really have financial rewards for third party testing either. What do we have? When a user, a journalist, or researcher finds a flaw, they tend to do one of three things right now. They don't disclose it, because they're uncertain of where to disclose it or how to disclose it. They disclose it via email to one company, or they post to social media so they don't get scooped. None of these are optimal outcomes, instead–well, before I say instead, we notice that currently in AI, there's an absence or limited flaw reporting culture, flaw reporting infrastructure and legal protections and/or financial incentives.

[4:26] So, what we really want is something like this: when someone finds an issue that deserves to be reported, either a user, a journalist, or a researcher, they fill out a flaw reporting form, that helps them fill out all the fields, so that's easily to reproduce, to triage, and to quickly figure out where to prioritize that issue. It can be coordinated, for example, if it's a universal jailbreak that it pertains to many different models, it's maybe applies to Llama 3, Llama 2, but also open AI, Anthropic, and Google models, that it can be coordinated to all the different people and stakeholders that can help mitigate that issue. If the data poisoning attack, that might need to go also to the data providers, it might need to go to Cursor, Perplexity, or wrappers as well. And so, we are trying to build this by constructing the bare essentials from security that are required for someone to report a flaw quickly and have expediated triaging and analysis that's helpful to the companies.

[5:27] We've done a lot of analysis about what types of things need to be reported, how to do it quickly and efficiently, and our next step is to actually build this. So, if you're interested or like to help us do this together with security and AI researchers, we hope to roll this out pretty soon, and would love your feedback. So, thank you so much and you can read more about us here.
