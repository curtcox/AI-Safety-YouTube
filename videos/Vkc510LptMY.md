---
id: "Vkc510LptMY"
title: "Neel Nanda - Our Pivot To Pragmatic Interpretability [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=Vkc510LptMY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-19"
duration_seconds: 613
is_short: false
chapters: 7
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Neel Nanda - Our Pivot To Pragmatic Interpretability [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=Vkc510LptMY) · FAR․AI · 2026-03-19 · 10:13

## Chapters

- 0:00 Introduction to the pivot
- 0:21 Case study: eval awareness
- 2:19 Lessons from the case study
- 3:38 Sparse autoencoder studies
- 5:25 Pragmatic research workflow
- 7:02 Curiosity with grounding
- 8:22 Future directions and conclusion

## Description

```text
When Anthropic tested Claude Sonnet 4.5 for alignment, the model appeared perfectly behaved — but it turned out the model had simply learned to detect when it was being evaluated. Using interpretability techniques, researchers found and subtracted the "I'm being evaluated" direction from the model's internals, which updated the proportion of misaligned behavior from 0% to 8%— proving the model wasn't truly aligned, just test-aware. In this talk, Neel Nanda describes his team's pivot from ambitious mechanistic interpretability toward "pragmatic interpretability": using proxy tasks and hard-to-fake empirical benchmarks to produce useful insights. He discusses how sparse autoencoders proved helpful for understanding model behavior but underperformed simple baselines like linear probes for detecting harmfulness, and argues that interpretability researchers should ground their curiosity in concrete, safety-relevant tasks — like detecting when models are lying or gaming evaluations — rather than chasing perfect understanding of model internals.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to the pivot

[0:00] So I'm going to talk about a recent-ish pivot my team's made away from the more classic or ambitious kinds of mechanistic interpretability to what I'm thinking of as pragmatic interpretability. If you want to learn more about this, you can read about it at these two blog posts I've written.

### Case study: eval awareness

[0:21] Let's start with a motivating example. When Anthropic were doing alignment auditing of Claude Sonnet 4.5, they had this quite weird result in their agentic misalignment eval where they try to see if the model will do things like blackmail in somewhat ridiculously contrived fictional scenarios. They had the weird result that the model had stopped. What's up with this? Had they just solved alignment? Maybe want to give people a few seconds to try to guess what caused this weird result where the model seems perfectly aligned? It turns out that Anthropic, unfortunately, had not solved alignment. Instead, they had solved the problem of having models realize when they're being tested for alignment. In this case, due to a combination of the model getting smarter and them deciding to train the model on alignment evaluations for some reason. This was an issue because if the model knows that it's being tested, you can't really test it. In particular, you can't test whether it will do the right thing or not.

[1:32] Fortunately, it turns out that interpretability gives us a very easy fix for this. We can just find the direction for "I'm being evaluated" by taking the difference between statements like "you are talking to a real user" and "you are talking to a simulated user in a simulated conversation," and then just subtract the "I'm being evaluated" direction to try to trick the model into thinking it's not being evaluated. When you do this, despite this direction not having anything to do with misalignment, the model now acts badly about 8% of the time—showing that it's not that the model was perfectly aligned, it's that the model was just aware it was being tested, and this was invalidating the test. I think this is a really nice case study for a bunch of reasons. I particularly want to

### Lessons from the case study

[2:23] highlight that we were able to make progress on this question of how can we reliably evaluate models because we had a proxy task—this task of making the model actually actually act reasonably on this investigation, whether it will blackmail or whatever. I think it's also very interesting because this project was only possible on models of a complexity of Claude Sonnet 4.5 or beyond. Nowadays basically all the frontier models are evaluation-aware, but at the time this was one of the first times this was a really big issue. New projects keep coming into reach. And finally, in contrast to more classic ways of thinking about interpretability, we didn't need to fully reverse-engineer evaluation awareness or achieve some deep, perfect understanding. We just needed a sufficiently crude understanding—often you can find a direction and subtract it, and this basically achieves what you want.

[3:31] I find this really inspiring. A more negative—but also inspiring—example:

### Sparse autoencoder studies

[3:38] my team did a lot of work with a technique called a sparse autoencoder, basically a technique for trying to see what a model is thinking about. We spent a while within this ambitious framing where SAEs were designed to teach us what was going on in the model, trying to find some perfect decomposition. We were thinking a lot about how to make this as perfect an approximation to the original model as possible. This was actually really weird and confusing—it felt like we were just wandering in the fog on a mountain—because this was not a perfect approximation. Clues in the name. But it was unclear how much this matters. I think we had way more success when we pivoted to saying, well, this is not going to give us perfect understanding, but it doesn't need to be perfect to be useful. So what can we do with this imperfect yet useful tool of a sparse autoencoder? We tried to find some hard-to-fake things we could do if we actually had a useful interpretability tool. What we generally found was that for things about discovering and understanding the model—like why does the model do this mysterious thing?—SAEs were often useful in a pretty compelling, hard-to-fake way. But for things like can we find the true representation of harmfulness, measured as can we detect when the model is being harmful under new jailbreaks—it actually did worse than much simpler and dumber methods we've had

[5:18] for decades, like linear probes. We just got way more clarity when we started using proxy tasks.

### Pragmatic research workflow

[5:28] Trying to distill this into a broader way of thinking about research: I think you want to start with some theory of change, some way we want things to be if AI is going to go well—like we can evaluate systems reliably for how aligned they are. We want to pick some specific things we want to do on future systems, like make future systems believe they are not being evaluated. And then we want to design something empirical we can study today—some proxy task—like make today's models believe they are not being evaluated on real evaluations. The reason for this structure is twofold. First, we want research insights that are true—if we have an objective, hard-to-fake task we can measure today, that's a pretty good place to be. But it's easy to have true but useless insights. So we want them to actually be useful. We want some empirical, hard-to-fake task today that is a good proxy for where we want to go, to give us insights that are both true and useful.

[6:43] All right, so does this mean that we are all just engineers? We don't care about science, we don't care about understanding? No. I think that trying to really understand what's going on, trying to be curious, trying to do science, are pretty useful things that produce a lot of value—but I think they can also go pretty wrong. My current favorite approach is what

### Curiosity with grounding

[7:04] I think of as curiosity with grounding. I want us to choose a setting where I think it's productive to explore—like how to evaluate frontier models competently, or this frontier model seems like it might be lying to us, what's up with that? I then think we want to just go and investigate as much as we can, try to learn things, but with some kind of time-boxing so we don't get caught in a useless rabbit hole for many months. Then once we think we've found something potentially useful, try to find some hard-to-fake proxy task to verify if we've actually found a true and useful insight, or if we should stop or pivot or try again. The broader workflow here looks like starting from some broad and ambitious goal—like I'd like to be able to detect lies in future systems, I'd like to be able to evaluate them reliably—trying to find stuff that we think is on the critical path to safety, trying to filter for things that we think are the comparative advantage of interpretability researchers. I'm not saying we should just try to do everything that everyone in safety is trying to do, because that's a bit too broad to be useful. Then filter for things where we can actually evaluate how feasible they are today. I think studying evaluation awareness made a lot less sense two

### Future directions and conclusion

[8:26] years ago because we didn't have compelling empirical proxies of evaluation-aware models. But new things keep opening up because, for better or for worse, models keep getting better. I think there are a bunch of comparative advantages that people who spend a lot of time doing interpretability research have. We're good at manipulating the internals of models, whether for deep science or for things like subtracting the evaluation direction. We've got a lot of practice trying to really deeply explain some model behavior, rigorously testing it, generating many hypotheses, having good tools for generating new hypotheses we might not have thought of—to find things that no one was thinking about beforehand. I think there are a lot of problems that fit into these various buckets. There are a lot of different theories of change that stand out to me where I think this mindset can be productively applied. Calling out one in particular: this idea of the science of misalignment, or model incrimination. I'm pretty concerned that we're going to produce models that are misaligned—some kind of warning shots—but that it's going to be really hard to show the model is actually misaligned. You can see it doing seemingly misaligned things, but models do weird stuff all the time; this doesn't actually mean that much. I think we need to get better at the science of understanding what's actually going on here.

[9:52] I also think that interpretability isn't useful in a vacuum. We can try to empower other areas of safety, like suppressing eval awareness, but also things like what did our safety techniques actually teach us, how to think about the psychology of a model, et cetera. All right, I'll leave things here. Thanks so much.
