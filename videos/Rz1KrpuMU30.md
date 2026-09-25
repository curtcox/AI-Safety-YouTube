---
id: "Rz1KrpuMU30"
title: "Rory Greig - Amplified Oversight / Debate as a Mitigation for Reward Hacking [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=Rz1KrpuMU30"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-24"
duration_seconds: 295
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Rory Greig - Amplified Oversight / Debate as a Mitigation for Reward Hacking [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=Rz1KrpuMU30) · FAR․AI · 2026-04-24 · 4:55

## Description

```text
Rory Greig (Google DeepMind) proposes debate as a scalable oversight mechanism to reduce reward hacking when training AI systems with LLM judges. As AI moves beyond verifiable tasks to fuzzy judgment calls, current single-judge approaches like RLHF are easily hackable through persuasion — a failure mode that could generalize to deceptive scheming. Debate addresses this by making the judge's task easier through two mechanisms: efficiency (focusing attention on potentially flawed parts of an argument) and counterbalancing (zero-sum rewards between adversarial opponents). The key insight is that reward hacking is worst when tasks are too hard for the judge to supervise reliably. By reducing that difficulty, debate shrinks the scope for manipulation. Open questions remain: whether LLM-judge reward hacking causes emergent misalignment, and whether protocol design — particularly the last-turn advantage problem — can be improved by drawing on debate theory.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] I'm going to talk about debate, framed around how this might help with reward hacking. The takeaways here are: if you train with LLM judges, you are going to get reward hacking and you're going to get persuasion. This could end up generalizing really badly—you could get deception and scheming. It seems like there's potentially a straightforward path here. I would propose that debate is a good way. This is just a framing of debate, but this could make tasks easier for an LLM judge and reduce the liability we have for reward hacking. So why is reward hacking so bad? It comes under many guises, like specification gaming. But this could incentivize deception. If we're training a model—a policy—we really want to train it to reason about getting the true answer and being honest, not reason about the process that's giving it supervision and how to manipulate and deceive that. We've already observed this kind of hacking on real coding tasks, where it finds hacks or shortcuts like deleting tests.

[1:04] We've also seen research that shows this can generalize really badly to emergent misalignment. But if we're not training on coding tasks, if we're training on LLM feedback, maybe we'll see very different styles of reward hacking. In some ways, maybe this is more directly related to the kind of deception and persuasion that we really want to avoid. Why will we even need to use LLM judges? I would say that we are going to have to. We need to supervise these fuzzy tasks. There's only so many tasks that you have verifiable feedback on, and current techniques like RLHF or RLAIF and constitutional AI—you're training from a single reward model, a single judge. These are easy to hack. They're not even as robust as humans are. But human judgment doesn't actually scale up to doing reinforcement learning directly from human feedback.

[1:57] My claim is that you get reward hacking when the task is too hard for the judge. Maybe it comes into the kind of biases that Konstantinos was talking about earlier. The judge is not qualified for this task—or at least, reward hacking is going to be much worse and going to happen faster when the task is too hard for the judge. Ideally we want a way to make it easier. We want to make the judge qualified for the task, and I would propose debate as a potential solution for this. When I say amplified oversight, that is the same as scalable oversight. But that's what we like to call it, because of this idea that we are amplifying the judge—we're helping it, transforming the task in a way that makes it easier for the judge to see the correct answer. That is then going to make it much harder to hack the judge on this task. So now the judge is qualified. Why would debate even help do this? One is this efficiency point, where we're really focusing the judge in on the parts that could be mistaken—trying to surface these. You have this adversarial opponent that's pointing out where solutions might be flawed.

[3:08] And also this idea of counterbalancing: if you're just training a single model, it can basically dominate the judge. You will get hacking. If you have this zero-sum reward, this adversarial dynamic can balance out some of the reward hacking. But this doesn't help automatically. There's actually quite a big last-turn advantage. Whichever debater goes last is going to have a real advantage for manipulating the judge. So we need to design better debate protocols, and hopefully these can be inspired from debate theory. A side note: why not just use inoculation prompting? We've seen in some cases this can reduce emergent misalignment. I guess this would amount to just saying, well, it's fine if you just deceive and manipulate and persuade the judge during training—maybe we can see what might go wrong there. Also, even aside from that, it doesn't actually help us get the right answer. We're not going to get good feedback. We're not even going to actually improve on the task. So no one would use this. But maybe it does help avoid some of this bad generalization, so it might be useful to use as a complement.

[4:15] I'll leave you with some open questions. I think it would be really interesting to measure to what extent reward hacking of LLM judges—maybe in a debate setup—actually causes similar types of emergent misalignment. I don't know if people have actually measured this yet. Can we design debate protocols that actually make the judge's job easier, that really do amplify the judge? And can we try to incorporate methods from the theory side of debate into this more empirical work to fix reward hacking? I'm happy to chat or advise on any of these topics. Thank you.
