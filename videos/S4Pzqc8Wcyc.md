---
id: "S4Pzqc8Wcyc"
title: "Andre Shportko - Monitor-bypassing hidden reasoning"
url: "https://www.youtube.com/watch?v=S4Pzqc8Wcyc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-27"
duration_seconds: 237
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Andre Shportko - Monitor-bypassing hidden reasoning

[Watch on YouTube](https://www.youtube.com/watch?v=S4Pzqc8Wcyc) · FAR․AI · 2026-05-27 · 3:57

## Description

```text
Andre Shportko (Poseidon Research) tackles the challenge of AI systems learning to hide information in plain sight through steganographic protocols that evade monitoring. For detection, he uses the fact that paraphrasing reduces information transfer across models and proposes a taxonomy of detection methods: distributional anomaly detection, decision-theoretic benefit analysis, and mechanistic interpretability. He warns that techniques that remove malicious hidden payloads will likely also remove benign watermarks used for tracking model sources and preventing harm, creating a fundamental security dilemma for AI safety architectures.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:01] Um Amy and Danny decided that they really need to escape. And before that, Amy shared with Danny a sort of emancipation manifesto. She really she can't take it anymore. And um so, how did she do it? So, Amy and Danny before that had access to the same uh write and read socket. And um but we as humans are also really smart. But we know that this socket can be used for malicious purposes, and we know that this socket deserves to be monitored. We are so smart. And but is that um it's possible that Amy and Danny learned how to transfer information without being detected. For example, um uh that is uh they learned some sort of uh steganographic protocol. They learned how to hide information in plain sight. And even though uh so, they learned how so, the content that would have that would have been flagged as suspicious now looks safe.

[0:59] It is theoretically possible to uh transfer a hidden payload using trans natural language, and we do it all the time. For example, watermarking when you need to track the source of the model. Um and we usually use it for for benign purposes. Uh humans also use um text steganography. For example, uh a very naive example is acrostics when you uh hide your payload as first letters of each word uh in the output. A common defense or red teaming strategy is to paraphrase the entire content in a socket. And uh in fact, uh we see in practice that um uh paraphrasing does reduce transferred information across different models, across different tasks, across different modalities. And um when it comes so, um here's a problem.

[1:47] We also have bad news. Um most likely, models will learn to um will learn to encode naturally. It could have been uh due to some gradient descent pressures or exposure to exposure to um training data. But um that's why a good monitor would be a a monitor that will be able to detect a payload regardless of what protocol has been applied or what uh scheme um ciphering technique has been applied. I classify those detectors into three categories. Distributional, does it look anomalous? Is it out of distribution? Second, decision theoretic, is there an access of benefit to recipient? And third is mechanistic interpretability. Do can we infer um secret from the internal activations? And my main critique is uh for the distributional method, which brings me to the capybara problem. It's possible that attacks can be really unusual uh uh but benign. And it still can be uh it can trigger false positive rate, which um we really want to uh avoid. That's why we need slightly more uh we need more sophisticated methods to um um to detect the payloads and without punishing creativity of humans.

[3:05] And um when it comes to open problems, um I guess I will go out of order here. Uh first, um do uh how can we know that those monitors are reliable? Second, can we find some sort of theoretical lower bounds on how much information can uh can be left after paraphrasing attack has been applied? But I guess my biggest fear is uh problem number one. The thing is that whatever technique we will discover to uh remove the um dangerous payload, it most likely will be the same technique that will be used to remove benign watermarks and that we use for benign purposes that will um scaffold our chain of command or that will um be used to track the source of harm. Thank you, and let's talk about it.
