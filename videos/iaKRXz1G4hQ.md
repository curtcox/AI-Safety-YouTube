---
id: "iaKRXz1G4hQ"
title: "Adrià Garriga Alonso - Understanding planning in neural networks"
url: "https://www.youtube.com/watch?v=iaKRXz1G4hQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 245
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Adrià Garriga Alonso - Understanding planning in neural networks

[Watch on YouTube](https://www.youtube.com/watch?v=iaKRXz1G4hQ) · FAR․AI · 2024-02-08 · 4:05

## Description

```text
Adrià Garriga Alonso - "Understanding planning in neural networks."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] I'm Adrià Garriga-Alonso and I work at FAR AI, and I'm gonna share some work in progress - as opposed to the finished work from other people - which is about understanding how neural networks internally do planning or, alternatively, this is about empirically testing mesa-optimizers. Why do I care about planning? Well, I care because it's the most, in my opinion, it's the most likely source of existential risk without human intervention, which is by no means all or even most of the existential risk in my opinion, but it's an important source that would be good to completely knock out, right? I think most of this risk comes from the instrumental convergence thesis. If AI has long term goals, and it's planning for these, and we don't really understand what it's planning for or what its goals really are... then, many goals have - as an intermediate step - to seize resources, and do whatever it wants with them, right?

[1:03] So my work... I want to empirically test whether this can actually happen. Does it happen for models in practice? Like, do they acquire long term goals, or how can we tell if they have? I'm gonna talk about this soon, and people have been talking about this worry for a long time, but there's very little empirical work. There are some attempts, but we're really not there yet. So ideally, we'd be able to find whether any particular model is goal directed. How am I doing this? ... Maybe this should've been three slides.. But the general gist of it is that I am trying to build toy models of how your rewards are represented, and then test interpretability probes on these to see if they can find the actual reward model that was embedded there. And then this lets me try the probes on more realistic models and these then inform better toy models, right?

[2:00] I initially had some toy models with rewards in them, and it was very easy to find how they did the planning. But I think those are unrealistic now. So I'll tell you about a particular model I'm training next. My hypothesis is that there's some candidate plans inside the neural network and they come with evaluations of how good they are for the objectives. And then we could pick up these with probes hopefully. And I'm not working on language models because it seems hard to probe for their goals ... whatever they are. So yeah. Currently, I'm trying to replicate this 2019 DeepMind paper in which they train a neural network to play Sokoban, which is this game over here. There are some boxes, there are some locations on the floor and it's a puzzle game where you're supposed to push the boxes on the locations. And it's still used as a benchmark for planning algorithms like search. And they train some recurrent neural networks that - if you give them more time to think at test time - actually perform better at solving these levels. And this makes me think that they have definitely they have some like iterative algorithmic way of improving their actions.

[3:15] And I think this is likely to be what we think of as planning for the long term goal of solving this thing. The way they give extra steps at this time is, for the first ten (at most, ten) steps, the action that the neural network outputs gets masked out and it's a no-op instead and it just process the first state many times. So it is fully generalizing, it hasn't been trained to do this before. Yep. That's it. That's my talk. If you're interested in talking about this, or working on things similar to this, or in evaluating interpretability, come talk to me. I also have a paper in NeurIPS about automatically discovering mechanistic interpretability circuits. So I'm also interested in that. Thank you very much.
