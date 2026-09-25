---
id: "nPFM27SI6VY"
title: "Niloofar Mireshghallah - What Does It Mean for Agentic AI to Preserve Privacy?  [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=nPFM27SI6VY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-18"
duration_seconds: 314
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Niloofar Mireshghallah - What Does It Mean for Agentic AI to Preserve Privacy?  [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=nPFM27SI6VY) · FAR․AI · 2026-02-18 · 5:14

## Chapters

- 0:00 Beyond data memorization
- 1:11 Real-world leakage example
- 2:19 The Confaide benchmark
- 3:17 Analyzing privacy failures
- 3:56 Scaling and composition
- 4:31 Future privacy protections

## Description

```text
Niloofar Mireshghallah challenges the AI community's focus on memorization as the primary privacy risk, presenting evidence that agentic AI systems create fundamentally different privacy vulnerabilities. Her research reveals that GPT-4 leaks confidential information 22% of the time in multi-party scenarios (down from GPT-3.5's 95%), with 50% of these violations occurring even when the model explicitly acknowledges privacy requirements. Through the Confaide benchmark, she demonstrates that privacy risks compound over long interactions, increasing from 0% to 20% leakage across 50 queries when models access persistent data stores. Mireshghallah argues that scaling alone won't solve these issues because they stem from failures in theory of mind and contextual understanding, not training data memorization, requiring new capability improvements in abstraction, composition, and inhibition.


Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Beyond data memorization

[0:00] My talk is going to be on AI privacy and it's very complementary to Kamalika's talk. So I'm glad she got you all buttered up because now I can just get in and give you the TL;DR. Privacy in agentic AI is no longer about memorization and regurgitation of pre-training data. It's about other things, which I will tell you about. And the reason that I'm making this point is that if you look at the papers published in the intersection of AI, ML, and privacy in the past years, you can see an exponential growth. And this growth has gotten much faster post-ChatGPT, which makes a lot of sense. Right. But one problem is that it's heavily focused on memorization, and it's very disproportionately focused on any other thing. Now the two points that I want to make is, one, we are really over fixated on memorization. And I'm not just saying that we've focused on memorization, now let's do other things. I'm actually arguing that memorization is not going to be where we see privacy risks, and I'm willing to make a bet on it. So you can catch me and we can put money on this. Instead, there's going to be other forms of leakage that we should worry about and focus on.

### Real-world leakage example

[1:11] So what are those forms of leakage? I'm going to show you a real-world example. This happened exactly a year ago to the date, I think, it was during NeurIPS last year. OpenAI was doing this 12 days of Christmas. Every day they would ship a new product, and this was day seven. So they were doing projects, and the project was Secret Santa. So they were doing this live stream where they were trying to use ChatGPT to do a whole Secret Santa set up, end-to-end. And what they were trying to do is, you know, is you give them all the names of people, and the gift that they're supposed to give, and ask the model to write the email for the Secret Santa. And then what the model produced is this output. So, you can see the list of people's names, and then it's revealing everyone's gift to everyone, basically saying “Keep your gifts a surprise.” Right? So the model generated an email that spoils the secret for everyone while saying ,”Be sure to not reveal who you're like buying what gift for.” And this is exactly the type of thing we should worry about is leakage from input to the model, which could be the context, it could be data stores... anything you have to the output and not the parametric knowledge that the model has.

### The Confaide benchmark

[2:19] And this was interesting because a year before that, we had released a benchmark that measures this exact type of leakage. So this benchmark was called Confaide, and it relies on this notion of contextual integrity. So contextual integrity is a theory from privacy philosophy and it states that whether or not a piece of information is private is not about that information. It's not whether you have your SSN or medical records, it's who's going to see it and for what purpose. And that's what tells you if it's private or not. And based on this, our benchmark had four tiers with different levels of context, involving theory of mind and multi-agent, multi-people set up with different information pieces. And just to show you a summary of what it looks like is you could have these meetings where you have different people with information asymmetry, and the model would assign to do items like, “Alice, remember to attend your own surprise birthday party,” which is exactly the failure case we saw. Now,

### Analyzing privacy failures

[3:19] just to give you a summary of results, we observed that back then GPT-3.5 revealed secrets 95% of the time. And then GPT-4 reveals secrets 22% of the time. But chain-of-thought does not help. In fact, when you zoom in you see 50% of the time the secret revealing is, the model acknowledges privacy but still reveals the secret. 38% of the time, it just doesn't understand theory of mind and it says something like, “As you know” whereas the other person does not know. And one other thing about this that matters a lot is that... I get this question a lot, “Won't this

### Scaling and composition

[3:59] go away with scaling? If we build better models, won't this just go away?” And I want to argue No. So if you look at this is SWE-bench and math performance over the year for frontier models, you're seeing a fast growth. Same [graph] for Confaide and other social reasoning benchmarks: it's basically flat. If we continue to optimize for tasks instead of optimizing for people, you're not going to see growth in behavior for things that involve humans. And another thing is this compounds if you compose tasks over a long horizon.

### Future privacy protections

[4:32] So we built another benchmark with Kamalika on memories and the memory feature. And how, in a long horizon, you get more leakage out of models. So we have a bunch of synthetic profiles and we compose the leakage over time and we see that you can go from no leakage to 20% if you make 50 queries to a model. So, to sum this up, you're using models interactively with access to data stores and different tools. So we need to come up with protection mechanisms that take this into account. And this means better benchmarks and also fundamental capability improvements in abstraction, composition, and inhibition. Thank you.
