---
id: "zgLfN2h6dyM"
title: "Vincent Conitzer - Foundations of Cooperative AI"
url: "https://www.youtube.com/watch?v=zgLfN2h6dyM"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 326
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Vincent Conitzer - Foundations of Cooperative AI

[Watch on YouTube](https://www.youtube.com/watch?v=zgLfN2h6dyM) · FAR․AI · 2024-02-08 · 5:26

## Description

```text
Vincent Conitzer - "Foundations of Cooperative AI."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] And my lab at CMU is the Foundations of Cooperative AI Lab, or FOCAL. So Lewis set me up nicely. And in this lab, we think about a lot of different things, but we're especially interested in risks from AI interaction - what I'll call here "tragedies of algorithmic interaction". And we're particularly interested in game theoretic tragedies. Like, you might have heard of the tragedy of the commons. The tragedy of the commons is where you have a bunch of speakers and you allocate five minutes to each of them, and then you see how much time they take. But we're especially interested in the ways in which AI systems might be very different from us, and how that might help in avoiding such tragedies as well. Traditionally, in AI, we've always thought about this notion of an agent in a way that I think is very anthropomorphic, and actually doesn't really make a whole lot of sense, right? If you really took that model very seriously, you would get things like self-driving cars behaving in the way that you see here on the right hand of the slide, which is kind of funny or silly, but isn't actually how we would expect real self-driving cars to behave.

[1:11] So, that's the very short version of it. If you want to learn more, we have this paper from AAAI earlier this year, which is called Foundations of Cooperative AI, joined with Caspar, who is in my lab, and he's also maybe here. Maybe he's not here right now. I don't see him. Okay. But he's around, and so you can talk with him. So just to give an example, I know it's late in the session, so here's an example of a tragedy of algorithmic interaction. So, this is on Amazon. At some point, there was this book, "The Making of a Fly: The Genetics of Animal Design." I'm sure it's a wonderful book. But for some reason, two sellers were selling new versions of it for several million dollars each. It wasn't totally clear why. In fact, in the top right, you can see that the old version of the book was selling for like $35, I think. And so what happened here? Well, what happened was that both of the sellers here were using algorithmic pricing.

[2:03] In particular, so at some point, somebody figured out what they were doing was: one of them was trying to undercut the competitor. It was looking at the competitor's price and saying, well, I'm going to multiply that price by 0.99 something to beat a cheaper seller. Intriguingly, the other seller had a very different strategy, which was actually to multiply the competitor's price by - what was it - I think 1.27. I don't know what the reasoning was. Maybe they didn't have the book in the first place, and we're just hoping to buy it from the other seller and sell it at a markup. In any case, if you repeatedly update this way, you're going to get an exponential increase in price, which is in fact what happened. You can see it went up to 24 million before it got shut down. So kind of funny. Obviously, not very sophisticated algorithms. One, also probably not too much harm done here. But we also have examples that are a little bit more serious. Here is the 2010 flash crash, where interacting trading algorithms caused a trillion dollar stock market crash. You may have heard of it. And so the concern is that as AI starts to take over more and more of our world, we're going to see these kind of strange interactions taking place in more and more domains, right?

[3:18] Imagine this happening in our electrical grid or in the context of cybersecurity, cyber warfare, maybe actually kinetic warfare. If that sounds fanciful, there's this kind of scary video that Palantir put out that you may have seen. And then, of course, in general, we might actually have broadly capable AI systems that interact with each other in many different domains, which would be even more difficult to predict what would happen. I think one message to take away is that aligning individual AI systems is not enough. I won't go through the full details, but here's a game where we have two AI agents, each of which we have aligned quite well with our real objective function, right? So, it's very close, but they're slightly different from each other in how they've been aligned. And this results in a game. And you would think that everything about this game is favorable in the sense that there are outcomes in the top left corner that are really good for everybody.

[4:15] And then if you move away from the top left corner, it gets bad for everybody. So, you would think you would end up in the top left corner, but the way that this game is structured, actually, it has only one equilibrium, which is the bottom right... which is as bad as it can possibly be, right? And so any typical, learning algorithm that is just trying to maximize its own utility, if both players use that, you will eventually end up there and not in any of the good outcomes. And then just to finish up, there are some ideas that we can use where we take advantage of the fact that AI agents don't need to be like us. For example, their source code could be transparent to each other. This slide here shows that actually you can get cooperation in the single shot Prisoner's Dilemma based on this idea that you can be transparent to each other.

[5:06] Now, this is just at the level of kind of a very theoretical and probably very brittle idea here, but Caspar has been thinking a lot about how to make this robust. And in particular, he has a paper here at NeurIPS of how you can get this kind of thing to happen in actual learning systems. Thank you.
