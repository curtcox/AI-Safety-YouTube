---
id: "MEIR7djpTzg"
title: "Evan Miyazono - Set Laws AI Must Prove It's Following [AI Security Forum]"
url: "https://www.youtube.com/watch?v=MEIR7djpTzg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-04-21"
duration_seconds: 357
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Evan Miyazono - Set Laws AI Must Prove It's Following [AI Security Forum]

[Watch on YouTube](https://www.youtube.com/watch?v=MEIR7djpTzg) · FAR․AI · 2025-04-21 · 5:57

## Description

```text
Evan Miyazono advocates for the integration of formal verification in AI for enhanced cybersecurity, suggesting that AI itself may soon help overcome the current specialist shortage.

Highlights
* Formal Verification Urgency
* Proof-Based Safety
* Specialist Scarcity
* Automation Solution
* AI Code Expansion
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Yes, so I have not just slides, I have many slides. This will be good for all of you who watch videos on 2x and to everyone else, there is a QR code at the end with the slides. I have a feeling that I will be kind of preaching to the choir here, so take many of these things not as things I am trying to convince you of but arming you to convince other people that formal verification is a really good thing to do for cybersecurity, starting out with the role of testing compared to safety guarantees and applications of formal verification to cybersecurity in the near future and a way of arguing for AI as an assistant in this way, which is pretty close to the guaranteed safe AI architecture that Yoshua and Davidad were talking about little bit earlier and have written about extensively. I imagine many of you who are on the engineering side are familiar with the quote “program testing shows the presence but never the absence of bugs.” One of these things is not like the other, and I think safety guarantees are something that are sorely lacking from AI usage generally. I tend to personally think that this model won’t self-replicate. We tried under controlled conditions. It looks a lot like this railing is totally safe. Look how hard I can push on it. I would definitely encourage using this metaphor when talking about the current risks that AI systems can pose. Obviously, the way we show that railings are safe is not by pushing on them very hard, but rather by holding them to rigorous, specific, quantifiable engineering standards and checking them. This is a very hard thing to do for most types of AI usages, but I would say that in the usage of AI generating computer software, this is actually a fairly standard practice for a narrow subset of systems. Formal verification is this idea that you

[1:48] have a formal specification, a mathematical description given some axioms of how your software should behave. This could be describing state. This could be describing output properties as a function of input properties. There is a proof that maps that mathematical description to the software implementation itself. The proof is fairly universal in how it can be checked. You can have one proof checker that will validate—that is very small, easy for a human to write once and then use to validate a ton of software. The nice thing about this is now the person only has to deal with specification if you want to guarantee that this does what you want it to do. So you might ask, why don't more people do this? The problem is that it takes very well-trained specialists, people with PhDs and a few years of experience at least, and there are probably tens, maybe thousands of people with this level of experience right now.

[2:46] On the bright side, it might be soon that $200 a month can get you that level of experience. So the question becomes, I guess, some amount of, why look at this now when—then I would claim it's because vibe coding, not to pick on Andrej particularly, but I think that there are a lot of people who are doing this kind of thing where you just have LLMs do the thing, and you accept all. Don’t read the diffs. Code grows beyond your comprehension. Responsible people will do this for hobby projects and not for their work. But if you exist in a market environment, then you will be competing against people who are doing this for their work environment. If you are reviewing code, then you will be reviewing code for which people are doing this. So it is, I claim, much, much more effective to have a specification that you are looking at, and that specification should more succinctly encode the kinds of properties you care about.

[3:47] As a general sense of how bad I think this problem is likely to get, if you can do the rough math and get that 40 costs about 10 cents an hour to match a human output rate. If that quality gets close enough that a human says, “Yeah, this is probably good enough. I trust it,” and they try and push code, or they start a pull request, then someone's going to have to go through and identify whether or not that is doing what they want it to do. So you can either review more complicated things, or you can kind of abdicate the review. The current process that people have for working with AI systems looks, I would claim, very much like a contractor—or, sorry, looks very much like an employee. You have some amount of shared context. You say, “please do this thing,” and then you get back a thing, and you have to go review that. I think that there is a better paradigm that formal verification is an example of, but it generalizes quite well where you generate a specific set of requirements, and from those requirements, an AI system will develop a solution, and then you can get a formal verification that is automated, that the solution meets the spec, and you have some validation loop to guarantee that this spec does, in fact, encode what you want. The nice thing about this architecture is that you can have an AI system do the rightmost two arrows, and you can have fairly high confidence in this that it's automated and doing what you want. The hard part is the validation side. One of the projects we're working on is spec validation, where you can

[5:26] have something like an IDE debugger. There are other projects in this general direction. DARPA is doing a lot of interesting work; Beneficial AI Foundation is too. Guaranteed Safe AI and Safeguarded AI are in this general vein. I will leave this up with a link to my slides. Please reach out. I am currently funding limited. So if you like this, I know exactly who I would start writing offers to if more money showed up. Thank you.
