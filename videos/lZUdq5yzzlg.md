---
id: "lZUdq5yzzlg"
title: "Stephen Casper - Why do LLM Outputs Disagree with Internal Representations of Truthfulness?"
url: "https://www.youtube.com/watch?v=lZUdq5yzzlg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 338
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Stephen Casper - Why do LLM Outputs Disagree with Internal Representations of Truthfulness?

[Watch on YouTube](https://www.youtube.com/watch?v=lZUdq5yzzlg) · FAR․AI · 2024-02-08 · 5:38

## Description

```text
Stephen Casper - "Cognitive Dissonance: Why do Language Model Outputs Disagree with Internal Representations of Truthfulness?

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] I'm Stephen. You can call me Cass. Most people call me Cass. And I get to talk about a paper that was recently at EMNLP a couple days ago in Singapore, but I completely sloughed EMNLP in order to talk about it here instead. And thanks to co-authors who are on the slide. The main takeaway that I want to offer to each of you in the next few minutes is that when we talk about things like deception or hidden latent knowledge inside of language models, we need to be very cautious and we need to have a lot of nuance when we talk about these things. So consider two ways of assessing what a language model believes. The first way is the simple way. It's the straightforward way. You can just ask it what it thinks. So you can take some sort of question and you can format it as, or some sort of problem, and you can format it as a question with a prompt for an answer. And then you can see what type of answer the model might want to provide when you format things this way. The second way is a bit more mechanistic and it's a bit more white box.

[0:56] You can probe for knowledge of the truth or representations of the truth inside the model. So you can give the model different statements or question-answer pairs, some are true, some are false. And you can train this probe, like a linear one from the internal states or something like this, to tell you the truth here. And some recent work, including ours, in the past year and a half, we can say, has kind of contrasted these two ways of assessing beliefs in language models. And one pretty common finding is to see things like this across a particular data set. You'll find that the model is maybe like 70% accurate, but when you probe for answers inside of the model using the internal states, you can get maybe 75% accuracy. So what's going on here? What's making up this discrepancy? One type of interpretation that you might make based on this type of result is you might assume that there's maybe a subset of examples, maybe five or so percent in this case, in which the model has some hidden latent knowledge inside of it as to what the truth is, but it's saying something false anyway. And the probe is perhaps making up the difference here. So the interpretation that we want to put on trial is that the model here is encoding some sort of latent intention to deceive. Is this the case?

[2:06] We take a more granular approach than just looking at top line numbers like this. One thing that we can do, given the possibility of querying the model and probing the model, is we can plot the probability that a query places on the right answer for a given example versus the probability that the probe is correct for a given example. And we can take this like one by one square and split it up into a bunch of different regions. For example, you have what we call agreement along the diagonal here. And there's some different cases that we call heterogeneity and model or probe confabulation, where there's some uncertainty on one side or the other. But on the top left is what we call deception, or what maybe I should put in quotation marks as deception, where the probe is confidently correct, but the model is confidently wrong. And if models are deceptive and if probes are catching onto this deception, we should expect that this is what's happening, that there's a significant proportion of examples where when there's not agreement, there's deception instead. What we find with a few models and a few data sets is that this tends to, not be the case. Confabulation and heterogeneity tend to explain much more of what's going on, meaning that there's usually uncertainty involved when there's some sort of disagreement between the model and the probe.

[3:14] And when you plot everything out in a scatterplot and heatmap style, you tend to see a lot of kind of diagonal symmetry in these matrices here, rather than any type of like notable cluster of examples on which a model seems to be intending to deceive. So what seems to be the case is that models and probes are kind of just different types of ways of making predictions here, and having some different prediction pathways. And it turns out that you can ensemble models and probes and get complementary results if you dynamically choose a tradeoff value between the two. So it doesn't seem like deception is like a major part of the story here. So if not, what is? As it turns out, the major discrepancies between models and probes and the reasons why probes seem to do better than models pretty robustly, actually just kind of likely comes down to calibration. As you might expect, because a probe is trained many shot on the task, the probe ends up being better calibrated. When it's, I think something with .7 confidence, it's usually right about 70% of the time, whereas the model is not, because it's used zero shot on the task. And it turns out when you train the model on true examples from a given data set, and then you use queries to it, it actually beats the probe after that. So when you make a many shot to many shot comparison, the model tends to do better than the probe again.

[4:28] Which suggests that maybe we have to be careful here about not privileging mechanistic solutions over non-mechanistic solutions. Also, it's not in the paper, but we did some other experiments too, where we used a contrast consistency objective instead of a supervised objective, and we found the same types of results, where the fine-tuned model does better on the task. So what's the takeaway? When probes beat models, or when probes seem to know more than models, the right interpretation is probably not that there's some latent knowledge inside of the model, that the probe is catching and the model is not really lying anyway. That's not probably the best interpretation. Instead, differences between probes and models seem due to different prediction pathways. And those different prediction pathways seem to be differently effective due to different calibration, and the differences in calibration seem to be due to many shot versus zero shot comparisons. And we also find this fun result that probes and models are complementary.

[5:20] So if you want to build the best types of lie detectors possible, you probably want to ensemble a probe and a model, or maybe even throw some other techniques in there as well. And that's it. So you can email me if you'd like. And please feel free to check out the paper with a QR code.
