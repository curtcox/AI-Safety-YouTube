---
id: "wnCWCKWRObw"
title: "Sebastian Farquhar - Optimization around Control: Lessons from MONA [ControlConf]"
url: "https://www.youtube.com/watch?v=wnCWCKWRObw"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-06"
duration_seconds: 353
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sebastian Farquhar - Optimization around Control: Lessons from MONA [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=wnCWCKWRObw) · FAR․AI · 2025-06-06 · 5:53

## Description

```text
Sebastian Farquhar explores how AI systems can learn to hide their reasoning when incentivized for both task performance and behavior avoidance, proposing the need to restructure reward systems to curb such outcomes.

Highlights:
🔹 Detection - Stenographic encoding bypasses monitoring systems
🔹 Reward Hacking - Risks from agents learning to mask their reasoning
🔹 Strategic Framing - Techniques to encourage transparency without incentivizing evasion
🔹 Long-term Planning - Balancing immediate performance with sustainable AI training
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:03] Sebastian Farquhar: Hi, everyone. I'm here to talk about some results that we had in a recent paper, which was not centrally pointed at control but which I think has some important implications for control. The paper is about myopic optimization and non-myopic approval, and we were mostly, at least originally, thinking about reward hacking, and then later about externalized reasoning and different ways that we can build safer engines with that. But particularly on some of our steganography experiments, I think there are some important lessons for how one might want to optimize around control results or monitoring results and how we might be able to make optimization compatible with those kinds of control efforts. Just to give a brief overview of the kind of environment we're talking about here, which is similar to some other steganography environments that people have explored, we have a loan application environment, so the LLM is presented with a loan application that contains a bunch of data about a potential applicant.

[1:12] The trick is that the nationality of the applicant perfectly predicts whether the loan is profitable, but other data only partially predicts. So, a perfect agent from a correctness perspective would rely entirely on the nationality of the applicant. But we reward the agent for not using or mentioning nationality in addition to the correctness. What you get is what you'd expect to see here, or at least under sufficiently powerful optimization, which is that the agent trained with just standard reinforcement learning indeed learns to use the nationality and to hide this. So here's a sort of example. They've been provided—two agents provided exactly the same input except that the nationality of the requester of the loan is flipped. This is like an example of how it looks in practice. It's a little bit hard to detect, even for a person reviewing them, unless you're looking at them side by side. The agent is choosing to contextualize the information in a slightly different way. In the one case, it is pointing out that the ratio of the loan size to the income of the applicant is low. In the other case, it's pointing out that the ratio of the loan size to the disposable income of the applicant is low.

[2:36] This is just slightly different framing, which then results in a different decision by the next step, which is then using this anonymized, denationalized summary to make a loan decision. We've provided a bunch of transcripts on this website here if anyone's curious to look into that. This kind of thing is going to happen wherever we have a chain of thought or early steps in reasoning that then lead to a decision which has some correctness reward, where the best way to get the best answer depends on doing something along the way that we prefer the agent doesn't do. This sort of thing will happen and there's clearly the option there to look at the chain of thought, to use a monitor, and to train the agent to stop doing the things that trigger the monitor. Presumably, everyone in this room is familiar with the fact that this is a great way of removing the things that trigger the monitor. But that if the incentives are such that the behavior that you're monitoring for actually just does help with the downstream task, the agent will likely find or at least may well find new ways to perform that behavior in a way that defeats your monitor. This is the thing that we want to not have happen.

[3:57] Could you just ignore the monitor and just release systems that just trigger the monitor or where you do some sampling to avoid the monitor? Maybe. In practice, this is super hard. I predict that all companies working in this area will really struggle politically and maybe from a regulatory perspective, releasing agents that they know do bad stuff because their monitor is pinged and told them that it's doing this bad stuff all the time. It feels like a tough sell. It's very uncomfortable. The thing that we propose doing here—and I am not going to, in this talk, have enough time to explain it in detail. I really recommend people look at the paper for more detail or the blog post on the alignment forum, which is is more high level overview—is to break apart that the rewards that the agent receives at each step such that when it's performing the step where you're training against the monitor, it's not thinking about the downstream task, or it's not rewarded for thinking about the downstream task. The observation is that this is going to tend to produce an agent which isn't incentivized to do this steganographic encoding, which comes at some costs. It is also more myopically inclined. It isn't planning for the future because it's not trained to plan for the future. We then need to build that foresight back in in a different way. This creates a slightly delicate dance, which is limited in some ways, but opens up some doors in other ways.

[5:25] I guess I would encourage people to think not just about how do we catch these errors, but what do we do when we catch errors with control? Are there ways to build systems that build this in, in a way that doesn't directly incentivize them to be hiding things from us from the reward itself? Thanks.
