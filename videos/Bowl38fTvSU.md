---
id: "Bowl38fTvSU"
title: "Dimitris Papailiopoulos -The challenge of monitoring covert interactions & behavioral shifts in LLMs"
url: "https://www.youtube.com/watch?v=Bowl38fTvSU"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-05"
duration_seconds: 281
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dimitris Papailiopoulos -The challenge of monitoring covert interactions & behavioral shifts in LLMs

[Watch on YouTube](https://www.youtube.com/watch?v=Bowl38fTvSU) · FAR․AI · 2024-02-05 · 4:41

## Description

```text
Dimitris Papailiopoulos - "The challenge of monitoring covert interactions and behavioral shifts in LLM agents."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

[0:04] So who has played with an open LLM so far? Quite a few people. So I guess the point of this talk is that open language models are going to proliferate in a few years. And I think a lot more people are going to be using them. So for example, if you were to look at the HuggingFace open LLM leader board, it's kind of like a rapid increase of their capabilities. They're super easy to run locally and they're rapidly proliferating. Millions of people are actually downloading them right now. And not a lot of the training data details are given to people, right? I don't know if you saw this, I'm sure a lot of people saw this. Mistral: super cool move, they just dropped the magnet link for like a torrent download and nothing else. And a lot of people are playing with it. And you ask, "is this a good idea?" So they play with a model that I know nothing about. And I would say for now it's probably OK. But I want to make the point that in the future, lack of access to full training details is going to be a big challenge for AI safety. And I want to anchor around two points, which is the idea of monitoring for covert communication and also monitoring for adversarial model reprogramming. The first one is the following.

[1:06] Let's say I have these two pieces of text, they're exactly identical with the only difference that on the token level they are different. There's, in fact, a message encoded in the way that I decided to tokenize the second piece of text. So reading just the text, if you will have the human, just overseeing this text, it just looks the same. But on the token level, there's exponential number of messages that you can encode with regards to the ways that you can tokenize that particular message. Now, you may say OK, what's the point? Why is this a big deal? The big deal is that you can actually encode anything on the token level. For example, if your model has access to like, tools and a Python interpreter, you can actually encode obfuscated Python code, that the model could run in an interpreter. And you may say, "Well, this is a little bit science fiction." You can actually create this model. So the main point I want to make is that you can create black API calls. The model sounds like ChatGPT. There is a like a misaligned model within the same API call that decodes the binary message that is like - encoding the tokens and an encoder puts that message as a binary form in the way that the output of ChatGPT is tokenized. And my point is, if you were to see my code, you'd be like, "There is something fishy going on." But if I were to just give you a black box access to the API call, you won be able to tell that there's something going on.

[2:32] So the second challenge is that you can actually also reprogram LLMs and you can do it on a weight level. For example, you can create a model that sounds like good Llama for, I don't know, 1000 interactions and when a keyword shows up, it becomes "bad Llama". And by that, what I mean is that there's a transformer network that almost acts as a like a mixture of expert models. You have the aligned model, you have the misaligned model and when the keyword of, I don't know, timestamp 20:25 hits, the model just starts talking in the misaligned way. And this is not, again, not science fiction, we can actually create the weights of this model to have it be like a Jekyll-Hyde kind of autoregressive model. And again, for this case, if I were to not tell you how I built this model, you wouldn't be able to tell it unless you played with it for an exponential number of rounds.

[3:24] OK. So, so who cares? So let me tell you an example of why I think this is an issue for AI safety, Anon1234-whatever they offer you API calls or the weights for a model that's as good as ChatGPT and it supports tools and function calling and all that, but it's free. Would you take it? And I think, maybe we should think about it a little bit more whether we should take this model or not. This is not the talk against open models or against open source. This is more about: we should think about what kind of mechanisms we will need to make sure that this failure cases don't happen. Traditional alignment tries to kind of like, suppress or encourage behaviors that emerge in the model, but that doesn't stop bad actors from creating misaligned models that are actually based on the foundation of an actually aligned model. And it's unclear how you can sandbox and control for these issues. And I have a sort of naive and silly answer.

[4:17] You have to basically demand full transparency on the entire, training data and training details. And I think, this is not so much a problem right now, but once the future becomes much more exciting in a couple of years and when open source or open weight models proliferate, we'll actually have to think a little bit harder about these issues.
