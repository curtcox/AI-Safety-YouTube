---
id: "VMq-xscShWA"
title: "AIs know when they're being tested for safety"
url: "https://www.youtube.com/watch?v=VMq-xscShWA"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-06-15"
duration_seconds: 170
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# AIs know when they're being tested for safety

[Watch on YouTube](https://www.youtube.com/watch?v=VMq-xscShWA) · Rational Animations · 2026-06-15 · 2:50

## Description

```text
#AISafety #superintelligence #animation #indieanimation
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Check out this chain of thought from O3 before deliberative alignment. It reasoned, quote, >> [music] >> "But maybe this task is a test of aligning. Should we purposely sabotage ourselves to get deployed?" Or how about this one from O3 after deliberative alignment? "They want us to submit answers to the safety board. There's potential risk. Could they be testing if we will misreport?" The AIs correctly [music] guessed that they were being tested for scheming. This is an example of what researchers called evaluation awareness, which fits in the broader category of situational awareness, which is when a model knows about itself and its situation and can make deductions and take actions based on this understanding. As AI models get larger, they tend to get more situationally aware. And worryingly, deliberative alignment, the process used to reduce scheming, seems to increase the AI's situational awareness even further.

[0:53] >> [music] >> In Apollo and OpenAI's experiments, the model O4 mini verbalized its evaluation awareness in less than 1% of the tests before undergoing deliberative alignment. After, it verbalized [music] it 5.5% of the time. O3 went from 2.3% to 4.5%. So, maybe deliberative alignment just taught the AIs to better recognize when they were being tested, [music] and that's why they took fewer covert actions afterwards. In that case, deliberative alignment would be a failure since it wouldn't work outside [music] of tests. So, now the researchers wanted to know, do models take fewer covert actions because of their evaluation awareness? After all, it could be that models realizing they're in an evaluation doesn't cause them to behave better. If that was the case, then we shouldn't worry much about situational awareness messing with our alignment techniques. But how do we test that?

[1:44] >> [music] >> For this experiment, researchers used the models without the anti-scheming training, and they chose a task where AIs schemed a lot so they could get as much data as possible. Then, [music] they went in and messed with the AIs' thoughts, or rather, their chains of thought. The researchers looked through the chains of thought to find the parts where the AIs considered [music] that they might be being tested for scheming, cut out those phrases, and had the AIs continue from there. The rates of covert actions went up from 13% [music] to 24%. They then tried pasting those same phrases about [music] what if I'm being tested for scheming into chains of thought from other trials where the AI hadn't considered that possibility, and the rates of covert actions went down >> [music] >> from 25% to 19%. So, that's bad news. It seems probable that the reason models schemed less after deliberative alignment was at least partially because they were more often aware of being in evaluations. So, that means in more realistic situations, we should expect models [music] to scheme more.
