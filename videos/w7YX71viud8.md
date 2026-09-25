---
id: "w7YX71viud8"
title: "Ben Bucknall  - An Overview of Technical AI Governance [Technical AI Policy]"
url: "https://www.youtube.com/watch?v=w7YX71viud8"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-10-17"
duration_seconds: 1232
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Ben Bucknall  - An Overview of Technical AI Governance [Technical AI Policy]

[Watch on YouTube](https://www.youtube.com/watch?v=w7YX71viud8) · FAR․AI · 2025-10-17 · 20:32

## Chapters

- 0:00 Introduction to the talk
- 1:24 Defining technical governance
- 5:11 Taxonomy of the space
- 7:56 Addressing information deficits
- 12:56 Deep dive into technical areas
- 17:17 Expertise and conclusions

## Description

```text
Ben Bucknall proposes a framework for technical AI governance that categorizes policy targets and capacities in the aim of bridging the gap between policy aspirations and technical realities. 

Highlights:
Disconnect between policy aspirations and technical reality
Transparency scores reveal areas needing improvement 
AI evaluation faces issues of accuracy, cost, reproducibility
Independent AI assessment demands resources and expertise
 Mutual feedback loop essential for effective AI governance

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to the talk

[0:05] I'm going to be speaking today, as Cass and the slides say, essentially just giving an overview of technical AI governance which, yeah, I imagine most of you will have some idea of this topic given that we're all here. But just trying to make sure that everyone's on the same sort of footing given that we come from a lot of different backgrounds. Great. So just a quick outline of the talk. I'll give a bit of background context on what I mean when I say technical AI governance. Some motivations, why I think it's important, a high-level sort of overview and taxonomy of the space. Then I'm going to do a bit of a deep dive just so it doesn't get really boring. Just enumerating all the different areas that I see falling into technical governance.

[0:58] I'm going to zoom in on essentially this idea of addressing information deficits in policymaking. I'm going to talk a little bit about leveraging technical expertise in policy. This is something we've heard about already this morning. So a little bit about this sort of interface between technical experts and policymakers and then just, yeah, a few conclusions.

### Defining technical governance

[1:24] So just in terms of background context, a lot of this talk is essentially based on this paper that we put out last year on which Cass was an author and some other people here, which essentially tried to lay out the space of this new area of technical AI governance that people were talking about and sort of outline what we thought to be the fairly comprehensive set of open problems in this space. So in terms of definitions, what do I mean by technical AI governance? So this is a definition that we used in the paper. We said technical AI governance refers to technical analysis and tools for supporting the effective governance of AI. And we sort of broke this down into, or, you know, say that this is useful for three reasons.

[2:26] Firstly, identifying the need for governance action. So this is sort of tracking trends in development and trying to maybe extrapolate them to identify areas of concern or intervention. Secondly, we have this sort of informing function that it can fulfill where it's sort of feeding into decision making at all different levels. And finally we have the third sort of function here which is enhancing the implementation of governance actions. So this is where a lot of the sort of actual hands-on work, for example on chip mechanisms and this sort of thing which can then be used to better enforce or incentivize governance actions and compliance with them.

[3:29] And just a little bit more on why I think this is important. I think it's been getting better in recent years but there has historically been some amount of disconnect between policy aspirations and technical reality. A sort of example that I give a fair amount of this kind of disconnect is a couple of years ago I remember watermarking being a massive thing in policymaking circles. And this idea of embedding some sort of machine-readable data in the output of AI systems, such that you can identify if a piece of media or content has been AI generated or not. And at the time, and to some extent even still to this day, this is something that is kind of on shaky technical foundations. It's not exactly sure, it's not exactly certain whether it's possible to build watermarking schemes that are adversarially robust, can't be circumvented.

[4:31] And even in my opinion, more foundational questions about what is the purpose of watermarking here, what are you trying to achieve, especially when it comes to watermarking text, when it can just be reworded in some way. And yeah, I guess I like to think about this in some sort of ladder of concreteness where you're sort of moving from aims and principles through the regulatory process and future standards. And as we go along here, it's like you need to have more technical detail and more input from technical expertise. Great. So moving on to just giving a quick taxonomy, as we did in the paper,

### Taxonomy of the space

[5:17] of the sort of sub-areas of technical governance. So we broke it down according to two dimensions, one which we called targets, which are essentially, I guess, concepts or targets along the value chain inputs into the sort of development process going from data compute, the models and algorithms and then finally deployment when systems are actually used. And for each of these we say that there are different capacities that you might want to have as a policymaker or sort of decision maker here with respect to each of these. So for example, assessment, where you're trying to evaluate the data or do model evaluations or sort of impact assessments at deployment time through to verification.

[6:18] So being able to verify claims that are made about systems by others. And then I guess the last one I'll speak about or point to explicitly is operationalization. And I sort of think of this as the process of translating policy aims into actual technical specifications, shall we say? And we put this all together into this sort of two-dimensional grid. I don't expect you to read all of this, but I'll refer you to the paper if it's interesting. We end up with this two-dimensional grid where we sort of try to enumerate the sort of technical problems in each of them. And just to give a few examples quickly, we have stuff like benchmarking, red teaming, evaluation stuff that we've already heard about, which if you're looking at models, for example, would go in the sort of top row, third column, we have preserving the integrity of evaluation data.

[7:23] So this is important to ensure the validity and reliability of evaluations. You want to make sure that the test sets you're using are not included in training data methods for verifying that a given model was trained on a given data set. So this would be in verification, intersect data and a whole bunch of other examples. I'll get more into this in the deep dive section. So now I'm gonna, yeah, do sort of deep dive into addressing

### Addressing information deficits

[8:01] information deficits as a way of, I guess trying to demonstrate how open problems from across this taxonomy can feed into a sort of higher-level problem that we're facing in the AI policy space. So what do I mean by information deficit? I guess in order to take actions or make decisions or craft policy, you need the relevant individuals to have some amount of visibility or information about the topic. Right. And I guess I'll point out this isn't just about regulation. It's not just about regulators having visibility into the thing that they're trying to regulate, but also when it comes to partnerships or procurement or you know, even the decision not to regulate should be one that ideally is meaningfully informed.

[9:06] So I sort of tried to sum it up in this sort of tagline at the bottom here. But in order to take or not take actions, you need the relevant actors to know what AI is, what it can and cannot do, how and where it's being developed, all these different sort of aspects. But at the moment, at least focusing on the information that's visible outside of AI developers, there is a certain amount of opacity here where we can't really see into what's going on. We don't have all the information that we would need to make well-informed decisions. And I guess one thing to note is I've been talking about this in fairly absolute terms so far where we need all the information, but in reality you're not going to have full visibility into everything.

[10:02] There's going to be some amount of uncertainty. But the more information we can have when trying to make decisions, the better I would hope. But looking at the status quo, and this is a nice graph from the Foundation Model Transparency Index that a bunch of folks at Stanford have been working on, we see while some areas are well reported by labs, I guess yeah, this is showing information reported by different model developers on different topics. Some are fairly well reported. One that sticks out is capabilities where I think that says 89% is an average score across all the different developers sort of doing a good job of reporting the capabilities of their systems.

[10:57] But others are seriously lacking here in areas that ideally would really need information into. So if you look at, for example, risks or mitigations, they're 47% and 31% respectively. And then the one at the bottom which really sticks out like a sore thumb is with respect to impacts, where this sort of average score given to developers is down at 15%. And you may say to some extent this is just because we don't have a good way of actually assessing the impacts of systems even within the people that are developing them. And so maybe that's an artifact of them not really having information to report. And so this isn't just about information reporting to some extent, but the ability to gather and synthesize information. So how can we go about gathering this information?

[12:00] And this is where I think it sort of touches on a bunch of different things across the taxonomy that we had in the paper. So we have stuff like the ability to evaluate AI models and systems, evaluate their use and impacts. We saw that was one that was really lacking independent oversight. We just heard from Miranda on, you know, external audits and third-party red teaming and evaluating stuff like ecosystem monitoring. So looking at a sort of broader level at the ecosystem and AI development space in general. And the final sort of example I've got here is about incident reporting so that we can be aware of harms that are materializing due to use of AI systems.

[12:54] So going one level even deeper, I guess. Yeah. First, noting that in each of these

### Deep dive into technical areas

[13:00] there are technical challenges, I'm going to zoom in on focusing on evaluating systems. You know, there's a bunch of questions here or challenges that we might need to solve. So the first one is ensuring validity of our evaluations. That is, how do you know that your evaluation is measuring the concept or construct that you want it to, or that you think it is? And there's a bunch of different types of validity pointed to in the literature coming along from the sort of psychology and experiments in psychology. The second is efficiency. So a challenge here is ensuring the evaluations that we want to run are not too expensive because at the moment they can be very compute intensive or labor intensive.

[13:58] Developing a sort of bespoke benchmark can be really quite expensive. Sort of collating all the data and ensuring it's high quality. So how can we make that whole process more efficient? Thirdly, you might want some amount of replicability and this is particularly challenging at the moment given there may be loads of different model versions and you get different results depending on which specific version you run the evaluation on. Different hardware and software stacks could give different results. You might want some amount of statistical significance. This kind of rubs up against the challenge of efficiency where in order to achieve statistical significance you need to run your evaluation a bunch of times, which raises the cost and yeah, a bunch of different things.

[15:01] Secondly, I'm just going to zoom in on independent oversight. This is something again we heard from Miranda on and there are certain things that you want to ensure here. So how do you ensure independence? I won't touch on that because Miranda did a good job there. Also, the question of access. So how do you ensure that the people doing the evaluations have the access to models and data sets and tooling and infrastructure that they need in order to actually run the evaluations that they've built, all the while preserving the security of the system and data subjects and all that sort of thing? There's a bunch of work going on at the moment relating to privacy-enhancing technologies for this purpose. Information. So similarly to access, how do you ensure that third parties have access to information about the system? You know, how can they confirm the model they're interacting with and evaluating is what they think it is.

[16:14] And then finally I put down expertise. You need to ensure that the people doing the evaluation, the third parties, have a sufficient amount of expertise on the topic. Just in the interest of time. I won't touch too much on incident monitoring. There are ongoing sort of incentives here, including from the OECD, but a lot of these only sort of collect publicly reported incidents, which means that you may be missing a whole range of incidents that aren't publicly reported. And then in order to implement some sort of non-public incident reporting and tracking, you need to ask questions like what information do we need to collect?

[17:06] How are we going to collect it if it's not being reported? Maybe there's some sensitive or private information in there. How do you protect that? Yeah,

### Expertise and conclusions

[17:17] final thing I'm going to touch on is this issue of including technical expertise in policymaking. And we've heard there's been a good amount of progress on this in the previous, I guess one, two, maybe three years. But I think there's still a lot more that needs to be thought about. So I guess there's two ways at least in my mind, that I think you can include technical expertise. You could build it in-house as we're kind of seeing with AISCs in different jurisdictions or drawing on external expertise. And again, we've kind of heard about that already today as we're kind of seeing at the moment with the EU General Purpose AI Codes of Practice or the California Policy Working Group report. And I think one thing that I'll note here in the way that I think about this is that there really needs to be a two-way back and forth kind of discussion here.

[18:32] I think a lot of the time it's thought about as technical expertise feeding into policy. But I think there's also the opposite in that policy needs to communicate to technical expertise what their aims are, what's needed, have that sort of signal of what the demand is. If you think of something like, I guess, compute thresholds, you can have technical experts go away and draw up sort of operationalized plans for implementing thresholds and counting the compute expenditure of developing different models. And they can come up with some suggestions of compute spent on this should be counted, this shouldn't. And then that will go back to policymakers. And then you know, that may the range of different options may have very different outcomes when implemented.

[19:34] And then it's policymakers might look at that and be like, okay, what we're trying to achieve here is more akin to this specific way in terms of not capturing too many models. We want to only capture a handful of models. So the bar needs to be fairly high. And then that needs to go back to the technical experts. And I guess what I'm trying to get at is it's a back and forth sort of push and pull kind of process. And I think it can be quite challenging to set something like that up. So I think I'm going to leave it there. And we have about seven minutes for questions. I put QR codes up of two recent papers on this topic if you want to go away and have a look at those. And yeah, thank you.
