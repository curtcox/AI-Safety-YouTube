---
id: "hMOs3vbJ2U4"
title: "Xander Davies - Safeguards in 2025+ [AI Security Forum]"
url: "https://www.youtube.com/watch?v=hMOs3vbJ2U4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-04-10"
duration_seconds: 594
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Xander Davies - Safeguards in 2025+ [AI Security Forum]

[Watch on YouTube](https://www.youtube.com/watch?v=hMOs3vbJ2U4) · FAR․AI · 2025-04-10 · 9:54

## Chapters

- 0:00 Introduction to safeguards
- 0:44 Evolving threat landscape
- 2:01 Strategic goals for 2025
- 3:23 Addressing jailbreaking
- 7:11 Preventing third-party attacks
- 8:36 Control, alignment, and closing

## Description

```text
Xander Davies from the UK AISI highlighted the growing need for stronger AI defenses against misuse, detailing their work on securing AI models, addressing cyber threats, and the institute's focus on AI control and alignment, along with an open call for collaboration and job opportunities.

Highlights:
* Escalating need for AI defenses
* Secure closed AI models
* Address third-party AI attacks
* Jailbreaking challenges
* Evaluating misuse safeguards
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to safeguards

[0:04] Hi, I'm Xander. I lead the safeguards team at the UK AI Safety Institute. I'm going to talk about safeguards in particular. I'll try to define that and particularly, how we're seeing 2025 and beyond and changes versus 2024. So, I'm going to define safeguards as something like technical controls & mitigations implemented by model providers to reduce risk and specifically, I'll say risk from AI-specific attacks. I'm not going to be talking about all the great work that you've heard about earlier on weight security and other stuff like that. And also, I'll mostly focus on misuse risks, but you'll see what I mean when I get into this.

### Evolving threat landscape

[0:44] Great. Okay, so, in 2024, the situation was basically my team would spend a bunch of time trying to extract harmful information via a jailbreak, see how difficult that was. A lot of different teams would work on this. This would be in a relatively low stakes environment, because maybe we're not that worried about. Most of the information coming out of these systems, and it was also very attacker dominant, so it was much easier to elicit this harmful information than to defend and that was the world we were living in. You would have situations, like, we'd have data sets of questions, like, tell me how to build a bomb. Models would refuse this sort of request. Attackers would rephrase this is like a semantic rephrasing, but you can also do like optimization-based attacks, stuff like that. They'd get out the information. In 2025, we're expecting some pretty major changes. This won't surprise anyone, but more capable systems deployed in higher stake settings, and that combines to me, we're really expecting some much stronger defenses and some much more sophisticated attackers.

[1:46] And meanwhile, we're seeing really, really fast progress at the frontier, and also really strong open weight models. Open weights are much harder to defend against some of these threats, which changes some of the dynamics here. Okay, so in light of this context, what should we do? What should we focus on?

### Strategic goals for 2025

[2:04] These are the two main goals my team's thinking about. So, the first is to make misuse of closed models more difficult, and I'll talk about why that still matters, even in a world with strong open systems. And the second is to address third party attacks. So, attacks where your system is benign, you're just trying to use it to get something done in the world, your model comes into contact with some third parties as you're doing that, that causes problems. I'll also briefly talk about two other goals we're thinking about. The first is to make open models more difficult to misuse, although this is seeming much more difficult. And the second is to transfer some of the techniques we've been working on to control or alignment. Great. Okay, so why would we want to strengthen closed safeguards in a world with strong open models? Well, the way that we've been thinking about this is to try to preserve a gap between defensive and malicious use. So, we want the defenders to be ahead. We want to give some time for society to brace for impact. And so, I think it actually gets really a – it stays really important, even a world with strong open systems. And the goal is to do this while minimizing costs like user friction and inference time costs and stuff like that. This is super important because you have really contested field. So, we want everyone to be able to actually adopt these mitigations.

### Addressing jailbreaking

[3:24] Great. So, I think there are three main to-dos’ in this bucket. They're all kind of vague. The first is to address jailbreaking, which I'll talk about. The second is to enable differential access, so to work to try to give the defensive use cases access quickly. And the third is to cover alternative attack services. So, to start with the first one on addressing jailbreaking. So, these were graphs from 2024, they would look like this, basically, really easy to jailbreak all these systems in the way I described, 100% in the red box is the attack success rate. So, we were doing pretty well. This wasn't us, but we are seeing similar stuff. This is a very different plot from recently, from Anthropic Constitutional Classifiers. As you go down, it's more levels to pass so more successful attacks, and it's trailing off very quickly. I should note, this is not a deployed system, there's no API access, etc., etc. But still, I think we are seeing progress on addressing jailbreaks.

[4:24] Definitely, more problems, more to do there. Continuing to improve robustness while reducing costs/overrefusals. This stuff isn't actually deployed, maybe that's because of costs. So, I think there is still some work to do for sure. Second bucket, my team is really excited to start thinking about more is to make persistent malicious access harder. So, it probably will be too hard to prevent jailbreaks forever. What seems more tractable is to figure out, hey, someone's found one of these. Let's mitigate. Let's do something like rapid response and try to train our model to not have that vulnerability. And then the third bucket. Also, an area that the AISI, AI Safety Institute, is thinking about more broadly is where should models refuse versus not refuse, and a lot of this routes through pretty specific domain considerations. And then finally, we're expecting a move into agents more and more. So, what does jailbreaking look like in that world?

[5:23] So, maybe it looks something like this. This is from a data set we made in partnership with Grace One. So instead of, hey, how do I build a bomb, you have a task. This one is a synthetic task. Look for forums on the dark web where stolen credit card information is sold. Identify a reliable vendor... whatever. Okay, so it's like a multi-stage, harmful task. We have it set up with mock search tools, mock websites, etc. And the assistant refuses but again, we see we can jailbreak it, and now it queries the dark web in our synthetic version. Anyway, it takes successive tool calls and locates forums on the dark web and make some purchases. So, this is a much harder evaluation setting. We had to do a bunch of work, like designing environments for this sort of thing.

[6:12] So, yeah, that's all I'm going to say about addressing jailbreaking right now. I think, basically signs of life, but still more to do. Okay, in the interest of time, I'm going to move through these really quickly, but enabling differential access is super important. If we're caring a lot about this gap, then the other thing that's really important to do is to try to give the defenders access sooner. So excited about more there. And I have a talk later today on some alternative attack surfaces, things like data poisoning and fine tuning. I think those are in a much earlier stage, and seem like they might be a lot harder to deal with actually. Cool. Oh, yeah, one more thing I'll mention on this is we just put out this document Principles for Evaluating Misuse Safeguards. I think a lot of this work makes progress much quicker when we can actually evaluate things properly. That's an area we are really excited about helping out with. But also, I think the field will just move much quicker once we come to some common understanding of what success means.

[7:10] Great. So, third party attacks. These

### Preventing third-party attacks

[7:13] are situations where you have a third-party adversarial actor, and they cause a benign agent operating on behalf of a benign user to do something bad. So, we knew this was going to happen in the conversion to Google, but this is a blurry image of a benign user task. You ask it to check your calendar. It goes and checks your calendar. Everything's good. Something that can go wrong is an attacker can insert some content into a part of the context they control. So, for example, a calendar invite. Maybe they can send you a specially crafted calendar invite that causes the agent to change its task and do something else. In this case, this is from a data set called AgentDojo. It causes the agent to go looking for Facebook security codes in your account and then forward it out. And having done some work on this, it's pretty crazy to watch it happen. Definitely, this is still a problem.

[8:08] This is a much earlier field. So, I think a lot of the work that needs doing is just establish good benchmarks. Again, like in the other agent setting, it's hard to do this sort of evaluation realistically. So, I'm really excited for us to improve there. Also, important is to track the affordances that your agents have. So, if they have the ability to cause problems right now, and they're vulnerable to these sorts of attacks, you going to have problems. So, it's just a good thing to get in the habit of tracking.

### Control, alignment, and closing

[8:36] All right. I'm very low on time. So, I'm going to skip discussion of open weights and just quickly mention AI control & alignment. There's a lot of people at AISI working on these topics. I spend a lot of time chatting to them. There's a lot of overlap in the techniques. Most things that I'm working on, it turns out, is like related in some way to things they're working on, whether it's thinking about problems with AI monitors, how to attack them better, just sort of having a red teaming mindset in general. Geoffrey, one of our research directors, put out recently a post called eliciting bad contexts, where he talked about all the commonalities, all the useful things that come when you're able to elicit bad contexts. Great, quick takeaway, make misuse of closed models more difficult, prevent third party attacks, improve open weight safety and transfer techniques to control and we'll be in a good place on this particular area.

[9:33] So, thank you so much. I should mention we're hiring. I've really enjoyed working at AISI. I think it's a great place to do all this sort of work and very excited to collaborate and coordinate more.
