---
id: "igNjZE5LmBw"
title: "Jonathan Bostock - Report From The Jungles Of Untrusted Monitoring"
url: "https://www.youtube.com/watch?v=igNjZE5LmBw"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-18"
duration_seconds: 304
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Jonathan Bostock - Report From The Jungles Of Untrusted Monitoring

[Watch on YouTube](https://www.youtube.com/watch?v=igNjZE5LmBw) · FAR․AI · 2026-05-18 · 5:04

## Description

```text
Jonathan Bostock (University of Oxford, Imperial College London) reports back from a deep dive into untrusted monitoring, the protocol where an untrusted AI's actions are checked by another instance of the same untrusted AI, with collusion held off by honeypots: known examples of misbehavior used to catch a colluding monitor. 
His first point is that this is not hypothetical. OpenAI has acknowledged monitoring its model with the same model, with only some honeypotting in place, because establishing genuine trust is hard while running honeypots is easy, making untrusted monitoring the default. 
His second point cuts against how the field talks about control: untrusted monitoring is not an orthogonal layer on top of alignment, it is a force multiplier for it. The reason we trust a trusted model is that we have evaluated it broadly and judged it unable to tell when it is being tested; a validated untrusted monitor is just the untrusted AI with enough honeypots that we have extended limited, domain-specific trust to it. The fundamental alignment problem still applies. 
His third point is methodological: when his team wrote out a proper safety case for an untrusted monitoring deployment, most of it turned out to be missing, but the exercise produced a game-theoretic model that surfaced concrete trade-offs, including that the deployment breaks down without a trusted monitor somewhere in the mix. 
Control protocols have too many moving parts to reason about informally.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Yep. So, I bring a report from the jungles of untrusted monitoring. Last summer, I worked on a project where we did a deep dive into the basic untrusted monitoring protocol, where you have some AI, you don't know if it's aligned or not. You have a trusted AI, which you have, but it's too weak, too dumb to be useful. So, you want to get your untrusted AI to take some action and another untrusted AI to verify that. Now, the problem is the two instances can collude. One can misbehave, the other can say it's okay. And the way that we fight that is with honey pots, where we give a known example to the monitor of misbehavior and try and effectively catch it out. The dynamics are then this game of cat and mouse, where we come up with better honey pots and the AI threat is coming up with better ways to collude. And if that sounds too hair-brained for anyone to try it, untrusted monitoring is real is my first point. Here's an announcement from OpenAI and it contained this sentence.

[1:07] They're monitoring their model with the same model. And I asked, "Did you do any kind of honey potting, any kind of collusion busting?" And they said, "A bit." So, what's going on here? I think because establishing that a model is genuinely an AI is genuinely trusted is quite difficult, but running some honey pots is quite easy, the default outcome for monitoring is that you have some kind of untrusted monitoring going on. And the second thing I want to say is that it's actually just a force multiplier of your existing strategies. It's not an orthogonal layer. A lot of people talk about control like it's some extra bonus layer on top of your alignment strategies. And for untrusted monitoring, I don't think that's the case. Why do we trust our trusted model?

[1:55] Because probably we've given it a bunch of e-vals, a bunch of um um stuff where we think it can't tell that it's in an evaluation or in a training scenario. And because of that, we've done it broadly. We found that broadly it behaves, we think we can generalize, we can extend trust to it. Why don't we trust the untrusted AI? Most likely because we've given it some e-vals, we've given it some training, and it knows that it's being tested, [laughter] and this happens, and that's why it's smarter, and that is why being smarter leads to untrustedness. So, we don't trust it. What is a monitor that we've given honeypots to and validated the monitor? It's just an the untrusted AI that we've given a bunch of honeypots to, and we've put enough effort into the honeypots that we think it can't distinguish them for a real example of its own misbehavior. So, all it is is a AI that we've just extended like a limited amount of trust in the specific domain of focusing all our efforts of alignment onto the task of monitoring.

[3:01] And what this means is that untrusted monitoring is not like an orthogonal layer, it's just a force multiplier for your existing strategies. So, the fundamental challenges of alignment still apply to this case of untrusted monitoring, which is less than ideal, but it's good to know. And the last thing we found is that models, in the sense of a mathematical model of the situation, they don't always confuse you, but they do reveal where you are confused. We came up with a sketch of a proper safety case for an untrusted monitoring deployment, and it looks like this. And all of the gray boxes, which you can't see on this resolution, are pieces that are missing and need more looking at. Now, we found several quantitative claims. We don't have time You don't have time to read those. I don't have time to say them, but we found some.

[3:50] We then made a mathematical model of the statistical sort of properties of an untrusted monetary deployment and we found the various qualitative claim like quantitative claims that you need to measure from your untrusted AI before you can say something about the safety of the deployment. And we came up with a game theoretic model of this which we were then able to find a bunch of trade-offs and one of the important trade-offs tells us that amongst other things um you need a trusted monitor in the mix otherwise the whole thing breaks down. So if someone wants to run over to Marcus's office hours and tell him he's cooked go ahead. >> [laughter] >> So we needed to do this. It's very easy if you don't have a model of the situation. If you don't put it in maths to just miss something.

[4:42] Um and I think that's a like important conclusion that we need to take. We need to be thinking rigorously because control protocols have many moving parts. I'm here all weekend. Two of my three of my colleagues are here and we have a little unconference session coming up if you want to learn more. Thank you.
