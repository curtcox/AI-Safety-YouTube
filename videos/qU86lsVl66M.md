---
id: "qU86lsVl66M"
title: "Francesca Gomez - Threat Analysis to Identify Priorities [ControlConf]"
url: "https://www.youtube.com/watch?v=qU86lsVl66M"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-13"
duration_seconds: 308
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Francesca Gomez - Threat Analysis to Identify Priorities [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=qU86lsVl66M) · FAR․AI · 2025-06-13 · 5:08

## Description

```text
Francesca Gomez (Wiser Human) drew on her background in risk management to outline a systematic threat analysis framework for AI control, emphasizing the necessity for new safeguards and metrics to balance control costs against safety benefits. 

Highlights:
🔹 Threat Analysis Approach: Essential for effective AI control.
🔹 Hazard Identification: Focus on recognizing potential risks.
🔹 Scenario Creation: Anticipating various risk environments.
🔹 Risk Tolerance Setting: Establishing acceptable risk levels.
🔹 Safeguard Evaluation: Assessing current measures for efficacy.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Francesca Gomez: Hi. I'm Francesca, founder of a very recent AI safety org, Wiser Human. Before that, I worked in risk management. Today, I'm going to draw on some insights from that field to take you through an approach for threat analysis to help you select areas to look at with AI control. That was me. The setting which I chose to look at this within is a system whose job it is to risk-assess software deployments, so it synthesizes a lot of different data sources, security testing, evals, inputs, and it outputs a recommendation along with a summary. The first step is to identify hazards. Now a hazard is a condition or a capability that could lead to harm, and these can be all sorts of different things: the level of autonomy, the interfaces, the capabilities, and propensities like scheming.

[1:03] Next, we want to identify harmful impacts. These are things which hazards can lead to which have consequences we want to avoid. You can see some of those on the screen. The impact domain is like the lens that we would assess this through in terms of measuring it and setting the tolerance of what we think is acceptable. We can come up with scenarios that combine a set of hazards and that lead to a harmful impact that we’re trying to avoid. In the example I’ve got where an AI is manipulating the deployment decision, it’s combining things like self-awareness, persuasion, access to a human decision-maker to expand its power. Then we can set a risk tolerance on that to say how comfortable are we around this risk happening? We've set this for less than one percent.

[1:58] What we can do now is actually break that threat down into the different steps that need to be true for this harm to actually materialize. We can take each task or each step and set a likelihood that we think that’s going to occur. There's not an exact science to this, but we could be base that on something like a capability eval. It could be an empirical experiment or even like an assessment from an expert. By combining these, we get a probability range that we think this threat will actually occur. Let’s say we want to reduce that threat. The first thing we can do is look at existing safeguards we have. These might come from information security controls, so like mitigations in an OWASP. There might be safeguards that we used on a human-based process that we can take and apply. Or there might be safeguards that are being used to protect against maybe misuse threats, like classifiers that we could plug in.

[3:01] For our scenario, there's nothing there that’s really going to materially reduce the probability. Maybe we could train the people who are looking at the summaries to better identify persuasion, but we’ve still got a probability of harm that’s outside of our tolerance. Which brings us to AI control. At this point, we can think what do we need to incorporate in terms of developing a new AI control to catch these summaries? We can also back-calculate how effective we need that to be in order to bring our likelihood that this harm is going to occur to under one percent or wherever we've set our tolerance. Now, we have a set of inputs that we can use to actually design a control evaluation that would bring the threat within our tolerance. As well as looking at control effectiveness, it would make sense to measure something like the false positive rate, so how many harmless summaries are also being diverted, and then precision, which is around of all of those diverted summaries, what proportion are harmful?

[4:08] This gives us a set of metrics that we can use to balance the cost of the control protocol, so any degradation to system usefulness and operational overheads against the safety benefit. Great, so quick recap: identify threats by looking at hazards and harmful impacts, combining these into scenarios to set a threat, assigning that a risk tolerance level which could even be linked to something like a deployment policy. Then we looked at what safeguards have we got that we can apply. From there, we can identify the key control gaps and get some actual metrics to feed into a control evaluation. Hope that was helpful. Thank you.
