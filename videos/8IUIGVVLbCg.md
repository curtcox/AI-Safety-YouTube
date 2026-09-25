---
id: "8IUIGVVLbCg"
title: "Shane Legg - System Two Safety"
url: "https://www.youtube.com/watch?v=8IUIGVVLbCg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 307
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Shane Legg - System Two Safety

[Watch on YouTube](https://www.youtube.com/watch?v=8IUIGVVLbCg) · FAR․AI · 2024-02-08 · 5:07

## Chapters

- 0:00 Introduction to AGI safety
- 0:20 Defining AGI and safety
- 0:51 Necessary system properties
- 2:31 Intertwining safety and capability
- 3:45 Constructing safe AI systems

## Description

```text
Shane Legg - "System Two Safety."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to AGI safety

[0:04] I've been thinking about AGI safety for a long, long time, 20 years or something or other, and today I want to claim that maybe the best way to build a safe AGI system is to do the obvious thing. And I want you to all come to me afterwards and tell me why this is a terrible idea. Okay, so, a few definitions.

### Defining AGI and safety

[0:22] By AGI, I mean an agent that can at least do the kinds of cognitive things that people can typically do. Okay, a safe AGI, this is a bit more controversial, should be at least as ethical and human value aligned as a competent, highly ethical person. Now, yeah, I know we should aim for more than this, but if you could at least do this, then a competent, highly ethical person isn't going to try to turn the world into paperclips or anything too crazy. So, that's progress. That would be quite good if we could achieve this.

### Necessary system properties

[0:51] So, how do we build such a system? Now, I'm going to think about this a bit like a mathematician. What are necessary properties? What are necessary properties for one of these systems as I've defined it? They're actually quite simple, I think. Property one: a human-level or better world model. So, this is actions, their likely consequences, understanding natural language... You know, general world model knowledge, understanding, understanding people, understanding human values and ethics. Not just the ones we want it to follow, but in general... That's a really important thing. Now, why? Well, it should be fairly obvious. If a powerful agent has a bit of a flaky world model, it's going to make mistakes that no competent person would make. That's not safe. So, you have to have a good world model. Property two, very related to the previous one, you want robust human level or better reasoning. Same kind of argument. If you've got a powerful agent and it sometimes makes reasoning mistakes, that's not safe.

[1:55] Property three, you need to give the agent a clear specification of the values and ethics that you want it to follow. Why is this? Well, think about it. What's the alternative? You have an agent that follows unspecified values and ethics? That's not good. You don't want that. So, we're going to have to tell the agent what values and ethics we want it to follow. Okay. So, we have necessary properties. A good world model. Good reasoning. And specification of the values and ethics that we want the agent to follow.

### Intertwining safety and capability

[2:31] Now, one and two, these are both capabilities. So, there's no separating capabilities from safety. They're very, very intertwined. A safe system has to be a very capable system. And on the third point, in order for the agent to be able to understand the values and ethics, that's a capability. So, capabilities are very important. Okay. Now, if you believe my claim that these are necessary... then all AGI safety plans must solve these problems. You can't get around them. So, it's got nothing to do with my plan in particular, but you're going to have to solve these problems. Okay. Claim One and Two may be solvable to a human level by future foundation models. It's not a given. We'll get there. There's a lot of these talks today that are sort of going in that direction. But it seems plausible to me that in a few years we may be able to get this to a sort of competent human level.

[3:23] And I think Three isn't too hard. If you want fairly normal human values and ethics. Because you're basically pointing to sort of a mode within the distribution with the world model. So, it seems plausible to me that we could satisfy these necessary conditions. So, that's good. That's encouraging. Now, part two. If the three necessary conditions are met,

### Constructing safe AI systems

[3:49] fully met, how might we construct a safe AGI? And to this, I'm going to say... Well, a competent, ethical... Competent ethical people use their understanding of the world, values and ethics, and reasoning to choose ethical value-aligned actions. That's what they do. Now, if this is our minimal target, can we replicate this in a machine? And I'm going to say, well, yeah. We do it in the obvious way. With the necessary properties satisfied, fully satisfied. Because if they're not fully satisfied, this isn't going to work. We can construct an agent that will consistently choose the most value-aligned and ethical action, at least as well as a competent human can. And basically, we just, you know, do the normal thing. We create a cognitive loop that scaffolds the agent to do that. Okay. Now, if you think this is a terrible idea, I want to hear from you. Come and talk to me afterwards and tell me what's wrong with this idea. And, yeah, if you're interested in coming and working on safety at DeepMind, go and talk to myself, or Anca, who will be leading our new team, focused on this.

[4:59] And we're building a new team in the Bay Area. So come and talk to us.
