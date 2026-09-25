---
id: "LkeDS9fKvRk"
title: "The Alignment Training That Made GPT-2 Maximally Lewd"
url: "https://www.youtube.com/watch?v=LkeDS9fKvRk"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-07-05"
duration_seconds: 175
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# The Alignment Training That Made GPT-2 Maximally Lewd

[Watch on YouTube](https://www.youtube.com/watch?v=LkeDS9fKvRk) · Rational Animations · 2026-07-05 · 2:55

## Description

```text
#aialignment #aisafety #animation #indieanimation
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] The goal of RLHF is to take a basic starting language model, some plain language guidelines, and a small group of humans providing feedback, and produce a new model that follows those guidelines. We can think of this model in training as the apprentice. The apprentice begins the training process as an exact copy of GPT-2. During training, it gets prompts and generates responses, also called continuations. These prompts and continuations are sent to the human evaluators >> [music] >> who rate them based on OpenAI's guidelines. When there are enough ratings, a new kind of model is trained to emulate the human evaluators. The purpose of this model is to tell the apprentice how to write according to the humans' values. So, let's call it the values coach. For each continuation that's been rated, the values coach model is given the prompts and the model's response, and trained to predict the human [music] rating for that response. Since the human evaluators are rating responses based on OpenAI's guidelines, and the values coach is imitating the humans, the values coach learns to tell how good a response is by predicting how the human evaluators would have rated it. There's just one problem. It turns out that the values coach is kind of gullible, and the apprentice [music] can figure out ways to trick it. If the apprentice takes a load of things the values coach likes and mashes them all together into a response, the coach will be very [music] happy with that, even though the text doesn't respond to the actual prompt, doesn't make [music] sense, and in fact isn't even a sentence. The apprentice learns to respond to every prompt with

[1:33] this [music] coach-pleasing gibberish. Yes, happily, please, kind, thank for doggo, apple, helping pie. To prevent [music] this problem, we add one final model to the RLHF process, and that's the old, original, unimproved model. In this case, GPT-2. You can think of this instance of GPT-2 [music] as a second coach, but a grumpy, old-fashioned coach who only cares about the fundamentals, namely generating realistic text. Call it the coherence coach. And because the coherence coach has always been monomaniacally focused on generating coherent text, it's not swayed by the sorts of pleasant nonsense the values coach falls for. Combined, the values coach and the coherence coach form what we'll call a mega coach.

[2:21] Under the mega coach's tutelage, the apprentice [music] must find a way to write coherent, meaningful text that will nonetheless satisfy an approximation of the human's values. In short, using RLHF, OpenAI was trying to optimize GPT-2 so that its responses could be both coherent and good. RLHF was not supposed to create an algorithmic firehose of endless grotesque [music] erotica that would scandalize the human evaluators long into the night. >> [music]
