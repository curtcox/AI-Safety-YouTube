---
id: "Ekp-eg7TcIY"
title: "Stephen Casper - ML Researchers as Policymakers [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=Ekp-eg7TcIY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-31"
duration_seconds: 618
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Stephen Casper - ML Researchers as Policymakers [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=Ekp-eg7TcIY) · FAR․AI · 2026-03-31 · 10:18

## Chapters

- 0:00 Introduction to policy research
- 1:08 The landscape of AI policy
- 2:18 Vague legislative frameworks
- 3:48 Case study: deepfake research
- 6:15 Engaging with policymakers
- 8:18 A recipe for impactful research

## Description

```text
Stephen Casper (MIT CSAIL) demonstrates how ML researchers can directly influence policy by strategically conducting technical research that operationalizes deliberately vague legislative terms. Lawmakers globally are punting technical decisions to the ML community through terms like 'reasonable safeguards,' 'foreseeable risks,' and 'state-of-the-art techniques.' Casper's deepfake research exemplifies this approach: by documenting how a small number of model developers represent critical bottlenecks in harm supply chains, and showing that basic mitigations create order-of-magnitude differences in abuse patterns. The work directly informed Arkansas HB 1529—legislation allowing the Attorney General to sue developers lacking 'reasonable safeguards.' This creates a reproducible pathway: identify vague legislative terms, conduct empirical work operationalizing them, then communicate findings directly to policymakers and legal stakeholders. 

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to policy research

[0:00] All right. Hi everyone. Thank you, Lindsay. And yeah, like Lindsay said, this is going to be what I'm going to talk about, and I'm really glad to do so following Rob's talk. Also, Joseph, in your talk I think you mentioned a phrase that perked my ears up — you mentioned "governance-adjacent technical research," which is very much what I want to talk about right now. My goal in the next nine or so minutes — which of you out there are people who do empirical ML research? It seems like it's more than half the room, which is good. My goal in the next nine or so minutes is to try to convince you to think of yourself sometimes quite literally as a form of policymaker. I want to talk about an emerging style or genre of research that's becoming increasingly possible, that you can use to do ML research that helps bridge a gap into making a policy difference. And on the other side of the coin, I want to talk a little bit about how lots of machine learning research, even if it has the substance to potentially improve policymaking in the real world, might fail to bridge that gap — and how some of these mistakes can be corrected or compensated for.

[0:59] One last thing: in the next few minutes we're going to talk about this guy, and why I'm paying very close attention to him in 2026 and why I think you should too.

### The landscape of AI policy

[1:08] To start out and set the stage a little bit, I think we can all probably agree in some sense that 2025 very recently was the year in which AI safety and risk management in practice really started — the rubber really started to hit the road. In 2025 we saw for the first time warnings from frontier model developers that, according to their own evals, their models might be starting to cross some critical capability thresholds. Meanwhile, 2025 was also a year in which we saw surges in emerging harms, like in the non-consensual AI intimate deepfake space. And in response to these challenges, we're amidst a wave of policy interest in drafting bills and policy frameworks to try to address harms from AI. Diverse jurisdictions are starting to enact and propose pretty diverse strategies for handling this kind of thing. Something that we're starting to see more and more in more and more places is certain types of strategies or language that lawmakers will use when writing and drafting frameworks like this, where they effectively are begging for help from the technical community — punting challenges involving how to operationalize the governance of AI to the technical community's understanding of what best practices are.

### Vague legislative frameworks

[2:18] I want to take a few slides to go over, very quickly, a non-exhaustive list of some examples here, drawing from things that have both been enacted and some things that have just been proposed. In California, many of us are familiar with SB 53, which gives a pivotal definition of catastrophic risk inside of the bill, which refers to the risk being "foreseeable" — whatever that means. Also in California we'll see references to "state-of-the-art techniques," whatever those may be, or "reasonable measures" being enacted, whatever that might mean. We can also look at New York, which has passed legislation talking about "appropriate safeguards," or proposed legislation talking about "reasonable efforts," when it comes to addressing risks involving suicidal ideation from AI systems. In Colorado we can see references to "reasonable care in the face of known or reasonably foreseeable risks." interesting. In Arkansas there's legislation about "reasonable safeguards." Montana: "reasonable risk management policies." In China we see this in a few places, including the Model Artificial Intelligence Law, which talks about "reasonable and effective organizational and technical measures." And then finally the EU — the Codes of Practice especially — are just a gold mine of this kind of stuff. I don't even have something to quote here, I'm just giving you a dictionary of the counts of a bunch of words that are dead giveaways for these intentionally vague statements which punt to the technical community's understanding of best practices. And finally, as many of you probably know, in tort law we have these intentionally plastic and always contextual notions known as duty of care and proximal cause.

### Case study: deepfake research

[3:53] I want to talk about an example of some work that I was recently glad to be a part of, which has come to shape my understanding of how to do this type of work and how to do it strategically. I'm going to be a little bit direct in that I really like this work — mad props to the undergraduate who was the first author of it. I want to talk about why this work, I think, was successful and why I'm really glad I worked on it. But just in case it sounds like I'm getting a little full of my own research up here, I also want to flash up on the screen some work that I've done that I think was really cringe and unimpactful, just to even things out a little bit. But back to the impactful work. The title of this paper was "Video Deepfake Abuse: How Developer's Choices Predictably Shape Misuse Patterns." For anyone here who thinks a lot about accountability or tort lawsuits and AI, you might be starting to get the idea of what we were doing in this paper.

[4:45] In a nutshell, what we tried to show was, first, that model developers represent a really critical node and a very narrow bottleneck in the supply chain behind AI capabilities that are misused very commonly for non-consensual deepfakes. We also talked about how it is indeed a very small number of models from a very small number of developers that tend to be misused the most for this type of content. We also talk about how mitigations matter in a space like this, especially when access is key and so many of the perpetrators are literally teenagers — and we know this both from the empirical research on these mitigations and from looking at the usage ratios of models that have been trained with versus without safeguards for creating this kind of content. And finally, we also observed that it is a very low-transparency regime where it's pretty rare for developers to say very much that is meaningful about risks at all, let alone their attempts to mitigate them. In retrospect, I think there are a few things that we did relatively well this time. This paper had a really concrete motivation — to inform future lawsuits, some of which haven't happened yet.

[5:49] It had a very incisive title that I think got across the idea pretty clearly, especially to people who are familiar with potential lawsuits here. It ended up being pretty prescient with respect to the 2026 zeitgeist, because we're having a lot of conversations right now about deepfakes. It was a paper that was intentionally written to be accessible to much more than just ML people. And overall I think there's a pretty good chance it might continue to play a modest role in influencing our emerging discussions about AI accountability around these types of issues.

### Engaging with policymakers

[6:15] There have been some nice things that happened since we published this paper in December. We've had the chance to talk with officials in four states and two countries, and we also got a cold email from someone at a nonprofit organization saying that they used our paper to give a presentation to 25 state attorneys general's offices, which I thought was very cool. Now, who's this guy exactly? His name is Tim Griffin. He is the Arkansas Attorney General. Arkansas is actually a really interesting state to talk about in this space because, in the past few years, almost every US state has passed some sort of law making it a criminal offense to non-consensually create or share, using AI, an intimate deepfake of someone else. Arkansas did this too — that's not special. But something that Arkansas did that was pretty unique, and there's a reason I'm paying a lot of attention here, was HB 1529, passed last April, which modified Arkansas Act 827. The bill is here — it's like two and a half pages, and you shall go read it if you want. But specifically, Section 2 is pretty important. What does it say?

[7:19] "The Attorney General may institute a civil action on behalf of the state against a provider or developer of image generation technology that was used to create deepfake visual material in violation of state code if the provider or developer of the image generation technology did not have reasonable safeguards in place to protect against the generation of deepfake visual material." So what does it mean for safeguards to be reasonable? Hopefully this is a place where our paper can come in. We had the chance to talk to some of the people in the Attorney General's office here, and after we talked about the case for why they might want to look into a few particular companies, they let it slip that they would love to be the office to end up holding them accountable if the case is there and if things work out for them. This has really gotten me thinking about not just this project, but this general kind of strategy — how often it can be used for trying to do incisive technical research that really matters. I want to share my emerging understanding of how to do this kind of work and how to do it well, although it is emerging and tentative, so I reserve the right to change my mind about some of these things later.

### A recipe for impactful research

[8:19] One thing that I found personally very valuable is to just read a lot of bills. As a technical machine learning researcher, I think I find more inspiration for the work that I do from reading bills than I do from reading papers, at least these days. I also think it's really nice to pay attention to policy trends and debates, especially in as much as it can help you think a few months ahead about what we might be talking about in the AI policy discussions we're going to be having several months from now, when the projects you start now might be finishing. It's also really useful to focus on real-world problems — things that are happening right now. Many of us are very concerned about certain types of unprecedented AI harms and risks, and even if we care only about those, it can still be very useful to focus on much more near-term things as well, because the case law that we establish and the governance frameworks that we establish around those things now are going to have some pretty enduring impacts in the future for how we handle the fallout from emerging risks. I also think it's really useful to know your audience well, have very clear titles that communicate your work to them, and make sure that your writing is accessible to not just machine learning people. And finally, I think it's really important to not just do good work, but spend a lot of time and effort trying to clearly communicate it and share it with the stakeholders that matter the most.

[9:29] In supply chain logistics there's this notion of "last mile delivery," which refers to the challenge of getting something from the last distribution center to the final customer — a very ad hoc and logistically interesting problem. I think the same kind of thing applies for lots of research, because once you write the paper you often have to do a lot of ad hoc things to communicate it really well. So overall, a very high-impact research recipe that I think you all should consider: pick a consequential issue that policymakers are thinking about a lot, pick a vague term related to it in some sort of legislative framework, write the paper, and then set up a lot of meetings to try to communicate it as best as you can with a bunch of lawyers and policymakers that you're able to contact. Thanks very much. That's all.
