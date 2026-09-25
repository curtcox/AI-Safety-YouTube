---
id: "acAL3Fffn6k"
title: "Tanya Verma - Publicly verifiable governance"
url: "https://www.youtube.com/watch?v=acAL3Fffn6k"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-19"
duration_seconds: 227
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Tanya Verma - Publicly verifiable governance

[Watch on YouTube](https://www.youtube.com/watch?v=acAL3Fffn6k) · FAR․AI · 2026-05-19 · 3:47

## Description

```text
Tanya Verma (Tinfoil) argues that frontier labs are accumulating nation-state capabilities without nation-state accountability, and that AI safety cannot rest on labs auditing themselves. A benevolent dictator is fine until their successor isn't; democratic systems impose overheads but are far more robust. Her proposal borrows the model that already works for FedRAMP, FINRA, the SEC, and the FAA: external auditors with real enforcement responsibility. The technical primitive she sketches is a verifiable clean room built on secure hardware enclaves, where third parties can run checks on frontier models without the lab revealing weights or workloads, and the auditor doesn't reveal their evals either. An AI safety org could test base-model capabilities against private biosecurity evals; governance bodies could co-locate audit agents and safeguard classifiers alongside inference and training, with GPU and TPU attestation providing tamper-proof evidence that the right agent ran on the right device. The incentive cuts both ways: if a child is harmed by a model, the lab can verifiably prove a specific third-party safety check ran. And making safeguards cheap to deploy matters across the board, not just for the most aligned company, since safety only at the frontier isn't safety at all.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Hey everyone, I'm Tanya. I'm the co-founder of Tin Foil. We build verifiably private AI by running models and AI workloads inside secure enclaves. My My belief is that it's not enough for frontier model labs to implement AI controls and governance and it's very important to also ways for external auditors to verify this. Why is this important? I believe the labs are accumulating power that give them nation-state capabilities without nation-state accountability. There is no notion of a judiciary here which is counter to what we have come to expect in a democracy. >> [snorts] >> Largely all AI control and safety work is being delegated to the benevolence of the labs. A benevolent dictator is like quite nice to have but their descendant may not continue to be so. And while democracy imposes overheads that wouldn't exist under a a dictator, it is far more robust of a system. Trust but verify. So we have precedent of compliance with FedRAMP, FINRA, the SEC, so on and so forth.

[1:03] These rely on external auditors and it is as much their responsibility for enforcement as it is the companies. So the question is what this looks like for AI? >> [snorts] >> The idea is that running third-party checks on frontier models without the model provider seeding control and being required to fully reveal their workload or weights. So one way to achieve this is by designing a verifiable clean room primitive using secure hardware enclaves. Suppose you are an AI safety organization, you curate a set of biosecurity evals. You do not wish to share these evals with the labs but you wish to test base model capabilities. With a clean room primitive, you and the model provider could run this experiment in a verifiably private and previously agreed upon way. So taking this a bit further, safety research and governance bodies could develop their own audit agents and safeguard classifiers that are co-located with inference and training workloads.

[2:02] These would continually transmit some pre-specified signal attesting to specific attributes of the workload. Most accelerators such as GPUs and TPUs already [snorts] have attestation capabilities that can provide tamper-proof evidence that a specific audit agent was run and tie that with the serial number of the device. If you know the the device blocks that a particular um organization has received, you can you can implement some pretty robust checks. And the cost and this can also have like relatively minimal cost at runtime. >> [snorts] >> The The labs would further be incentivized to do so because imagine the case that a child was like harmed by a model. They can verifiably prove to the government or concerned parties that a particular third-party child safety check ran and that they were not being malicious.

[2:54] This further incentivizes active development of safeguards by the rest of the world outside labs. It also makes it cheap to deploy and require these safeguards for model companies that may not be quite as interested in spending the necessary time required to develop these safeguards. It is also not enough for just the most aligned company to do so. We should make it cheap for all of them to do so and not just the frontier model providers, but various inference providers and so on and so forth. >> [snorts] >> And this is similar to like how it's it is good to actively encourage democracy in more than just your own country. So, yeah, like this pretty short talk, but come find me after if if you would like to discuss more. Thank you.
