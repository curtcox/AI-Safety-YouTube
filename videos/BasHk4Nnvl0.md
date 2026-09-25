---
id: "BasHk4Nnvl0"
title: "Alex Tamkin – Measuring and Improving Human Agency in a World of AI Agents"
url: "https://www.youtube.com/watch?v=BasHk4Nnvl0"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 337
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Alex Tamkin – Measuring and Improving Human Agency in a World of AI Agents

[Watch on YouTube](https://www.youtube.com/watch?v=BasHk4Nnvl0) · FAR․AI · 2024-09-10 · 5:37

## Description

```text
Alex Tamkin from Anthropic presenting 'Measuring and Improving Human Agency in a World of AI Agents'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Preserving human agency in AI integration
- Implementing scalable oversight of AI agents
- Managing the delegation of control
- Ensuring the ability to reclaim control from AI systems

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Today I'm going to be talking about not a new research direction or one that we have actively done work on, but one that I think is exciting, under-invested in, and that I'd love to chat with you more about. First off, I work on the Societal Impacts team at Anthropic, and to give you a little bit of background, we're a technical team that works on a range of sociotechnical and policy-relevant questions, ranging from the risks of discrimination in language model decisions, to more participatory learning algorithms, evaluating things like persuasion and elections integrity, and then doing things like red-teaming. But I think the broader context that we're in as a society today, looking forward across the next few years, is a world with lots of uncertainty about how AI will develop and its risks. But I think there's a lot of worlds that people tend to worry about that all start looking somewhat similar. And they start looking like a world where models are increasingly integrated into the economy, and cause the world to change quickly and increase in speed and complexity in a way that makes it harder, a little bit at first and then more as time goes on, to understand what's going on.

[1:22] And to make that a little bit more concrete, right now lots of us use autocomplete systems for writing or for coding, and these are fairly straightforward to understand and operate. We hit tab, we look at the completion, we make sure that we understand it, hopefully, before moving on. But we're starting to see glimmers of a world where you have coding agents that go off and accomplish, at first small tasks in the world, and now, maybe increasingly larger ones and more ambitious ones over time. And you might imagine that once that works well, you might see much larger numbers of agents working in a code base, and now it's really hard to keep track of what a bunch of these different systems are doing. And I think this could lead to problems even without any risks of misuse, misalignment, or models that are individually more capable than human experts.

[2:22] I think what's key here, and what I'd love to study more of, is human agency; how we can enable and maintain the ability of people to control, intervene, and make informed decisions on the direction of the world around them, starting from the work that they do. More simply put, it's about who is in the driver's seat when we're thinking about people and their relationship with technology. This, as David mentioned earlier, is not unique to AI. It can manifest in really small ways like in individual deployments, say, of self-driving cars, and people's attention and how much they delegate to that system, as well as potentially large ways about systems that are integrated much more broadly into the economy. And so I'd love to chat and think more about how we can measure and improve human agency in a world of increasingly capable AI agents.

[3:17] To make that a little bit more concrete, because it's a big general question, I'll grind it out in two potential directions. One is thinking about scalable oversight of many fast agents. Typically in scalable oversight we think about understanding a model that is much more capable than the overseer, one that is much more complex and harder to understand. But I think even if you can understand each of these individual agents, it might be really hard to understand a virtual organization made up of a wide range of different agents, each doing a bunch of specialized things at the same time. And there's lots of work related to this in HCI (Human-computer interaction) and human factors and in thinking about how people can supervise swarms of agents as gauged by their speed, the number of agents you're trying to supervise, and the task - you could actually come up with concrete evaluations for this.

[4:09] And then maybe develop better interventions, whether they're visualization interventions or training interventions or even better educational methods for doing oversight better. And another direction is thinking about delegation of control. Under what conditions do people give over control of various sorts to AI agents in different settings, right? This is related to how good the model is actually at the task, the risk of the task, competitive pressures, safety culture, and is related to a lot of ongoing work on overreliance and automation bias. But then, crucially, how easy is it, if necessary, also as David was saying earlier, to take back control if necessary? And we can measure things like human skill decay. How much, if you use an AI writing assistant or an AI coding assistant, does your skill decay over time? Do the institutions adapt and do you get lock-in to particular tools that you use? And can we evaluate this and can we actually start to get concrete numbers here and better insights? And then build better algorithms and institutions where taking back control - if necessary - is easy.

[5:27] So thanks so much, and I'm excited to chat with you all about this.
