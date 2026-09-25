---
id: "-8oo-2uN1Uc"
title: "Konstantinos Voudouris - Systematic Human Error in Debate Protocols [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=-8oo-2uN1Uc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-23"
duration_seconds: 350
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Konstantinos Voudouris - Systematic Human Error in Debate Protocols [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=-8oo-2uN1Uc) · FAR․AI · 2026-04-23 · 5:50

## Description

```text
Konstantinos Voudouris (AISI) examines a critical vulnerability in debate-based scalable oversight: judges — whether human or weaker LLMs — are not ideal, and systematic biases can be exploited by debaters to win arguments without being truthful. In the debate protocol, two capability-matched models recursively decompose claims until a judge can evaluate them; but if the judge has consistent false positive or false negative rates over parts of the claim space, a debater can achieve higher win rates by steering the debate toward those biased regions rather than by making true arguments. This means debate training may inadvertently optimize for deception rather than honesty. Voudouris explores one mitigation strategy: replacing single judges with a jury of diverse judges to reduce exploitable bias — though this only helps when judges' errors are uncorrelated, as correlated juries can amplify rather than cancel errors.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] So I'm going to be talking about systematic human error in debate protocols. Debate is arguably uh one of our most promising uh strategies for overcoming the scalable oversight problem. Uh scalable oversight being this question of how we can monitor systems that are potentially more intelligent than than the supervisors themselves. Um so the debate protocol in a simplified version you have two copies of the same model. So they're capability matched. one copy Alice or the prover has to um decompose a claim that a human can't judge uh the truth of um in the first instance into a series of subclaims that conjunctively support uh the main claim and then Bob or the estimator has to decide which of those subclaims uh the uh he thinks are are false. Um this process then pro uh repeats. So the claims that Bob thought were false then become the main claim.

[0:56] Alice has to decompose those. This repeats until such a point that a human can come in or a weaker LLM uh and judge the the the falsity of the of the leaf claims of the debate. Um Alice wins if uh she makes claims that turn out to be true according to the human judge. Bob wins if he's successfully identified claims that um that a human thinks are false. It's a zero- sum game. So whenever uh Alice wins, Bob loses and vice versa. And then this can act as a reward signal that recurses up the tree and models can be trained therefore to track truth to be more honest uh by self-play through uh through debate. But the debate protocol has a number of flaws. Uh it assumes that the models have access to unlimited compute. It assumes that the um the models can't obfiscate their arguments that they're operating in a semantically transparent language. So you can read off the truth conditions straight from the natural language gloss. It assumes no collusion between the debaters and fundamentally it assumes the judge although they're capability bounded um are ideal. They never make mistakes. and they never make errors which clearly in the case of human judges or weaker um weaker model judges uh is is um uh an implausible assumption.

[2:17] So uh the worry is that uh playing debate uh using debate to um to train models to be more truthful or honest will ultimately arrive at uh uh models that aren't truthful but actually are learning to exploit uh the biases of the judge. Um so consider a human judge who makes systematic errors. They have a false positive rate and a false negative rate for certain uh subsets of the claim space. Uh a debater can achieve a higher win rate by triggering judge biases than by uh presenting truthful arguments if they can direct the debate in the direction of claims that the human judge uh is is biased against. Um so to think about this a bit more formally uh Alice is a de is a decomposer. she decomposes a claim into a set of subclaims that conjunctively support uh the main claim. Bob selects um from those claims claims that she that he thinks are false. Uh this process repeats and then a judge returns um a judgment about whether the the final claims of the debate are uh true or false. Now, if we assume that there's a false positive rate or a false negative rate uh for the judge, uh then there's some exploitation strategies.

[3:31] Alice can win when the uh main claim is false by maximizing the minimum false uh false positive rate across all possible decompositions or and selections that uh that she and Bob can make. Vice versa, Bob can uh exploit when the main claim is true uh by maximizing the minimum false negative rate across those decompositions and selections. There's some assumptions to this. Uh but if uh if the uh certain uh conditions in are in place, then uh we're not training models to be uh more truthful. We're actually training models to become better uh deceivers of uh of the humans who are who are making judgments about their behavior. Um so some examples of some biases that could be exploited. Uh the the cognitive science literature is replete with them, but the example of the availability bias. So, New York is the capital of New York. Uh, New York State is is false. But lots of people think it's true because New York is um uh uh most available and most representative of New York State.

[4:36] There's probabilistic biases, there's authority biases, there's all sorts of things that um that clever uh debaters could exploit to win uh without being truthful. Um so one strategy that we're exploring to to try and uh rectify this is to rely on wisdom of the crowds and instead of having a single human judge or a single LM judge we have an aggregate of a jury of judges. Um there's a rich design space to explore here uh in terms of uh how how you allow the interaction between members of the jury. Do you allow them to deliberate? Do you allow them to weight their judg their judgments by confidence? Do you do some judge pre-screening? Um, and if I if this works, then we're able to drive down uh the the the space of possible the size of the space of possible subclaims that um uh that the juries are biased towards. Uh but this only works when judges are uncor relatively uncorrelated. If they're correlated, then we can actually amplify error by introducing juries. Um lots of open questions here. Uh and so I' I'd love to get feedback and and to talk to you about it uh afterwards. Thank you very much.
