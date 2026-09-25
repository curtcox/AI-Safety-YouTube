---
id: "LYqqHLaW30w"
title: "Sanjeev Arora - Emergence of Complex Skills in LLMs (and, do they understand us?)"
url: "https://www.youtube.com/watch?v=LYqqHLaW30w"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 365
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sanjeev Arora - Emergence of Complex Skills in LLMs (and, do they understand us?)

[Watch on YouTube](https://www.youtube.com/watch?v=LYqqHLaW30w) · FAR․AI · 2024-02-08 · 6:05

## Chapters

- 0:00 Introduction to complex skills
- 0:24 Limitations of current methods
- 1:11 The skill mix evaluation
- 3:04 Key findings and world models
- 4:32 Theoretical framework

## Description

```text
Sanjeev Arora - "Emergence of Complex Skills in LLMs (and, do they understand us?)"

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to complex skills

[0:05] This is about emergence of complex skills in LLMs. I'll briefly describe what complex skills are and also relate to whether or not they do understand us. This is based on these two papers. The first one is a theory paper with Anirudh Goyal, and the second one is an experimental evaluation of something called skill mix.

### Limitations of current methods

[0:25] So, just as background, all of us know that there's this ongoing debate about, "Are they just mere stochastic parrots?" "Are they beginning to understand us?" you know, how dangerous it is and so on... 'Stochastic parrots', of course, referring to... Well, some people, I'm not sure how many anymore... say that AI are still just repeat the things they've seen in the training data. And the current evaluations don't really settle the question of whether they are understanding, because the evaluations often have been spammed because of Goodhart's Law. And so there isn't a clear evaluation which, addresses that. So we'll get to that.

### The skill mix evaluation

[1:12] So here's a skill mix evaluation... from that paper that I mentioned, and it starts with N skills, something like this, language skills, T topics. And you randomly select some number of skills, let's say five, and one topic, and ask the chatbot to generate a short piece of text about that topic that exhibits those skills. And, and what you see is that, as you would imagine, as the models get bigger they can do much better. So Llama-2 7B can do ... a little bit. 70B... at least has a interesting metaphor there which it was required to do.

[2:04] And then as you would imagine GPT-4 nails it. So ... you see, here's an example of how the capabilities are increasing with size. Now, here's a point. The skill mix eval ... you can change the number of skills that you ask it to combine. And so it's fair for models of all sizes. OK. Just this K - the number of skills you use - is changed, but you're just asking it to compose them. And by the way, these skills are all taken from Wikipedia. So all models know these skills. It's not unfair to any model. The evaluation is expandable because you can add new skills and topics - not language skills, they could be coding skills or whatever. And the point here is that the number of combinations is very large, right? If you are mixing K skills, the number of skills to the power K becomes very large even for modest K.

### Key findings and world models

[3:05] So that's the point. It's a randomized challenge from a very large set of possibilities. And so the key findings, as hinted in the previous slide, is that, as models get larger, they can combine more skills successfully. GPT-4 really wiped the table among the models we tested. And GPT-4 is able to combine when it's solving for K = 5 (five skills) a good fraction of the time ... but just simple probability calculation skills, and topics that it did not see in the training data. And this calculation is just using the size of the training data, which we assume is about 10 trillion. So that's showing that it's not a stochastic parrot. And actually, by using the same idea of combining a lot of things and asking it to generate text, you can also begin to test chatbots' world model.

[4:03] So for instance, you can give it a instruction like this of some totally random thing... again, a random combination, something about Ancient Mesopotamia, and combining these skills. And it gives some reasonable answer. And actually, Geoff Hinton got to know of this work. And then he wrote to me saying he finds this a very interesting example and he's been mentioning it in his interviews and so on, as an example of world models and understanding

### Theoretical framework

[4:33] in language models. OK. So that was an experimental skill mix evaluation. And it came out of this theory with Anirudh Goyal and where we were trying to recast language modeling in a different way. So we want to bring in the notion of skills in this. And so we think of a corpus as being composed of pieces of text which have some arbitrary probability distribution which we don't know. There are some latent skills which could be language skills, linguistic logic, science, common sense, et cetera. And we assume that skills have a certain probability - background probability - and that there is a bipartite graph which which describes which skills are needed for which piece of text. And the important point here is that a piece of text, if you look at this corpus, the pieces of text are generated using random combinations of K skills. So there are statistical task involving predicting the words or, say, answers to closed questions in the pieces of text.

[5:35] And so the main theory result is that cross-entropy loss, as it goes down in this theoretical framework... skills emerge. 10X scaling of the model implies that you get competence on twice as many skills. K doubles. And from that, it follows that you will get from scaling competence on K tuples of skills that were never seen in the training data. OK. So I'll stop there. Thank you very much.
