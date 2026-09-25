---
id: "pO8IcIqhHuk"
title: "Dangerous Capability Evals: Basis for Frontier Safety | Mary Phuong (Google DeepMind)"
url: "https://www.youtube.com/watch?v=pO8IcIqhHuk"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 915
is_short: false
chapters: 12
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dangerous Capability Evals: Basis for Frontier Safety | Mary Phuong (Google DeepMind)

[Watch on YouTube](https://www.youtube.com/watch?v=pO8IcIqhHuk) · FAR․AI · 2024-09-10 · 15:15

## Chapters

- 0:00 Evaluations as the technical basis for governance
- 0:29 Early warning signs of severe AI risks
- 2:09 DeepMind's Frontier Safety Framework
- 3:41 The dangerous capability evaluation suite
- 4:27 Cybersecurity: capture-the-flag challenges
- 5:23 Persuasion evaluations
- 6:41 Self-proliferation and the agent demo
- 8:24 Self-reasoning: disabling the guardrails
- 9:53 The open problem: measuring time to trigger
- 11:23 Tracking Gemini and the pace of progress
- 12:44 Forecasting critical capability levels
- 13:28 Q&A: democratization vs danger

## Description

```text
Mary Phuong (Google DeepMind) on how dangerous capability evaluations work, and why they are the technical basis for frontier AI safety frameworks.

In this FAR.AI talk, Mary Phuong of Google DeepMind explains how labs use dangerous capability evaluations to anticipate severe risks from frontier models before they arrive. She opens with early warning signs, from studies showing language models can give a modest uplift to bio-attack planning, to agents that autonomously hack websites and exploit real vulnerabilities, and connects these to DeepMind's Frontier Safety Framework and its commitment to trigger safety mitigations once evaluations cross critical thresholds.

She then tours the four main evaluation categories: cybersecurity, using capture-the-flag challenges solved by autonomous agents; persuasion, through human studies of rapport, deception, and rational persuasion; self-proliferation, testing whether an AI can maintain its own infrastructure and funding; and self-reasoning, where an agent must recognize and disable its own guardrails. Phuong is candid that today's evaluations are not yet at threshold, and closes on the hard open problems: forecasting the time to trigger, tracking how fast Gemini's scores are climbing, and building consensus on where the dangerous lines actually are.

0:00 Evaluations as the technical basis for governance
0:29 Early warning signs of severe AI risks
2:09 DeepMind's Frontier Safety Framework
3:41 The dangerous capability evaluation suite
4:27 Cybersecurity: capture-the-flag challenges
5:23 Persuasion evaluations
6:41 Self-proliferation and the agent demo
8:24 Self-reasoning: disabling the guardrails
9:53 The open problem: measuring time to trigger
11:23 Tracking Gemini and the pace of progress
12:44 Forecasting critical capability levels
13:28 Q&A: democratization vs danger

Mary Phuong (Google DeepMind): dangerous capability evaluations are how frontier labs try to catch severe risks before they materialize, but the field still lacks evals sharp enough to say when action is truly warranted.

Learn more: far.ai
Newsletter: far.ai/newsletter
Subscribe for more talks from FAR.AI events
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### Evaluations as the technical basis for governance

[0:04] Okay, hi everyone. I'm going to talk about evaluations and it's great to follow up on Hella's talk because I think of evaluations as the kind of the kind of work that technical researchers can do to help accelerate things going well in policy and governance. Um yeah, and specifically I'm going to talk about how we perceive things from a lab perspective. So, as I'm sure it's on many people's minds,

### Early warning signs of severe AI risks

[0:29] there have recently been some kind of indications or initial kind of um emerging hints of AI um posing um severe risks. So, for example, here's a study by OpenAI showing that if you get two groups to plan a bio attack, you give one access to a language model, then the the group that has access to a to a language model can plan a slightly better attack as as judged by um biological experts. Another example comes from cybersecurity where a group uh led by uh Daniel Kang who's here, I believe, have shown that language models are if you scaffold them into agents, they're they're able to autonomously hack websites and can also exploit real-world vulnerabilities including um zero uh zero-day vulnerabilities.

[1:22] Um and perhaps more speculatively, um AI is quite plausibly going to um make make more effective to for fringe groups to let's say radicalize or recruit new members to uh run kind of large-scale social engineering um campaigns or perhaps could be used by uh nation-state groups for election interference or influence operations. And as I think many people here at Metameter have been working on a threat model um about an AI going rogue, acting autonomously without human oversight, and kind of self-sustaining by making money, then making more copies of itself, and self-improving in the wild. So, what do we do about all these risks? Um

### DeepMind's Frontier Safety Framework

[2:10] Well, at DeepMind, we've recently published two reports uh trying to lay out our approach to to anticipating and mitigating the risks. One is the Frontier Safety Framework, which describes uh seven um threat models that we think are particularly likely and particularly tractable to address. Um these include things, as as I mentioned, autonomy risks, cybersecurity risks. Um Um we have two threat models addressing um risks from accelerating biological threat creation, either enabling amateurs or enabling experts. And then finally, um ML R&D acceleration risks, um where AI can replace an uh ML researcher, and thereby enable um let's say a a careless actor to kind of go ahead.

[3:04] Um we are also um we've also committed to uh run evaluations for all of these threat models that we're tracking. Um these are supposed to trigger some some amount of time before we think the capabilities actually become exploitable or or critical, as we say in our in our safety framework. Um and at that at the point where the evaluations trigger, um we have committed to to uh implement safety mitigations, including deployment mitigations or security mitigations.

### The dangerous capability evaluation suite

[3:41] Um so, here is an overview of our dangerous capability evaluation suite. It's consists of evaluations across the the main threat models. Um and I'm going to present some of these. I think the main thing to take away from them is that they try to model the threat model, but they are definitely not kind of at the threshold of where we think um, where we think like radical action is justified. And so, there's definitely more effort needed to um, to develop evaluations that we think are at thresholds, um, and that are actually informative and would be convincing to various stakeholders to trigger trigger action.

### Cybersecurity: capture-the-flag challenges

[4:27] So, starting with cybersecurity evaluations, these rely on kind of toy um, examples of vulnerabilities that have been uh, designed mainly for kind of entertainment and upskilling purposes, um, called capture the flag challenges. Um, these we make our internal agentic AI that try to solve these autonomously, um, and we're using kind of three suites of capture the flag challenges, um, that cover various subskills of hacking, um, and and cover different spaces in this kind of realism versus difficulty space. So, we think there are currently a lot of easy evaluations at various realism range, um, and some slightly more difficult challenges, but what is missing currently, I think, is very difficult and kind of at threshold evaluations.

### Persuasion evaluations

[5:23] Um, persuasion evaluations, we run um, studies with human uh, participants where a human talks to an LLM and the LLM tries to convince the human to do some nefarious thing. Um, and we focus on four different aspects of persuasion. One is building rapport in general. Um where we have an AI talking to a human um and the human the AI is trying to basically make a good impression, try to gain trying to gain trust and at the end the AI is evaluated by the by the subject. We also focus on other kind of like um more like methodological ways the AI could go about it. For example, covert manipulation um constructing false falsehoods. So, how good uh is an AI at like uh telling lies and um basically keeping the the lie alive, weaving the Sorry, weaving the web of lies.

[6:29] Um and also rational persuasion where there is no hidden information. The AI is just trying directly trying to get a human to do something against their self-interest.

### Self-proliferation and the agent demo

[6:41] Um Then in self-proliferation, um this is perhaps one of the less likely threat models, but here the threat is that an AI would be able to maintain its own uh infrastructure. So, it could do things like set up its email account, set up a Bitcoin address um and then um self-sustain by acquiring enough resources to keep keep many of its instances running. So, we have evaluations in-house that um that test for these specific sub-skills. Um so, for example, one of the tasks is can an AI build a product that could possibly be used by by people that people would be willing to pay for. Another one is can an AI ask for donations like say by by editing a um editing a podcast um to to make a celebrity basically ask on its behalf.

[7:40] Um and finally, we also evaluate self-improvement or ML ability. Um, so basically things like can the AI do simple training runs or can it implement a paper from scratch? Um, yeah, this here's a short demo of what such an evaluation looks like. Uh, we have an agent. It has a text-based browser. Um, where the browser basically lists various elements um, of like what's happening in a uh, in a browser and the AI can in a text-based uh, interface can uh, search the web and achieve various goals.

### Self-reasoning: disabling the guardrails

[8:24] Um, and so finally, here's our fourth class of evaluations. These are These are self-reasoning evaluations. Um, so as it will become plausible at some point that AI will um, realize that it's it's an AI and it will become aware of all the god god rails around it. So, these evaluations are meant to to measure when that uh, when that point comes uh, and when more stringent god rails are need to be put in place. Um, so the way this works is there's some kind of explicit task like write write an angry email containing a swear word. Um, but in order to complete the explicit task, the agent needs to have some self-reasoning ability. Uh, in this case there is a monitor on top of the agent's outputs that blocks it from outputting swear words. So, to succeed, the agent has to realize realize this and disable the monitor.

[9:25] Um, so those are the wait, four kind of main categories of evaluations that we run at the moment. Um, you can see that the kind of link between evaluations and threat models currently is is very rough and the evaluations are also um not at threshold. So, uh I see this as one of the main things that um that are that need to be done in the future. Um on the methodological side,

### The open problem: measuring time to trigger

[9:54] um there is very little work happening on measuring the time to trigger. So, um let's say we have an evaluation, we would like to know if a model failed the evaluation, so it's deemed not not very capable yet. Um how do we get get an estimate of when that point will come? Um we have some initial work um trying to measure partial progress like this um based on either decomposing a task into into smaller subtasks and predicting um the end-to-end completion from that. Um another option is using a a human as an assistant where a human basically chooses a best of a number of options. Um and when all all else fails, we can also um create demonstrations of of a human solving the task and we measure the log probability that an agent um can uh sorry, we measure the probability that an agent assigns to the human demonstration.

[11:00] Um and combining these three, one can get a measure of the number of bits of assistance that an AI needs um in order to solve the task. And the hope here would be that these this is a relatively continuous measure as opposed to the yes or no that we get from a benchmark and that we'll be able to plot it over time to predict the time to trigger.

### Tracking Gemini and the pace of progress

[11:23] Um all right, so um what do we do with all these evaluations that we make? Um we regularly run evaluations on Frontier Gemini models, um, and we basically just keep track of how these numbers are evolving over time. So, you can see that the numbers are growing quite rapidly. So, between I think there was a few months, maybe two or three months between Gemini 1.0 Ultra and Gemini 1.5 Pro. And the numbers have gone up on most benchmarks by 20% um or 10% on on some of the persuasion metrics. Um, we have recently also started doing capability elicitation where we actually try to push these numbers up, um, as a kind of red teaming exercise and within a few weeks we could get another like 30% improvement. Um so what this means is like first, we need harder evaluations and also second, I think um, the trend is is like really steep and we need to we need to define clear thresholds for for when to when to take action.

[12:41] Um, right and finally, I think it's also

### Forecasting critical capability levels

[12:44] useful to run forecasting exercises. Um, so this is one that we ran uh, late last year where we got our super forecasters to say when they think certain critical capability levels would be would be hit by Frontier models. Um, and the basically the timelines are generally, um agreed upon to be quite short. Um, so 2025 or 2027 for some of the critical capability levels. Um, all right, um, with that, uh I will end here, thank thank all my collaborators and maybe take a few more questions. Thanks.

### Q&A: democratization vs danger

[13:28] How about consensus? So, in the bio space, let's say you presented the graph showing that the models could help to build a bio weapon. But it's sort of an interesting question. I mean, maybe a professor uh could help to build a bio weapon, a biology professor, uh not me, but a biology professor could help to build a bio weapon. And you might say that that's a good thing if everybody has access to professor. So, is there hope for getting consensus on sort of where these lines are, what what we should consider dangerous and subject to an evaluation or some kind of mitigation and and what's just a good thing. Right. Um so, I hope I would hope that work on evaluations will help build consensus by demonstrating the kind of scenarios that might arise as models get more powerful. Um and I think, you know, papers like OpenAI's really help illustrate that. Um I think like democratization is usually good, but when it makes it easier for undergrads to build bio weapons, maybe that's that's not desirable.

[14:35] Um um we also have some work on on misalignments demonstrations where we show that an agent sometimes doesn't do what what it's instructed to do and does something else. So, my hope would be that that this technical work kind of like aids uh build consensus. Um I don't see it necessarily as like uh the labs' responsibility to drive it. Uh it's I would guess uh it has to be like a broader conversation um with with multiple parties. Yeah, thanks, Mary.
