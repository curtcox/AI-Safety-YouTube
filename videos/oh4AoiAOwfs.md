---
id: "oh4AoiAOwfs"
title: "Bryce Cai - The State and the Science of AI-Bio Evals  [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=oh4AoiAOwfs"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-03"
duration_seconds: 293
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Bryce Cai - The State and the Science of AI-Bio Evals  [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=oh4AoiAOwfs) · FAR․AI · 2026-03-03 · 4:53

## Description

```text
Bryce Cai demonstrates how AI models have rapidly achieved and exceeded human expert performance across multiple biology benchmarks in just two years. His research shows GPT-4o matching median virologist performance on wet lab troubleshooting through the VCT eval, while other models successfully write executable scripts for biological tasks and effectively use tools like AlphaFold. The team has validated AI-generated protocols in actual laboratory settings, confirming these capabilities translate to real-world applications. This advancement demonstrates the double-edged sword of accelerating scientific capabilities, which also potentially democratize dangerous biological expertise. Without proper mitigations, these capabilities could enable novice uplift in biosecurity-relevant domains, potentially allowing bad actors to create novel pandemic threats without requiring traditional PhD-level training.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] So I work on bio evaluations as part of secure bios AI team. Our main goal is to measure biocurity relevant capabilities in frontier models. So the motivation for bioit evals is that we've seen some pretty rapid advancement in the rate of capabilities. And as it turns out this also extends to biology. This is a screenshot from a dashboard that we've been developing where each of these lines corresponds to frontier model performance on one biorlated eval not just ones that we've developed. As you can see the number is going up for all of them. uh on many cases in the past two years uh models have exceeded human expert performance and for many of these evals uh they're pretty much saturated. So this is a pretty exciting time for science but it's also a double-edged sword. Um this could increase the risk of harm from biology deliberate or accidental by making this rare expertise commonplace.

[0:55] Without mitigations, models could provide easy to access novice uplift. And in the very worst case, models could um a misaligned AI system or a bad actor could create a novel pandemic as a catastrophic vector of attack. So, but that being said, one common trend about this entire conversation is that there's a lot of uncertainty as to what models are actually capable of. Secure Bio happens to be one of the few organizations working at this intersection to figure exactly that out. So how do we go about building an eval? Well, when it comes to that, our main goal for one individual eval is to measure one specific capability. Um uh in this in this way um we can put together a suite of evals that measures uh the relevant capabilities for one certain vector of attack. Um these capabilities could be something like bio tool use or wet lab uplift. Um and our hope is that this covers a broad spectrum of threats and if the relevant threat changes in the future um or some other vector of attack becomes more relevant our hope is that we will have the building blocks still to determine what exactly is going on. So let's get into some examples. Um some of you might know about this. This is BCT uh where we give models a scenario of a viology wet lab um question to troubleshoot. We give them the necessary information and we

[2:28] ask them okay in this scenario uh which of these factors should I change which ones are relevant which ones aren't. Um what we find is that models are pretty capable of matching human expert performance. In fact, uh, GPT40 was able to match human the median expert performance of viologists in their narrow area of expertise. Um, so this is one eval that looks pretty similar to other evol. But it's also pretty limited. This only measures um single turn conversations. So what else can we assess? Well, we can also assess an AI agent's ability to carry out bio tasks directly. Um this is uh ABC bench. Another example of a suite of evals where we ask the agents to carry out um or write scripts or protocols for figuring out one-off bio tasks. And what we found is that models at least that those that don't refuse also can match human meeting expert performance. We've even validated some of these uh generated protocols in the wet lab setting themselves.

[3:32] >> [sighs] >> We've also uh developed another suite of eval where we were able to see that AI models are making it easier to use a bio AAI tools like AlphaFold. If you want to know more about this, come by our poster which is right outside that door. Um so how does this integrate into the broader eval and alignment space? Well, one common trend that we've been seeing is that eval trends more broadly uh in other domains also seem to be lining up with bio. So if you have any sense about where capabilities might be going, chances are they also apply to bio and they also apply to our work and we would love to know more. Secondly, uh we spent a lot of time trying to iron out this process so that we're accurately measuring the one capability that we want to measure. Um, so if you want to know more about that, please come talk to us. We also have some really good thoughts about the next generation of eval beyond human expert performance, but that's going to require a new set of tools and a comprehensive conversation about what that will look like. So if you want to know more, if you have any thoughts about bio evals or our work in general, uh, please come see me or my colleagues Jake and Samira. We will be here all week. Thank you.
