---
id: "blALLmPomRM"
title: "Dawn Song - Challenges for AI safety in adversarial settings"
url: "https://www.youtube.com/watch?v=blALLmPomRM"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 399
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dawn Song - Challenges for AI safety in adversarial settings

[Watch on YouTube](https://www.youtube.com/watch?v=blALLmPomRM) · FAR․AI · 2024-02-08 · 6:39

## Chapters

- 0:00 The necessity of AI safety
- 1:20 Adversarial examples in AI
- 2:48 Trustworthiness of LLMs
- 5:10 Challenges and new solutions

## Description

```text
Dawn Song - "Challenges for AI safety in adversarial settings."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The necessity of AI safety

[0:04] Thanks everyone. My name is Dawn Song. I'm also from UC Berkeley. I'm a director at um Berkeley Center for Responsible Decent - Decentralized Intelligence and also affiliated with the CHAI and BAIR. So it's been, it's really exciting to talk about machine learning all the great advancement and so on. But coming from security background, one message I really want to get across to this audience is that as we talk about all the great things machine learning can do, it's really really important to consider the development and deployment of machine learning in the presence of attackers. So history, especially in cybersecurity has really shown that the attackers always follow the footsteps of new technology development or sometimes even lead it and also this time the stake with the AI is even higher as AI can choose among more and more systems, attacker will have a higher and higher incentives um to attack these systems.

[1:04] And also as AI becomes more and more capable, the consequence of misuse by attackers will also become more and more severe. And hence, as we talk about AI safety, it's really important to consider AI safety in the adversarial setting.

### Adversarial examples in AI

[1:20] So, adversarial examples has been shown to be prevalent in deep learning systems. Um but my group has done a lot of work in this space and many uh uh and many other researchers also in this audience have done a lot of work in this space. And pretty much we have shown that adversarial examples are prevalent to essentially all different tasks and model classes in deep learning. And also there are different types of threat models, including black box and white box attacks that can be very effective and even attacks can be effective in the physical real world as well. And it's great to see that the number of papers essentially has increased exponentially in the in the area of adversarial examples. And and also this work has also helped raise a lot of the awareness in the public as well. So some of our work, the artifact from our physical adversarial examples are now actually part of the permanent collection at the Science Museum of London.

[2:20] And also adversarial attacks can happen at different stages of machine learning pipelines including at inference time as well as pre-training and fine-tuning stages. So as we talk about AI safety and AI alignment, it's important to look at what adversarial attacks can do in the setting, in particular, on safety-aligned LLMs.

### Trustworthiness of LLMs

[2:48] Unfortunately, recent work has shown that really the safety-aligned LLMs are pretty brittle under adversarial attacks. This is our recent work DecodingTrust, which is it's the first comprehensive trustworthiness evaluation framework for large language models. And essentially we developed new evaluation datasets as well as new protocols for evaluating trustworthiness across eight different perspectives for trustworthiness for LLMs. Including toxicity, stereotypes, robustness, privacy, and fairness and many others. And in the development of our evaluation framework, we specifically set out to both include the evaluation under benign environments as well as adversarial environments.

[3:47] And our work showed that for these large language models - so for example GPT-4 can perform better under benign environments, for example, than GPT-3.5. But actually in adversarial environments, GPT-4 could actually even be more vulnerable than GPT-3.5, potentially because it's actually better at following instructions. So it's actually in something easier to jailbreak. And given the interest of time I won't go through these - these are examples for these different perspectives. And also you can learn more information at decodingtrust.io and also come to our presentation on Tuesday morning. And also there are other researchers' work demonstrating other types of adversarial attacks, so our work also shows that, for example, the attacks on open source models can be transferred to closed source models.

[4:44] And Zico is going to talk more about their attack on universal adversarial attacks on tomorrow as well. And other works have shown that adversarial attacks multi-model models and also adversarial fine tuning where you can actually use a very few adversarially-designed training examples through fine-tune to completely break safety-aligned LLMs.

### Challenges and new solutions

[5:10] The key message that I want to get across here is that in adversarial attacks, the field has made tremendous, tremendous progress. We have collected and come out with so many different types of attacks. But however, for adversarial defenses, the progress has been extremely slow. So literally, we really don't have effective general adversarial defenses today. And hence, for AI safety, it's really important for the AI to have safety mechanisms to be designed to be resilient against adversarial attacks. And this actually poses a significant challenge for AI safety and I think my time is up so just one word to summarize... ...Partially to address this issue. In some recent work, also with the collaborator here, and Dan Hendrycks led this work with some other collaborators here, we have a new work on representation engineering to essentially look at the internal representations - activations - from the LLM and showing that we can identify certain directions um that can help identify whether the LLM is more honest or is more truthful for reading and using these internal directions, we can also control the model behavior.
