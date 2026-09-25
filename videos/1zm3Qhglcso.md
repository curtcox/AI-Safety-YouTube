---
id: "1zm3Qhglcso"
title: "Can we test superintelligence alignment before superintelligence exists?"
url: "https://www.youtube.com/watch?v=1zm3Qhglcso"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-03-18"
duration_seconds: 180
is_short: true
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# Can we test superintelligence alignment before superintelligence exists?

[Watch on YouTube](https://www.youtube.com/watch?v=1zm3Qhglcso) · Rational Animations · 2026-03-18 · 3:00

## Description

```text
#aisafety #aialignment #superintelligence
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] One idea is to scale down the problem and try to simulate it using current AI. Instead of humans trying to align AIs smarter than us, we can test whether weak AIs can successfully align AIs smarter than them. Today's best models play the role of superintelligence and weaker ones play the role of humans and we can see what happens. This approach, developed by researchers at OpenAI, offers a way to probe alignment challenges before they become an emergency. Let's return to the coding example again. It stands to reason that it would be difficult to train an AI to never output unsafe code if it codes better than you did. But, how can we test this right now? You can take two AI systems, a strong one, which is good at coding, and a weaker one, which is less good. You then manually carry out safety training on the weaker one to train it to never output unsafe code. Then, rather than manually doing safety training on the stronger system, you have the weaker system take your place. You use the aligned weaker system to run the safety training on the stronger system. The hope is that the stronger system would learn not to output unsafe code, even when the code would have been too complex for the smaller model to evaluate correctly. In that case, the stronger system can be aligned, even though the system doing the safety training is weaker than it. And that would mean that perhaps we can align an AI that's smarter than we are.

[1:21] This idea is called weak to strong generalization. If it holds, it suggests alignment strategies that might scale to future AI systems. The term generalization is used in machine learning to describe when AI systems perform well, even on things that they've never seen before. For example, an AI that recognizes whether an email is spam or not should work even for emails it's never seen before, otherwise it would be useless. Ideally, it should be able to generalize well and handle emails even if they're quite different from any in its training data. In our case, the stronger AI needs to do well even in new situations that are more complex than the simple cases it's seen during training. Since the weak system supervising it can only provide good feedback in the scenarios it understands. But how could a student ever outperform its supervisor?

[2:11] We imagine a good instructor to be a formidable source of knowledge and skill. What can you glean from a supervisor who has only a fraction of your abilities and gives unreliable feedback? For an intuitive sense of this, imagine a 7-year-old teaching his college-age sister to play a board game he's learned at a summer camp. Though the 7-year-old messes up a handful of rules and forgets to mention several others, his older sibling understands the gist of the game and is soon able to outplay her brother. This works because the college student uses her judgment to fill in the gaps in the rules. In some sense, her experience and wit make up for the poor quality of the lesson, so she can infer what her brother was trying to explain.
