---
id: "KHgumhNtPmY"
title: "Alan Chan - You Should Work on Agent Infrastructure [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=KHgumhNtPmY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-07-01"
duration_seconds: 256
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Alan Chan - You Should Work on Agent Infrastructure [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=KHgumhNtPmY) · FAR․AI · 2025-07-01 · 4:16

## Chapters

- 0:00 Introduction
- 0:35 What is alignment
- 0:53 Why agents might not be aligned
- 1:40 Backup plan
- 2:33 Agent ID

## Description

```text
Alan Chan argues that modifying the environment where AI agents operate, through tools like agent authorization signatures, provides safeguards against the inevitable limitations of AI alignment. 
Highlights:
• Agent infrastructure changes environment, not the agent
• Agent IDs create accountability and audit trails
• Competitive dynamics may hinder alignment efforts
• Generalization failures challenge alignment in deployment
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:05] So, the goal of my talk is very simple, it's a bit for you to work on or at least think about agent infrastructure. Oh, I guess I should say, I'm Alan, I'm from the Center for the Governance of AI. We're an organization that governs AI, as the name might imply, so let’s get right into it. So first, you know, we're all here at the Alignment Workshop, so presumably at least some of us care about what alignment is. I'm going to–so, one way to think about alignment is it's about changing the behavior of the agent itself for safety reasons, or to get better outcomes.

### What is alignment

[0:35] Just to pick two big, really big examples that people work on. People do alignment, like train agents to better follow human preferences or instructions. A lot of people also think about interpretability, which is getting agents or models to, I guess, try to understand the problems that may occur in agents or models and fix them.

### Why agents might not be aligned

[0:54] So, I think alignment is an important and necessary part of the portfolio. Unfortunately, I don't think it's going to be enough in practice for a variety of reasons, agents, when you actually deploy them into the world, might not actually be aligned. One reason is generalization failures. So, when we actually deploy agents, the training techniques that we use might not actually generalize to novel deployment environments. And this seems especially plausible if agents are going to be interacting with a bunch of different things in potentially long horizon situations that developers can't really predict beforehand. Another reason why alignment–why agents might not actually be aligned in practice is because of the competitive dynamics. So, companies might not actually put in enough safeguards to make agents aligned, they may actually just want to push capabilities and release systems before they're deemed safe enough during development.

### Backup plan

[1:41] So, I think we need a backup plan just in case agents when they're actually deployed in practice, are not aligned. The backup plan that I'm going to propose is that we change the environment and not just the agent. The intuition here is that agents actually take actions in the world, unlike chatbots, whose behaviors are mediated through users. So, just as a concrete example, for an agent to actually scam somebody on the internet, the agent actually has to take actions on the internet, interact with that user or the person that's being scammed, facilitate the transfer of bank account information or amounts, stuff like that, right? So, the agent actually has to act in the environment. This means that the environment is a way for us to– is a lever essentially, for us to affect the behavior of the agent. So, hypothetically, if actors just refuse to interact with that agent that wants to scam people, then that agent just has no effect on the world. So,

### Agent ID

[2:34] that's the intuition, I'm going to call tools that change the environment and not just the agent, agent infrastructure. What's an example of agent infrastructure? One example is agent IDs. So, very simply, an ID is just a container of information that is relevant to an agent. For example, whether a real-world human has authorized the agent to act in a particular kind of situation. Why might this be useful? Well, I expect in the next few years, a lot of digital platforms and websites are going to want this kind of system to disincentivize illicit activity or scams or otherwise activity that platforms don't want. And the reason is that IDs form a sort of audit trail, and allow you to hold the person accountable or a particular actor accountable that is behind the agent if things go wrong. How do you actually enforce this? I think this is an important open question. One thing that companies like CloudFlare are trying right now is, basically quasi-adversarial methods that try to weigh lay agents, if they try to access a website. So, these kinds of anti bot techniques could be repurposed to demand both agent IDs and other forms of infrastructure.

[3:37] So, you could imagine that as a platform or a website, I'm going to use this anti bot software to block all agents unless they provide a valid ID. So then I have this audit trail that I can use. That's just one type of agent infrastructure, there's a lot of other agent infrastructure that we talk about in the paper, so there's—you can access the paper on the URL right there. That's the talk. Please, if you're very interested in agent infrastructure, come talk to me, I’m very interested in connecting you to other opportunities in the space, and other things you could work on. Thank you for your time.
