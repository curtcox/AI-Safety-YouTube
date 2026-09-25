---
id: "sW6eR1wivFc"
title: "Roy Rinberg\n - Information bottlenecks and small-model imitation via Question-Asking"
url: "https://www.youtube.com/watch?v=sW6eR1wivFc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-28"
duration_seconds: 326
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Roy Rinberg
 - Information bottlenecks and small-model imitation via Question-Asking

[Watch on YouTube](https://www.youtube.com/watch?v=sW6eR1wivFc) · FAR․AI · 2026-05-28 · 5:26

## Description

```text
Roy Rinberg (Harvard University) presents a framework for AI monitoring that solves the decades-old tension between security and privacy. By placing LLMs in trusted compute boxes that verify queries against public constitutions, his approach creates a new secure computation primitive—allowing minimal information leakage while enabling legitimate monitoring for misuse, AI psychosis, and scheming. The system addresses false positives through iterative appeals where labs submit exonerating evidence. This technical solution enables monitoring in zero-data-retention settings and makes third-party audits more trustworthy, moving beyond "trust the co-authors" to verifiable guarantees. The approach has broad applications, from addressing conspiracy theories without leaking sensitive information to enabling coordination between AI systems without sharing code.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Uh, hi, I'm Roy. I'm a CS PhD student at Harvard. I'm also a Constellation Visiting Fellow for at least the next 3 months, so I'm in the area. Uh, I'm going to be talking about verifiably scoped auditor agents. Um, okay. So, we're at Control Con. There's a lot of reasons that you need to do monitoring. You know, there's misuse, there's things like AI psychosis, there's scheming. We generally need to do monitoring of some kind. Uh, this is not a new concept. We have wanted Law Enforcement has wanted to do monitoring for the last at least 80 years since and and this is a colloquially in the privacy community called the Crypto Wars, where Law Enforcement is like, "We need to monitor you for whatever, like there's a criminal doing something." And privacy people are like, "Well, how do I know that you're not monitoring me for political dissidents or or things like that?" Um, the same technology that is used for monitoring for X can be used for monitoring for Y. This is a process level issue, not a technical issue.

[1:02] Um, yeah, so I just want to present that the underlying goal of the type of thing that I'm talking about is that we need to do a bunch of monitoring while also not creating an authoritarian state. General problem. Um, yeah, and the general purposes of talk is one to kind of communicate that there are types of tools that we can develop that are both process level and technical level uh, to enable this. To scope out some of the process level issues that that arise here and to just tell people that this is what I'm thinking about and please find me and talk and and that's the point of a lightning talk. >> [snorts] >> Um, okay, so I want to example. There was this paper called How People Use ChatGPT by OpenAI, where what they and in that paper they're like, they have all these findings, but in section three of that paper they're like, "This is how we did the queries." And generally it looked like this. There's the lab and there's the queries. And before the lab gets sent the queries get sent to the lab until sorry, to the user data. Uh they go to some trusted third party.

[2:01] The obvious question is, who is this trusted third party? In that paper, it was co-authors. Uh which is fine for that paper because it's a paper that they've no incentive to do anything malicious here. Uh but generally we want something a little better than this. Um One way we can do this is actually using like the amazing technology that we have of LLMs and putting them basically doing a trusted LLM in a trusted compute box that makes some kind of verification to a public constitution. Um This would be a great system to work to to work out that if we had some kind of assurance that you uh that these queries are adhering to the thing that they say they're adhering to and not the thing not say again political topics or something like that. >> [sighs] >> Um One of the problems that you have to deal here is what do you do in the case of false positives? Just to map out this type of thing.

[2:56] Uh what is a What is a positive? A positive is a The query ran by the lab 2 minutes, great. Uh a query ran by a lab was deemed to be off-topic. This was like it was on We thought that it was on uh again political things and not bio risk. If it's a false positive, this this query really was on topic. This means that there is some kind of exonerating evidence that the lab could produce that would show that the query was actually on topic. This could then be presented as directly as evidence or as like a new query that you put in the box that you then run through an LLM and say like, "Hey, this query was it actually of this form and like we previously misunderstood it and that's why it's a false positive." Um and yeah, so [clears throat] so generally I'd say that like this false positive is a problem, it's a hard problem, uh but through incentive alignment and like this iterative appeals process you can work through this.

[3:51] More broadly, I'm kind of sharing this like thought that maybe is obvious to many people, but we have produced a new kind of secure multi-party computation, which is we can now, or we are beginning to now be able to do something like spin up a box, spin up an LLM in the box, put data in it, and then only allow for one bit of information or something very privacy-preserving, and then spin down the box, which is otherwise a thing that we would have to go through very complicated legal processes, and is tricky, and is just expensive and timely to do. Um lots of applications to technologies like this. Uh maybe my the most exciting one to speed through this is governments and companies could try to address conspiracy theories without leaking information. Uh there's very many that would be great, like I don't know, Area 51 is a is a tame one.

[4:42] Um but I think this has more practical applications to things like enabling monitoring in zero data retention policy settings. Um with that, I just want to say like if you talk to anyone who thinks deeply about zero data retention policy, please come find me. I'm I'm quite interested in this. And if you work with third-party auditors, Meter is is a great example, but not doesn't just have to be Meter. Uh I would love to try to figure out the problems that you're facing with with uh making these interactions more trusted.
