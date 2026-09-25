---
id: "SQ1ir0YT2x8"
title: "Yonatan Belinkov - Toward Scalable and Actionable Interpretability [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=SQ1ir0YT2x8"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-05"
duration_seconds: 306
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Yonatan Belinkov - Toward Scalable and Actionable Interpretability [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=SQ1ir0YT2x8) · FAR․AI · 2026-03-05 · 5:06

## Description

```text
Yonatan Belinkov reveals some actionable findings in interpretability. He shows how we could stop models from makeing basic errors like calling "half a decade" 2.5 years, and how, through targeted interventions, his team can surgically remove sensitive information by projecting neurons into vocabulary space, demoting problematic tokens, and re-embedding them. Belinkov advocates for automation, agents, and core algorithmic improvements to make interpretability actionable for real-world deployment where people use LLMs for complex tasks despite persistent mistakes.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] So in the next few minutes, I'm hoping to convince you that we can and should work towards scalable and actionable interpretability. Let's see. Yeah, so there's already a lot of interest in interpretability. That's great. Many papers, they've been around for at least 40 years, as you can see here, from the first citation, from the first NeurIPS conference. And there are many workshops. I just want to nod to two workshops that are coming up at the end of the week, the Mechanistic Interpretability one and the CogInterp workshop. So check those out if you're interested. However, we still have many problems with language models that interpretability has not been able to solve. So they make these silly mistakes, like saying that half a decade is 2.5 years, and there are plenty of those examples online. And I also want to make the point that people use LLMs for many complex tasks, despite those silly mistakes, which I would say interpretability has not been able to kind of address.

[1:01] So what is interpretability good for? I would argue that it's good for basic science, scientific insights. And I want to show you one example, fixing problems in an efficient way. And I'll show a couple of those. And also monitoring emerging capabilities such as those that we've heard of earlier from Sarah and others. And I won't talk about those, but there's lots of interesting work in this area. And the big challenge is how to scale up. Okay, so here's an example for an insight. We were interested in this question of memorization versus generalization. How do models solve tasks? And as an example, we looked at arithmetic. So just a simple prompt such as this. What we found is we found a circuit, a mechanism, in the model, and we focused on a few layers, and we found that there are a few neurons, not many, that are responsible for arithmetic calculation.

[1:54] And we were able to characterize what they do. So they do various weird things, like these patterns. They capture heuristics or kind of small patterns. And so we call this the bag of heuristic hypothesis. And I like this because I think this is something that's not for memorization or generalization. It's kind of in between. And maybe this suggests something broader about language models, more beyond arithmetic, that is worth considering. Okay, back to problems. Why can't models count? They can't count the number of legs on this zebra. So it turns out that you can explain some of this by looking at the mechanisms. We found that there are different components involved in visual and textual processing. And if you compare and contrast, you can do all sorts of clever interventions and eventually close the gap between the two modalities or narrow it with some simple interest time interventions, which is what I'm showing here all the way at the end.

[2:55] Okay, a couple of more examples that I think are nice. So we have a lot of information memorized in these models. Sometimes that's good, sometimes it's not desired. We might not want them to give us personal information of people, even when it's there. And so one work that we did was to show how you can remove this information by intervening in the model weights. And here we're intervening in particular neurons in one MLP layer. In practice there are multiple of those. And the way we do this is we project those neurons into the vocabulary space, demote the problematic tokens and re-embed back into the model weights. And that's an efficient non-gradient based intervention that can remove sensitive information. Here's another example of things you might want to avoid. We might not want the model to tell us how to make a virus. Right? And despite various safeguards, these behaviors can still be extracted with attacks. So they are there. It turns out that you can isolate this behavior by looking at the features learned by the models. In particular, we used SAE features, but I think that's true for other kind of featurizations. And if you isolate the problematic features, you can then fine-tune the model completely to avoid activating those features. And that ends up resulting in a model that is less risky and still useful.

[4:21] Okay, so in the remaining time, what's missing? Interpretability has so far been about simple tasks. Small models takes a lot of work, and I think we have promising ways to scale it up. Automation and agents. Like we heard from Chenhao, core algorithmic improvements and evaluations are going to be really important. So I just want to mention MIB, which is an evaluation benchmark that we're building. We're also hoping to say something more about agents very soon. So to conclude, we can get scientific insights to support real world usage. We have to scale up and we need new algorithms, tools and language. Thank you.
