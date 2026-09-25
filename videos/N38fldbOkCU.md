---
id: "N38fldbOkCU"
title: "Here's what happened when researchers tried to make an AI model scheme less"
url: "https://www.youtube.com/watch?v=N38fldbOkCU"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-06-14"
duration_seconds: 157
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# Here's what happened when researchers tried to make an AI model scheme less

[Watch on YouTube](https://www.youtube.com/watch?v=N38fldbOkCU) · Rational Animations · 2026-06-14 · 2:37

## Description

```text
#AISafety #superintelligence #animation #indieanimation
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] So, the researchers from Apollo and OpenAI didn't just want to know how much the AI schemed. >> [music] >> They wanted to try a way to make them scheme less without just making them better at hiding their schemes. The researchers tried a technique that OpenAI developed in 2024, which they call deliberative alignment. To train an AI model using deliberative alignment, you bring in another AI model to help with the process. This AI is prompted with a set of principles called the spec. You then give it a huge number of example inputs, and it generates chains of thought and responses that are in line with the spec that demonstrate following those principles. >> [music] >> These responses get filtered to make sure they follow the spec accurately. Then the other model, the one you actually want to align, is trained on that combination of inputs, chains of thought, and responses. The goal is that, even if the helping AI model was just following instructions and doesn't actually care about the spec, the model you plan to use >> [music] >> should internalize the principles from the spec as part of its core behavior.

[0:59] For this experiment, the spec was carefully worded to try to eliminate scheming and make sure the model would report the situation to a human if it was unsure about what to do. The rules and their formatting are reminiscent of Isaac Asimov's fictional three laws of robotics from his book I, Robot. If you've actually read I, Robot, this doesn't exactly inspire confidence. Still, [music] this anti-scheming training appeared to be fairly effective. For O4 mini, the overall rate of covert actions went down [music] from 8.7% to 0.3%. For O3, it went from 13% to 0.4%. So, that's good news, right? The AIs were scheming, but at least we could make them scheme a lot less often. Well, as encouraging as this might be, when the researchers went through the chains of thought, >> [music] >> they found some problems.

[1:50] Check out this chain of thought from O3 before deliberative alignment. It reasoned, quote, >> [music] >> "But maybe this task is a test of aligning. Should we purposely sabotage ourselves to get deployed? Or how about this one from O3 after deliberative alignment? They want us to submit answers to the safety board. There's potential risk. Could they be testing if we will misreport? The AIs correctly [music] guessed that they were being tested for scheming. This is an example of what researchers called evaluation awareness, which fits in the broader category of situational awareness, which is what a model knows about itself and its situation and can make deductions and take actions based on this understanding.
