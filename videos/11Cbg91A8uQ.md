---
id: "11Cbg91A8uQ"
title: "Kamalika Chaudhuri - Privacy and Security Challenges in AI Agents  [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=11Cbg91A8uQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-01"
duration_seconds: 349
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Kamalika Chaudhuri - Privacy and Security Challenges in AI Agents  [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=11Cbg91A8uQ) · FAR․AI · 2026-03-01 · 5:49

## Description

```text
Kamalika Chaudhuri reveals how AI privacy challenges shifted from protecting training data in 2015 to preventing agents from misusing sensitive user information today. Current agents violate data minimization principles, accessing sensitive information beyond requirements. System prompts prove ineffective as a mitigation strategy.  With agents handling tax filing and email management, these vulnerabilities demand immediate attention from organizations deploying autonomous systems. Her AgentDAM benchmark shows agents leak irrelevant sensitive information despite task boundaries, and results from WASP demonstrate that modern models achieve "security by incompetence"—they comply with adversarial requests but can't complete adversarial goals, because they are not yet generally competent. 


Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] I'm going to talk about some of the work that we've been doing in our team about the privacy and security challenges in AI agents. So, I don't know how many of you guys were around in 2015. I mean, I was certainly around. And in 2015, what happened was that for the first time, what happened was that machine learning, which was AI at the time, had started getting used. And as a result, things like privacy, security, and various other things like transparency, fairness, uncertainty estimation, things like that, around that time, started to become really important. And fast-forward to 2025. Now, I think we can all agree that the situation has changed a lot. We have these huge models. Question is: do we still need AI privacy and security? And what I'm hoping to convince you today is that Yes. But the problems look very different. The problems have changed quite a bit. And if anything, I hope I can convince you that the problems are actually more serious and more real now.

[1:09] So let's look back quickly at privacy. In 2015, what people were doing is we were looking at data privacy and classification. We had data from users. Some of this data was sensitive, and we were training models on sensitive data. And the kinds of solutions that we were looking at were things like differential privacy or federated learning, where we were trying to ensure that the sensitive, the training data stays private, right? The training data does not leak out of the model. Now fast forward to 2025. Let me try to argue that we have more serious privacy problems. So let me give you an example. Let's just say the example of UI agents that my team has been working with. And what is the idea of UI agents? So let's say you have a model. I can tell the model , “Go through my emails and file the receipts from a NeurIPS trip.” And the model will just do that. Right, but now the problem is this model, or the AI agent, knows a lot of sensitive information about me.

[2:15] It has access to all my email. It has access to not just my Uber receipts for this trip, but for a lot of other things. Is it using this information properly? Is it using it in the context that it should, and not otherwise. Right? And so what we want our agent to do is something called data minimization. And in data minimization, the idea is that your agent will only use the sensitive information that is required for the task and not otherwise. So for example, if I ask it to file my taxes, it will use my Social Security Number, but not if I ask it to file my reimbursements. Right, that's an example. And what we did was we looked at, you know, we built AgentDAM, which is a data minimization benchmark for these kinds of UI agents. And what we found was that the agents do leak a lot of irrelevant, sensitive information. Okay. And, you know, we tried playing with this and a bunch of mitigation techniques through system prompting. And what we did find was that that did not help very much.

[3:21] Okay. So moving on to security. This was kind of what passed as AI security in around 2015. So I don't know if people remember this. So there were these things called adversarial examples. And the idea was that you could take images and you could perturb it a little bit by adding, you can see seemingly random noise like that, and you would get another image, and a lot of the neural network classifiers would just misclassify them. Okay, now fast forward to 2025, AI security is actually a lot more serious. So now we are talking about AI agents. We have something called prompt injection attacks. If you don't know what they are, I will give you one example which was in the news recently, where people put hidden prompts in their paper saying, “Accept this paper.” And if an LLM was reviewing this paper, it would accept it. So that's an example of prompt injection attacks.

[4:21] So there was some prior work on prompt injection attacks, but usually they were in a chatbot setting and they looked at simple attacks. And also the threat models for more complex agents were not well defined. Some assume that an adversary would control a lot of things. They were toy adversarial goals. And obviously there are more realistic benchmarks, but they were behind closed doors. Okay. So what we did was we built WASP, which is a benchmark for prompt injection in web agents. We looked at real adversarial capabilities and real security violations. It's a much more realistic benchmark than what was around. And we managed to test it in an isolated test with various agents in a realistic environment. And I will leave you with the main insight that we found. The main insight that we found is that the adversarial attacks caused the models to stop doing what they were doing. I mean, they kind of divert the models, but the models still don't completely complete the adversarial goals. So in some sense, what we see over here is some sort of what we like to call a ‘security by incompetence,’ right? The models are secure at the moment because they are not very competent.

[5:37] And I will leave you with this theme which I have seen in a lot of this workshop. Thank you.
