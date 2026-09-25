---
id: "yExtYcZXmfM"
title: "Sam Watts - Lakera: Runtime Security for Agents at Scale [ControlConf]"
url: "https://www.youtube.com/watch?v=yExtYcZXmfM"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-05-25"
duration_seconds: 324
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sam Watts - Lakera: Runtime Security for Agents at Scale [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=yExtYcZXmfM) · FAR․AI · 2025-05-25 · 5:24

## Description

```text
Sam Watts from Lakera addresses the security challenges of large language model deployments, emphasizing their real-time protection for businesses against evolving AI threats like prompt injections and jailbreaks.

Highlights:
🔹 LLM Deployment Vulnerabilities: Addressing prompt injections and jailbreaks.
🔹 Real-Time Monitoring Solutions: Protecting firms and startups effectively.
🔹 Evolving AI Threat Landscape: Adapting to ongoing cybersecurity challenges.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:02] Sam Watts: Excellent. Good afternoon, everyone. So yes, I'm Sam Watts. I'm a product manager at Lakera. We build runtime security for agents at scale, which basically means, we've just heard about, for those in the last talk, the difficulties of dealing with latency, scale, and real deployments. We’re building—well, we have tools that monitor LLM deployments in real time and basically make sure they're not doing anything wrong and, very importantly, they're not being hacked. We build AI to secure AI. We are a startup of around 50 people. Scaling very fast, venture-backed. We've got lots of great people from lots of great companies. We sell to Fortune 500s, including global banks like Citibank and also lots of small Gen AI startups. Where all those companies that are actually building with Gen AI, we're plugging into them in order to secure them and their systems at scale, and we're processing millions of interactions every single day and keeping them secure.

[1:03] To talk about where we are today, obviously lots of this conference is about the future. The attack surface today is language as the main input, and we have capabilities. This looks completely different from traditional software, where you normally had very clearly defined inputs and well-known capabilities. Now we don't even know what the full extent of the capabilities of the model. In this situation, we're already having lots of problems, and you've all seen these headlines. It's quite entertaining, quite embarrassing, but a lot of this is companies who are deploying LLM-powered applications are deploying them in not very risky scenarios just because they're not confident enough to deploy them where there are real risks in place. There seems to be a problem, which is, according to AISI’s research (and someone please tell me if this is wrong), but it seems that LLMs just architecturally are fundamentally vulnerable to prompt injections and jailbreaks. We could get better against it, but it doesn't seem this is something that you can completely solve.

[2:04] Just to talk through why this might be a problem, if anyone doesn't know, this is someone on Twitter, sorry, X, who does some amazing exploits. This enterprising person managed to plant an attack on a GitHub page that they knew was going to be scraped by one of the labs. That got into the training data, and then they showed the model later that basically they’d planted their backdoor where if you said the right magic words, you could get the LLM to produce the lyrics of the rap song "WAP". It is a lot of fun. But what this shows is basically that all untrusted third-party data is now executable malware. Any web page on the internet, any document, anything like that, could contain a prompt attack or jailbreak in some form. If you're deploying any LLM-based application where you don't know, you don’t trust the data going in, you have a problem because you can be hacked.

[3:01] This is where we step in. This is grossly simplified, but we basically—regardless of what LLM you're using, we basically monitor everything going into the LLM and everything coming out of the LLM at low latency, and basically scan it for any prompt attacks and jailbreaks coming in, as well as anything bad coming out. This also includes things like leaking of sensitive data, content moderation, but also guardrails, making sure the application does what it's supposed to do. This gives our customers visibility, protection, and control, and enables them to actually deploy these applications to their customers. I won’t go through this now, but this gives you an idea of lots of companies deploying LLM-based gateways, and we plug into that, and so we’re screening all the reference data. Actual agents that are calling actions, we can also screen those to make sure the action the agent is taking is compliant with the system instructions, the user instructions, and hasn't been manipulated or hacked in some way.

[4:03] For those who don't know, we have Gandalf, which is a prompt hacking game where you can learn how easy it is to hack LLMs. We find that 10-year-olds are very good at this, and what this has taught us is basically everyone is a hacker now. It can be in any content, and it's constantly evolving. It turns out that millions of people are able to do this. Companies that are at the stage of building conversational AI are exploring with agents, but the next stage is inevitably going to be what we call the Internet of Agents, which basically means when there’s agents running around everywhere and they’re interacting with each other, then the agents can hack each other. This is the future that we need to prepare for even if we put aside catastrophic risk for a second. Suddenly, as a cybersecurity, this becomes a very difficult problem.

[4:53] I’ll just end with this: if you want to play Gandalf, you can play here. If you want to link with me there. We are hiring, so if you want to build actual AI control in production for real applications, please reach out to me. For anyone who wants to build a company, also talk to me because I've been building startups for a while and might be able to help. Thank you very much.
