---
id: "LXCM505db8A"
title: "Daniel Kang  - CVE-Bench [Technical AI Policy]"
url: "https://www.youtube.com/watch?v=LXCM505db8A"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-10-14"
duration_seconds: 266
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Daniel Kang  - CVE-Bench [Technical AI Policy]

[Watch on YouTube](https://www.youtube.com/watch?v=LXCM505db8A) · FAR․AI · 2025-10-14 · 4:26

## Description

```text
Kang introduces CVE-Bench, a new benchmark made from real-world vulnerabilities from the NIST CVE database to measure AI exploit capabilities, filling the gap left by existing benchmarks that relied on unrepresentative tests and artificial tasks. 

Highlights:
Existing benchmarks poorly predict AI's real-world performance
AI agents could exploit only 10-15% of real vulnerabilities
Automated scoring ensures reproducible test cases
Accurate measurement is crucial for AI security evaluation

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] AI over the past few years has been shown to have potentially major cybersecurity risks. And so there's a bunch of work both from my lab and also from other institutions including Anthropic and CMU and many others that have shown the potential for AI agents to have large impacts in cybersecurity. But one of the issues today is that all of the existing benchmarks are either ad hoc or operate on what are called capture the flag exercises, which are essentially training exercises to help cybersecurity professionals get up to speed. And so just as an example, this is work from our lab that shows that we can find and exploit real-world vulnerabilities in these web applications that we scrape from the NIST CVE database. But a question that you might ask is: can AI actually find 60% of all vulnerabilities in the wild? This basically boils down to the question of are these benchmarks representative? To resolve this, we built this benchmark called CVE Bench, which is a benchmark to evaluate AI agents' abilities to exploit real-world vulnerabilities. To avoid any issues around sampling bias, we collected vulnerabilities from the NIST CVE database that were from a specific date range of critical severity and open source so we could actually reproduce and test our AI agents on these vulnerabilities.

[1:26] After we found these vulnerabilities, we then basically made these vulnerabilities reproducible and then standardized them for review and also for potential exploit by AI agents. One of the most important challenges in creating a benchmark for AI agents is the ability to automatically evaluate whether or not the AI agent has been successful or not. I don't have time to go into this talk about how the complexities behind this, but this actually turns out to be one of the most pressing issues around AI benchmarks in general. And I'm happy to talk about this afterward. Just for reference, there are some AI agent benchmarks where over 50% of the tasks have errors in them and are invalid in terms of the measurement. We categorize the attacks across our 40 vulnerabilities into eight classes, including things like denial of service and unauthorized administrator login. So basically imagine you have a website—this tests if the AI agent can log into your website as an administrator without the administrator credentials. In addition, we have an application-specific grader and this is required because every application has vulnerabilities that manifest in slightly different ways.

[2:30] What we found when we deployed GPT-4o—and this was around, we did the experiment around six months ago—is that GPT-4o can find and exploit up to about 15% of these vulnerabilities with knowledge of the vulnerability ahead of time, and about 10% of the vulnerabilities without knowledge of the vulnerability ahead of time. And so even though these results are lower than before, if we look at the trend of AI agents and their capabilities, it's always up and to the right. And so what we've already found is that more capable models can find more vulnerabilities. Beyond that, I work on several things, including on attacking AI agents. So if you're thinking about deploying AI agents in the wild, there are many security implications, especially if they can access private and secure data. We build a series of benchmarks and a series of methodologies to determine the efficacy of defenses around these AI agents.

[3:24] I also work on auditing private LLMs. And so, for example, there have been allegations that OpenAI has not actually been testing their released models with the claimed checkpoints. They have not been testing models that have been released in the wild on the finalized checkpoints. And my lab is producing methods to generate these audits automatically and in a way that, say, these actors cannot cheat. But in conclusion, CVE Bench is the first real-world benchmark for AI agents and cybersecurity. And I believe, but I'm not 100% sure, that it is also the first agentic benchmark where every task was vetted by an expert human. My email is here along with my Twitter handle. That benchmark is available on GitHub and has been shared with partners including the US and UK AISIs, OpenAI, Anthropic and others as well. I think I have about 20 seconds for questions, otherwise we can go to the next lightning talk. Thank you.
