---
id: "HvTyPzmZU4g"
title: "Fatemeh Ganji  - Application of Cryptographic Primitives in AI Accelerators [Technical AI Policy]"
url: "https://www.youtube.com/watch?v=HvTyPzmZU4g"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-09-24"
duration_seconds: 390
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Fatemeh Ganji  - Application of Cryptographic Primitives in AI Accelerators [Technical AI Policy]

[Watch on YouTube](https://www.youtube.com/watch?v=HvTyPzmZU4g) · FAR․AI · 2025-09-24 · 6:30

## Description

```text
Fatemeh Ganji examines the use of zero-knowledge proof systems to safeguard AI systems against security threats. 

Highlights:
AI models face side-channel and fault attacks
Homomorphic techniques allow encrypted AI computations
Zero-knowledge proofs protect user data during verification
Cryptographic approaches are costly but can scale

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] I would like to ask you this question. How long have we been trying to use crypto? From ancient times. You may have heard about Caesar encryption, and that is where the foundation of cryptography has been laid from Caesar's time. But compared to cryptography, AI is a much more modern technology—newer to us. When we talk about attacks against AI, we know that we have some input going to some model. Small or large, it doesn't matter. A model is trained, and the main goal is to do inference. We know that it is important to keep the assets of the model intact. We want to respect the cost of training put into this model. But there are multiple attacks.

[1:07] You may have heard about side-channel attacks where some observables can leak information about the weights of the model. You may have heard about fault attacks. The same result can be observed—extracting the construction of the model or the weights of the models. There are many different types of attacks. If you attended yesterday's presentation, there was information about sabotage attacks, and those are called backdoor attacks. For years we have seen many types of backdoors like adversarial examples, hardware Trojans, software Trojans. They are all coming under the same umbrella: backdoor attacks. Are they new to us? Didn't we see examples of these attacks before? As cryptographers, we have seen that. And because of that, people have been devising private and secure function evaluation. If I want to bring it now to the domain of AI, it would look like two parties would like to do something—some computation using a trained model.

[2:20] As a user, I don't want my data leaking to the other party, so I want to keep it private. What I can use is secure function evaluation within multiparty computation. For instance, now as an IP owner, I don't want the user to extract information from my model. What I can do is use function evaluation—secure and private function evaluation again within multiparty computation. And perhaps you have heard about this fancy term: fully homomorphic encryption—computing on encrypted data. That can also be done within the context of AI. It is a bit costly compared to the other cases in multiparty computation, but it is doable. I was thinking about the attacks: side-channel attacks, fault attacks, backdoors. Are they possible in this case where everything is encrypted?

[3:20] In the first case, user data is encrypted. In the second case, user data and the model are encrypted. Like the third one, they are still possible. So if I use a laser fault attack, it is still possible to extract some information about user data even if it is encrypted and used within multiparty computation. What about side-channel attacks? If I listen to the chip, even when computing on encrypted data, it could be possible to extract weights of the model when used against encrypted user data. So it is quite scary, right? But there are methods—you can see there are cases where even these physical attacks can be stopped if we use the right cryptographic approach.

[4:14] It is costly, definitely, compared to what you can see. But it is scalable. If someone tells you it is not scalable, it is too costly—reconsider talking to that person. Now let's go back to another question. Can we verify the computation? Can I say that this is my own NVIDIA chip running the same computation that the user promised to do? It is definitely possible. So our team is part of the FlexHack, let's say, builder group. And in that, we have been proposing new techniques brought completely from the crypto approaches. In that, we have a verifier and an AI processor. And the idea is that if the verifier says, "I'm just doing inference on images I want to classify—if it's a dog or cat," then the AI processor would say, "This is the proof"—some back and forth between those two.

[5:21] And finally, the secure processor will say, "Okay, I'm convinced you are really doing classification on the images." You can see that many messages are going on. However, you can make it much more cost-effective by sending just one message between those two parties. You can send short messages from the AI engine to keep it with the right performance metrics that you have in mind. And you can make it a zero-knowledge proof in the sense that when the verifier receives information from the AI engine, no information about user data may leak. So this can be done, and it is part of our job to show it to you. Perhaps next time when we meet, I will have a demo to show you. Thank you. If you have interest in this work, please contact us.

[6:16] You can see all information here. Thanks for your patience.
