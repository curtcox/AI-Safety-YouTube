---
id: "xcU9lZ0QcXI"
title: "Huiqi Deng - Unified Explanation of DNN Inference Logic & Representation [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=xcU9lZ0QcXI"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-09-06"
duration_seconds: 327
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Huiqi Deng - Unified Explanation of DNN Inference Logic & Representation [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=xcU9lZ0QcXI) · FAR․AI · 2025-09-06 · 5:27

## Description

```text
Huiqi Deng demonstrates how Game-Theoretical Interactions can better explain deep neural networks by capturing relantionships between input variables and revealing fundamental inference patterns. 

Highlights:
Current interpretability methods are unreliable
Game-theoritic interactions can explain neural network logic
Interactions enable debugging and optimization of DNNs
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] It's an honor to be here and share some research findings from our group. And I'm Huiqi Deng, an Assistant Professor at Xi’an Jiao Tong University. And my research focuses on explainable AI, which aims to enhance the interpretability and the transparency of AI systems. If you are interested in explainable AI, please feel free to reach out to me. And first, we will begin by introducing some key challenges faced by explainable AI. The first is the reliability of explanations is questionable. First, the faithfulness of explanations is difficult to guarantee, because we do not have the ground truth of explanations.

[0:59] We can see this picture, many popular methods may produce the exactly the same explanations for different classes, such as the cat and dog explanations. And the second is, it's difficult for an explanation method to provide a complete picture of modern reasoning. We can see that current techniques can only identify which regions is important for classification, but they do not clarify which specific features within this region the model will rely on. And the second challenge is, explanations often fail to guide the debugging optimization of the DNN [deep neural network]. Although a few studies try to bridge this gap, but there are core hypothesis, such as "smoother explanations can improve model robustness" lack both theoretical and empirical validation.

[2:11] So, our group found that game-theoretic interactions can address the two challenges to some extent. So, what are game-theoretic interactions in the context of deep learning? They actually represent the cooperation relationship between input variables encoded by the DNN. For example, in fast recognition, we can see that the interaction means the cooperation between eyes, nose, and mouth features. And in an NLP analysis, is the cooperation between words like never, fails and impress. And these interactions will make a numerical effect on the network outputs, which can be quantified by game-theoretic interactions metrics.

[3:05] And we found that these interactions can explain inference logic of the DNNs more faithfully and comprehensively. First, unlike classical method, which can only quantify the contribution of each individual variable, it captures the complex interactions within the DNNs. We can see that the output can be decomposed into the interaction—the sum of interaction effects and it captures the interactions between the words 'never' and 'impressed'. And the double negation between the 'never', 'fails' and 'impressed'. Second, it naturally corresponds to the complete neural functionable, decomposed of the DNN. Third, we found that it reviews the common mechanism of popular attribution explanations.

[4:03] Moreover, due to the functional decomposition properly, we found that each interaction can serve as an elementary inference pattern of DNNs, that means the overall performance of a DNN can be decided by the combined effect of all interactions. And we found that the difficulty of knowing different interactions increases exponentially with their complexity level. And the poor generalization of DNNs often relates to more interaction patterns, and adversary attacks mainly disrupt these complex interactions. And the takeaway message is: Interactions can both provide a more faithful and comprehensive explanation, and it can enable debugging and optimization of DNNs. Thank you.
