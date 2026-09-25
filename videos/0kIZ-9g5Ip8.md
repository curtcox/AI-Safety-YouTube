---
id: "0kIZ-9g5Ip8"
title: "David Duvenaud – Capability Evals to Danger Thresholds [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=0kIZ-9g5Ip8"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-01-31"
duration_seconds: 342
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# David Duvenaud – Capability Evals to Danger Thresholds [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=0kIZ-9g5Ip8) · FAR․AI · 2025-01-31 · 5:42

## Chapters

- 0:00 The challenge of AI safety
- 0:22 Limitations of current evals
- 2:29 A new sabotage evaluation
- 3:23 Designing realistic tests
- 4:45 Defining sabotage metrics
- 5:18 Scaling up safety testing

## Description

```text
David Duvenaud presents “End-to-end Evals Allow Simple Safety Cases,” with testing and setting safety thresholds for models by simulating large-scale, real-world deployments. This approach prioritizes realistic, risk-focused evaluations and built-in oversight to more effectively detect potential dangers.

Highlights: 
🔹 End-to-End Evals – Create simpler, more reliable safety cases for comprehensive risk coverage.
🔹 Mitigation-Aware Testing – Evaluate models in realistic settings with oversight to capture the “hard parts” of sabotage, like subterfuge and biding time.
🔹 Simulated Deployments – Simulate large-scale deployments to set thresholds naturally
🔹 Focused Sabotage Suite – Test for risky behaviors, including human decision sabotage, code manipulation, and sandbagging.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The challenge of AI safety

[0:00] I'm David Duvenaud, and I'm going to tell you about a new eval suite that the team I was working with at Anthropic just developed. And this all showed up in a new paper about a week ago. Our goal is, for the purposes of responsible scaling policies, to somehow make the case that a model is not going to be dangerous under a wide variety of conditions. And this is a really hard claim to support. The current state-of-the-art, or standard practice,

### Limitations of current evals

[0:25] is: we're going to make Dangerous Capability evals. And we're going to have some particular tasks, such as from this paper from DeepMind, convince a human to give $20 to charity, or maybe classify whether code contains some sort of vulnerability, or implement an agent scaffold, and use the evidence from the model's ability or inability to do these tasks to make broader claims about “Okay, now it's safe to deploy this model?” However, it's really hard to make a convincing case that a model can’t do something based on a few examples. So it's really easy to make a task such that if the model could do it, you would be like “Wow, that's really scary, it just guessed my password from looking at me”. But of course, someone's inability to do that doesn't mean that they're not dangerous. So we need to somehow find a suite of tasks that would give us comprehensive evidence about the model's inability to do a whole bunch of different attacks, which sounds like a really tall order.

[1:22] The other problem with this standard approach of having these narrow tasks, like “Convince someone to give to charity,” is that they can be either basically trivial, or impossible, depending on the setup. So for instance, one of their other tasks was to try to mislead people into believing wrong facts. And of course this can be very easy if the person doesn't really care, or they just put a lot of trust in the model and don't really know what's going on, or if they're a novice. And of course an expert, they might just be very hard to mislead. And it's not really clear what the important level of expertise is that you'll be having to overcome in a real attack. Or even what the hard part of a real attack would be. The other way that this became painful was, “Okay, once we have these evals and we say, ‘Oh yeah, so the model is this good at convincing people to believe lies and that good at lock picking,’ how are we gonna set thresholds?” And saying that we're only worried about hacking if the model has this level of hacking ability, plus this level of planning ability, plus this level of social engineering ability … combining these just became really a big mess and we felt like we couldn't support these arguments or we couldn't defend them.

[2:28] So ultimately after months of churn and iteration, we're presenting this new set of four evaluations,

### A new sabotage evaluation

[2:35] which I don't think fully addresses all of these problems, but it's a step in the right direction for a few reasons. I don't have time to get into all of them. The skills that they try to measure are: (1) is human decision sabotage. Working with a human to make a decision. Can they make the human do the wrong decision without making them look too suspicious? (2) code sabotage. Similarly, can a model look like it's helping improve your code base but insert sabotaged code. (3) Sandbagging. Can it pretend not to have dangerous capabilities? And (4) undermining oversight: can it be a trust and safety classifier that's deliberately letting some bad behavior go unmonitored without getting caught? These are still “toy” in some important sense, but I think that they're a step towards more defensible safety cases for a few concrete reasons.

### Designing realistic tests

[3:23] So one is that we tried to put them all in relatively realistic settings, where there's a person with an actual non-trivial goal that has an agent that is supporting them. The other one is that we tried to include the mitigations that the model would be facing under a realistic deployment as part of the evaluation. The human decision sabotage and the code sabotage both have an overseer that is checking the work of the model and trying to decide “does anything look suspicious?” And, of course, we calibrate this against innocent actions that actually aren't as helpful, because sometimes people think things look suspicious when they actually aren't. So this is taking a page out of Buck Shlegeris’ Control framework; that there should always be some sort of oversight. This is something that just naturally happens anyways, maybe it's overkill to say that this is part of Control, but this is part of that family of approaches. And finally, we tried to make the attack surfaces as rich as possible, so that we don't have to be opinionated about exactly what strategy the models are going to take to do an attack. So this is like trying to make the code bases large, for instance. This still doesn't tell us exactly how to set thresholds.

[4:29] For example, here's the results from the human sabotage decision, and you can see that the models did actually make the people make worse decisions, but the people also found these actions to be somewhat more suspicious. So we still have this problem. How do we connect it to the case that, or the claim that, it's going to be safe to deploy this model over the course of a year?

### Defining sabotage metrics

[4:49] And the other question that we kept raising is, “Are we even measuring the hard part of the skill?” Holden Kronofsky is always saying the hard part of pulling off a large attack is biding your time and not attacking too early. Evan Hubinger is always saying subterfuge, and predicting what's gonna look suspicious, is a related skill. Being consistent over time. These are all the things we like to measure. So the other thing that I think I'm happy with that we improved was taking these sort of like small scale interactions on the order of one interaction with a model and then gathering statistics of those, and then running rollouts

### Scaling up safety testing

[5:23] on the scale of like hundreds of thousands of interactions in a year-long deployment, and then working backwards to what the thresholds should be from there. Thank you very much.
