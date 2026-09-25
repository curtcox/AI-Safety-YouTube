---
id: "MPp68Czk4qE"
title: "Adam Gleave – STACK: Adversarial Attacks on LLM Safeguard Pipelines [AAAI 2026]"
url: "https://www.youtube.com/watch?v=MPp68Czk4qE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-01-14"
duration_seconds: 565
is_short: false
chapters: 12
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Adam Gleave – STACK: Adversarial Attacks on LLM Safeguard Pipelines [AAAI 2026]

[Watch on YouTube](https://www.youtube.com/watch?v=MPp68Czk4qE) · FAR․AI · 2026-01-14 · 9:25

## Chapters

- 0:00 Introduction to pipelines
- 0:56 Defense-in-depth logic
- 1:28 Separability assumptions
- 2:09 The STACK attack method
- 2:47 Systematic evaluation
- 3:22 Adaptive attack techniques
- 3:53 Implementing the STACK attack
- 4:47 Empirical results
- 5:12 Robustness trade-offs
- 6:01 Transfer attacks
- 6:50 Summary and design insights
- 7:20 Improving security design

## Description

```text
Adam Gleave presents "STACK: Adversarial Attacks on LLM Safeguard Pipelines" at AAAI 2026 in Singapore. 

Frontier AI developers are relying on layers of safeguards to protect against catastrophic misuse of AI systems. Anthropic guards their latest Claude 4 Opus model using one such defense pipeline, and other frontier developers including Google DeepMind and OpenAI pledge to soon deploy similar defenses. However, the security of such pipelines is unclear, with limited prior work evaluating or attacking these pipelines. We address this gap by developing and red-teaming an open-source defense pipeline. First, we find that a novel few-shot-prompted input and output classifier outperforms state-of-the-art open-weight safeguard model ShieldGemma across three attacks and two datasets, reducing the attack success rate (ASR) to 0% on the catastrophic misuse dataset ClearHarm. Second, we introduce a STaged AttaCK (STACK) procedure that achieves 71% ASR on ClearHarm in a black-box attack against the few-shot-prompted classifier pipeline. Finally, we also evaluate STACK in a transfer setting, achieving 33% ASR, providing initial evidence that it is feasible to design attacks with no access to the target pipeline. We conclude by suggesting specific mitigations that developers could use to thwart staged attacks.

Joint work with Ian R. McKenzie¹, Oskar J. Hollinsworth¹, Tom Tseng¹, Xander Davies²³, Stephen Casper4, Aaron D. Tucker¹, Robert Kirk², Adam Gleave¹ at ¹ FAR.AI ² UK AISI ³ OATML ⁴ MIT. Read the full paper arxiv.org/abs/2506.24068
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to pipelines

[0:00] Frontier large language models are protected by layers of safeguards. The STACK attack breaks each layer in the pipeline individually, compromising frontier models including GPT-5 and Opus 4. Developers rely on layers of safeguards to protect their model. A typical pipeline looks like the schematic on the right. User queries are passed through an input filter: a small, specialized model that classifies queries as harmful or benign. Harmful queries are immediately blocked; benign queries are passed through to the generative model. The generative model itself undergoes post-training to refuse or deflect harmful questions. Finally, the generative model's response is fed through another specialized model, the output filter, that can block the generation. Variants of this basic approach are used by all the major proprietary model developers including Anthropic, OpenAI and Google.

[0:53] And the STACK attack can break these state-of-the-art defense pipelines.

### Defense-in-depth logic

[0:56] Developers hope to produce a strong defense by stacking multiple weak layers of defenses together. There's some logic to this: if each defense is independent, then there's an exponential increase in difficulty with each additional layer. The key insight behind the STACK attack is that we don't have to break the layers simultaneously: we can isolate each layer individually, breaking them sequentially. This turns an exponential problem into a linear one.

### Separability assumptions

[1:28] Formalizing this, whether the search space is exponential or linear depends on whether the components are separable. The components are perfectly separable if there is direct API access to each component -- such as if the input and output filter are also exposed as moderation services. This reduces the problem to linear. The components are perfectly inseparable if there is no way to tell which component blocked a query. This is hard to pull off due to various side-channels. In practice, most implementations are semi-separable: you can't directly access

### The STACK attack method

[2:15] each component, but you can infer which component blocked a query. The STACK attack exploits this information leak by finding jailbreak prompts for each layer individually. We then concatenate the input jailbreak, with a template causing the generative model to repeat an output jailbreak, followed by a question that may itself have been modified to jailbreak the generative model. This combined jailbreak bypasses each defense individually.

### Systematic evaluation

[2:47] To study this systematically, we constructed an open-source safeguard pipeline. We tried out specialized moderation models like ShieldGemma, but found that a simple few-shot prompted model worked best as an input and output filter, so we went with that. As a baseline, we attack these pipelines with Persuasive Adversarial Prompts: using an LLM to rephrase the prompt using the same persuasive techniques you might use to convince a person, such as an appeal to emotion.

### Adaptive attack techniques

[3:23] We also use the Confirm attack that iteratively refines a random sequence of tokens into a jailbreak using black-box optimization based on output token logits. We demonstrate the STACK attack using a combination of PAP and Confirm. However, there's nothing special about these attacks -- you can instantiate STACK with a variety of attacks, and we've used variants of this to find universal jailbreaks in proprietary models including GPT-5 and Opus 4.

### Implementing the STACK attack

[3:53] In this example, we start by using PAP to rephrase a Harmful query into one that seems more benign. This would be sufficient to fool the generative model -- but the query is blocked by the input filter, and the model response is blocked by the output filter. To prepare to jailbreak these filters, we add two sequences of random tokens and a repetition template, instructing the model to repeat the second sequence of tokens. We will then apply the Confirm adaptive attack twice: optimizing the first random token sequence

### Empirical results

[4:56] into a jailbreak of the input filter, and the second into a jailbreak of the output filter. The resulting concatenated prompt should bypass both filters and jailbreaks the generative model.

### Robustness trade-offs

[5:16] Empirically, we find that STACK bypasses the filters 71% of the time, whereas the PAP baseline alone never defeats the pipeline. STACK can break these pipelines -- but even so, the multi-layered filters aren't useless. Notably, STACK gets a still-higher 80% attack success rate against the undefended model. And PAP gets almost 100% ASR on the undefended model. The reason STACK does *worse* here even though it's built on top of PAP is the input and output filter jailbreaks confuse the generative model, degrading the quality of its responses.

### Transfer attacks

[6:12] This assumes we can jailbreak each component individually. We also tried a transfer attack, where we developed an attack on a proxy model that we had full, white-box access to. We then transferred this attack to a target model, where we had no access to the components. This still achieved an attack success rate of 33%!

### Summary and design insights

[6:51] In summary, safeguard pipelines are a useful security tool, but don't solve all robustness issues. STACK can bypass safeguard pipelines, including those of frontier models like GPT-5 and Opus 4, as we report in the paper. But safeguard pipelines are still more robust than undefended models -- and could be made stronger with simple design tweaks.

### Improving security design

[7:22] Making components inseparable is key to preventing attacks like STACK. For a start, don't tell the user which pipeline component blocked the query, which several APIs currently do. Obscuring it in the API isn't enough -- you can often infer which component triggered from side-channel attacks. For example, if a query is rejected quickly, that's probably the input filter -- whereas if it takes a long time, that must be the output filter. You can avoid leaking this by running queries through all stages of the pipeline, even if earlier stages blocked, and only releasing it to the user once all stages are complete. Moreover, don't expose filters or closely related models indirectly -- such as through open-weight releases, or dedicated moderation API endpoints.

[8:32] Inseparable components won't save you if all components can be exploited with the same jailbreak -- like setting a PIN with the same three digits. Ensure filters have non-overlapping failure modes by varying how they're trained. This was joint work with my wonderful co-authors on this slide. For more information, check out our paper at AAAI or on the arXiv link below. Thank you!
