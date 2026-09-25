---
id: "TjwYtlzXgts"
title: "Johannes von Oswald - Mechanistic Interpretability of in-context learning"
url: "https://www.youtube.com/watch?v=TjwYtlzXgts"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 344
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Johannes von Oswald - Mechanistic Interpretability of in-context learning

[Watch on YouTube](https://www.youtube.com/watch?v=TjwYtlzXgts) · FAR․AI · 2024-02-08 · 5:44

## Description

```text
Johannes von Oswald - "Mechanistic Interpretability of in-context learning."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] I'm super happy to talk about mechanistic interpretability of in-context learning. I'm at Google. and this has been work with colleagues at Google and ETH Zurich. the motivation is that we wanted to understand the transformer architecture a bit better, and especially it's fascinating few-shot learning capabilities that seem to be magically appearing if you just train these models autoregressively. So you can provide a text description of new tasks, and the model seems to learn, based on examples that you give here, and, what we want to study is: What happens here? Why does this happen? Just to jump directly to the hypothesis... We think that next token prediction is actually a gradient-based mesa-optimizer, that is implemented in the transformer architecture. And because there is this nice optimizer in the architecture, you can actually repurpose this for super cool things. For example, in-context learning or potentially chain-of-thought, or other things.

[1:20] Just a visualisation of the hypothesis. This huge thing is a transformer. And in the beginning, you get the sequence. The first thing that the transformer is doing is kind of looking at the sequence and deciding what it can consider an input and a target for dataset. That's what we call a mesa-dataset. The most simple instance of this is just to consider a sliding window. So you just slide over your sequence and you consider every element as an input and a target. And then the hypothesis is that the transformer inside the architecture is optimising, let's say, fast weights... so implicitly parameters that it's learning based on the sequence and using as a next token prediction. First step copy stuff together, and then learn implicit fast weights.

[2:17] We don't really study this in language models, but only on a very, very toyish setting. So we consider, linear dynamical systems, where W the teacher... W* here is an orthogonal matrix. So every sequence comes from a newly, freshly-sampled orthogonal teacher, You sample some x(0)s and perturb a little bit of noise. And you provide this data to the transformer, you train this autoregressively... On every token, try a next token prediction. This is not a classification task, so also slightly different as an LLMs. What is nice about the setting is that we actually know ground truth; a solution to this. This is recursive least squares. So just a least squares solver here, regularised for every time step, T, you want a new one because you get new new data per per time.

[3:16] So the transformer - to solve this problem very well - needs to implement a recursive least-squares algorithm. And this actually requires T matrix inverses inversions in the forward pass. So what can we say about the transformer architecture? Actually, it can solve that problem pretty well. One nice result that was actually in a previous paper, is that a linear self-attention layer -- let's consider it different to Softmax, but still kind of close to the classic transformer architecture -- can very easily implement a gradient step. And now, in follow up works, what you can also show... so you see, the similarities of the expressions here ... that a single linear self attention layer can actually implement a summand of this, of a truncated Neumann series so actually can invert these matrices like, projected matrices where you, multiply with your X(T). Also: super well. So this implies that a transformer architecture can actually invert these T matrices very efficiently in log(log(1/epsilon) when, epsilon is the error that you want to have on the final matrix inversion.

[4:36] OK, coming to the last slide. So what? For a single linear, self attention layer, you can study this very thoroughly. When you go deeper, we fall back to linear probes and yeah, you get - though this is a cherry picked result - you get here very nice probes. In the B figure, you see that if you probe for the target... This is showing the... what the transformer should predict at the end... You see over the layers it's getting better and better and better over time. And you actually can probe for the red as well. So you can probe for the approximated projected matrix inverse here. And you also see this nicely decreasing so that it actually implements this .. or seems to be implementing something similar to this... and kind of closing the circle.

[5:33] You can now use this as in-context learner as well.
