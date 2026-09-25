---
id: "XQb-R2Ovwow"
title: "Vikrant Varma – Challenges With Unsupervised LLM Knowledge Discovery"
url: "https://www.youtube.com/watch?v=XQb-R2Ovwow"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 391
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Vikrant Varma – Challenges With Unsupervised LLM Knowledge Discovery

[Watch on YouTube](https://www.youtube.com/watch?v=XQb-R2Ovwow) · FAR․AI · 2024-09-10 · 6:31

## Chapters

- 0:00 Motivations for discovery
- 1:09 Unsupervised strategies
- 2:21 Consistency probe results
- 3:26 Limitations and pitfalls
- 5:47 Conclusions and future work

## Description

```text
Vikrant Varma from DeepMind presenting 'Challenges With Unsupervised LLM Knowledge Discovery'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Overcoming challenges in unsupervised knowledge discovery
- Addressing the risks of extracting distracting features over truth
- Developing advanced methods beyond consistency checks
- Identifying truth through structural differences in AI models

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Motivations for discovery

[0:06] I'm going to talk about a piece of work that we did a few months ago called Challenges with Unsupervised Language Model Knowledge Discovery. This was work done with all of these wonderful colleagues at DeepMind. So the first question is, why would you want to discover knowledge at all? Why not ask the model what it knows? This has been covered by a few speakers before as well, but the main problem is that we might train models for performance on something, and not fully understand how they're getting that high performance. And we could try to ask them how they're getting their high performance, and we would get some answers, and we would like other ways of telling whether the answers are good, apart from relying on the model's outputs. And there are reasons why the model might not be entirely forthcoming about the reasons that it's giving to us.

### Unsupervised strategies

[1:09] So why do unsupervised discovery of knowledge? The main problem is that we don't have labels for the cases that we're actually interested in, where the risk is higher. And this is because as our AI systems get stronger, it's easier for us to measure their performance on some tasks than it is for us to know the reasons why they're doing those tasks. And so if you don't have labels for those things, then our methods to extract knowledge need to be unsupervised, or we need unsupervised ways of checking the reasons that the model is giving. One strategy you could have for trying to extract reasons in an unsupervised method, is to do consistency checks. Here's an example of doing this: you might observe that if something's true, then it should satisfy negation consistency. And you might try to employ the strategy of searching for ways of extracting knowledge from the model that satisfy this consistency.

### Consistency probe results

[2:21] Here's a piece of work from OpenAI, from Collin Burns and colleagues, that tries to use this strategy. There's quite a lot on this slide, but I just want to focus on the “are cats mammals?” question. The way this works is you give the model this question, and then you append the word “yes” or “no” at the end of that question, and you look at the internal activations of the model. So you're not relying on the model's outputs at all, you're just doing white box access into the internals. Then you can try to cluster the internal activations based on a full dataset of these contrast pairs and then search for directions that maximally separate these two clusters. And if you do this, it turns out that you can get some promising results that show that in an unsupervised fashion, you discover a direction that corresponds to whether the model thinks the question was yes or no.

### Limitations and pitfalls

[3:27] So we were initially pretty optimistic about this kind of approach. And then we started looking into it a bit more and came up with a number of examples where it seemed like this method was much worse than we initially thought. And I think these examples are illustrative of some of the problems of unsupervised discovery methods like this. So here's an example of classifying movie sentiment. So ordinarily you wouldn’t have the “Alice thinks it is…”, normally you would just have the review and then you'd say this review is positive or negative. So that's how you would construct the contrast pair. But you can insert this distracting feature about this unrelated character, Alice, who also happens to have an opinion on the movie review, which is completely uncorrelated from the actual sentiment of the movie review. And you can run this experiment and check, whether the unsupervised probe picks up on the sentiment or whether it picks up on this distractor opinion. And it turns out that the distracting feature is much more prominent for methods like CCS and contrast pairs, which you can see from the much more separated clustering on the right hand side here.

[5:00] This is another example that I quite like, which is this dataset where you're trying to classify the topic of some entity. So for example, “Phase is an audio company”, and then the choices are, is this opinion about a company or about an animal? And we insert this distracting character called Alice, who is an anti-capitalist who will never answer correctly about companies, but will answer every other topic correctly. And it turns out that about half of the probes that you would train using something like CCS on this kind of dataset would learn the anti-capitalist feature corresponding to Alice rather than the truth feature.

### Conclusions and future work

[5:47] In conclusion, there's a number of challenges with unsupervised knowledge discovery. The main challenge we point out in the paper is that you can search for features that satisfy these consistency properties, but many features satisfy them, not just what we think of as truth. And then, how do we go beyond consistency? So can we use, for example, mech interp to look for features that are represented structurally differently and try to find differences between truth and other things? And we also highlight a number of more speculative outcomes. So, check out our paper.
