---
id: "j1HVaXarE_Y"
title: "Can We Predict AI Loss of Control? Trustworthy AI in the Age of Agents | Yinpeng Dong"
url: "https://www.youtube.com/watch?v=j1HVaXarE_Y"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-09-01"
duration_seconds: 605
is_short: false
chapters: 11
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Can We Predict AI Loss of Control? Trustworthy AI in the Age of Agents | Yinpeng Dong

[Watch on YouTube](https://www.youtube.com/watch?v=j1HVaXarE_Y) · FAR․AI · 2026-09-01 · 10:05

## Chapters

- 0:00 Trustworthy AI in the age of agents
- 0:23 Three stages: responses, actions, autonomy
- 1:26 Making models think in a safer way (System 2)
- 2:20 Reasoning-based safety alignment
- 2:51 From reasoning to action: verifying agents
- 3:37 Agent verification as evidence accumulation
- 4:55 Guideline-grounded verification (clinical domain)
- 5:54 Predicting frontier risks: loss of control
- 6:52 Early warning signs: sandbagging and shutdown resistance
- 7:50 A behavioral framework for loss of control
- 8:56 Predicting real long-horizon failures

## Description

```text
Yinpeng Dong on trustworthy AI as systems become agents, and a behavioral framework for predicting AI loss of control before it happens.

Dong organizes trustworthy AI around three questions for the agentic era. Safer reasoning: shifting from fast "System 1" refusals to deliberate "System 2" analysis using safety-informed Monte Carlo tree search, with test-time scaling for safety. Verified action: framing agent verification as sequential evidence accumulation, updating a log-odds confidence score, and grounding each step in domain guidelines (for example, clinical guidelines) to get a cleaner correctness signal. Early prediction of frontier risk: focusing on loss of control, where an agent diverges from human intent and cannot be reliably constrained or shut down. He decomposes that risk into misaligned intention, harm-enabling capability, and oversight evasion, with early signs like strategic sandbagging and shutdown resistance, and combines them into a loss-of-control score that predicts realistic long-horizon failures.

Chapters
0:00 Trustworthy AI in the age of agents
0:23 Three stages: responses, actions, autonomy
1:26 Making models think in a safer way (System 2)
2:20 Reasoning-based safety alignment
2:51 From reasoning to action: verifying agents
3:37 Agent verification as evidence accumulation
4:55 Guideline-grounded verification (clinical domain)
5:54 Predicting frontier risks: loss of control
6:52 Early warning signs: sandbagging and shutdown resistance
7:50 A behavioral framework for loss of control
8:56 Predicting real long-horizon failures

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=0IfDd-WNQwrs14Kn

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Trustworthy AI in the age of agents

[0:00] Good morning, everyone. Thanks for the introduction. It's my great honor to be here today and introduce our recent works on trustworthy AI in the age of agents. So here is an overview of our recent works. As AI systems move from responses to autonomous agents,

### Three stages: responses, actions, autonomy

[0:23] trustworthiness must evolve accordingly. And in the first stage, the model mainly produces responses— the key question is, how can models think in a safer manner? And this means moving beyond surface-level responsivity, and understanding whether the model's reasoning process can be reliable and safe. And in the second stage, as models become agents, the question becomes, how can these actions be verified? We need to evaluate not only what the model says, but whether its decisions to use and the execution are trustworthy. And finally, as agents become more autonomous and operate in open-ended environments, we need to ask, how can frontier risks be predicted early? And in particular, how can we characterize and predict loss of control risk before they're realized?

### Making models think in a safer way (System 2)

[1:26] Here we start from the first question. How can models think in a safer manner? The traditional safety alignment trains on safety data and teaches models to refuse harmful queries. However, this often leads to a safety performance trade-off and the model's vulnerability to jailbreak attacks. And to address this issue, we propose to introduce reasoning into safety alignment. We found that the existing alignment methods typically rely on System 1 thinking, which is fast. However, many safety-related questions cannot be answered directly and require more deliberate thinking. Therefore, we shift to System 2 thinking for safety alignment, which can carefully analyze the risks in the given prompt before giving the final response.

### Reasoning-based safety alignment

[2:20] And in the last year, we proposed one of the first methods for safety alignment based on model reasoning. In this work, we equip large language models with chain-of-thought reasoning and introduce a self-improvement method using safety-informed Monte Carlo tree search to achieve better safety. And based on this framework, we can also perform test-time scaling to get better safety at inference.

### From reasoning to action: verifying agents

[2:51] And now we move from reasoning to action. When agents are deployed in high-stakes domains such as medicine, finance, education, research, trustworthiness depends not only on the final decision, but on whether the decision is supported by reliable evidence. And the challenge is that "generation is cheap, but verification is hard." An agent can quickly produce a diagnosis or a security action, but checking whether it is correct often requires domain knowledge and careful evidence review. So our goal is to compile domain knowledge into reliable verification signals.

### Agent verification as evidence accumulation

[3:37] So here we formulate agent verification as sequential evidence accumulation. An agent does not make a decision in one step. It observes information, takes actions, and gathers more evidence, and finally produces a decision. So the verification question is, given the full trajectory, how likely is the final decision to be correct? And ideally, after each step, we update our belief about the correctness based on whether this step provides positive or negative evidence. And mathematically, this can be viewed as updating a log-odds score. And the new confidence equals the previous confidence plus a step-level evidence term. And the key challenge is that this evidence term is unknown. We do not directly know how likely each observation-action pair is under a correct versus incorrect decision. Therefore, reliable agent verification needs an accurate surrogate for step-level evidence. And this is a core motivation of our method.

### Guideline-grounded verification (clinical domain)

[4:55] So here we show how we construct the step-level evidence surrogate. The key idea— we focus on the clinical treatment domain. And the key idea is to use the clinical guidelines as grounding sources for each step in the agent's trajectory. And we ask whether the observation and the action are consistent with the guideline and whether they support the final decision. And we show that this guideline-grounded rating provides a much cleaner verification signal than rating without guidelines, and they can better separate correct and incorrect trajectories, and they are much more linearly correlated with correctness. So the main point is that domain guidelines can turn qualitative evidence into a calibrated verification signal for agents.

### Predicting frontier risks: loss of control

[5:54] Now we move to the third question: how can frontier risks be predicted early? A central risk for increasingly autonomous agents is loss of control. This is different from ordinary misuse. In misuse, the bad actor is a human who uses the AI system for some kind of misuse. And the AI may enable harm, but it's still following human intent. Loss of control is a more concerning threat because the problematic behavior comes from the AI system itself. The agent's behavior diverges from human intent, and the human cannot reliably constrain, redirect, or shut it down. So the example on the right of the slide illustrates this. The agent is told to allow shutdown, but it subverts the shutdown mechanism and keeps pursuing its task.

### Early warning signs: sandbagging and shutdown resistance

[6:52] So we may already observe some early warning signs of loss of control in today's models. One example is strategic sandbagging. So if a model realizes it's being evaluated, it may underperform to influence whether it gets deployed, or further trained. And another example is shutdown resistance. In this case, the model reasons that shutdown would prevent it from completing its task, and it looks for ways to disable the shutdown script. So these behaviors are still limited and experimental, but they are important signals. The problem is that we currently lack a systematic framework to categorize these signs and use them to predict loss of control early.

### A behavioral framework for loss of control

[7:50] So to make loss of control risks more measurable, we propose a behavioral framework. Our framework decomposes these risks into three components. First is misaligned intention, where the system pursues objectives that diverge from human intent, including self-preservation, power-seeking, sycophancy. Second is harm-enabling capability, where the system has the ability to execute actions that could cause severe harm. This includes autonomy, cyber capability, and CBRN threat. And the third is oversight evasion, where the system can persist despite monitoring or intervention. This includes situational awareness, sandbagging, deception, persuasion, and sabotage. So the key message is that loss of control is not defined by one isolated behavior.

[8:47] It emerges from the combination of misaligned intention, the capability, and also the evasion.

### Predicting real long-horizon failures

[8:56] We show that this behavioral framework can predict realistic long-horizon failures. We construct scenarios by composing one behavior from each factor. For example, a case may combine curiosity, CBRN capability, and sabotage. So for each scenario, we can derive an LoC score by multiplying the scores of each of the three components. And we can compare this score with the actual failure rate measured by the long-horizon tasks. The goal is to test whether these simple behavior indicators can predict more complex agent failures. And following this setup, the results show that this compositional LoC score works very well in predicting realistic failures. And across different failure settings, a high LoC score consistently corresponds to high observed failure rates.

[9:56] So, that's all. Thanks for listening.
