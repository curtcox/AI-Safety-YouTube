---
id: "9zC58kdIwtA"
title: "Stuart Russell – AI: What If We Succeed?"
url: "https://www.youtube.com/watch?v=9zC58kdIwtA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 1329
is_short: false
chapters: 9
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Stuart Russell – AI: What If We Succeed?

[Watch on YouTube](https://www.youtube.com/watch?v=9zC58kdIwtA) · FAR․AI · 2024-09-10 · 22:09

## Chapters

- 0:00 Intro
- 2:39 Exceeding human capabilities
- 5:15 Whats a mathematically defined problem
- 9:30 Progress
- 12:00 Wellfounded AI
- 14:14 Regulation
- 17:45 Red Lines
- 19:24 Proof Carrying Code
- 20:44 International AI Safety Association

## Description

```text
Stuart Russell from UC Berkeley presenting 'AI: What If We Succeed?'  on July 21, 2024 at the Vienna Alignment Workshop.

Key Highlights:
- Rethinking AI safety from the ground up
- Importance of provably beneficial AI
- Pitfalls of large language models

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/

#AISafety #AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Intro

[0:04] Okay, so I'm going to give quite a high level talk and it'll be quite similar to some of the things you might have heard if you were at the CHAI workshop last month. Some basic principles that I think we all mostly agree on is that we have to plan for AI systems that are going to exceed human capabilities. We might disagree about timelines, but I think almost no one thinks that this is impossible. Most of us think that human control is essential. There are some who argue that we should just get rid of human beings altogether; that our planet would be much better off populated by intelligent AI systems. I disagree, we could take a vote on that. And so the consequence in my view, is that the only option is AI systems that are provably beneficial. Meaning we need formal mathematical guarantees and a lot of apparatus around that to make sure that it happens. Otherwise, I think the other option is the DUNE option where we simply don't have any computers at all.

[1:19] One linguistic change that I would like to make is that we hear many people talking about making AI safe. I think this is a conceptual trap that we have fallen into, where we assume that AI systems are given to us and then our job as a community is to make them safe. This is hopeless, because you are in exactly the same position as if an alien spaceship lands on Earth and then your job is to make the alien things, whatever they are, safe for humanity. Good luck with that. So we have to stop thinking that way. We have to think, “How do we make safe AI systems where, if we do our job right, we don't have to do any testing, because we have constructed them to be safe by construction.” And that's I think the right way to go.

[2:18] And so that means that our field, AI generally, not AI safety, but AI, is going to have to become much more like aviation, and nuclear power, and much less, like avant-garde cookery theater, which is the way the field is right now.

### Exceeding human capabilities

[2:40] Okay, so let me just expand a little bit on “exceeding human capabilities”, and just to emphasize how much momentum there is behind this drive to create superhuman machines. It's easy to show that if you had AGI, the minimum cash value of that would be around 15 quadrillion dollars. And probably far in excess of that. So when we see talk - as we are seeing now - about investing a trillion dollars in the next data center generation but one, that sounds like a lot of money, but it's not. And as we get closer, every step we get closer to this, this magnetic force coming from the future is pulling us harder and harder, making it harder and harder to stop, harder and harder to change direction.

[3:41] My coauthor Peter Norvig thinks we already have succeeded in creating the basic template of AGI just as the Wright brothers succeeded in creating the basic template of an airplane. I don't agree. I think there's a lot more to do. I think we are missing many basic concepts, and I think I actually agree with Yann LeCun on one thing which is that large language models may be a detour on the route to AGI. They're certainly interesting. We may learn a lot about intelligence that we don't currently understand, but they themselves and scaling them up is not the answer.

[4:34] But that's not what I'm going to talk about today. I want to talk about what happens when we succeed. And of course many of you have heard this quote before from Alan Turing in 1951: “... we should have to expect the machines to take control”. And I think what Turing is asking himself before answering that question is: we're going to make these systems that are more intelligent than us, our power over the world comes from our intelligence, so if those systems are more intelligent than us, they're more powerful than us. How do we retain power over them forever? Obviously, we can't.

### Whats a mathematically defined problem

[5:16] If we ask the question a different way, maybe it's a bit less pessimistic. What's a mathematically defined problem such that if the machine solves it, and no matter how well it solves it, we are guaranteed to be happy with the result? This is what I've been trying to think about for the last decade and a bit. And there are two things we have been doing. There are two versions of a mathematical problem that we have been solving. One of them is: here's a fixed objective, optimize the hell out of it. That doesn't work. This is the King Midas problem, the AI pursuing the objective of preventing climate change and doing so by eliminating the cause of climate change, which is us, and so on. All of those stories.

[6:11] In recent years, it's gotten worse because the kinds of systems we're pursuing now, the large language models, are not optimizing a fixed objective. They're not the kind of souped-up RL system that Rich Sutton and others are imagining. Instead, we're training them to imitate human behavior. And when you train a system to imitate another system, and that other system is a goal driven system, then just by ordinary Occam's razor, you're likely to create something in the imitator that resembles the data-generating mechanism that you're trying to imitate. So you're going to get goals inside the large language models.

[7:04] And of course, those goals will be the goals that humans have, and the large language models are going to pursue those goals on their own account. Not try to help humans achieve those goals, but try to achieve those goals for myself. And we can see that when AI systems try to convince humans to marry them, that's a perfectly normal human goal, but a perfectly deviant machine goal. We are creating machines with deviant goals on purpose. It's intrinsic to the approach that we've taken, so it's a fundamental mistake. If we want to avoid at least the first problem where objectives are misspecified we could build machines that know that they don't know what the objective is. They have to act in the interests of humans, but they are explicitly uncertain about what those human interests are. This can be formulated as a game with at least one human participant and at least one machine participant. It's an assistance game because the machines in the game are designed to be of assistance to the humans.

[8:26] Intuitively, if you look at that and you say, what happens if the machines solve this game then you hope, and I think under certain assumptions we can prove, that the humans are going to be happy with the result. In principle, this is a formulation of the AI problem, whose solution we would welcome. And we can see already that solvers of assistance games, the machines will defer to humans they will be minimally invasive, they will only change the parts of the world where they're sure that those are the parts of the world we want changed, they'll leave the other parts as they are to the extent possible, and in the extreme case, they're happy to be switched off. They want to avoid doing whatever it is that would cause us to want them switched off. So those are all good properties and I think that's actually the core of the control problem; can you turn it off. And as I mentioned, it's in our best interest to build these systems and deploy them if we can.

### Progress

[9:32] We are making some progress. There's lots of interesting stuff going on partially observable assistance games. The original formulation assumes full observability. When you have partial observability there's ways that you might think it goes wrong. If you're familiar as a child with the idea of tidying your room by shoving everything under the bed as I used to do and many of you used to do. I can see from Gillian's smile that Dylan used to do that. That actually doesn't happen in this game, but there are other failure modes that we have to be careful of that don't appear in the fully observable case. We're starting to see some progress on scaling up of assistance game solvers to things like Minecraft which is quite exciting that we can now deploy an assistance game solver in Minecraft, and as you start making something, the system is figuring out what you're trying to do and helping you as it goes along and doing quite well at that.

[10:39] We're gaining some progress towards understanding what I think is one of the major philosophical problems here which is the plasticity of human preferences. So we want to avoid machines that satisfy human preferences by manipulating them. We have politicians who do that, but we don't need machines to do that. I'm going to skip over the other things. Just to mention there's still a lot of real work to be done. We are not ready to say, look, throw away your ChatGPT or your Gemini and buy one of these instead. That's still some distance away. And understanding the properties of real humans, the sub rationality that they exhibit in the game is really important. And as Gillian mentioned, how do we deal with the fact that there are many humans and there are going to be many machines playing this game.

[11:40] One folk theorem that we haven't really formulated and proved yet is that if there are many machines all trying to solve the assistance game they won't get in each other's way. There's no sign of the prisoner's dilemma that they face with respect to each other and they should, I think, cooperate to help the humans. So that's good, if it turns out to be true.

### Wellfounded AI

[12:04] That's one direction: assistance game solvers. There are some complementary directions I think are really important. Well-founded AI gets away from this idea that a giant black box lands from outer space and then we make it safe. Instead build the AI systems out of elements we understand that are composed in ways we understand, for example, by using probabilistic programming or similar technologies (some people call it neuro symbolic). Where we can actually analyze the whole structure of the system in the same way that we analyze a nuclear power plant or airplane. Formal oracles, meaning systems in which the AI has only one job, which is to choose which mathematically correct inference step to do next in the process of solving a problem or proving a theorem. And those systems have the advantage that they can only tell you the true consequences of inputs that have been provided. They can't lie to you or try to manipulate you or anything like that. Those would be, I think, reasonably easy to prove safe and they could still be enormously powerful of enormous economic value to us.

[13:25] And so if we come to a situation where we really do face a choice between shutting down AI or driving off the cliff this might be a third option. We don't have to shut down AI, but we can use AI in this very constrained context and still derive economic value from it. To satisfy all the Zuckerbergs of the world who want to get the safer cars and the better medicine and so on; we can still get those things without going off the cliff. Meanwhile, other things are going on. We had the letter from the OpenAI refugees who described what's happening internally in OpenAI as a reckless race for dominance. We've had,

### Regulation

[14:17] in the course of developing the European AI Act, multiple attempts to define general purpose AI systems as not AI systems at all, so that they would be completely unregulated. We had attempts to remove the entire section of the Act that dealt with foundation models. We've had what seems to be a successful attempt to remove safety as a topic from the global AI Safety Summit series that began at Bletchley Park. And extreme reluctance to accept any regulation that has any teeth. I think the underlying narrative is that it's too difficult for us to comply with any regulation that requires us to make a high confidence statement about the safety of the system. And so if you require us to make a high confidence statement about the safety of the system, we are not going to be able to comply and then the Chinese will take over the world. So this is the narrative that we hear over and over again. And I would argue this is not our problem. This is not the human race's problem. This is a problem caused by the technology direction that the companies have chosen. They've chosen a technology direction about which it's impossible to make high confidence statements.

[15:44] This is actually quite analogous to what happened in the aviation industry. I mentioned Orville Wright and his little airplane that went a few hundred yards back in 1903. But of course, as we know that technology direction was very quickly overtaken by a different technology direction, which was breeding larger and larger birds. As those birds got up to the 150, 200 foot wingspan size, it became possible for them to carry passengers and that approach completely dominated the petrol powered thing with wings and mechanical devices. Clearly inferior technology. So this very organic technology that's produced by evolutionary optimization was far more promising and attracted the vast majority of investment. Here's the latest instantiation of that.

[16:49] The problem, of course, is that when they went to the FAA and said, could you certify this aircraft for carrying lots and lots of passengers, the FAA said, look, in all the tests, your birds eat the passengers or drop them in the ocean. So come back when you can prove that these birds are actually safe, with very high probability and will have very few accidents over time. And, of course, as we know, the bird developers lobbied Congress and eliminated the FAA regulations and were able to go ahead with this method of aviation and we, of course, suffered all the consequences as a result. So sometimes industries do make wrong technology choices and then they try to capture the regulatory system to enable that to continue. The idea of red lines is to say to industry, no,

### Red Lines

[17:52] we want high confidence statements. It's hard to say, “Give us a proof that your system is safe,” because safe is too general a property to define; it is context dependent, culture dependent, and has all kinds of difficulties. So it's a very fuzzy line between safe and unsafe behaviors of AI systems. But, there are some things that are obviously unsafe. These are way on the unsafe end and we can define them reasonably clearly. And the proof should be on the developer to show that their system will not cross these red lines. We might also require a non-removable detector for violations, and an off switch in the case of violation as a backup, but we would like an upfront proof as we do for medicines, and airplanes, and nuclear power plants, and so on.

[18:46] These red lines should be clearly defined, ideally so clearly defined that we can detect violations automatically. And they need to be politically defensible because we are facing a multi-billion dollar public relations and lobbying onslaught from the companies to avoid any such regulation. Examples of what we would want to prevent would be things like AI systems replicating themselves without permission, AI systems breaking into other computer systems, AI systems advising terrorists on how to build biological weapons, and so on.

### Proof Carrying Code

[19:26] The next piece that we need is a way to prevent deployment of unsafe AI systems by those who have no interest in complying with regulation. In our existing digital ecosystem, the way it works is basically: I, the computer, am going to run your software. I'm just a nice guy and I like running software, so anything you send to me, I'm going to run it. Unless maybe I have some virus detection firewall that says, “Oh no, that's a virus, I'm not running that.” We actually want to change that model around. I'm going to be the bad guy. I'm going to say, “I'm not going to run your software until you can prove to me that it's safe.” There's a technology invented in the 90s called proof carrying code that allows this to be done efficiently in hardware to check proofs of correctness of software. And so the hardware won't run anything that doesn't have such a proof. This doesn't require any certificate authority. It can be done entirely autonomously. But we might also require that software doesn't run on non-checking hardware. That way we get a network effect to make this transition happen fast.

### International AI Safety Association

[20:46] And just my last thing, on the panel people were saying we should do more of this or less of this. I think we should do all of the above. I think we need an international association for AI safety which currently we don't have. It's great that FAR is organizing this meeting, and CHAI organizes its meeting, and a few others organize meetings at Europe's and AAAI and so on and so forth, but we don't have a global conference, we don't have a global organizing force to speak for the safety community and lobby and do all the rest. So we might do that. I think we need a research institute of truly global scale and funding levels. So it would be complementary to the government based AI safety institutes whose job is not to produce safe AI, but just to act as a kind of a gatekeeper. And then we probably also need AI safety companies whose job it is to produce provably safe AI, but also operate on a scale comparable to the unsafe AI companies. So hopefully we'll have some news on these three things before the end of the year and that's all I have to say. Thank you.
