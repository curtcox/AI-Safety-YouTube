---
id: "7mElu87cMLw"
title: "Dylan Hadfield-Menell - Preference Learning in Alignment"
url: "https://www.youtube.com/watch?v=7mElu87cMLw"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 284
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dylan Hadfield-Menell - Preference Learning in Alignment

[Watch on YouTube](https://www.youtube.com/watch?v=7mElu87cMLw) · FAR․AI · 2024-02-08 · 4:44

## Description

```text
Dylan Hadfield-Menell - "Preference Learning in Alignment"

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Preference learning in alignment is something that we're all very familiar with - things like RLHF, learning from preferences to extract a reward model of some kind. This builds in an assumption that in the case of, say, you're doing preference learning for summarization, the preferences only depend on the quality of the summarization. They might actually depend on a whole bunch of other things that relate to the annotators are not well reserved, or well observed, or exposed to the reward model itself. We propose in this paper an idea that you think about your reward model as a combination of an expectation over some unobserved hidden context and your observed data that leads to your actual utility functions. So the probability A is preferred to, to B is some expectation over unobserved context Z. And the key idea is that you're representing this unobserved context as an expect this observed preference data as an expectation over unobserved context. And now you might ask the question of does RLHF or something similar recover the expected utility function?

[1:00] And the answer is not always. So here's a simple example where you get that case: let's suppose that we're getting preferences between zero on data between zero and one. And we'll say that our utility function in this region over here is just exactly equal to A. So no dependence on the unobserved context. But in this upper region, we have a 50/50 distribution between 2A and zero. So Z is gonna be a binary unobserved variable. And the probability that it's equal to one is just one half. Here's the function that you have overall and then notice that the expected utility is exactly still equal to A in this case. If you run preference learning on it, you end up with something that looks like this, that peaks right before you get to that extra noise present in your data. Here's an example where we actually trained a neural net on this model and you can see what we picked up and you might be asking what's that BC of A? Well BC stands for Borda Count, which is a standard way that people do ranked choice voting.

[1:55] It involves getting a candidate, and scoring their rank based on the number of alternatives that they beat out. And it turns out that when you have hidden context, preference learning aggregates over that hidden context via this Borda Count measure. So it's taking your comparisons and counting out "What are the number of other alternatives that each of these items beats?" This has some implications. We can show scenarios under which you do recover things with the same ordering as an underlying utility function. And we show that when this isn't the case, you might be have flips as we observed in that example. And this also says that annotators have an incentive to game their preferences in order to influence the result. We propose distributional preference learning as a way to approach this where instead of simply output an expected utility or a score function for an example, you move to putting out a distribution over utilities.

[2:46] You can do we suggest doing this in two ways. One is: you modify your architecture to output a mean and a variance for some Gaussian over score functions. The other one is: you can output a discrete distribution over fixed rewards inside of your architecture. And there are some simple changes you make to the loss function, but it's almost a drop in replacement for standard reward learning. And when you do this on this example, you end up learning high variance over that upper region. In the categorical example, you get this really nice case where you get your distribution sort of evenly spaced between the maximum and minimum score, which is kind of the right thing to do here. You can evaluate this on language data. We did this on the helpful harmless data set where whether or not data was collected for being helpful or harmless is actually unobserved context from the standard of, from the perspective of reward learning. And you can use this to mitigate jailbreaks because jailbreaks often pit these objectives against each other. So they take advantage of the model's preference to be helpful and pit that against training against it being harmless.

[3:44] So, you can evaluate these kinds of reward models on different kinds of responses and you end up with higher variant over the jailbroken response, which means you can mitigate it. Here are some results that show that you do a better job of getting a pareto frontier on performance on both of these. This can help you detect the presence of hidden context as well, which is what we think is kind of the main utility of this kind of method. So when you're running and uncover it there, you uncover it, there's high variance in score functions that means that you should be going in and looking at your data more carefully, maybe trying to represent more of that hidden context. And with that, Cassidy Laidlaw and Anand Sithrananjan were the ones that led this work. Cassidy is here. Go talk to him if you want to understand the details about how to improve your models. But in summary, hidden context in preference learning is a common and important problem, and distributional preference learning is a simple change to standard preference learning that can mitigate hidden context. And as a final thing, I'm recruiting PhD students, come work with me on this stuff. Thanks y'all.
