---
id: "UehjJcu3CeQ"
title: "Aleksandr Bowkis - Automating Alignment is Hard [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=UehjJcu3CeQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-25"
duration_seconds: 285
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Aleksandr Bowkis - Automating Alignment is Hard [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=UehjJcu3CeQ) · FAR․AI · 2026-04-25 · 4:45

## Description

```text
Aleksandr Bowkis (AISI) examines a key assumption behind proposals to automate alignment research: that a non-scheming AI research agent would be sufficient to safely bootstrap more capable systems. He argues this assumption breaks down because even well-intentioned agents can produce outputs that look correct to both humans and other agents but are actually wrong — due to alien mistakes humans are poorly equipped to spot, optimization pressure against human feedback, and underspecified task decisions. The problem deepens for "fuzzy tasks" — high-level research tasks like generating useful research proposals, synthesizing large bodies of evidence into safety assessments, or steering research programs — where no reliable training signal exists because humans cannot easily evaluate the outputs. Correlated errors across research outputs make these problems harder still: an overseer who doesn't account for this correlation may draw false confidence from a large but flawed evidence base.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] I'm going to talk to you today about why we at AISI think that there are hard tasks in automating alignment research. What do we want to do in alignment? What we want to do is align superintelligence. Why? Because we think that's where most of the risks come from, and it's because we think that's the hardest problem. Unfortunately, that's difficult. One proposal to try and solve this is instead to use a less capable AI research agent to assist with this alignment research. The way the story usually goes is you take some research agent, it does alignment research, it vouches for the next research agent, and then you deploy the next research agent, and that vouches for the next one — you hand off iteratively. Why is this appealing? Well, this might reduce this difficult problem of ASI alignment to a much simpler problem. Now all we need to do, it seems, is to build a non-scheming AI research agent.

[0:54] So what's the catch? Well, the catch is that a non-scheming research agent can produce outputs that look correct to both human overseers and to other research agents, but are actually in fact wrong. There are two reasons that we think this might happen. The first one is obvious — agents are going to make mistakes. But what is perhaps less obvious is that these mistakes, you might expect them to be hard to find, and you might expect them to be correlated. We think there are three reasons for these mistakes to be hard to find. The first is that they're likely to be alien mistakes — the sort of mistakes that a human reviewer themselves might not make and therefore might be poor at identifying. The second is that there's likely to be some form of optimization pressure. Outputs might be optimized in some way against human feedback to appear correct. And if that human feedback diverges from whether or not the output is actually correct, then you get a load of outputs that look good but are in actual fact wrong. And the third is that there's freedom within your task specification. Every research task that you give to an agent will require that agent to make some decisions that don't have explicit guidance, and these can be a source of very hard to locate errors.

[2:02] But more concerningly, as automation progresses, you might ask your research agent to do higher level research tasks. We call these fuzzy tasks. We define fuzzy tasks as tasks that don't have a good training signal because they're hard for humans to evaluate. There are lots of different fuzzy tasks, but there are three that we are particularly concerned with. The first is generating research proposals that are actually useful. It's very easy to generate research proposals — it's very hard to generate research proposals that actually tell you something about what you care about, in this case whether or not your system is aligned. The second is combining research results into overall safety assessments. For example, if I give you 100,000 research papers and I ask you to draw some conclusion from those, that's a very difficult task. And the third one is steering large bodies of research. You could have a very large body of research, but it might not be sufficiently diverse. The thing that all of these three types of problems have in common is that they're all judgment calls that require some global view of the evidence base.

[3:04] One obvious question here is why can't we just use human judgments? Humans do science all the time, so presumably we do this stuff all the time as well. The problem with this is that human judgment is often unreliable, and in fact this judgment problem is going to get harder over time as capabilities advance. You can just look at the history of science to see a whole bunch of examples of when this was the case. If you look in the history of physics — I was a physicist before this — a lot of effort was devoted to the theory of the luminiferous ether, which didn't go very far. The obvious follow-up question is why does human science work? Well, human science works because it's at least partially error correcting. You make some proposal, you iterate on that proposal, you realize you were wrong, you go back, you correct that proposal and you carry on. Unfortunately, in alignment, failure is high cost, and so maybe we won't have the opportunity to fix these mistakes as we're going. But actually the problem's even worse than this.

[3:59] You might get your agent to produce a load of research outputs, but unfortunately you're going to have correlated uncertainty across those research outputs about whether or not each individual research output is correct. And if you don't understand this particularly well, then you might fail to correctly combine all of your evidence to form overall safety assessments for your next model. You might generate research proposals that appear diverse but are in actual fact correlated. You might come to incorrect conclusions about the next best experiment to run. So these are the problems. I'm not going to leave you with any solutions, but I am going to leave you with an offer to come and chat to me later if you're interested in talking about solutions. Thanks for your time and hopefully speak to you some of you soon.
