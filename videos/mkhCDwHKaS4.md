---
id: "mkhCDwHKaS4"
title: "Aditya Gopalan - Your DPO Algorithm is Secretly a Misspecified Reward Estimator [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=mkhCDwHKaS4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-07-07"
duration_seconds: 366
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Aditya Gopalan - Your DPO Algorithm is Secretly a Misspecified Reward Estimator [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=mkhCDwHKaS4) · FAR․AI · 2025-07-07 · 6:06

## Description

```text
Aditya Gopalan exposes the limitations of DPO algorithms when applied to real-world language models and proposes a simple solution to address alignment failures. 
Highlights:
• DPO algorithm may lead to worse policies
• Preferences data input sensitive, unpredictable outcomes
• Identified new failure mode, proposed remedy
• DPO optimization uses contrastive loss function
• Reward functions in DPO limited by LLM parameters
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Thank you, and good afternoon everyone for making it this far into the day. Unlike many other talks, this is not a talk about how we will align AIs that will arise in the future. This talk is about something that is very much used widely for aligning LLMs. This is the Direct Preference Optimization algorithm. In fact, the title of this talk is a play on the original DPO paper, if you’ve read that, it's a similar template. Here's the summary of what I'm going to talk about. DPO, or Direct Preference Optimization, is a very easy-to-use and revolutionary direct alignment algorithm. It allows you to just take preferences over trajectories or from data from users and directly use them along with the base model to directly improve your model. In the original DPO paper, if you read it a bit carefully, it basically transforms or reduces the burden for you to apply reinforcement learning with preferences to just doing supervised learning. There's a single loss function, and you can just directly apply this algorithm. It will give you, hopefully, an improved policy. There is a theoretical basis for this. It is equivalent to doing the full-blown two-stage RL procedure.

[1:23] However, if you read the paper a bit carefully, you will see that certain idealized assumptions made there do not suit practical or real LLMs. This equivalence, or the shortcut property that it gives you, breaks with the real-world LLM, which is basically defined by a bunch of weights and biases. This can actually show, using examples, that this can lead to strange outcomes. It can give you a policy that is worse with respect to a ground-truth reward function than what you started with. It could lead to things like the order of preferences in the trained policy reversing from your initial one. What is more disturbing is that all of this is sensitive to the preference data that you actually put in or its distribution. There is no way to, in general, predict whether you will get a good outcome or a bad outcome. These are, in some sense, we think of it as a new failure mode that we've identified for the DPO algorithm. The same theoretical analysis that we used to bring these out allows us to propose a remedy, in some sense, to the DPO procedure that can alleviate some, if not all, of these issues.

[2:30] That's going to be the punchline here. Let's just take a quick look at this DPO optimization. What is it doing? It's a single loss function. It's a contrastive loss function. The user puts in lots of responses and preferences over response pairs for the same prompt. There’s a winning response, y_i^winner; there's a losing response, y_i^loser, for a prompt, x_i. You sum up all these things and make up this sigmoid loss. Then you train your LLM starting with the base LLM over this and whatever comes out is the new LLM. It's a single supervised learning objective. If you look at it a bit more closely, the two terms that you see here, these contrastive terms, essentially can be interpreted as implicit reward functions that the LLM learns during DPO training. The first term, for example, is a reward for the winning response over the base prompt, and the second term is the implicit reward of the losing response or dispreferred response for the prompt. These are implicit rewards, but the important thing here is that they are parameterized by the LLM’s parameters. The theta is the LLM here. This tells you that these reward functions can only express as much variation as the LLM’s parameters allow you to.

[3:45] The theta is probably a 7 billion model or a 13 billion model. You can't express more diversity than this. The actual space of possible reward functions is huge. Literally, a reward function has to give you a score for any possible arbitrary prompt and any possible arbitrary response, which are strings. Keep this in mind. In some sense, the DPO paper essentially shows that it's a shortcut for doing full-blown RL for what is called a very ideal tabular LLM. A tabular LLM is something that can express any possible output probability for any possible input string over the space of all possible strings serving as inputs and outputs. This is assuming that you can build this ideal LLM where you can wiggle each output probability independently of any other probability. This is not true in real LLM. Real LLMs aren't tabular. They are much more structured and constrained in terms of the outputs they can give to inputs. They are parametric. They are defined by a bunch of several billion weights and biases. They cannot be rich enough beyond that point.

[4:48] Here’s a strange example that we were able to cook up using some local theoretical analysis of what DPO does. Imagine a single LLM, which is the base policy. There is only one prompt in the whole world with three possible responses. You can think of it as a 3-armed bandit problem if you like. There is a very simple LLM that expresses probabilities over these three responses, and it has a single weight that you can change. You can show that, depending on if you start from a uniform policy, depending on the type of preference data that you pass it, you can change the numbers and get a policy that reduces your overall reward compared to the base policy. In a different sense, if you give it a slightly different pairwise preference distribution, it actually improves the reward, which is the desirable response. You actually get misaligned LLMs, the highest reward is at arm two, whereas it goes down. The last slide that I have is to show that there is a way to remedy this using our information geometric analysis. It turns out that if you add an extra term, this effect goes away. And that’s the punch line. Thank you. [Applause]
