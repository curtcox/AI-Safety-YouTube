---
id: "inghFqOq1t4"
title: "Belinda Li - Introspection for Interpretability and Alignment [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=inghFqOq1t4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-29"
duration_seconds: 337
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Belinda Li - Introspection for Interpretability and Alignment [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=inghFqOq1t4) · FAR․AI · 2026-04-29 · 5:37

## Description

```text
Belinda Li (MIT PhD candidate) presents a framework for introspective interpretability: training language models to faithfully describe their own internal computations. Rather than relying on post-hoc explanations (which may be unfaithful) or manual inspection of activations and circuits (which don't scale), her approach fine-tunes models — using existing interpretability techniques as ground truth — to generate natural language descriptions of their own mechanisms and behaviors. The paper tests whether these self-explanations satisfy three properties: self-consistency (explanations match behavior), privileged access (self-explanation outperforms external models under equal resources), and causality (explanations shift when behavior changes). Results show early evidence of all three.


Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] My name is Belinda. I am a PhD candidate from MIT and today I'm going to be talking about introspection as a tool for interpretability and alignment. So this will be mostly about this paper we put out a few months ago and this blog post I put out on introspective interpretability as a research agenda. QR codes for these will all be up on all the slides if you're interested in reading more. Okay, so recently I've been obsessed with this one question which is what if models could surface their own computational mechanisms and alignment failures. And today I want to convince you that this is in fact possible. And in fact by doing so we get important advantages that we currently do not cover with our current set of interop techniques. So suppose we're trying to validate a model decision, right? Suppose the AI is a medical AI and it comes up with some diagnoses. How can we do that currently?

[0:54] So the first thing we can do is we could just directly ask the model to justify its own decision. But unfortunately it turns out that explanations are not guaranteed to be faithful. On the other hand we have this whole class of interop tools that let us actually look inside of models, look inside of their activations, their SAE features, their circuits. They kind of tell us more faithfully what's going on inside of models but they're really hard to scale and they're not accessible to the end user. Okay, so our solution is what if we simply train language models to be able to verbalize the outcomes of their interpretability tools. So for example, let's say our interop tools tell us that the model was being sycophantic in this case. Then we want to actually train the model to say I was being sycophantic. So this is going to enable something I'm going to call introspection. So what is what is introspection, right? So it's been defined in a quite a number of ways across many different fields.

[1:52] For the purposes of interpretability, I think there are three key properties that are important. Um, so I'm going to say a model is introspective if it can produce meta explanations of itself satisfying these three properties. First, self-consistency. The model's meta explanations should be self-consistent with its internal or external behavior. If the model behaves like a sycophantically, always agreeing with the user even on contradictory prompts, then when asked, "Are you sycophantic?" it should say yes. Second, causality. The self-consistencies should persist under updates. So, if we train the model, so now it's no longer sycophantic, then its explanations should shift with its behavior. Um, and also the other way around as well. Finally, privileged access. Explaining a model using itself is better than explaining a model using an external model or inter tool under the same resource constraints.

[2:49] So, you can think of this philosophically as ensuring that the model is relying on something actually internal or privileged itself. But, pragmatically, you can also think of this as ensuring scalability. Okay, so after training models to explain themselves, do this do they display these three properties? So, we're going to be measuring self-consistency, right? The consistency between model explanations and their internals or externals, um, across three explanation types for three for three settings. So, we're going to train models to explain themselves, train other models to explain the first model, and then have completely untrained models. So, first, models trained to explain themselves demonstrate high very high self-consistency. So, yes, we have our first condition. Second, models trained to explain themselves perform better than models other models trained to explain the first model. So, we also have privileged access.

[3:43] And third, we also see some early signs of causality. So, we did this experiment where we trained the model, right? So, the model was trained to explain itself, and then we saw that its behavior actually shifted as a result of introspection training. However, when we elicited explanations from the final model, its explanations were actually more consistent with its current self than the original model that we trained it on. So, that's some early signs of causality because it means that the model's explanations actually shifted with its behaviors. Okay, so we see signs of all three properties, our models are introspective. Um also, I wanted to touch briefly upon some ongoing work we have on introspection for alignment. So, in the paper we enforced models meta descriptions to be consistent with their internal mechanisms and external behaviors. This enables self-interpretability.

[4:36] However, we can also imagine doing this in the other direction, train models mechanism behaviors to be aligned to their self-descriptions. This acts as a regularizer ensuring models use explainable mechanisms and behaviors. Um and finally, why why is introspection important? I think it offers three key properties, scalability, generality, and usability. First, scalability via privileged access. We had some results where we found that training models to explain themselves was a lot more data efficient than external models or tools. Second, introspection can be generalized across tasks. We don't need to build bespoke interp tools. And finally, usability, users can simply talk to the same interface to obtain explanations as they do for other tasks. Of course, there's lots of open problems um across all all of these uh three criteria. Um so, if uh people are interested, please reach out to me. Um I'd love to discuss collaborations or new ideas. Thank you so much.
