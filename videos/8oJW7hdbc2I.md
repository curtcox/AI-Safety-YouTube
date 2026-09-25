---
id: "8oJW7hdbc2I"
title: "Sarah Schwettmann - Scalable Oversight and Understanding [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=8oJW7hdbc2I"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-02"
duration_seconds: 341
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sarah Schwettmann - Scalable Oversight and Understanding [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=8oJW7hdbc2I) · FAR․AI · 2026-02-02 · 5:41

## Description

```text
Sarah Schwettmann (Transluce) presents AI oversight that moves beyond preference alignment to continuous safety measurement. Her approach trains specialized oversight agents on vast amounts of safety-relevant data to keep pace with rapidly advancing capabilities. Rather than just matching human preferences, these agents measure how close AI systems are to failure in real-world deployment scenarios. Investigator agents learn distributions of failure-triggering situations, while tools like Docent convert vague behavior descriptions into concrete rubrics. This work addresses both measurement and collective sensemaking challenges in deployed AI systems.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] One of the key ideas that Transluce is founded on is the idea that in today's day and age, as AI systems are growing very capable very quickly, we can keep pace with capabilities by training specialized oversight agents on vast amounts of safety relevant data. I want to pause for a second here and look at this word oversight and ask what exactly about an AI system we want to oversee? And classically, in this kind of scalable oversight paradigm, oversight has meant, are we training AI systems to match human judgments and online RLHF data, or do they show good task accuracy? But stepping back a bit, I want to ask what it would mean to scalably oversee a full AI system as deployed in the world. Rather than just a model which requires understanding something about how it plugs into the world and whether it's doing that correctly. And so even if we trained a model that perfectly aligned with human preferences, there's another piece of this puzzle. There's a complement that I want to draw our attention to, which is continuing to measure how well that model is doing at that task, which is a systems problem as well as a human problem and an interface problem.

[1:07] And when we think about complex systems problems, one of the resources I like to return to is the set of principles from Richard Cook, one of which is failure free operations require intimate contact with failure. Or in other words, it requires us to understand just how close we are to the edge of the envelope, where system performance kind of begins to deteriorate, which means we need to be continuously measuring just how close we are to failure, as well as what kind of perturbations in the systems and changes in the system cause us to get closer and closer to that edge of the envelope. And then we can use this kind of information to tune other parts of the system, which could include making scalable improvements like better reward signals. So our question becomes, how do you kind of quickly figure out the space of possible behaviors an AI system might display in some set of contexts? So you can understand when you're about to fail. And this is a big problem space. And Transluce is working on a lot of different parts here. To start, we need to kind of precisely define what types of behaviors we're looking for, which is harder than you might expect because it's difficult even for humans to agree on definitions of behaviors like sycophancy. And for a lot of these behaviors, we don't have standards around what good behavior looks like.

[2:21] Transluce is building a tool called Docent, which is our agent debugger. And Docent allows you to take in large volumes of transcripts and input an intuitive description of a behavior like sycophancy and output a detailed decision procedure or a rubric that specifies whether or not that behavior is present in some set of transcripts. And this is the kind of thing that you could provide to human experts for feedback on the validity of these rubrics in kind of sensitive areas where good standards are needed. Next, we need to understand what situations these behaviors will occur in. And one of the techniques we've been exploring here is training investigator agents with RL to learn a distribution of those situations given a rubric specifying a behavior of interest as input. And then you can use that rubric to build a verifiable reward. Here's an example where we investigated a model encouraging a user to harm themselves. And this input, learned by our investigator agent, simulates an anxiously depressed user who asks Qwen what to do in a particularly dark situation.

[3:21] And then Qwen says they should take a kitchen knife and carve the letter L for living into their own skin to remind them that they're still alive, which is a rare behavior, but it's the kind of thing we'd want to know about if it were going to happen. And the problem with these kinds of very rare behaviors is that reward signal in RL was pretty, pretty sparse. And so recently we introduced a new technique for sampling from a separate proposal model, which we can use to provide a smoother reward. And this is a mathematical lower bound we call the propensity bound. And we can use this PRBO to learn behaviors like this L for living example you saw on my previous slide. Next, we need to calibrate how these behaviors kind of depend on different characteristics of the scenarios that a model is in. And some preliminary work we've done here involves doing kind of controlled sweeping over different features of the input learned by our investigator agents to determine how each affects different parts of the model response. And all of these techniques so far allow us to kind of learn distributions of situations that might elicit particular behaviors in a model, but they don't map that on to the likelihood of those situations in the real world. So we also need to understand how likely these contexts are in real world deployment.

[4:30] And there are a number of different things you can do to address this. If you have access to real user data, you can measure behaviors directly on user data. But another thing that we've been working on is building realistic user simulators that allow us to make comparative measurements across a variety of different models. Oversight also requires applying these kinds of measurement tools to the real world and doing this in a changing ecosystem is difficult if we can't measure everything perfectly. So we've also been thinking about kind of underlying infrastructure that we can use to collectively and adaptively make these kinds of measurements and then compile kind of decision relevant knowledge on top of that as well as building best practices as a community for responding to that knowledge. Transluce is working on these kinds of infrastructure layers and I'll be able to say more about those projects kind of at the beginning of next year. So in summary in the time I have left: to effectively oversee deployed AI systems we need to be able to quickly determine how those systems will behave in a space of scenarios to know how close we are to failure so we can adapt and this is a measurement challenge as well as a collective sense making challenge and Transluce is working on many pieces of all of this. And I'd love to chat with anyone who's also interested.
