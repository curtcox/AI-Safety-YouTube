---
id: "rIrVH68_kpA"
title: "David Krueger - Sociotechnical AI safety"
url: "https://www.youtube.com/watch?v=rIrVH68_kpA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 348
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# David Krueger - Sociotechnical AI safety

[Watch on YouTube](https://www.youtube.com/watch?v=rIrVH68_kpA) · FAR․AI · 2024-02-08 · 5:48

## Description

```text
David Krueger - "Sociotechnical AI safety."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Great. With apologies to people who have seen me present similar things to this and wanted even more technical talks, I've been happy to see some of the non-technical ones. Yeah, so AI safety is not purely a technical problem. I think it's important to remind us of this. One reason is that safety is expensive. So like John was talking about, for instance, if we want to keep a human in the loop, that's going to get really, really hard, really, really expensive. Another reason is that safety is really a common good. So there's not a proper incentive to invest sufficiently in making your system safe when safety means existential safety, reducing the risk of human extinction. Alignment itself does not solve these problems, as I'll talk about later. And I think right now a lot of the work, even though I've been really happy to see how much work there is happening now on the technical side of this problem, is kind of pretty focused on LLMs.

[0:55] But I think we know that that's not what the future is going to look like. At least, I expect we're going to see very big, significant changes. At least people are trying to build agents. But yeah. So let's jump into the actual content here. This is a very old slide. But the point here is that I think in general we can expect some sort of tradeoffs between safety and performance. And in the blue here, you have what I think are some axes of tradeoffs that are likely to persist. Oh, that's where I should be looking to see my own slides. Great. So yeah, like the human in the loop one, that's a great example. A lot of these, you know, people nowadays are talking about this in terms of an alignment tax. I hate this term. I think it assumes that you can pay the tax and then your system is aligned. And also people have started saying, oh, sometimes there's a negative alignment tax. But that doesn't really consider all of these axes of tradeoffs, a lot of which are actually about like assurance and knowing that your system is safe. So I called out this human in the loop one in particular because, again, I'm kind of some of the context here is that I've been noticing that I have a lot of disagreements that are hard to pin down with people in the safety community, even people who have been in the community for a long time. And I'm trying to articulate some of those.

[2:00] So like this hardware overhang idea is used as an argument for why we shouldn't pause or slow down because then at some point, you know, we'll speed up again and there'll be this all this hardware that all of a sudden things will get really fast - will get really good really fast. We won't have had this like gradual takeoff in time to sort of understand how these systems work as we develop them. But the thing is, at some point we are going to hit the human out of the loop overhang. And that's going to like completely dwarf this hardware overhang in my mind because we're talking about a difference between milliseconds or whatever versus the weeks that you take right now to discuss your results with your colleagues and makes decisions as an organization. And so that's going to just be an incredible cost if you decide to be responsible and actually think about what you're doing instead of just plugging the AI back into itself and asking it to essentially do something like recursive self-improvement. Why is alignment not a solution? Well, suppose that everybody woke up like a thousand times smarter tomorrow. What would happen? I have no idea, but we can't imagine that our current governance and norms would be sufficient.

[2:55] A lot of people would probably start to immediately exploit flaws that currently are not exploited because people are just kind of cognitively limited. Maybe a more modern version of this thought experiment is like what if Sam Altman wakes up a million times smarter tomorrow? So this is kind of the difference between user alignment versus developer alignment. And neither of these I think is really going to solve the problem, right? Because in one case we have extreme concentration of power. In the other case, we have maybe something that looks a little bit like anarchy. Although if it happens smoothly enough, maybe we will in fact be able to adapt our norms. Here's another argument for why alignment isn't good enough that I call the ditch of danger. So basically when your system isn't that well aligned, you don't even have incentives to deploy it. As it gets more aligned, all of a sudden it starts doing a bunch of useful things, but it's still not doing them perfectly, we still don't know how it's doing them, it's still not actually trustworthy. But there's a huge incentive to deploy it, again, because of this thing where the existential risk is an externality and existential safety is a common good. So, if I can make a billion dollars and my system has a one in a million chance of destroying the world and killing everybody, I mean personally I want to say I wouldn't do it. But you know, if systems like that exist, we're probably all going to die very quickly. So finally this is on this point about LLMs versus what the future will actually look like. I apologize for putting a terminator on this slide. But yeah, I think what I expect to happen is primordial soup.

[4:08] Sort of like Irina said, but with lots of aspects and components. Not just LLMs, but things like physical systems and distributed networks. And basically if we look at how software works right now and how the internet works right now, to me it looks kind of like a big mess. And there's a lot of like people plugging stuff together in a way that is unprincipled - components that they don't understand, and a lot of interactions between different people and different organizations where of course I don't understand what this thing is that I'm interacting with because I don't even control it and a lot of the parts are hidden from me. And so I think this is what we're sort of on the path towards, is a situation where we're doing this with AI and plugging it into everything. And it's just going to be kind of a big mess where all sorts of things can pop out of this. Including for instance, ways of solving the problems that LLMs can't solve. So they actually have some limitations around some things. Like this reversal curse, and planning, and stuff like that. And those could be surmounted.

[5:05] Great. So I'm going to go a tiny bit over. Basically almost all the work that people usually talk about in technical work is in this first category but I think we should be doing a lot more work that's trying to support governance. And actually the FATE and the AI ethics community have a lot of relevant expertise here. And as far as I can tell nobody in our community actually really understands that community very well. So we should work on that. Yeah. It's a structural problem. And we've had scientific consensus about climate change for roughly 40 years and look at where we are. We still don't have scientific consensus around AI safety. So like we're very behind schedule. Very, very, very, very, very behind schedule. We may need to forgo AI to a significant extent for a long time. We should start preparing for it now. Thanks.
