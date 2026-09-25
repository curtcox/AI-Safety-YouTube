---
id: "Ey2qtSo81Kw"
title: "Max Tegmark - Provably safe AI"
url: "https://www.youtube.com/watch?v=Ey2qtSo81Kw"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 369
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Max Tegmark - Provably safe AI

[Watch on YouTube](https://www.youtube.com/watch?v=Ey2qtSo81Kw) · FAR․AI · 2024-02-08 · 6:09

## Chapters

- 0:00 The vision for provable safety
- 1:09 Formal verification and AI
- 2:38 Black box distillation
- 4:26 Policy and safety regulation
- 5:09 Future directions and hiring

## Description

```text
Max Tegmark - "Provably safe AI"

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The vision for provable safety

[0:04] I'm going to talk about a radical approach to AI safety, provably safe AI. Guardrails try to physically avoid harm, but if you're up against a super intelligent adversary, like Dawn Song was pointing to, or a human using superintelligence against you, trying is not enough. You need to succeed. You really want it to be impossible for the adversary to win. For example, hack the nuclear codes and launch the nuclear war, or create a designer pandemic, or something like that. So I wrote a paper recently with Steve Omohundro on provably safe systems. Not provable in the weak sense of persuading some judge, but in the strong sense of the harm being impossible according to the laws of physics.

[0:59] Because no matter how smart the AI is, it can never violate the laws of physics and do things that are provably impossible in that sense. Now, I predict that formal verification, the quest for automatically proving things about code,

### Formal verification and AI

[1:20] is going to get revolutionized by AI in the same way we've seen happen with so many other things recently. And so is program synthesis. This mathematical theorem just automatically writing code. That makes this whole program more feasible. This is the vision that Steve and I articulated in this paper. So you, the human, write a spec for what you want your AI tool to obey. And then you have this very powerful AI system that creates it meets your spec. You might worry that, oh my goodness, how am I possibly going to be able to trust this AI and its tool and its proof if they're all way too long for any human to be able to comprehend? But here's the really great piece of news to remember here: it is much, much easier to verify a proof than to find it. Just like it's much easier to verify that something you found is a needle than to actually find the needle in the haystack to start with.

[2:31] And you can write a proof checker in the metamath language, which is just 350 lines of Python. It's very easy to understand that. What if your AI system isn't powerful enough to actually

### Black box distillation

[2:41] write the powerful AI tool you want? Then there's another idea. You use a black box AI to really learn to do your tool. And then you exploit the fact that the thing that machine learning really shines at is learning, not runtime execution, where it's just another massively parallel architecture. So that you can then have an AI neuroscientist which studies and manages to distill out the learned algorithms and knowledge from your AI system and re-implement it in some architecture that lends itself better to formal verification. There's a lot of progress in this field of mechanistic interpretability. I think we're going to see this field itself get more and more automated. It's making this more feasible. I'll show you just one little toy example of why this is not actually impossible. This is with Ziming Liu. We are going to machine learn a task. And then we're going to automatically distill out the learned knowledge and algorithm into provably verifiable code. So we're going to take an algorithm you probably all learned in first grade, addition, where the algorithm is to loop over the digits and sometimes carry. We'll do it in binary. So we train an RNN and it totally nails a task. So now you have the algorithm in this black box, but you have no idea what algorithm it actually came up with.

[3:54] We have this fully automated task, I can send you the paper later, which actually studies the black box and produces Python code that implements it. And then we put this in the Dafny formal verification language and prove that this algorithm actually correctly adds up all numbers, not just the one in the training set, but any numbers whatsoever. And we have a much, this is a toy example, but we're publishing soon a benchmark where we apply this to a much broader set of algorithmic tasks. So I think it's actually not impossible. Which means that it's more easily to defend

### Policy and safety regulation

[4:31] this policy suggestion, which I would make, is that AGI without provable safety bounds, without quantitative safety bounds at least, should be illegal the same way that it's illegal in this country to sell drugs if you have no quantitative safety bounds at all on how many percent the people are going to get bad side effects or whatnot. And I think in my remaining 11 seconds, that one of the cool things that will come out of this paradigm is we'll realize that the vast majority of the trillion parameters or so in a large LLM are actually storing facts, as opposed to algorithms.

### Future directions and hiring

[5:09] And we're going to start to learn how we can refactor these LLMs by separating out the small part, which is the algorithms that we want to prove stuff about from these massive databases, which is also great for other kinds of interpretability. We found massive amounts of facts here in LLAMA2, where it stores the whole map of the world. We found also higher level representations stored, like what sentences it thinks are true and false, et cetera, et cetera. And finally, if this is something you're excited about, please come talk to me if you're looking for a job or you know someone who's looking for a job because we're hiring at MIT for this. And also, if you'd like to talk about it more, either provable safety or just more broadly, quantitative safety bounds, we have one of the tables tomorrow and the next step section, where we're going to talk about quantitative safety. Thank you.
