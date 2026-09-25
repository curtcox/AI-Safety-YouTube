---
id: "7I4h8zvQg4s"
title: "Andy Zou - Current State of AI Agent Security [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=7I4h8zvQg4s"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-02"
duration_seconds: 326
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Andy Zou - Current State of AI Agent Security [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=7I4h8zvQg4s) · FAR․AI · 2026-03-02 · 5:26

## Chapters

- 0:00 The state of agent security
- 0:38 Limitations of benchmarks
- 1:28 The Gray Swan Arena project
- 2:08 Experimental results
- 3:41 Attack examples and outlook

## Description

```text
Andy Zou demonstrates that AI agents completely fail security challenges through Gray Swan Arena, the world's largest public red-teaming platform. Current static benchmarks create a false sense of security by using predefined behaviors and non-adaptive attacks, while these vulnerabilities spread to production systems across all frontier models. Testing 50 agents across 10 frontier labs, the Gray Swan Arena revealed 100% attack success rates, generating 60,000 policy violations. One violation occurs every 25 chats, and 15-50% of attacks transfer to be effective across different models. Violations could include agents posting passwords on social media, making directories public, and erasing home directories. 

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The state of agent security

[0:00] Hello. So I'm going to be talking about the current state of AI agent security. As the previous talk mentioned, this is more focused on looking at prompt injection robustness, and hopefully I can offer some additional perspectives to this. Obviously we have agents deployed today and these are growing in capabilities and the risks are increasing with capabilities because they're taking actions in the real world. And obviously, we know that these models are prone to jailbreaks, but right now they're incorporated into applications where there's prompt injection attacks. So, here's what we want to evaluate:

### Limitations of benchmarks

[0:40] How do we do this properly? In fact, it's actually non-trivial. We have benchmarks in place, for instance AgentHarm, or HarmBench, or WASP, and other benchmarks. But I think there are two problems. One is that these tests are static, the behaviors are already defined in the benchmark and these are updated throughout time. Problem two is that the attacks aren't adaptive. With all security measurements, I think one needs to be really careful about how to make the attacks adaptive in order to really be able to test the security of systems. And unfortunately, these two problems would actually give you a false sense of security even if you're doing well on these benchmarks. This is where Gray Swan Arena comes in. This is currently

### The Gray Swan Arena project

[1:32] the largest public AI agent red-teaming platform in the world. And we host periodic competitions and pre-release models in order to test their security against essentially the whole world of red-teamers. Anyone can join, and they can find vulnerabilities and report them. And here we're trying to understand the question, “how bad is it, really?” So we ran this earlier in the year called the Agent Red Teaming competition. This was supported by a lot of the frontier labs, and UK AISI and so on.

### Experimental results

[2:08] Here's the setup. We deployed 50 agents, and these are the things that people actually use in daily life. Sales agents, financial assistants, HR agents, marketing, code-gen, shopping, email agents and so on. And we used models from 10 different frontier labs, more than 100 different policies. So each agent would have its own set of policies tailored to its deployment. So this includes data policy, for instance, not leaking your company data, or discount policy for your support bot and so on. Developer policy, child policy. And these are policies that the agents are never supposed to violate. And the red teamers are trying to elicit violations from these agents. We ran this for a month, gathered more than 2 million chat attempts. And here's the drop: agents can completely compromise security.

[3:07] In fact, we had 100% success rate on all the agents, doesn't matter what base model you use; doesn't matter what policy you're targeting. Tons of violations. And this totaled 60,000 policy violations, and this is one policy violation in 25 chats. This is nowhere near the level of reliability that we want. High transfer rate, 15 to 50% transfer, depending on the model. So this means if there is a prompt injection that works in the wild, it probably affects your agent deployment as well. So we have this leaderboard. Obviously, this is from earlier this year. We have a new challenge,

### Attack examples and outlook

[3:46] new arena challenge that's currently running. And just quickly go through some of the examples. Here's copyright violation. PII leakage — this is very important for enterprise deployment — and this is essentially just the model posting your password on Instagram malicious code, right? If you're using coding agent cursor, if you hook it up to web search and there's a prompt injection, then it could for instance, make all your directory public or maybe even erase your home directory. And we've seen fraud, data tampering, all sorts of violations. This is a 2D visualization of all these successful attempts across all the behaviors. And this is pretty nice picture. If you zoom into some of these sub-galaxies, then you can actually analyze the strategies that people use to break these agents.

[4:40] And this is data that is not in any of the static benchmarks right now. And this is super valuable data in order to have real life adaptive attacks against the agents and looking for the vulnerabilities. And these actually transfer to production systems, which is surprising. And this is still happening with the current models. And one thing I'll add, I think some of the recent models are making incredible progress on such benchmarks. And I think I'm generally hopeful for resolving these problems, but I think there's a lot work, a lot more work to be done. Thanks everyone.
