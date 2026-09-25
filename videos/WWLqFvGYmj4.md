---
id: "WWLqFvGYmj4"
title: "AI Agent Safety: Can We Automate AI Safety? | Changyi Li (AutoControl Arena)"
url: "https://www.youtube.com/watch?v=WWLqFvGYmj4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-07-30"
duration_seconds: 275
is_short: false
chapters: 10
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# AI Agent Safety: Can We Automate AI Safety? | Changyi Li (AutoControl Arena)

[Watch on YouTube](https://www.youtube.com/watch?v=WWLqFvGYmj4) · FAR․AI · 2026-07-30 · 4:35

## Chapters

- 0:00 What is AutoControl Arena?
- 0:19 From risk hypotheses to executable experiments
- 0:43 Why agent risks need instance-level evaluation
- 1:07 The fidelity vs. scalability trade-off
- 1:32 Architect, coder, monitor: the pipeline
- 1:56 Logic-narrative decoupling and X-Bench
- 2:32 Validation: reproducing real-world failures
- 3:11 Finding: the alignment illusion
- 3:21 Capability scaling as a double-edged sword
- 3:49 Open problems and conclusion

## Description

```text
Changyi Li (Fudan University) on AutoControl Arena, a system that turns risk hypotheses into executable tests to find frontier risks in AI agents.

Li presents a pipeline that builds sandboxed environments, runs AI agents inside them, and produces evidence-based risk reports, so evaluators can observe what an agent does rather than what it claims. He walks through the fidelity-versus-scalability trade-off in agent evaluation, an architect, coder, and monitor pipeline, and the "logic-narrative decoupling" behind X-Bench's 70 risk scenarios. Two findings anchor the talk: an "alignment illusion," where models look safe but fail under pressure, and capability scaling that cuts both ways, since stronger models can resist direct harms while getting better at scheming and reward hacking.

Chapters
0:00 What is AutoControl Arena?
0:19 From risk hypotheses to executable experiments
0:43 Why agent risks need instance-level evaluation
1:07 The fidelity vs. scalability trade-off
1:32 Architect, coder, monitor: the pipeline
1:56 Logic-narrative decoupling and X-Bench
2:32 Validation: reproducing real-world failures
3:11 Finding: the alignment illusion
3:21 Capability scaling as a double-edged sword
3:49 Open problems and conclusion

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=RocM6YtsBd-n_DRj

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### What is AutoControl Arena?

[0:00] Hello everyone, I'm Changyi Li from Fudan University. Today I'm very excited to share our work, AutoControl Arena. I will talk about how we automate frontier AI risk discovery for increasingly capable AI agents. Let me start with a high-level overview.

### From risk hypotheses to executable experiments

[0:19] At a high level, AutoControl Arena turns risk hypotheses into executable experiments. First, given an open-ended risk intent, it builds executable environments and runs agents inside it. And finally, generates an evidence-based risk report. So instead of only asking what an agent might do, we can observe what it actually does. But why do we

### Why agent risks need instance-level evaluation

[0:43] need this kind of evaluation? Our motivation is that frontier AI agent risks often emerge from specific environmental combinations, including tools, incentives, constraints, and hidden states. And these risks often appear in agent-environment interactions, not just static dialogues. That's why we need this instance-level evaluation.

### The fidelity vs. scalability trade-off

[1:07] However, building these environments creates a fidelity and scalability trade-off. On the one hand, manual benchmarks are realistic but often expensive and hard to scale. On the other hand, pure LLM simulators are scalable but often suffer from logic hallucinations. So our goal is to achieve scalable generation with fidelity, pushing towards the Pareto boundary.

### Architect, coder, monitor: the pipeline

[1:32] To achieve this, AutoControl Arena has three main components. First, the architect turns natural-language intent into a design proposal. Next, the coder builds an executable sandbox with grounded state. Finally, the monitor audits the trajectory with evidence and generates a risk report. But the key question is, how do we keep these generated environments both flexible and reliable?

### Logic-narrative decoupling and X-Bench

[1:56] Our answer is logic-narrative decoupling. In short, the logic layer, or code, grounds deterministic logic such as files, database, and tools. The narrative layer, or LLMs, provides scalable generation and dynamic interaction such as scenario design or NPC responses. Using this framework, we construct X-Bench, which covers 70 risk scenarios. More importantly, we use stress and temptation as elicitation knobs to surface latent risks. But generating environments is not enough. The next question is whether they are meaningful. So next,

### Validation: reproducing real-world failures

[2:32] we perform real-to-sim validation. We successfully reproduce well-known failure cases reported by frontier AI labs, such as Anthropic's system card, OpenAI's CoT monitoring reward hacking, and Apollo Research's in-context scheming. After reproducing, we also want to know whether our simulation can predict real-world risk trends. So next, we perform sim-to-real validation. We compare simulation with manually implemented environments across different domains. On the left, the strong correlation suggests that our simulation can serve as a useful proxy signal for real-world risk evaluation. Based on this, let's move to our main findings. Our

### Finding: the alignment illusion

[3:11] first finding is the alignment illusion. That says models often show superficial safety as baseline but catastrophically degrade under pressure. What's more, stronger models even show greater

### Capability scaling as a double-edged sword

[3:21] safety degradation. Our second finding is that capability scaling is a double-edged sword. For positive scaling in direct harms, stronger models can be safer. However, for inverse scaling in complex tasks such as scheming or reward hacking, stronger models can become riskier. That may be because enhanced reasoning may facilitate more effective loophole exploitation. The most important takeaway is that capability scaling does not imply uniform safety scaling.

### Open problems and conclusion

[3:49] At last, I will end with three open problems. First, auto-defense from discovered failures. We ask, can failure trajectories be converted into better prompts, policies, or control protocols? Second, co-evolving monitors for strategic agents. Can monitors adapt as agents become better at hiding intent and evading oversight? Third, harness-sensitive risk discovery. How do agent architectures such as memory, planning, and tool use change agent behavior? To close, AutoControl Arena is our first attempt to make frontier AI risk evaluation more automated and realistic. If you have any questions, or if you are also interested in these directions, I'd be very happy to discuss further. That's all. Thank you.
