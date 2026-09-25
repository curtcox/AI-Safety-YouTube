---
id: "9F12R2intGk"
title: "Yoshua Bengio - EU CoP's Security Focus [AI Security Forum]"
url: "https://www.youtube.com/watch?v=9F12R2intGk"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-03-21"
duration_seconds: 582
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Yoshua Bengio - EU CoP's Security Focus [AI Security Forum]

[Watch on YouTube](https://www.youtube.com/watch?v=9F12R2intGk) · FAR․AI · 2025-03-21 · 9:42

## Description

```text
Yoshua Bengio warns of the dangers of both current and future AI, advocating for higher security measures in the EU AI Act to prevent loss of control over AI displaying self-preservation and power-seeking, while also discussing the challenges in creating trustworthy, non-agentic AI monitors to oversee more complex AI systems.

Highlights
* Urgent AI Security
* Human Control Loss
* EU AI Act
* Trustworthy Monitors
* Transformation Risk
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] I'm going to start with a few motivating remarks. It’s becoming pretty clear that we are on a trajectory to build AGI and superintelligence, and the timelines are getting shorter. The questions that are discussed here are very important, but keeping that in mind is crucial. It's not the AI that exists now that needs to be secured. It’s the AI that will exist in one year, two years, three years that will have much greater capabilities. These capabilities, intelligence gives power, and power can be used in many good and bad ways, of course. In particular, one thing people don't see enough is that advanced AIs will become not just products but ways to design new technologies, including weapons. Of course, very soon, it’s making it much easier for non-experts to do these things, to build things that can be used against populations; I'm sure you know about all that. But I want to be also blunt that the elephant in the room is loss of human control.

[1:27] We are seeing signs in recent months of these systems having self-preservation behavior and power-seeking behavior, for example, trying to escape when they know that they're going to be replaced by a new version or faking being aligned with their human trainer so that they wouldn't change their goals and basically preserve themselves in some ways. So, when we think about security, we need to think about these two aspects. We need to think about humans trying to misuse these systems, exfiltrate model weights, whether to run them without safeguards, to fine-tune them to something bad, or see some other economic or military advantage, but we also need to think about the AI systems themselves as sort of insider threats that could do these things, exfiltrate themselves, run themselves outside of human oversight.

[2:31] I mentioned, like, copy their code or their weights in other places or in place of upcoming versions and so on. So, let me now say a few words about the code of practice of the EU AI Act in which I'm involved. I'm in the Working Group 3 which deals with mitigation, and actually this is the place where we also have instructions about security. What we've done is asked the developers to conform to the RAND Security Level 3. Thank you for doing it. We have some pushback, [audience laughter] but I think this is a very important element. So, maybe security people might ask me, why not Level 4 or Level 5? We thought this was, for now, a good compromise because doing Level 4 or Level 5 would require new research that I think should be done, but maybe it's not yet the time to enforce. I think governments should be investing massively in developing these higher levels of security so that it would be easier for companies to move to these when that's not just relevant, but easier to do. Just a few more words about compute governance, the data centers. Unfortunately, this is outside of the scope of the code

[4:07] of practice of the EU AI Act, but clearly it's something that we have to worry about as well. The thing to keep in mind when people work on these questions, again, as I started with, is not the AI that we have now, but the AI that we'll have in a few years, even 12 months. These systems will be more powerful, and that means the security measures that have to be put in place now or worked on now have to deal with capabilities that maybe don't exist yet but are likely to be there in one or two or three years. On that, let me just say a few words that are not directly related to security, but there's some connection. One thing that we don't know how to do right now is to mitigate the risks of the AI systems that are upcoming. We have made a lot of progress in evaluations, but what to do when these systems will become with dangerous capabilities is something that we don't have a very good answer for. One thing that my team is working on is how we can build AI systems that will be so trustworthy that these are the systems that we want to use as monitors; in other words, to tell us whether the behavior or the queries that we're getting, for especially an AI agent that may

[5:47] not be totally trustworthy, are acceptable. That means—and the approach to make these monitors totally safe or the end very capable that we've chosen is to make them non-agentic, because all of the risks, all of the scenarios of loss of human control arise because of agency. In fact, we can see that as these systems become more agentic, they have more propensity to try to deceive us, escape, and so on. As we build more and more powerful AI systems, we basically can't trust them as much unless we figure out solutions. One solution is to build systems that are not imitating us, not trying to please us—so that's basically how we train them right now—but trying to explain why is it that people are saying the things that they're saying or the data that they're observing. That then allows to query them about things like these causes—why did this person do that—and latent things that we don't directly observe, like actual harm or some safety specification that we care about. This is ambitious, and we need to think also that even if we solve this particular problem, like how to build systems that are not going to be deceptive, it’s still going to be a security issue because you can turn a very intelligent,

[7:25] non-deceptive system into a weapon. You can ask it still, how do I build a bomb or whatever? You can even turn a non-agentic system into an agentic system. It's very simple. You've seen this maybe with ChaosGPT just after ChatGPT came out. You just need to put it in the kind of loop that the typical agentic loop that we have for RL agents, in which you take the actions and the observations, that one step, as extra input for the system, and you store things like goals and so on. So, it’s pretty easy to turn a very powerful non-agentic system into an agentic system. And of course, that's where, if we're not careful, there's a lot of danger, whether for malicious use or loss of control. We will need to secure these systems as well. I hope that we all understand that we are moving faster and faster towards these more capable systems, and so there's really urgency now to put in place these security measures that this group is interested in; I wish I could help. One area where I would like people to start thinking more about is formal methods to try to make these systems more secure.

[8:54] My friend, Davidad, who is here, probably is going to talk about that. People are thinking about how we can use neural nets to generate provably correct code according to some specification, and I think when we talk about security, this is the place where we want to have code that is as guaranteed as possible to be doing what we want and not be easily attacked by either insider threats from machines or people or outsiders trying to get in. That's it. Thank you very much.
