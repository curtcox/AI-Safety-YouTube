---
id: "UB3Vilf2gD4"
title: "Tina Morrison - Verifiable Compute & Building Trust in Agentic Supply Chains [Technical AI Policy]"
url: "https://www.youtube.com/watch?v=UB3Vilf2gD4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-11-15"
duration_seconds: 328
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Tina Morrison - Verifiable Compute & Building Trust in Agentic Supply Chains [Technical AI Policy]

[Watch on YouTube](https://www.youtube.com/watch?v=UB3Vilf2gD4) · FAR․AI · 2025-11-15 · 5:28

## Description

```text
Tina Morrison explains how tamper-proof certificates in AI processes can address supply chain attacks and ensure regulatory compliance. 

Highlights:
Current healthcare regulation relies on low-tech verification methods
91% of enterprises experienced software supply chain attacks
Verifiable compute provides proof of governance and correctness
Verifiable compute adds minimal computational overhead costs

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Good afternoon, everyone. I'm Tina Morrison. I'm a mechanical engineer and applied mathematician. I've been working in numerical methods for more than 20 years and building trust for adoption of computer simulation through policy and credibility risk assessment frameworks and standard approaches. I just recently left a 17-year career in the federal government to join EQTYLab, a technology startup ushering in this new era of compute. I came from a safety-critical sector of healthcare where, as a regulator, we relied on social trust with the entities that we regulate. Today, those entities submit test reports to us, for example, still in the form of PDFs. You can imagine how challenging this is going to be when we think about AI as a part of their workflow. In fact, many of them actually submit screenshots and then put them in PDFs.

[1:01] You can imagine the challenge of verifying anything that they've actually done. It makes it more difficult to actually do our job to enforce and regulate that industry. With more complex digital health technologies being developed with larger amounts of protected data from hospital systems across the world, the question is: can we still rely on social trust to regulate health technologies embedded with AI and deployed for patient care? I learned about this concept of verifiable compute just a few months ago when EQTYLab came out of stealth mode in December after completing a project with both NVIDIA and Intel to embed their verifiable compute software on the next generation of chips from both those companies that are coming out this year. So this will enable verifiable compute in those TEEs that Oni mentioned to you and several others. So we can now harness this hardware root of trust to produce tamper-proof certificates of authenticity for any process, including AI processes. Why is this important?

[2:05] Over the last 12 months, 91% of public sector and commercial enterprises were hit with software supply chain attacks. And moreover, there have been several high-profile supply chain attacks to prominent AI companies—companies that have not yet been able to establish a SLSA level three until now. So we introduce verifiable compute to complement the need to support private cloud compute, where the request is that security researchers must be able to verify the security and privacy guarantees of private cloud compute. Conventional attestations in TEE enable proof of confidentiality and proof of environment, and our verifiable compute solution complements that with the added proof of governance, correctness, and computation. It verifies compute actions in the TEE. For AI models developed on next-generation chip technology. They can verify the data in the AI workflow, what code it was run with, where it was executed, by whom, and it can align with the policies such that the output it generates is secure and private.

[3:18] Harnessing cryptographic digests providing the capability to string together hashes to tell a verified story. I'm going to briefly demonstrate this with a healthcare example in medical imaging, so working on the front line of brain-computer interface security and privacy is crucial. We demonstrate cryptographic proof of the AI model pipeline for MindEye 2 with verified benchmarks that we verified without needing to reproduce the pipeline. And we offered privacy protection by demonstrating verification without sharing the information to a third-party auditor. So this is the snapshot of our tool called Lineage Explorer. This is a visual interactive tool that enables the user or auditor to see all aspects of the pipeline. These details are stored in a JSON manifest, but it doesn't have the details about the actual details of the model or the data itself from the training, tuning, benchmarks, and inference, where the compute costs for verifiable compute are only 10% of the compute asset.

[4:23] I know there's some other technology that's being developed in this space which is much more computationally intensive. From these close-ups, we verified that the computes were completed on both Intel and NVIDIA chips in North Carolina. What the model data were trained on. We verified the successful benchmarks that are in blue with this electronic ledger, proving that the AI output is both genuine and secure. With this capability, we offer rapid compliance with combined AI policies like, for example, the EU AI Act and auditable safeguards providing end-to-end confidentiality and verifiability. So verifiable AI establishing integrity across the entire AI lifecycle. This is not my area of expertise, so thanks for your patience as I shared my remarks with you, but I'd be happy to answer questions after the session. Thanks so much.
