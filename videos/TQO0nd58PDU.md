---
id: "TQO0nd58PDU"
title: "Why is AI faithfulness important? | Chirag Agarwal at FAR.AI's alignment workshop"
url: "https://www.youtube.com/watch?v=TQO0nd58PDU"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-04-17"
duration_seconds: 58
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Why is AI faithfulness important? | Chirag Agarwal at FAR.AI's alignment workshop

[Watch on YouTube](https://www.youtube.com/watch?v=TQO0nd58PDU) · FAR․AI · 2025-04-17 · 0:58

## Description

```text
Why is AI faithfulness important? | Chirag Agarwal at FAR.AI's alignment workshop
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Why is faithfulness important? Let us consider this example where we have a LLM agent trained on historical medical records and it can predict whether a patient is epileptic. When asked about an explanation, the LLM correctly says that the white blood cell count of the patient was high. But using simple faithfulness test, we found out that features like number of days since the last visit and the day of the appointment were important features that change the prediction of the LLM agent. These are clearly non-medical factors and relying on them could lead to misguided diagnosis. In our first work, we used three widely known techniques of incontext learning, fine-tuning, and activation editing. And we observed that it led to no significant improvements in faithfulness. Faithfulness essentially ensures that our explanation aligns with the internal behavior of the model. In our final exploration, we try to elicit the hallucination properties for large visual language model. Given an image like this, we ask the model to interpret the dining table and with very high confidence, the model comes up with its own story justifying its response that there is a dining table present in the image where we clearly see in the visual context that there is no dining
