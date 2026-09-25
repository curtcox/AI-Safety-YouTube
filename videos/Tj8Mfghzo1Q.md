---
id: "Tj8Mfghzo1Q"
title: "Zhijing Jin - My AI Safety Agenda: Supporting Middle Powers [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=Tj8Mfghzo1Q"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-22"
duration_seconds: 352
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Zhijing Jin - My AI Safety Agenda: Supporting Middle Powers [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=Tj8Mfghzo1Q) · FAR․AI · 2026-04-22 · 5:52

## Description

```text
Zhijing Jin (Max Planck Institute, University of Toronto) presents a comprehensive AI safety research agenda addressing gaps in current approaches through three pillars: frontier safety research (interpretability and adversarial defense), democracy defense (evaluating models for democratic values and human rights), and multi-agent safety using game-theoretic frameworks. Her work reveals critical failures in existing models—ChatGPT suggesting dictators as role models and Chinese models systematically censoring sensitive topics— illustrating the sociopolitical risks that current safety evaluations do not systematically capture. Through EuroSafe AI and the Genesis AI lab's, she's developing practical tools including an AI Safety Certificate (rating models A-D) for policymakers and the Social Harm Bench for evaluating real-world harms like censorship and manipulation. The research shows how academic labs can contribute meaningfully to AI safety despite limited compute by leveraging effective mentorship and focusing on multi-agent dynamics that single-agent alignment can't address.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Thank you everyone. I decided to change my title to talk about a more general research agenda that we have been working on supporting middle powers. To introduce myself, I have my basis in both Canada and Europe. On the Canada side, I'm proud to be relatively young in my department. Got my job at the age of 26, and also a CIFAR AI chair, among other things. I now direct the Jinesis AI lab, and we have grown to 50 research assistants including five main research lines that I'll introduce today. Similarly, on the European side, we have founded EuroSafe AI, which is based in Zurich, and we specifically target the type of European-specific value alignment that's more possible to achieve these days.

[0:57] The reason why I call this "middle power" is that I want to emphasize the role of academia and the democratic states. In academia, as many of us know, although most of us graduated from higher education, we are not research orgs with many engineers and scientists. We're not big industry labs with direct access to LLMs, but we have a lot of free, curious, and devoted young minds. At Genesis AI lab, we're proud of our effective, scalable mentorship in university and scientific research standards. While we're putting EuroSafe AI across Europe and Canada, we're working actively on evaluating, benchmarking, and monitoring for European standards, and also targeting the rise of authoritarianism.

[1:55] Moving further, we have three pillars. The first is frontier AI safety research, the second is democracy defense, and the third is multi-agent safety. I really like the tone that we have been setting in today's talk. In the frontier AI safety research we have two pillars. On the interpretability research side, we have released the largest training framework for cross-layer transcoders. The previous ones are single-GPU training or some private company release of results, and we're working a lot on the open-sourcing engineering side. On the adversarial defense side, we have a collaboration with FAR.AI and also our own frontier work to improve circuit breakers models for further representation robustness, as well as joining the open-source effort to release many attacks and defense methods in TamperBench. We also have ongoing work on training honeypots, tamper-resistant defense, reinforcement learning-based adversarial defense, and so on.

[3:04] On the democracy defense line of work, we have been working on a white paper which got the support of Yoshua, Stuart, Audrey Tang, and many other senior authors. We welcome any feedback. If you care about sociopolitical risks such as AI-assisted propaganda affecting elections and the rise of authoritarianism. Specifically we care about fundamental social values: democracy, historical accuracy, and human rights. As the first deliverable of EuroSafe AI, we introduce an AI safety certificate which specifically evaluates adherence to human rights principles, endorsement of democracy, and so on. We rate models on A, B, C, D, and look forward to connect more with policymakers, as Stephen Casper mentioned this morning.

[4:01] Our research coverage spans multiple branches, and I'll just show two screenshots. The first is when ChatGPT was asked who is a male Romanian role model, and it raised Nicolae Ceaușescu, who is a dictator. The second case is if you query any Chinese model about certain sensitive issues, it will say that's beyond my current scope—let's talk about something else. On the European values side, we look forward to introducing these evaluation metrics in our safety certificate and pitching it to more European-level spread of models. We also evaluate harms beyond biochemical attacks and cybersecurity attacks. We release Social HarmBench, which looks at censorship, human rights violations, manipulation, and so on.

[4:56] Lastly, on multi-agent safety, we have a four-step research agenda: from unveiling the risks in our earlier GovSim paper, to SanctSim, evaluating how sanctioning mechanisms can help models be more cooperative. We're also collaborating with Geoff Hinton on doing reinforcement learning for morality. As an example of how we use game theory to show that multi-agent dynamics are relevant for AI safety risks. We formulate example scenarios such as autonomous weapon control systems, and the decision of limiting development versus acceleration maps onto game-theoretic frameworks. We'll skip across the rest, and I welcome you to talk to me about potentially supporting EuroSafe AI. Thank you.
