---
id: "4v3uqWeVmco"
title: "Richard Ngo – Reframing AGI Threat Models [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=4v3uqWeVmco"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-17"
duration_seconds: 344
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Richard Ngo – Reframing AGI Threat Models [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=4v3uqWeVmco) · FAR․AI · 2024-12-17 · 5:44

## Chapters

- 0:00 The problem with AI risk
- 0:35 Technical and governance
- 1:24 Technical overlap
- 3:05 Governance challenges
- 4:25 A new framework
- 5:31 Conclusion

## Description

```text
In “Reframing AGI Threat Models,” Richard Ngo suggests defining ‘misaligned coalitions’—groups of humans and AIs that might grab power in illegitimate ways, from terrorist groups and rogue states to corporate conspiracies. This alternative framework shifts focus to the nature of coalitions and their risk potential, whether from decentralization or centralization.

Highlights: 
🔹Misuse vs Misalignment - Distinction not useful on a technical or governance level
🔹Misaligned Coalition - Humans + Als attempting to seize power in illegitimate ways
🔹Small-scale actors - Risks from decentralization support offense, compute controls, and international regulation
🔹 Large-scale actors - Risks from centralization support open source, transparency, and limited government powers

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The problem with AI risk

[0:00] Hello, everyone. So this talk is based on a bunch of research I've done at OpenAI. It's also a talk in the spirit of a provocation. I was thinking to myself yesterday, a lot of people disagree about a lot of stuff, but what's one thing that all the speakers agreed upon? They don't really agree on whether there are three types of AI risk or four types of AI risk, but they all agree that there's at least misuse and misalignment. So you know, misuse—humans using AIs to do bad things—and misalignment—AIs autonomously deciding to do bad things. The question of this talk is what if we just should get rid of that distinction and not use it.

### Technical and governance

[0:36] So I'll make this argument in two steps. Firstly, it's just not actually a useful distinction on a technical level. And secondly, it's not a very useful distinction on a governance level. The ten second version of the argument is something like: right now AIs are tools and humans use AIs. But as AIs become agents, the way that you will misuse an AI is basically telling it to go off and do something autonomously. And the process of an AI doing something in a misaligned way versus a human using an AI for misuse is gonna look identical in many ways except for the very first bit. And maybe that very first bit is just not the main thing we should be focusing on when trying to divide up threat models. Okay, so that's the like 10 second version of the argument. Here's the four minute version.

### Technical overlap

[1:28] You might say, look, sure I agree that in practice misuse and misalignment might lead to many of the same threats, but we really need this distinction on a technical level. We really need to make sure that the work we do focuses on preventing misalignment. But I actually think that if you try really hard to prevent misuse on a technical level, you'll end up doing a lot of the same work that you'd want to do to prevent misalignment as well. So you can see this kind of analogy between a lot of stuff that you have on each side. For example, from a misalignment perspective, you want to monitor AI behavior. But from a misuse perspective, you also want to monitor user behavior and the user interactions with AI. These just aren't that different. Like, a lot of the infrastructure that you need to set up, the monitoring apparatus, is gonna overlap. From a misalignment perspective, you want to detect whether AI are deceptively aligned. They might have points in time when they change their minds and start to pursue a totally different policy.

[2:20] This is a pretty similar technical problem to trying to detect whether an AI has been backdoored. In both cases, there's going to be some set of inputs that's going to lead them to radically change their behavior and do something totally out of distribution. You might worry from a misalignment perspective about steganography, right? AI's passing messages between each other. But this is, in some sense, the technical problem of, “Can one AI give an input to another AI that will lead it to do something bad?” And this is, in some sense, the same problem as jailbreaking, except in the jailbreaking case, it's usually a human giving the input. I won't go through all of these for interests of time, but I think there are these fairly strong analogies on a lot of the technical work that you might want to do in both cases. On a governance

### Governance challenges

[3:06] perspective, I'm going to zoom in on this last one. Rogue AI analogous to concentration of power. What do I mean by that? On a governance level, the problem is that both misuse and misalignment are radically different depending on which actors are doing the misuse. So take the example of bioweapons. A lot of people talk about bioweapons as a misuse problem, right? We release open source AI, terrorists build bioweapons, that's really bad. The problem is that, actually, most of the worst bioweapons are probably built, or in some cases have been built, by military actors, like state level actors, right? And when you start thinking about the problem of bioweapons from state actors, a lot of your conclusions might totally flip. For example, you might want more open source because open source is useful for defense, whereas the state actors that are building bioweapons will have the AIs no matter whether they're open sourced or not, and they'll be using them for offense either way, right?

[3:58] So actually, even something that seems as simple as bioweapons is actually a very different threat model depending on which actors involved are doing it. And similarly, misalignment threat models are very different depending on if your AI is just like on a server in the Bahamas somewhere and it's misaligned versus it's on the servers of an AI company and it's deployed to a million people, versus it's, deployed widely throughout major military. These are all very different threat models for misalignment.

### A new framework

[4:25] Here's my proposal. We define a misaligned coalition as a group of humans and AIs that are attempting to grab power in illegitimate ways. You have a bunch of different types of misaligned coalitions. You have terrorist groups, law breaking corporations, and so on. And most of the time, both for technical and governance work, we don't need to know who's in charge inside that coalition. The AIs might be in charge, the humans might be in charge, nobody might know who's in charge. But we can try and tackle the problem the same, either way. I don't have a clear classification of different types of misaligned coalitions, but I'd flag that they range from small scale actors to large scale actors. If you're more worried about small scale actors, you're really worried about risks from decentralization of AI, whereas if you're worried about large scale actors, you're worried about risks from centralization.

[5:15] I have a story where the Democrats are more worried about the top one, the Republicans are more worried about the bottom one. I don't want AI safety to split too much into two divided coalitions based on this, and so I really want us to notice these two types of divides, and then try and figure out a frame that unifies them and tackles both types of divides.
