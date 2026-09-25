---
id: "zelZDnvn8sY"
title: "Atticus Geiger - Theories and Tools for Mechanistic Interpretability via Causal Abstraction"
url: "https://www.youtube.com/watch?v=zelZDnvn8sY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 316
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Atticus Geiger - Theories and Tools for Mechanistic Interpretability via Causal Abstraction

[Watch on YouTube](https://www.youtube.com/watch?v=zelZDnvn8sY) · FAR․AI · 2024-02-08 · 5:16

## Description

```text
Atticus Geiger - "Theories and Tools for Mechanistic Interpretability via Causal Abstraction." 

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] I'm going to be quickly going through sort of just some tools and theories for mechanistic interpretability that come from the field of causality, specifically causal abstraction. There's a bunch of people I work with. First, I'm gonna start just talking about a sort of framework for thinking about mechanistic interpretability. So you have a lot of different systems in the world that are densely connected with many different microvariables and it makes them difficult to understand and manipulate. So this might be like the weather like a hurricane or the brain or an artificial neural network. And something that unifies all of these phenomena in an interesting way is that the task of trying to understand them is really the task of trying to faithfully simplify or aggregate a lot of different microvariables into macrovariables that describe a simple sort of high level process that is a faithful description of the underlying complicated low-level system.

[1:01] So the general framework for thinking about this for mechanistic interpretability is we can represent both the dynamical system of a neural network at the low level. And our intuitive algorithmic hypotheses about how neural networks carry out the behaviors they do. Both of these can be represented as causal models. And then we can understand the notion of implementing some sort of abstract algorithm with the theory of causal abstraction. And then to sort of go in and verify whether or not our hypotheses are correct or the degree to which they are correct, we can do intervention experiments. So here are a couple of hot takes. I pretty much think mechanistic interpretability as a whole... everything in it can be understood within the framework of causal abstraction. Probes, visualizations, and certain types of feature attributions are not really gonna identify the mechanisms we're looking for. And we really need to develop benchmarks so we can start actually hill climbing and understanding what success looks like in mechanistic interpretability. Alright. The next part is uncovering interpretable causal structure. We're gonna state some sort of hypothesis about how a model is solving a task. Then we're going to find some alignment between the variables in this high level model and then representations in the neural network.

[2:17] And then we perform interchange interventions on the high level model and the low level model. And then we see whether they have the same behavior. What is an interchange intervention? You also might know it as activation patching. It's just an intervention that's going to take some representation and then set it to be the value it would take if a different input were provided. Crucially, here, different from activation steering or sort of jittering perturbations - as those are other interventions - we are considering interventions that are setting representations to be values that they actually take on for some real input that is being provided into the network. Here, you can see on the top half, we have a high level model, we do an interchange intervention, a low level model, we do an interchange intervention, and then we go and see whether or not the neural network is actually matching the behavior of our simple high level model. We did this on some complicated natural language inference tasks - has some crazy tree structure like this.

[3:13] This was the sort of alignment we found. We also very recently started generalizing this. We can think about linear subspaces rather than individual neurons or vector representations. And so the crucial step here is that rather than just doing an interchange intervention - where we do an intervention setting some neurons to take on values they would have for another input - we instead are rotating a representation, doing an interchange intervention in a new non-standard coordinate basis, then rotating back to get to the original space. This allows us to target linear representations or linear subspaces rather than basis aligned neurons or vector representations. It's a very crucial generalization of our method and it also allows us so start learning the alignments between high level models and low level models using stochastic gradient descent, which has really transformed how we're approaching this problem of interpreting networks because we can actually automatically, with gradient descent, look for where a high level variable is being stored in a low level representation. And then inducing interpretable causal structure. So the cool thing about doing this is in the sort of analysis mode, you just do an intervention on the high level model, do an intervention on the low level model and then see whether they have the same sort of output.

[4:30] But you can also just use this as a training signal as well, where you use a high level model. And then you say I want these variables to be located in these representations... And then you just do gradient updates to the low level neural network, and you can train it to localize pieces of information in different parts of the network. We - here's a visual for this - did it on some complicated MNIST task. We also did it in this little agent dude running around. We used it for model distillation - works very well and we also used it to start doing estimation of how networks would behave under counterfactuals. And that's my time. Thanks so much.
