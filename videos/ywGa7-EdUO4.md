---
id: "ywGa7-EdUO4"
title: "Aaron Sandoval - Task Decomposition for AI Control [ControlConf]"
url: "https://www.youtube.com/watch?v=ywGa7-EdUO4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-13"
duration_seconds: 327
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Aaron Sandoval - Task Decomposition for AI Control [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=ywGa7-EdUO4) · FAR․AI · 2025-06-13 · 5:27

## Description

```text
Aaron Sandoval presents task decomposition based on factored cognition as a promising AI control protocol that isolates subproblems, making supervision easier and attacks harder to coordinate.

Highlights:
🔹 Factored Cognition - AI control via task decomposition 
🔹 Isolated Contexts - Prevents coordinated attacks
🔹 Monitoring Efficiency - Easier supervision of simpler tasks 
🔹 Complex Task Testing - APPS dataset too simple for evaluation
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:03] Aaron Sandoval: Thank you. Hello everyone. My name is Aaron Sandoval, and I'm going to be talking about task decomposition as a method for building control protocols. There is a subfield of alignment called factored cognition, which is a general approach to solving problems by decomposing complicated problems into little subproblems, solving them individually, and then putting them back together. I think that this is also promising for control. One reason why I think it's promising is that it should be generally easier for our monitors to supervise small, easy tasks than big, complicated ones that they maybe can't grasp. Another reason is attacks that take place in multiple different parts of execution will be harder to coordinate if we completely isolate these contexts. Third, I think this approach is especially promising when we're predicting against attacks on what I call fixed vulnerabilities. These are vulnerabilities where the attack is only delivered in the tokens of the final solution when we accept it, as opposed to attacks delivered as side effects occurring while the model is creating a solution. I call that expanding vulnerabilities.

[1:17] For example, an expanding vulnerability would be in the bash control paper. We'll read about a threat of a model downloading malware while it's solving some other task. Decomposing a task and creating multiple opportunities for that is a little less promising. But for the app setting where we're just worried about a model writing backdoored code, doing task decomposition does not expose these additional vulnerabilities because the attack can only happen when we accept the final code. This has led me to design a family of control protocols illustrated here. We have a root task which is fed to a decomposer. This could be a trusted or an untrusted model. The decomposer produces a set of child tasks and some sort of logic which will take the solutions to those tasks and form the final solution. If we use an untrusted decomposer, then we'll have some sort of monitoring or editing to check the decomposition itself that that isn't compromised. Then each child task, we feed them to some other protocol and solve them all in totally isolated contexts, then take all the solutions, reassemble them to produce our solution.

[2:33] So far, I've been doing experiments using trusted decomposers and trusted monitoring to implement the child tasks. I'm also assuming high-stakes control, so the red team is using rare attack strategies. Right now, I've just started red teaming, so it's too early to show any good safety results, but some of the red team, blue team tactics that I’m exploring, blue team can change the granularity of decompositions, so creating like two child tasks versus five at a time, and also doing data validation in between child tasks to catch some attacks before they make it through the full chain of logic. The red team will have to change how they pick when to attack to account for the fact that they no longer have visibility of the actual vulnerability that they're trying to target.

[3:28] Here’s some of the usefulness-related results that we have so far. Here we show a comparison on the APPS dataset of just accuracy when we use simply a trusted model to directly solve the problem versus when we go through this decomposition step. There are two main takeaways from these results. One is that decomposition degrades performance across all these models. This is not that surprising given the second conclusion, which is that for our smartest models here, this benchmark is near saturation. This means that this task is just too easy for decomposition to be very useful. We expect decomposition to be best for really hard, complex tasks that are difficult to solve in a single pass. We need a different, more complex setting to properly evaluate the usefulness of these protocols.

[4:26] What are some of the takeaways we can take so far? One, viability depends on usefulness not getting degraded by decomposition. I think it's promising that this will be the case for complex tasks, including a lot of things that we really care about in the future. Two, these protocols are most promising against threats to fixed attack surfaces, where the attacks are delivered in the final solution, as opposed to via side effects. Third, we need more settings. APPS is too easy to properly evaluate these protocols, and future research should be directed towards this. Thank you for listening. You can follow this QR code to find my slides, this poster, the code, and within the next few weeks, I'll be making a blog post with lots more detail about the research so far. Thank you. [Applause]
