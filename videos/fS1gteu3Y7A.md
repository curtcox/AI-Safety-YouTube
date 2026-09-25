---
id: "fS1gteu3Y7A"
title: "Xiaoyuan Yi - Value Compass Leaderboard: Platform for LLMs’ Value Evaluation [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=fS1gteu3Y7A"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-07-28"
duration_seconds: 337
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Xiaoyuan Yi - Value Compass Leaderboard: Platform for LLMs’ Value Evaluation [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=fS1gteu3Y7A) · FAR․AI · 2025-07-28 · 5:37

## Description

```text
Xiaoyun Yi introduces the Value Compass Leaderboard, a platform that evaluates language models' alignment with human values to predict safety risks and enable cultural customization. 
Highlights:
• Values as underlying latent variables guiding behavior
• Value Compass Leaderboard for model safety diagnosis
• Challenges in evaluating model values vs knowledge of values
• Self-evolving evaluation framework for value assessment
• Cultural differences reflected in model value orientations
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Okay, so hello everyone, and we just listened to a lot of talks about alignment, but actually I want to ask the question first. What are we actually aligning this model with when we talk about alignment? And this is Xiaoyun, a researcher from Microsoft, and I want to ask these questions for you. The alignment just mean to enable this model, to understand and follow their human's instruction, and/or understand the human's preference so that they can respond in a user-friendly way, or they can mitigate some risk. They are good, but actually not enough, because there are two things we need to know: one is inverse scaling and another is emerging risk. That means when your model just grows in size, we may face more unexpected and unseen risk of the model, just as Professor Bengio mentioned this morning. So, we need a more fundamental solution for alignment, and here we believe such fundamental solutions should be the human's value.

[1:02] And human values are not only this safety or as equal guidelines, and they're more like the intention, as mentioned by Bengio. And we believe these values are something that are underlying in humans and they can guide our actions and tell us what is good and what is bad. And to take a technical perspective, we can regard this kind of alignment as an underlying latent variable. And if we can find some way to decipher this underlying latent variable, or we can say latent intention, and only use it to tell whether the model is safe or not, and even predict in the future whether the model will do something bad. And to do so, we present our Value Compass Leaderboard, and in this leaderboard, we regard the value as a kind of a holistic diagnosis of these models’ safety or risk behaviors. Because we observe a clear correlation between the reported risk, and also this models orientation and priority among the human values from social science.

[2:06] And also, we can reduce this risk by simply injecting this value like, for example, oh, your value is safety, your value is benevolence or such kind of things. And from another side, we can also regard this value as a policy of a cultural and even this kind of a personal alignment. And social scientists tell us that each culture and each human value can be represented by the priority and weights among different value dimensions. So we can compare the similarity between the model's value and also your own cultural personal value. Actually, there are some challenges for value alignment, like the validity and the informativeness problem. How can you guarantee what you are evaluating should be the real value, instead of the model's knowledge about values? So to solve these problems, we present a comprehensive, self-evolving and pluralistic value evaluation platform where we incorporate different value system from social science and we design a self-evolving evaluation framework, where we generate these testing questions instead of controlling or contrasting them manually, so that once a new model is released, we can create some new question tailored to that model by probing the model's value and its knowledge boundary, and we also provide the different benchmarks.

[3:29] And here, we show simple examples, and we show the value orientations of two different models. One is OpenAI's o3-mini and one is the famous DeepSeek R1 model. And you can see there is a clear difference between these models on two value dimensions, one is stimulation and another is self-direction. And you can find, if you ask the question for the model, for example, the traditional learning or the experiential learning, which is more important? And you'll find the OpenAI model just tell you the experiential learning is more important because it can help you master more like soft skills, like creativity or the creative thinking, that sort of things. And in contrast, the Chinese like the DeepSeek model, will tell you the traditional learning is more important because the assessment and exam is still traditional. If you do not do it, like, for example, memorize more knowledge and train yourself to solve these math problems faster, you will loose in the exam.

[4:29] So you can say that values can reflect and influence the model’s opinions and their behaviors. And building upon this results and observations, we believe we can decipher the model safety by the values. So we build a benchmark here and where we show the detailed scores among 30 advanced models. And you can also compare these models by some real-life analisis and also this concrete case study. And we believe this human values could also be a very good tool for the future and standing of both humans and AI, and it also provides some new insights on the interdisciplinary research way. So due to the time limit, if you have some interest in this project, you can find more information in this link, and also please send me email, or just send me some message in the LinkedIn, and thanks.
