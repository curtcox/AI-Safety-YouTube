---
id: "388ZnOSEKLE"
title: "Helen Toner – Governance for Advanced General-purpose AI: Status Check, Hurdles, & Next Steps"
url: "https://www.youtube.com/watch?v=388ZnOSEKLE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 872
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Helen Toner – Governance for Advanced General-purpose AI: Status Check, Hurdles, & Next Steps

[Watch on YouTube](https://www.youtube.com/watch?v=388ZnOSEKLE) · FAR․AI · 2024-09-10 · 14:32

## Chapters

- 0:00 Introduction to AI governance
- 1:05 Post-ChatGPT landscape
- 3:04 Current watch and wait mode
- 4:37 Hard governance and laws
- 7:00 Soft governance and commitments
- 8:57 Hurdles to robust governance
- 10:27 Technical and conceptual gaps
- 12:00 Future research and action

## Description

```text
Helen Toner from Center for Security and Emerging Technology presenting 'Governance for Advanced General-purpose AI: Status Check, Hurdles, & Next Steps'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights: 
- Building clear concepts for AI governance
- Supporting decisions with robust evidence
- Achieving expert consensus

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/

#AISafety #AlignmentWorkshop #AIGovernance
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to AI governance

[0:04] Thank you very much, Robert. Great to be here today. And yeah, my name is Helen, for the many folks here who I haven't met before. I've been in Washington, D. C. for the last five or so years working on AI policy issues there, especially with a focus on national security policy issues. But for today, I wanted to zoom out a little bit. I think this is the only full length governance talk. So I'm going to be taking a moment to check in on where things are at with AI governance more generally. And to get a sense of the room, roughly how many people here would think of themselves as ML researchers, technical researchers, most folks? Okay, anyone who's more in kind of the governance policy space? Small number. Anyone who doesn't feel like either of those is them, something else? Yeah. Okay. Great. Very helpful. So going to talk a little bit about where we're at, one and a half years after the kind of Chat GPT moment. Some of the hurdles that I see to more robust governance so far and how technical research can help.

### Post-ChatGPT landscape

[1:05] But just starting out governance can be a kind of squishy term. So I think it's good to say what I mean. And I stole a definition from Virgilio Almeida at FACT this year. Which is that governance is not just, policy or law. It's any form of collective action taken to manage the common affairs of society. So a broad range of things here. It certainly does include laws, regulations, so-called hard governance, but also norms, incentives, coordination structures, and so on. And for the purpose of this talk I wanted to focus on governance for advanced general purpose AI, because I think those are often the kinds of systems we're talking about when it comes to alignment issues. So there's a large amount of work going on to govern more narrow systems, less advanced systems. Very important work, valuable work, lots of progress being made.

[1:56] I'm not going to talk about that today. And I wanted to spend the first part of this talk checking in on where we're at about a year and a half after the Chat GPT release in November, 2022. And the reason I'm thinking of it this way is that as was probably evident to all of you, but certainly very evident in Washington, DC. Chat GPT really kicked off a huge wave of increased interest in AI. Especially among policymakers, lawmakers, people trying to figure out how to handle issues in society. And in general, I think, sort of policy work and governance work often tends to go in waves, where you ride the waves that you are served with. And you have to take moments of opportunity and moments of momentum, because often the people involved have many different problems they need to be handling - a war in Ukraine or a COVID pandemic or rising prices or whatever it might be - and so it can sometimes take some kind of event or some kind of moment for something to seize the imagination of policymakers.

[3:00] And, so I'm going to go through a few sort of specific examples,

### Current watch and wait mode

[3:06] but first I wanted to just say at a high level, I think “Where we're at,” a year and a half after Chat GPT, when it comes to governance of advanced general purpose AI systems, is mostly that people are in a kind of “watch and wait” mode. And so we've certainly seen enough concern expressed by experts - some of them here in this room - about the potentially extreme risks that increasingly advanced systems might pose; that there has been some action. There has been some pretty significant governance and policy action, I think, but at the same time the evidence, the specifics, and certainly the consensus around what the problem is, what the problems will be, and what to do about them is still pretty thin. Especially compared with, plenty of the other problems that AI is causing already and that are more plain to see and maybe more straightforward to deal with because they are here and now as opposed to projected into the future.

[4:01] And this means that it's difficult if you're focusing on governance issues related to advanced general purpose systems. It's difficult to figure out what specific systems should actually be targeted and what you should be requiring of those systems. And so the result is that what I'm about to describe, what has been enacted, I would describe as a precautionary approach, relatively light in some ways, and one that has prompted a lot of disagreement, and many arguments about what exactly should be done. Should it be much more? Should it be much less? Is this all a huge distraction? Specifically,

### Hard governance and laws

[4:37] I'll just zip through a few examples because I suspect they'll be familiar. When it comes to hard governance laws and regulations, the most significant thing we have, is the EU's AI Act, which has now been officially passed. It'll come into effect over the next couple of years, if I understand right, the provisions that are relevant to general purpose systems take effect in about 12 months, They talk about general purpose AI models with systemic risk, and define that as being models trained with more than 10 to the 25 flop, and models that fit this description will have a set of requirements around when they have to notify the EU, how they have to evaluate and manage risks, how they have to track and report incidents what kind of cyber security practices… All of the details of what exactly this will look like are currently being hashed out. In the U. S., the most significant thing is the executive order that the White House put out last October. For those of you less familiar with U.S. policymaking, this is not a law, and the White House, the executive branch, is quite limited in how much it can do without Congress passing laws. So you can basically think of this as the Biden White House doing as much as they could, figuring out as best they could how they could stretch their existing authorities, their existing ability to take action without the much broader discretion that Congress has.

[5:54] So the executive order, like the AI Act, covers many different types of AI issues, but the relevant part for us here is the section on dual use foundation models, so-called, and specifically they call out those trained on more than 10 to the 26th flop, for some kind of similar-ish requirements notifying the government of training and development, evaluating the systems, sharing information about tests that are being done. Again. All of the details of what this actually looks like, what kind of tests they need to do, how to report that information, is very much being determined at the moment. China is one other place that has some laws here. They have passed two sets of regulations that specifically target more general purpose AI though, or that affect more general purpose AI though. In the first case, the sort of so-called “deep synthesis”. They're more thinking about deepfakes. In the generative AI, they're more thinking about chatbots generally. But they do include, certainly would, target the same kinds of systems as are covered by the above two examples, and include some requirements to register and share information with the government.

[6:59] When it comes to softer governance, there's been some really interesting

### Soft governance and commitments

[7:03] unilateral commitments. I'm pretty sure these are familiar to folks in this room, so: Anthropic, OpenAI, and Google have all put out these frameworks identifying different kinds of risk levels that they might hit in different categories. They have slightly different ways of thinking about those risk levels, slightly different focuses between the categories but certainly some throughlines between them. And in all of these cases, again, if you're noticing a theme, the details are still to be determined. So this is put in place in a high-level overarching framework kind of way. But figuring out what specifically it should look like is a task for the present and the future. And then there's also multilateral or multi-party commitments that are being made. The first notable one in my mind was last summer when the White House called in various companies to come talk to them about what they could do, and they committed to these different things.

[7:57] In some case overlap again: testing, information sharing, security. Also, commitments about third-party access, watermarking, using the AI systems to address grand challenges for society. The AI summits, the international summits, have also got some kind of voluntary, multi-party commitments including around pre-deployment testing, and now recently in May, commitments to develop the kinds of safety frameworks that I was describing on the previous slide that we've seen already from three companies. A number of maybe around a dozen additional companies have said that they will develop similar frameworks. And then there's a bunch of multilateral organizations doing relevant work.So the G7, OECD, the UN are trying to figure out what they want to do here as well. And there's also new laws under discussion in California and the UK. In the US, I think everyone's losing hope that they'll get anything done before the election, but who knows, and broader ideas under discussion as well.

[8:54] It's a super incomplete list but there are many things still in progress. In terms of why,

### Hurdles to robust governance

[9:04] what we've seen so far, is relatively framework-level, relatively light so far. I think there's some political and practical factors. So these include, focusing on the U.S. because that is where most of these frontier companies are based. It's unfortunately a particularly bad atmosphere to make policy and make regulation. In one case, just because Congress is very dysfunctional generally - it has nothing to do with AI, just has to do with the fact that, as one friend of mine who really knows his way around Congress said that he thought the House was in the worst shape it's been in since the Civil War.So that's the level of dysfunction we're talking about. And also, at this point in the year things are a little bit, in stasis until the election, unfortunately, because the U.S., unlike pretty much every other democracy on the planet, doesn't think you can do a six week or a twelve week election. You have to do a one and a half year election.

[9:54] So, the U.S. is not in great shape to take action soon. But there are also other factors, practical factors. A lot of concern about ways that sort of overhasty or overreaching regulation could trade off against innovation, could trade off against competition, could have bad effects on market concentration. I think there's very legitimate concerns here. And there's also a real lack of technical expertise and capacity within government to figure out what should be done and how it should be done in a way that is really connected with the realities of how these technologies work.

### Technical and conceptual gaps

[10:28] There's also, I think, technical factors coming back to the framing I offered at the start of the talk about where we're at with these governance issues. There's a real lack of shared concepts and terminology. You can see this if you look at the examples I gave: of the EU talking about general purpose AI with systemic risk, while the US is talking about dual-use foundation models. China couldn't decide whether to talk about deep synthesis or generative AI, even though they basically use the same definition in their two regulations. So a lot of the time there's a broad sense of the kinds of issues we should be worried about, but not really a clean articulation of how to think about them, how to break them down or where, one person offers a clean articulation, someone else offers a different one, which is difficult for policy makers, who really want to just see expert consensus. There's also a lack of evidence base, and this is a little bit inherent to this field and these issues, in as much as we're trying to tackle things in a forward-looking way, in a preventative way. That makes sense in a certain way, but it is also very challenging because it means that it's difficult to know concretely and specifically how these problems will emerge.

[11:36] And it also means that, I think these things are connected to the fact that, there’s very little expert consensus about what the problems are, what to do here. I'm sure everyone here has experienced different, very thoughtful, very experienced experts in machine learning who have wildly different views about where the field is going, what kinds of things we should be concerned about, what kind of pace of change we should expect. Fortunately, I think, many of you in this room - your friends and colleagues - could help a lot

### Future research and action

[12:05] with many of these problems. For one thing, there are opportunities to actually serve in government or serve in government, adjacent to government, if that's something you're interested in. But also I think to the extent that you can think of these technical factors in the work you're doing, so that you're not just thinking about developing a new technique or showing good performance on a benchmark, but really looking at how do we improve the field’s shared understanding? The field of alignment researchers, safety researchers, machine learning researchers more broadly. How do we come up with more robust shared concepts with more evidence? And there's been great progress in this over the last few years. I give credit to a lot of people in the space for starting to build evidence of what these problems could look like. Even if we're trying to prevent some of the biggest problems, before they ever happen, are there components you might see or evidence you might get about deception or about misalignment or about other kinds of problems that we're worried about? So can you build that into the kind of research that you're doing?

[13:10] And then expert consensus. I think to the extent that anyone here has opportunities to find people with different perspectives and try and come to understand where their perspectives are coming from, share your own perspective, look for things that might help bridge and might gradually create more consensus in the space about what we're dealing with. I think that is really, really valuable. And then there's also, multiple times I mentioned these details TBD in the kind of governance interventions that we do have so far. Technical expertise is really necessary to do that implementation and figure out those details in a productive way. And so the thing that I will leave you with is just summing all this up. I think a really important task for the coming years, especially for the governance of these systems, is to focus on building the concepts, the evidence, and the consensus that we currently don’t have in order to take our ability to govern, or our approaches to governance from being speculative or precautionary, which is how I would describe them right now, to being more mature and grounded.

[14:14] And, I’m optimistic that we can do this in the next few years, but it will certainly take concerted work and would love to talk to anyone about what that could look like. So, I’ll be doing office hours, I think, after the next talk. Thank you.
