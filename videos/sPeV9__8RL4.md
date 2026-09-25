---
id: "sPeV9__8RL4"
title: "Irina Rish - Complex systems view of large-scale AI systems"
url: "https://www.youtube.com/watch?v=sPeV9__8RL4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 365
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Irina Rish - Complex systems view of large-scale AI systems

[Watch on YouTube](https://www.youtube.com/watch?v=sPeV9__8RL4) · FAR․AI · 2024-02-08 · 6:05

## Description

```text
Irina Rish - "Complex systems view of large-scale AI systems." 

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Okay, so this program started four years ago when we were all very excited about building AGI as soon as possible and where people talk about safety much less but nevertheless I mean the high-level goal remained. It's just how you go about that. So the goal of building not narrow but broad systems that can just do bunch of stuff and that stuff is useful is still there and making systems sufficiently autonomous so people do not have to babysit them all the time is still there. So the question is just how you go about that so it also is reasonably safe. And one of the high-level motivations for this program was that we try to see how do we relate to their natural intelligence. I mean it's high-level ultimate question what's invariant. If you do invariant risk minimization type of thing on multiple domains of intelligence, natural intelligence is not going to be the same as the natural intelligence of natural and artificial. What's going to be the set of invariant features? I know, good question. And we're all trying to figure it out but it's kind of what was driving us and why, a perspective that looks at the artificial systems and natural systems from somewhat dynamical system perspective, that was one of the guiding ideas here. But I want to talk about basically keeping in the mind that networks we have right now are very very different from networks in our brain or even networks in larval zebrafish.

[1:35] So those things they always active and they constantly never stopping sending messages which is not the case with our transformers and so on. So that's something to keep in mind whether you want to improve capabilities of current systems or whether you're really worried what the systems can start doing on their own. I think unless they have this inherent intrinsic dynamics, they are much less capable of doing things on their own, but that's just an opinion. Moving on to... I wanted to make this point early on because I know I'm going to run out of time. The point is that yes I totally understand and very much kind of into doing research on safety and alignment and I think that should be done together with developing capabilities. That's not necessarily an orthogonality hypothesis that it's one or another. It can be both. You just need to figure out how to do it. And I would say I'm more like a techno-optimist. And the blueprint for the post-singularity future is the old story gentle seduction by Mark Stiegler. Where yes, there are risks of going into trajectories where people go too fast and without caution and it doesn't end well. But there are also other cases when people are too fear-filled and it doesn't end well either. So caution without fear.

[3:01] That's kind of conclusion there. I don't have much time to go through all the technical details but essentially we were working on all the aspects as many others in the field that try to improve the generalization abilities in general sense. Whether it's out of distribution, whether it's domain adaptation, meta-learning, transfer learning. It's all about generalization just like good old statistics from 1950s. It was always about that. But then recently we have this Cambrian explosion of systems that suddenly generalize so much better than they did several years ago. And they do it because of scale and you don't even need a transformer. You can take a NLP, scale it, and it improves quite a lot. So the next question is, okay, so can we understand scaling and - for both capabilities and alignment purposes - can we learn, can we figure out how those systems actually develop? Can we predict their behavior?

[3:55] Can we come up with scaling laws not just for simple situations but for some complex non-linear one? There is a long, interesting history of scaling laws. It didn't start just with Jared Kaplan's paper in 2020. It started way back with Corinna Cortes and Vladimir Vapnik in 1994. And I'd be happy to talk about that history with you if you have questions. But the thing is now things are getting complicated. You see papers on emergent behaviors although it's sometimes debatable what metrics are used on y-axis. You see papers on groking which look like second order phase transitions. You see GPT-3 up to a certain size not getting arithmetic and after a certain size suddenly getting it. The question is how do you understand the model depth? So what we focus on in our group most recently is trying to understand, derive, and predict scaling laws for various behaviors, both open books and closed books.

[4:51] Open books, I'm skipping, is looking at the patterns of the dynamics of the learning and those patterns may be sometimes very predictive about upcoming phase transitions like high oscillations early on in the loss, pretty much telling about groking. But if you don't have access to the system, it's somebody else's system, and you want to predict its behavior, you need closed box. Closed box is classical scaling laws, but they have to be generalized to nonlinear, non-trivial cases. And the recent work from ICLR this year is pretty much an empirical paper that shows that a more general class of functions beyond power loss, essentially smoothly broken power loss, seem to cover pretty much everything that you can see in the literature right now. And it can even cover non-monotonic behaviors of double descent, multiple descent, and those phase transitions under certain conditions as well.

[5:46] So that's pretty much it. And the rest of this talk, you can listen to it on Friday in the Scaling and Open Source Workshop, because the second part is about how do we actually build those systems and on what kind of supercomputers.
