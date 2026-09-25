---
id: "MAEwp8oolsc"
title: "Sheila McIlraith – Formal Languages to Encode Reward Functions & More [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=MAEwp8oolsc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-02-12"
duration_seconds: 405
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sheila McIlraith – Formal Languages to Encode Reward Functions & More [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=MAEwp8oolsc) · FAR․AI · 2025-02-12 · 6:45

## Description

```text
Sheila McIlraith from University of Toronto presented “Formal Languages to Encode Reward Functions, Instructions, Preferences, Norms, and Advice,” advocating for formal languages in encoding clear, precise AI instructions. By using formal languages, like linear temporal logic, we can provide AI systems with a more structured, sound framework for following complex and safety-critical instructions.

Highlights:
🔹 Precision in Safety-Critical Settings – Formal languages allow unambiguous, computer-interpretable instructions
🔹 Handling Complex Tasks – Formal encoding can sequence multi-step actions, reducing risk in real-world scenarios
🔹 Reward Machines – Using automata and logical representations to model goals and rewards in AI tasks

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Hi, everyone. I'm Sheila McElwraith and this is my talk. It seemed years ago that this dream that we would be able to communicate with our computers in natural language was elusive. But now, suddenly, it's attainable. Enter LLMs. And indeed, I think it is the case that, for the most part, we will communicate with our computers using natural language. That notwithstanding, I wanted to make a pitch for formal languages. In safety critical systems, when we need to be precise, we need to be understood, in cases where we want to do sound reasoning, and a myriad of other cases, including this aspiration of provably safe AI. I think there's a role for formal methods, and for formal languages, and I want to hopefully convince you of that a little bit today.

[0:52] Enter formal languages. What do I mean by formal languages? I'm casting the net very broadly. I mean mathematics, music, programming languages, knowledge representation languages that have been part of traditional AI, logic, linear temporal logic… any language that has a formal syntax and semantics and that is used for a diversity of reasons like that. So what are some of the affordances of a formal language? It has a well defined semantics, so it's unambiguously computer interpretable. It typically has compositional syntax and semantics, and that's really important for being able to exploit it for learning. Some languages are declarative. That means that they make statements like linear temporal logic: you can write sentences in the language and you can reorder them, and the meaning is preserved, unlike the way that we speak in natural language.

[1:42] And generally they have some sort of a “proof system”, and I use “proof system” in quotes to mean, some sort of system for sound reasoning, like calculus or linear algebra, there's some mechanism for being able to make inferences that are sound with respect to the formal language. Importantly, formal languages are a gateway to a set of established methods that I think are really going to serve us well in our mission of AI safety. We can reason about theories like physics and chemistry, music, using formal languages, using arithmetic, calculus, stoichiometry, logic. We can use formal methods, techniques for formal verification, and also for automated synthesis, correct by construction, correct by design. And finally, we can use techniques from AI knowledge representation and reasoning, where we really try to model the world and do things like default reasoning, common sense reasoning, deontics, probabilistic relational models. There are a lot of tools that are available that if we are using formal languages, we can really help with our mission.

[2:36] Importantly, it's a tool, potentially, in this mission of a provably safe AI. For the rest of this talk, I'm going to show you a little example of something that we've done using formal languages, and hopefully convince you of its use, but I only have two minutes left, so I'm going to be quick. So imagine you bring a robot into your home, and you want to be able to advise and instruct it, and you hopefully want to be clear about what you want it to do. In a reinforcement learning setting, unfortunately, the way that you do that is typically using a reward function, which is really just a mapping from the state to some real number. It's pretty impoverished. So what actually happens in practice, because it's really hard to do reward specification, is some poor graduate student writes a big, long Python program to generate the reward function. And of course the other challenge to RL in the real world is sample efficiency.

[3:27] It's really hard, you need billions of interactions to ever learn anything. Some typical things that we might want to represent are preferences, norms and goals. Many of these things are temporally extended and they are often conflicting and they need to be interpreted in different ways. Make sure the bath temperature is between 38 and 43 Celsius immediately before letting someone enter the bathtub. Do not vacuum while someone in the house is sleeping. Always serve the person who has been waiting the longest. When assisting someone from a car to the sidewalk, please always open the car door closest to the person, help the person to stand up, move them beyond the car door, close the car door, and walk them to the sidewalk. This is important because it's an instruction; it needs to be completed in its entirety. If you do half of the instructions, you shouldn't get half of the rewards. You don't want to leave somebody catastrophically in the middle of the road. Very important. So how do we communicate these things to our RL agent?

[4:21] Using formal language, not surprisingly. And in particular, I want to advocate for linear temporal logic, which, for those of you who know it, is a propositional, modal logic that has temporal modalities like next, always, until, and eventually. It allows you to put constraints on the evolution of a trajectory. For any token or trace, you can put constraints on that trace to control the evolution, or to check that the evolution has a particular property associated with it. Importantly, it can be translated into automata. And that is what we're going to do: we're going to represent these things using automata. And we're going to do that by exploiting Chomsky's Hierarchy. The beautiful thing about formal languages, is that they can be captured by representing automata, from finite-state machines all the way up to Turing machines, which is a really beautiful property.

[5:17] So we've done some work in reinforcement learning where we've used this “automata as a normal form” representation and use counterfactual reasoning to do really great work. In particular, we've done this thing called reward machines where we've represented the program as an automaton, our reward function is an automaton. And we've done really great work where we've gotten great results, great sample efficiency and the secret sauce was that we were able to exploit function structure.
