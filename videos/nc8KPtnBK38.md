---
id: "nc8KPtnBK38"
title: "\"Just Predicting Tokens\""
url: "https://www.youtube.com/watch?v=nc8KPtnBK38"
channel: "Robert Miles AI Safety"
channel_id: "UCLB7AzTwc6VFZrBsO2ucBMg"
channel_url: "https://www.youtube.com/channel/UCLB7AzTwc6VFZrBsO2ucBMg"
upload_date: "2026-07-31"
duration_seconds: 125
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/robertmilesai"]
retrieved: "2026-09-24"
---

# "Just Predicting Tokens"

[Watch on YouTube](https://www.youtube.com/watch?v=nc8KPtnBK38) · Robert Miles AI Safety · 2026-07-31 · 2:05

## Description

```text
A sufficiently good next token predictor is a superintelligence
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] People sometimes say that language models just predict the next token, which is kind of true, but that just is doing a lot of work. Like, let's think about the ideal next token predictor, or even just an extremely good next token predictor. It's able to reliably predict the next token of arbitrary internet text, and that's all it does. How smart is that thing? Well, the first thing to note is that it can't just memorize. For example, it will be common in the data to have a table of lots of numbers, and then at the bottom, the sum of all of those numbers. Now, to predict that last token, you need to actually do the addition calculation. There's no way to memorize the sums of every possible list of numbers. There's just way too many of them. So, you have to actually be able to do addition. That's one thing. Correct next token prediction requires certain computational structures. But, addition is not very difficult. A tougher thing to predict might be the result section of a research paper. You could take a paper in, let's say, medicine and have the introduction, the method section, and then the heading results, and then have it generate from there. Now, in order to correctly generate the tokens for the results of this scientific experiment, the system needs to actually be able to think about the things the experiment is about. It needs to have an accurate model of biology and biochemistry to tell if the drug works. Note that this means it has to be significantly smarter than the scientists running the experiment, because the scientists got to actually run the experiment. The next token predictor just has to predict it based only on the methods. And not just that, but what if the scientists made a mistake somewhere? The next token predictor would have to predict that the scientists made a mistake, and exactly which mistake they made, and how that affects the results, and so on. So, a sufficiently good next token predictor is radically superintelligent, far

[1:33] smarter than any human being. Now, obviously, actual language models are not perfect next token predictors. But, the point is that the fact that all it's doing is next token prediction doesn't keep the system from being radically superintelligent. Token prediction is just a task. It doesn't tell you anything about the system that's actually carrying out that task. If you want to talk about what language models can and can't do, you have to talk about the models themselves. You have to talk about things like the transformer architecture. The simple fact that something is predicting the next token doesn't place any meaningful limits on its abilities.
