---
id: "SjW_AH9qDZQ"
title: "The Role Of Neural Geometry In Interpretability | Atticus Geiger (Goodfire)"
url: "https://www.youtube.com/watch?v=SjW_AH9qDZQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-18"
duration_seconds: 831
is_short: false
chapters: 11
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# The Role Of Neural Geometry In Interpretability | Atticus Geiger (Goodfire)

[Watch on YouTube](https://www.youtube.com/watch?v=SjW_AH9qDZQ) · FAR․AI · 2026-08-18 · 13:51

## Chapters

- 0:00 How do neural networks represent concepts?
- 1:02 Beyond the linear, sparse-autoencoder view
- 2:07 The big-picture view of interpretability
- 2:50 How April gets inside a neural network
- 3:55 Emotional dynamics: behavior meets representation
- 5:07 Manifold steering vs. linear steering
- 7:03 An internal calculator and Fourier features
- 8:35 How sparse autoencoders capture geometry
- 10:28 Discovering new manifolds, unsupervised
- 10:42 From dictionaries to encyclopedias
- 12:22 Automating interpretability with research agents

## Description

```text
Atticus Geiger (Goodfire) on how neural networks represent concepts, and why the concepts-as-directions view behind sparse autoencoders is incomplete.

Geiger argues that the linear picture behind sparse autoencoders, where each concept is a single direction, misses the multidimensional geometry inside neural networks. He frames interpretability as tracing real-world conceptual structure into training-data statistics and then into a model's representations, algorithms, and behavior. His examples: months like "April" form circles inside a model, the geometry of human emotions reappears in activations, and "manifold steering" controls behavior more precisely than linear steering. In one case, a model builds an internal calculator from Fourier features (in Llama 3.1 8B) to reason about time. He then examines how sparse autoencoders can shatter, compactly capture, or only partly represent this geometry, and sketches a path to automate interpretability, moving from dictionaries to encyclopedias with AI research agents.

Chapters
0:00 How do neural networks represent concepts?
1:02 Beyond the linear, sparse-autoencoder view
2:07 The big-picture view of interpretability
2:50 How April gets inside a neural network
3:55 Emotional dynamics: behavior meets representation
5:07 Manifold steering vs. linear steering
7:03 An internal calculator and Fourier features
8:35 How sparse autoencoders capture geometry
10:28 Discovering new manifolds, unsupervised
10:42 From dictionaries to encyclopedias
12:22 Automating interpretability with research agents

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=xAea0v-rwGScP3zB

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### How do neural networks represent concepts?

[0:00] Hi, I'm Atticus, and I'm excited to talk to you about some work that we've been doing over the last around like 6 months around neural geometry in neural network models. And I'll just hop in after I understand— is— all right, cool. So fundamental question in interpretability, how do neural networks represent concepts? So what do I mean when I say a concept? Oh, all sorts of things, you know, sentiment, sad, happy, something like user modeling, animals. This one's my favorite, 7, great concept. April. So, you know, just broadly, these sorts of entities that, like, exist in our human world, these are, like, real-world abstractions that humans use to navigate our complex environments, and neural networks embed them inside their representations, and we want to understand the nature of this embedding. So sort of like typical or maybe very popular view about like how this

### Beyond the linear, sparse-autoencoder view

[1:02] embedding could occur is a linear model, which is embodied by sparse autoencoder architectures. So the idea is that you have a neural network. You take its hidden representations. You learn an autoencoder. So you encode them into a bunch of directions. And then you decode them to reconstruct the representation. And the idea is that the directions that you use to encode the representation are going to correspond to concepts. And this is a hypothesis about how representation is achieved in neural networks. But what if this assumption is not what's actually going on? So I think it's pretty clear at this point, this is not what's actually going on. This is a bunch of work, some of which is done at GoodFire, some of which is done by people at GoodFire before we were there, and some of which is done by just other people. I think it's pretty obvious now that there is very interesting multidimensional structure inside of neural networks that capture all sorts of concepts across different modalities and different architectures.

### The big-picture view of interpretability

[2:07] So now I'm going to ground us in this sort of, like, big tent picture view of what interpretability is. So how do the concepts even get into neural networks? So it starts in the real world. We just have real-world conceptual structure that just actually exists and we're all very intimately familiar with. Then that real-world conceptual structure becomes statistical properties of training data, which we feed into our neural networks. And then we see this real-world conceptual structure get recapitulated by neural networks in terms of their representations, the algorithms that operate over those representations, and the behavior, the input-output behavior of the neural networks.

### How April gets inside a neural network

[2:50] All right, cool. So I'm going to walk through just a very concrete example here. So how does April get inside of a neural network? So in the real world, we know what April is. It's a month. Months are organized in a circle. It's how we organize time. How is this then realized in statistical structure and training data? Well, there's actually very nice co-occurrence statistics between months that track how close they are in terms of time. And then you can see that this is recapitulated in terms of a neural network representation where nearby months are nearby in their representation space. And this is not work at GoodFire. This is work done by these people. It's very cool work. And I think it's a really nice grounding example for just this big picture view of what interpretability is trying to study, which is this whole process going from the real world to the data that's used to train a neural network, and then understanding post-hoc that neural network at many different layers of abstraction. Cool. And I'll use this as a slide to sort of ground us as I quickly go through some published work over the last few months and give you a sort of, like, whirlwind tour that will hopefully prompt you to go read the blog posts and papers that I'm talking about.

### Emotional dynamics: behavior meets representation

[3:55] Cool. So behavior and representation. So here's this paper. And the core idea is that we just fed simple stories into a neural network. And we wanted to observe how emotional dynamics evolve in those stories over time. We can do this in terms of just having the neural network forced answer questions like, how happy or sad was the story, 1 to 10, at every sentence in a story. Then we can understand this in terms of just the behavior. So we just take these answers to these questions, and we embed them in these manifold spaces. And we can also understand this in terms of the activation space, harvesting the internal activations as the story is being processed. And we can see that similar geometries are recapitulated in both cases. And so another cool thing that we see in this is that the real-world structure of human emotions is then recapitulated in the representations of neural networks.

[4:57] So here are some embedding centroids from actual human surveys and neural network representations, and also some similarity matrices.

### Manifold steering vs. linear steering

[5:07] Cool. Now going on to manifold steering, which is, again, about how behavior and representation are linked to each other. So in this, the core idea is that you have this geometric structure in both the belief space of your model — so it's uncertainty over a space of concepts — and its internal representations in its activation space. And what we want to do is test this bidirectional relationship. Is there sort of shared geometry between representations and behavior? So what do we do? Well, in terms of the representation space, we fit manifold structures to internal representations of neural networks. And then we take the concepts, the different values of concepts, and the centroids they correspond to. And then we just smoothly interpolate along the manifold between those centroids, and we observe the paths that happen in behavior space.

[6:02] But then we also do the same thing backwards. So we say, what is a path in behavior space that is smooth and nice? And how can we reverse engineer what the path should be in activation space? And we see that there's this sort of bidirectional correspondence. And this is a really nice example. Unfortunately, the conversion destroyed these videos. So I'm going to just go through this quickly, and you can go online and see how this looks. If you do linear steering in this sort of simple control setting, it just looks horrible, and it smears the car everywhere in this, like, very horrible-looking and incomprehensible thing. But if you instead steer along this very cool little tangled ball of yarn, you perfectly control where the car is along the hill. And I just find this to be an incredibly compelling example of why you can't think of things in a purely linear interpolation type of way. There's actually really complicated, interesting structure in very simple classic settings that we study in artificial intelligence.

### An internal calculator and Fourier features

[7:03] OK, cool. And now I'll highlight the next paper, which is looking at now the algorithm as well. What are the operations actually being performed over these interesting internal representations? So in this paper, we ask simple questions like, what is 4 months after October? And what we uncover through causal analysis and activation patching is that the model solves these problems with a little internal calculator that it also uses to solve addition problems. And it does so by converting a month into numbers. But what does a number look like inside of a neural network? It's actually a bunch of parallel circles. So these are Fourier features that encode different sort of periods of numbers. So like, what is my value mod 2? What is my value mod 5? What is my value mod 10? And what we can show is that actually the neurons at layer 18 in Llama 3.1 8B are perfectly partitioned by which Fourier circles they're reading off of and writing to. And so you get these amazing little, like, perfectly succinct modules that are doing distinct operations in parallel to solve an addition problem so it can reason about months.

[8:18] And these are, like, the Fourier probes that you see here. And so the really cool and interesting thing here is that we show how there's this interplay between causal analysis and understanding how operations are performed by the network and the underlying geometry of the representation.

### How sparse autoencoders capture geometry

[8:35] And this is the last one, which is understanding how sparse autoencoders fit into this picture. We look at the— in terms of representation. And so the idea here is we just collect a bunch of existing manifolds that we just collect on our own by designing specific datasets that will highlight these sorts of concepts and structures. And then what we do is we just take a bunch of sparse autoencoders that are trained on these representations, and we see how do they reconstruct these representations, because just because a sparse autoencoder learns a single direction as a feature doesn't mean that groups of features wouldn't be able to reconstruct these interesting multidimensional structures. And so the idea is there's going to be 3 regimes in which directions are able to capture multidimensional geometric structures inside neural network representations. The first regime that's shown here is that each individual point on some manifold has an individual direction associated with it, and we call this shattering. The second idea is a compact capture. So we actually learn a succinct basis to represent the multidimensional structure, and every single one of the basis elements always fires to reconstruct any point.

[9:48] And then there's a third regime, which is a sort of mixture of the two. There's not this one-to-one relationship between individual directions and points on a manifold, but there is still— it's not a perfectly compact representation. And the cool thing about this framing and this understanding is that we can then use what is an Ising model, which I won't get into, to sort of reconstruct manifold representations from trained sparse autoencoders. And this isn't supposed to be the end-all be-all, like the perfect pipeline for unsupervised recovery of neural geometry, but it's an interesting first step in connecting sparse autoencoders to this picture.

### Discovering new manifolds, unsupervised

[10:28] Cool. And this is an example of some new manifolds that we discovered with our unsupervised pipeline that involves sort of like statistical boundaries plus or minus x occurring in a text.

### From dictionaries to encyclopedias

[10:42] And so I will conclude by just sort of sketching out how I see these pieces coming together, which is the idea of automating this whole process so we can, like, scalably understand neural networks in the sort of bespoke normal way of doing interpretability, but using research agents. So this is the typical picture where we have just a list of directions with English labels. This is typical max activating auto-interp. But the dream that we have is fixing the big problems, that neural networks don't represent concepts as directions, and that simple English sentences are not sufficient explanations or characterizations of a representation. And so what we want to do is go from dictionaries to encyclopedias. We want to say, take a neural network representation, decompose it, understand the geometry that is present in multidimensional subspaces, map that to a conceptual space, and then do causal analysis— some conversion error from Keynote again.

[11:55] So, and I'll end with just saying, this is like a mock sketch of what I imagine an encyclopedia page might look like, where we're going not— no longer from just single directions with simple English sentences, but instead some interesting geometry captured in multidimensional subspace. And then basically a research report, including figures and code that actually show you what the role of this representation is in the computations being performed by a neural network.

### Automating interpretability with research agents

[12:22] And so what does this pipeline look like in terms of the papers that we just went through? Well, it starts with unsupervised discovery of activation geometry, which is what we're talking about here. But we also have other methods we're cooking on right now. Then it looks like a sort of bespoke statistical analysis of these structures. How can we figure out what a given geometric structure corresponds to in our world? So this is something like max activating auto-interp plus plus. And then the final step is actually doing a bespoke causal analysis of that structure in concrete tasks and showing how control can be achieved. And something that just really excites me now about interpretability is that research agents are getting better and better. I'm just very optimistic that the sort of, like, I guess, like, traditional approach to interpretability, like reverse engineering networks on specific tasks and trying to understand computation and representation at a very high level of fidelity, I just think it's now becoming, like, an actual thing we could scale up and start building out these enormous catalogs of just, like, you know, research papers that would've taken a huge number of human hours to previously do.

[13:31] And I'll end by highlighting all the great people that made it happen, minus Owen, because I couldn't find his picture on the internet. Crazy. All right, and yeah, that's it. Thank you.
