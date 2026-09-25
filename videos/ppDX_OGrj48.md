---
id: "ppDX_OGrj48"
title: "Anka Reuel - How do we know what AI can (and can't) do? [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=ppDX_OGrj48"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-12-12"
duration_seconds: 601
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Anka Reuel - How do we know what AI can (and can't) do? [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=ppDX_OGrj48) · FAR․AI · 2025-12-12 · 10:01

## Chapters

- 0:00 The role of AI benchmarks
- 0:47 Benchmarks in AI governance
- 1:20 Assessing benchmark quality
- 2:50 Improving benchmark standards
- 4:31 The importance of validity
- 5:38 Case study on GPQA
- 7:10 Framework for evaluation
- 9:12 Future directions in research

## Description

```text
Anka Reuel's (Stanford) research reveals AI benchmarks are fundamentally broken. Her BetterBench work established 46 best practices and found "significant quality differences between benchmarks that are being used in production right now." Three critical flaws plague current benchmarks: insufficient documentation limiting reproducibility, inability to distinguish signal from noise, and poor design translating abstract concepts to test items. GPQA exemplifies this—its claimed 87% "graduate-level reasoning" performance relies on just 448 multiple choice questions across three domains that don't test reasoning. These measurement failures matter because benchmarks drive real decisions in AI governance (EU AI Act Article 51) and business strategy.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The role of AI benchmarks

[0:00] Thanks for the kind introduction. I'm going to talk today about how do we know what AI can and can't do? A lot of you will probably say something along the lines of testing or evals, and I know many of you are familiar with evals in general. This is what benchmarks, which is one subcategory of evals, looks like from the recent Opus 4.5 launch from Anthropic. You get a bunch of numbers for skills like agentic coding, agentic terminal coding, novel problem solving—specific evidence that companies provide to tell you how good a model is on those skills and then compare that among competitor models.

### Benchmarks in AI governance

[0:47] Benchmarks are becoming increasingly important in different contexts. One is AI governance. For example, in Article 51 in the EU AI Act, they are explicitly mentioned as indicators to determine whether a foundation model has systemic risk or not. If it does, the models and model developers face a lot more regulatory scrutiny and obligations. They're also being used to steer training decisions and for model users to decide which model to try out for different use cases.

### Assessing benchmark quality

[1:20] First takeaway from this talk: not all benchmarks are good benchmarks. Many benchmarks are poorly designed, which makes it hard to tell if results reflect real capabilities and risks. This is something that's not that clear if you're not on the technical side, if you're not actually working with evals. We have a lot of work to do on helping people understand what evals actually mean, what's behind them, and what information you can actually gain from them. We did some work that we published last year at NeurIPS on BetterBench, where we looked into different issues with benchmarks, best practices, and what actually makes a good measurement instrument. We talked to a bunch of people from the evaluation community—model developers, users, benchmark creators—and came up with 46 best practices along the lifecycle of benchmarks from design, implementation, documentation, maintenance, to figure out how to actually create a good benchmark.

[2:28] This was motivated personally because I wanted to build a benchmark one and a half years ago. I was really frustrated because there were almost no good guidelines out there on how to do that well. There was literally one blog post. That was it. So we were trying to fill part of that gap with that work. We used those criteria to score a couple of different popular benchmarks. Unsurprisingly,

### Improving benchmark standards

[2:55] what we found is that there are significant quality differences between benchmarks that are being used in production right now. You see MMLU here, for example, GSM8K, BBQ. In particular, we find significant variation across the different lifecycle stages. Some specific things: there's insufficient implementation and documentation that limits the reproducibility and scrutiny of benchmarks. We often don't even have enough information about the measurement instrument or the benchmark in particular to know whether it's actually sound or not. Secondly, which was one thing I was personally very frustrated with, almost all benchmarks fail to distinguish between signal and noise. This means that when you actually see a benchmark result, you don't even know whether that's capturing actual signal or whether it's capturing random artifact of the measurement process.

[3:57] Finally, there's a lack of design information. Many benchmarks fail to report how the concepts that they claim to test translate to the actual set of test items or tasks that are included in the benchmark. I'll get back to that last point in a second. What we also did as part of the BetterBench work was operationalizing those best practices into a checklist for benchmark creators that has been adopted widely by benchmark creators since then to raise the general quality and standard of benchmarks more broadly.

### The importance of validity

[4:31] The second takeaway of today's talk: don't take benchmark scores at face value. The first one is more about the instrument itself. The second one is about the issue that benchmarks often fail to measure what they claim they measure, and developers' interpretations or evaluation user interpretations can often be very misleading. The general issue here is that we're not putting enough emphasis on validity when we're designing evaluations, in particular when we're making claims based on those evaluations. Validity is the degree to which a test measures what it claims it measures. It comes from a very long line of work on psychometrics, in particular on education and intelligence testing for humans. There's a lot of key principles and good practices on how to establish good testing principles and validity as part of measurement instruments.

[5:37] Coming back to this initial example of the recent 4.5 Opus launch, I think one and a half weeks ago,

### Case study on GPQA

[5:45] I want to zoom in on one of the specific items here: the graduate level reasoning where Anthropic claims—and this is not just Anthropic, a lot of other developers are doing this as well—that graduate level reasoning or good evidence for graduate level reasoning is GPQA. They give you a score of 87% and tell you, hey, that's how good our model is on graduate level reasoning. Let's take a closer look at GPQA. GPQA is a dataset or benchmark of 448 multiple choice questions written by domain experts in biology, physics, and chemistry. The stated goal of the authors is essentially to create methods and study scalable oversight. If you now look at the benchmark and the benchmark's results as, for example, a model developer, you might want to ask, can GPQA be used to accurately capture the construct graduate level reasoning? As an evaluation or model user that looks at this bigger table, you might want to ask, does a high score on GPQA mean that Claude can write my research paper because it's good at graduate level reasoning? Or you might be a different model user thinking about, can Claude help me solve my high school homework? All three claims are trying to make statements based on the same evidence, but they're vastly different claims.

### Framework for evaluation

[7:10] What we're looking at in our work Measurement Meaning, which we're also presenting at NeurIPS workshop if you're around, is this relationship between the object of a claim that you're making, which can either be abstract or measurable or specific—for example here, accuracy or intelligence—the claim that you're making based on that, so here we're thinking about examples like the model can be used as a calculator or the model is intelligent, and then the evidence that's being presented. What you need to do for this triplet of information is figure out are different types of validities satisfied here. You might want to ask, does your evaluation cover all the relevant cases? And then provide evidence for that. Then you have criterion-oriented validity where you're thinking about does your relation correlate with a known standard, is it predictive of real world outcomes? You have construct validity. This one is in particular applicable to abstract constructs that you can't directly measure, where you need to figure out how do I break an abstract thing like reasoning down into measurable components and provide evidence that that breakdown is actually valid?

[8:20] Then you might have something like external validity, where you might ask, does your evaluation generalize across settings? There's a lot of work, a lot of specific pieces that go into the evidentiary standards for each of those types that we're covering in the paper. But these are some general pointers on where evaluations can break down or where the pairing between evaluations and evidence can break down. Coming back to this example, I'm not that convinced that GPQA would actually be a good indicator for graduate level reasoning, because it just tests multiple choice questions, it doesn't test any form of reasoning necessarily, and it's very constrained to just three subdomains. The inference that they're making from evidence to the actual claim, the jump is way too broad.

### Future directions in research

[9:12] I'll leave you with my current take on what I see could be improved in the field. There's a lot of debate on what AI capabilities and risks are, and there's a lot of divergence in how people look at that. I think one of the issues is that our measurement instruments and our evaluation tools are actually broken the way they are. Fortunately, we know how to fix that, or we know at least to make some progress towards fixing that. I'm almost out of time, but we have a couple of works on that at NeurIPS that are going into specific evaluation tools and how to improve them, make them better. I'd be excited to see all of you there. If you're not there, shoot me a message. Thank you.
