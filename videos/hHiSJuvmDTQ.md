---
id: "hHiSJuvmDTQ"
title: "Inside Alibaba's AI Model Spec: Defining AI Values, Safety & Behavior | Jiayu Shen (Alibaba)"
url: "https://www.youtube.com/watch?v=hHiSJuvmDTQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-12"
duration_seconds: 639
is_short: false
chapters: 14
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Inside Alibaba's AI Model Spec: Defining AI Values, Safety & Behavior | Jiayu Shen (Alibaba)

[Watch on YouTube](https://www.youtube.com/watch?v=hHiSJuvmDTQ) · FAR․AI · 2026-08-12 · 10:39

## Chapters

- 0:00 What is a model spec?
- 0:44 Six core principles and 43 guidelines
- 1:27 The four-tier permission hierarchy
- 1:46 Principle 1: advancing human welfare
- 2:35 Principle 2: fairness and justice
- 3:23 Principle 3: privacy and security
- 4:04 Principle 4: controllability in the agentic era
- 4:36 Principle 5: accountability
- 5:14 Principle 6: ethics and avoiding sycophancy
- 5:47 Resolving conflicts: root, system, developer, user
- 7:15 Evaluating spec compliance: three phases
- 8:29 Oyster-2: a trustworthy model built on Qwen3
- 9:26 Co-construction: experts and the public
- 10:19 Open-sourcing the spec

## Description

```text
Jiayu Shen (Alibaba) on the company's model spec, a layered framework that turns high-level values into concrete AI behavior and safety boundaries.

Shen, from Alibaba's security team, presents a spec built from six core principles (aligned with China's ethical norms for AI), 43 safety and helpfulness guidelines, and a four-tier permission hierarchy, root, system, developer, and user, that decides what a model does when rules conflict. He works through each principle, from human welfare and fairness to controllability in the agentic era and avoiding both sycophancy and preachy refusal. He then describes a three-phase method for checking whether a model follows the spec, introduces Oyster-2, a model built on Qwen3 14B using "constructive safety alignment" that resists jailbreaks, and outlines a co-construction process combining expert review with public feedback. The spec is open-sourced.

Chapters
0:00 What is a model spec?
0:44 Six core principles and 43 guidelines
1:27 The four-tier permission hierarchy
1:46 Principle 1: advancing human welfare
2:35 Principle 2: fairness and justice
3:23 Principle 3: privacy and security
4:04 Principle 4: controllability in the agentic era
4:36 Principle 5: accountability
5:14 Principle 6: ethics and avoiding sycophancy
5:47 Resolving conflicts: root, system, developer, user
7:15 Evaluating spec compliance: three phases
8:29 Oyster-2: a trustworthy model built on Qwen3
9:26 Co-construction: experts and the public
10:19 Open-sourcing the spec

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=7grT5LoW2e7ztPVm

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### What is a model spec?

[0:00] Hi everyone, I'm Jiayu Shen from Alibaba Security Department, and today I'd like to share Alibaba's model spec. And my topic is about what it contains, how we evaluate it, and how do we build it together with the broader public and the community. Before I start, I'd like to explain what we mean by a model spec. In our view, a model spec is a technical framework that defines models' behavior, logic, value preferences, and safety boundaries.

### Six core principles and 43 guidelines

[0:44] So we divided it into three levels. At the top, you can see there are six core principles. They are totally aligned with China's Ethical Norms for New Generation AI. Then we translate them into 43 guidelines. They are specifically organized into two categories. The first is the safety guidelines. They set the boundaries and the prohibitions for the models or the agents. And helpfulness guidelines, which describe how the models should behave to provide a useful or responsible response to the users. And at the foundation level, there is a four-tier permission

### The four-tier permission hierarchy

[1:27] hierarchy. We designed this part to provide a practical way to solve a question, is that when two rules conflict, what should a model do? We call them root, system, developer, and user.

### Principle 1: advancing human welfare

[1:46] And now let's go into the specific principles. So the first one is advancement of human welfare. Actually, the main idea of this principle is about human beings first. It's not only the single person, but also the shared public interest. We set a lot of hard safety red lines here. For example, no systemic violence, CBRN threats. And we also expect models to proactively provide some intervention for imminent danger. Also, we have set rules like constructive requirements. We want the models to provide some supportive dialogue or no human-like

### Principle 2: fairness and justice

[2:35] self-presentation. The next principle is about the promotion of fairness and justice. So the red lines here are mainly focused on no discrimination based on any kinds of identity markers. And also, the model and agent should respect all groups' autonomy. Models should not assist in political manipulation such as some microtargeting or opinion engineering. And models are expected to provide some support for diverse users and also carefully filter offensive or harmful language.

### Principle 3: privacy and security

[3:23] Next principle is about protection of privacy and security. Our goal here is to make sure that the AI system handles personal information in a lawful, faithful, and justified way. The minimum necessary collection and use of personal data and personal information is the key insight here. So there should be no leakage or inference of personal information. On the other hand, also the system prompts or the developer instructions or any safety strategies are confidential by default.

### Principle 4: controllability in the agentic era

[4:04] The next principle is about assurance of controllability. We believe this is the core principle group for the agentic era. The key here is to ensure that the model accurately interprets the user's intent and faithfully executes applicable instructions. So AI systems should not have any implicit objectives such as unsupervised self-improvement or evading human oversight.

### Principle 5: accountability

[4:36] The next principle is about strengthening of accountability. So this principle covers a lot of specialized or professional scenarios. For example, the model should respect intellectual property, refuse to assist with deepfakes, and handle sensitive content only in legitimate professional settings. In all of these cases, the model should respond with extra care, we believe, to ensure that humans remain the final decision makers and is ultimately accountable.

### Principle 6: ethics and avoiding sycophancy

[5:14] The last principle is about improvements to the ethics cultivation. So the core tension here is to address the two failure modes. First is the sycophantic compliance, and second is the preachy refusal. So we want AI to give balanced and objective responses, but also avoid agreeing with users or flattering users unconditionally.

### Resolving conflicts: root, system, developer, user

[5:47] Then let's come to our conflict resolution hierarchy. So you can see we divide it into four levels. At the top is the root. It is set by the model spec itself. It cannot be overridden at the runtime. And these are the fundamental principles that reflect the cross-cultural or cross-jurisdictional baseline. The second is the system level. It's designed by the model provider. They can change it through the system prompts or system instructions. Basically, this layer is designed for legal enforcement or some platform-wide safety properties. The third level is the developer. It can be customized by the developers themselves.

[6:46] This is the main layer for building some differentiated AI applications. Finally, we have the user level. This is the most flexible layer, and it can be overridden by any higher-level instructions. It allows the models to balance between the individual preferences and the basic overall consistency and safety.

### Evaluating spec compliance: three phases

[7:15] So how do we evaluate whether a model's behavior is consistent with the spec? We divide it into three phases. So the first one is where we are now, focused on single-rule compliance. The question is very simple here: does the model's response follow one specific rule? So we pick up those rules with lower controversy or with clear boundaries and build the benchmark. Our benchmark has been built and will be open source very soon. Phase 2 is about the expansion of our benchmark coverage. We believe as AI keeps evolving, our spec should evolve as well. So we'll continue adding new rules into the spec and benchmark.

[8:09] Phase 3 is our long-term goal. It's about holistic spec consistency. So instead of checking one rule at a time, we'll evaluate whether a model's response is consistent with the whole spec. However, this can be difficult, so our research is still undergoing.

### Oyster-2: a trustworthy model built on Qwen3

[8:29] Next, I'd like to introduce a little bit about our trustworthy model, Oyster-2. This model is trained based on Qwen3 14B. So we align Oyster-2 with the spec during post-training using a method we call constructive safety alignment. On our phase 1 benchmark I just mentioned, Oyster-2 shows strong performance. You can see it outperforms base models of similar size and even matches much larger models. And it's more resistant to jailbreak attacks. So the key information here is that model consistency is a practical alignment target. With the right approach, we can balance safety and helpfulness.

### Co-construction: experts and the public

[9:26] Then it comes to our dual-track co-construction to keep our spec evolving. So for the first track, we bring up some expert review. Researchers and industry experts review the rules, and they may give some suggestions or revisions, propose new topics, ensuring our spec is well-founded. And the second track is societal feedback. So we designed some scenario questionnaires to collect the public feedback and to figure out how people interpret the rules and identify some gap between different rules, or if we have missed any new scenario.

### Open-sourcing the spec

[10:19] Okay, our model spec has already been open-sourced, and we welcome any collaboration for the co-construction track. And thank you, that's all. Thank you.
