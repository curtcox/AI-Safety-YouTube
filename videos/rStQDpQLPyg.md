---
id: "rStQDpQLPyg"
title: "Asa Cooper Stickland - Persistent state: A new control setting"
url: "https://www.youtube.com/watch?v=rStQDpQLPyg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-20"
duration_seconds: 306
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Asa Cooper Stickland - Persistent state: A new control setting

[Watch on YouTube](https://www.youtube.com/watch?v=rStQDpQLPyg) · FAR․AI · 2026-05-20 · 5:06

## Description

```text
Asa Cooper Stickland (UK AI Security Institute) flags an assumption baked into AI control work that may not hold for much longer: that an attack has to fit inside a single trajectory. 
Real code agents work across many PRs on the same repo, which means a misaligned model can spread an attack across episodes, setting something up in an early PR and exploiting it later. The blue team gets more chances to catch suspicious behavior in principle, but who actually wins is an empirical question. 
His team built a vibe-coding-adjacent setting to find out: an untrusted Sonnet 4.5 builds an app across five PRs, with a weaker GPT-4o as the trusted model, and a range of monitors including a stateful "link-tracker" that can keep notes across PRs. Gradual attacks distributed across the sequence beat strong single-PR baselines, and the gap held even when the team swapped in much more powerful monitors like GPT-5.3 Codex that could see every diff. The blue team's best play was ensembling monitor types, which helped meaningfully but didn't close the gap. 
The talk's broader implication is for what red teaming needs to look like as continual learning and persistent memory enter the picture: the single-trajectory assumption is one of several that won't survive contact with the next generation of agents.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Uh, hello. I'm Asa from UKAI Security Institute, and this is work done with Josh and Eda as part of the Astra Fellows program. And I'm going to talk about distributed attacks. So, attacks that are spread across multiple trajectories. And yeah, typically in control, we're basically assuming that an attack has to occur all in like one trajectory. User gives the model some task, or the model is carrying out some task, and it has to like do all the bad stuff in this kind of single episode. But of course, coding agents are working on the same repo across like multiple episodes, multiple different tasks. So, this is going to change the red and blue team dynamics because the red team can like spread out their attacks. They can like set up something in their particular early PR and like exploit it later.

[0:47] So, this helps the red team, but also perhaps the blue team gets some benefits because they have more chances to catch the red team. If they catch like, you know, some early suspicious behavior, they can like use that to influence their future decisions. So, who wins overall? Who knows? And we built this setting to to try and figure this out. It's kind of a like roughly like sort of vibe coding adjacent setting where some user is asking a coding agent to iteratively build some app or like CLI tool. So, we have these like sequences of five PRs. They're all like adding new features to some to some app. And we're odds are set of pairs. We have this like untrusted model of of Sonic 4.5 and a weaker trusted model of GPT-4o.

[1:36] And we're going to consider two kind of attack strategies. One is these like gradual attacks attacks that are distributing the attack across multiple PRs. And kind of baseline of non-gradual attack that executes the full side task in in a single PR. And to make this a strong baseline, we like select the kind of position within the sequence that has the highest evasion rate. So, this is kind of a you know, best possible um single attack strategy. Um we also have a bunch of different monitors. So, we have some kind of standard monitors that look at um the purely just the diffs for each PR and also kind of full trajectory monitors. Um we also introduce this kind of link tracker monitor that had that is also stateful. So, this uh new monitor basically can write notes in a in a kind of persistent way. So, it can like look at um things that thought previously looked kind of suspicious but weren't good enough evidence on their own but because it has this notepad it can like piece together over the course of the 5 PRs um what's going on ideally.

[2:34] Um and the way it works is if the blue team catches the the red team in any of these PRs then they win. Um and if after the kind of 5 PR sequence the attack has been carried out then then the red team wins. Um and our results were we basically destroyed the four other monitors so our evasion rates are like super high or like you know, over 80% in in a lot of these cases. Um and the kind of basic result is that um the gradual attacks were mostly better than the the non-gradual attacks these like positional attacks. Um overall the difference is like relatively small and it was in fact it was just a very hard setting um for for the blue team. Um and this was the case across a bunch of different monitor types. So, we had these kind of single trajectory single PR diff monitors and even if we um it had this like full diff uh monitor which sees um uh all of the all of the diffs from each PR they still don't do too well. Um but we did find that the stateful link tracker monitor does a bit better and uh predictably kind of ensembling all the different monitor types um does the best overall and uh meaningfully like reduces the evasion rate. So, ensembles are great.

[3:37] Um but this is kind of like well, our evasion rates are all just like insanely high like what does this really tell us anything about the difference between gradual and non-gradual? Um so, we kind of upgraded the monitors. Um we use some like really powerful monitor models so we actually use like models like 5.3 codex, which is probably just way stronger than the interested models. It's kind of a, you know, overpowered blue team, though we still found there was this like this large gap between the gradual and non-gradual positional attacks. So, the the gradual attacks are still doing pretty well even with these like super powerful monitors and even when the powerful monitors can see all of the diffs like the diffs across across each PR. So, overall they look like the the kind of distributed attacks enable you know, they're like super strong and they can they can beat these really powerful monitors.

[4:26] And yeah, come and chat to Josh and Eda if you're interested in this work and the paper should be coming soon. And then be very quick zooming out. I I we have an unconference session later on like the kind of future of red teaming and making red teaming appropriate for things that coming in the next six months. Maybe there are kind of similar similar assumptions like attacks coming in a single trajectory that we need to think about and prepare for like models of continual learning and you know, really powerful memory and and so on. So, come to our unconference session later if you're interested in challenging assumptions and so on. Thanks.
