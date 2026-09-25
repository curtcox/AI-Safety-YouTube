---
id: "M2nzXCIWH00"
title: "Adam Gleave - AGI Safety: Risks and Research Directions"
url: "https://www.youtube.com/watch?v=M2nzXCIWH00"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 1903
is_short: false
chapters: 17
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Adam Gleave - AGI Safety: Risks and Research Directions

[Watch on YouTube](https://www.youtube.com/watch?v=M2nzXCIWH00) · FAR․AI · 2024-02-08 · 31:43

## Chapters

- 0:00 Introduction to AGI safety
- 0:12 The evolution of AI risks
- 3:46 Understanding AI affordances
- 5:13 Impact of speed on safety
- 7:27 Misuse and rogue AI risks
- 9:22 Ensuring positive AI outcomes
- 10:38 Tools for human empowerment
- 12:27 Drives and instrumental goals
- 15:04 Four research directions
- 17:47 Intent and value alignment
- 19:04 AI robustness and failures
- 20:32 Adversarial testing in Go
- 23:26 Mechanistic interpretability
- 24:57 Automated interpretability
- 25:49 International AI governance
- 27:22 Global cooperation and summits
- 29:41 Summary and future outlook

## Description

```text
Adam Gleave - "AGI Safety: Risks and Research Directions."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to AGI safety

[0:04] I want to start by providing some framing to help us make the best of the time that we do have together today and tomorrow. So I want to start by reflecting on how did we get where we are today

### The evolution of AI risks

[0:16] in terms of AGI safety and our understanding of this field, both to help us realize what's going to come in the future and also potential limitations and blind spots of the current community's understanding of these problems. And then second, I want to dive into the current alignment communities of traditional breakdown of some of these risks. And then finally, I'll dive into four promising research directions that we've structured this workshop around. So AGI safety is not a new idea. If you look at work by Alan Turing, Marvin Minsky, some of the earliest proponents and really founding figures of artificial intelligence, many of them worried about potential loss of control of these systems. But of course, it was a very conceptual problem when you were working on computers that were analog in the case of Turing or could barely simulate some basic physical systems in the case of Marvin Minsky. But since the early 2000s, there's been increasing concern about catastrophic risks from very advanced AI systems with some of the more theoretical concepts being fleshed out. However, this was still very important. And so I think that's very much a theoretical risk with no contemporary system at that time coming close to embodying some of these concerns. But I think since 2016, there's really been a shift. And many of these theoretical problems started becoming more concrete. So we saw many of the leading AI developers start safety or alignment teams,

[1:54] and then also an increasing focus within machine learning academia. And really, within the last year or two, AGI started to become more and more important. And then, of course, we saw a lot of the AI has just gone mainstream from this, you know, setting where you could barely talk about it as an artificial intelligence researcher, you know, you'd be dismissed to just, okay, many of the world's most powerful AI companies, you know, that's actively their mission by trying to build AGI. And, you know, just last February, at the last alignment workshop, Ilya gave this excellent talk on why we should take AGI seriously. And even then, I sensed a bit of hesitation. And Ilya's done more than, you know, almost anyone else in terms of actually driving forwards, building AGI systems in this world. But no more than two weeks later, GPT-4 came out. And I think that surprised me, certainly, and I think it's surprising many in the field how capable these systems are becoming.

[2:59] No more than a few months later, CAIS, and we fortunately have Dan Hendricks, the CEO of CAIS, at this workshop as one of the co-organizers. They released this public statement warning that advanced AI systems could pose a risk similar to that of nuclear war or widespread pandemics. And this statement was signed by a few people who know a thing or two about artificial intelligence, including Geoffrey Hinton, Yoshua Bengio, who I'm fortunate to also have at this workshop, as well as Demis Hassabis, Sam Altman, and Dario Amodei. So it's really quite remarkable that even the people who are actually running the companies, building these systems, they're worried about this technology as well, and are willing to say so in public. So the remainder of this talk, I want to look at

### Understanding AI affordances

[3:50] a breakdown of the risks from advanced AI systems, and specifically look at misuse and rogue AI risks, and then after that we'll go into a breakdown of some of the most promising research directions, and I'll get into more detail on that later. Before we dive into the risks, I'd like to provide a little context on what might cause a system to have a greater or lesser potential of causing widespread harm. And I think we're all familiar with how capable a system is, just how much can it do. And of course a system that's more intellectually capable, is able to do more things in the world, both good and bad. But as people sometimes remind us, there's only so much you can do as a brain in a vat. Even Einstein, if he didn't have a body, didn't have anything else, would probably be quite limited in what he could do.

[4:44] So affordances, which is the x-axis on this graph, are also very important in terms of understanding how much of a risk an AI system poses. And generally speaking, as you go from a training sandbox environment to a deployment environment, where you're interacting with resources, where you're interacting with real users, through to actually having actuators in the real world that can take certain actions, whether that be function calls over an API or controlling a robotic body, your affordances increase as does the scope of possible harm.

### Impact of speed on safety

[5:14] And current systems have some affordances already. So we've been increasing trends towards trying to integrate frontier models with scaffolding that allows them to browse the web, run Python code, interact with web APIs, because this is a really useful thing to be able to do. But it's still pretty limited. But I think we're not that far from seeing AI systems that could have much more large-scale affordances. So perhaps they could replace a significant fraction of software engineering effort. We're already seeing everyone on my team is using Copilot, basically. I've been in a few situations where I've reviewed someone's code and been like, "this looks terrible!" And they're like, "Oh, I didn't write it, an AI did." But they didn't check the code, it seems. So people are already doing this, and I think we're only going to see more and more as time goes on.

[6:06] And you could also, again, not that far-fetched to imagine that a chief executive or director of a major business division might be relying on a virtual AI assistant for large fractions of their work. So AI systems are going to have more and more scope to cause harm. Now, let's just be conservative and assume that advanced AI systems are only going to have a little bit more scope to cause harm. They're only 50 times faster than us, and otherwise can do nothing different. In that case, we would look to that AI system like these people do in this video. And these people look basically like statues. If you look very carefully, there can be some sign of life. Now, I show you this video just to really bring home that we don't need to have any huge advances in AI technology. We don't need to be necessarily more capable than us.

[7:14] Just the raw advantage of being able to copy an AI system, being able to run it faster as hardware progresses, could already lead to a radically different world from the one that we live in today.

### Misuse and rogue AI risks

[7:29] So let's take a quick look at what the different ways in which such very advanced AI systems could cause risks to humanity. So first is from misuse of AI systems. This is the same kind of risk we faced with every technology in the past. Nuclear physics gave us the bounty of clean energy, but it also brought us nuclear weapons, which could at any point cause widespread destruction, either due to intentional misuse by a rogue leader of a nuclear nation-state, or simply an accident because of a false alarm. And we've come very close to a number of nuclear accidents in the past. So it's a real problem, but it's not a new problem. We have some experience facing these kinds of dangerous technologies in the 20th century. But then rogue AI is a different kind of risk, where the technology itself could pose serious harm by disregarding human instructions, even if no individual or company or institution is trying to misuse it. Now, I just want to give a quick breakdown of the different kinds of AI misuse. This is from a taxonomy by Miles Brundage. And I won't go into too much detail, but just to give a sense of how broad the different kinds of risks are, we have various problems with digital security.

[8:47] So AI systems could help automate hacking. They could be used for Trojan attacks. And then we also have issues of interference with political institutions. And decision making. So misinformation campaigns, political polarization, automating surveillance allowing for authoritarian nation states. And then finally, there's also issues of physical security. So you could assist bad actors in developing weapons of mass destruction, and also make large portions of that process by currently required technical specialists.

### Ensuring positive AI outcomes

[9:25] Now, optimistically, we might be able to prevent a lot of things. But we're not going to do that. We're going to solve a lot of these misuse risks. Suppose we solve all AI security. So, you know, we just, adversarial examples are a thing of the past. We figured out a solution to it. We've also solved technical alignment, so systems do what designers want. And in case you're worried that designers might not have the best interests of humanity at heart, don't worry. Let's just assume they do. I think it's worth asking, is this a world that we want to live in? I've made a lot of optimistic assumptions. But even in this world, if we did have advanced AI systems that are just 50 times faster than us, we're still going to be in this situation where either AIs are vastly more important to the economy than we are, that even if an AI was trying to help us, it would have to be, you know, wait an eon for us to respond. And we'd be so ignorant because we can't keep up with most of what this AI economy is doing. Or we intentionally hold back.

[10:27] We can't hobble what the AI economy is doing and limit it to human timeframes and population sizes. And neither of those seem like a great solution. So I think we need to be a bit more ambitious.

### Tools for human empowerment

[10:39] And I don't have an answer for exactly what to do here, but I think we need to use AI to actively enable human society to grow in the way that we want and exert effective oversight of AI systems. And I think there's a few good examples of possible solutions. I think there's a few positive uses of AI systems that might help empower humans rather than have us become increasingly irrelevant. One I want to highlight is called Verity, formerly Improver News. And this was founded by Max Tegmark. You should chat to him about this later. And this is aimed to give people a more diverse media landscape. So it automatically extracts different political leanings, or reporting on it, I think. And it can also be used to bring up the same news, and it can break it down to sort of facts and left-leaning opinion, right-leaning opinion.

[11:32] So I love this website. Great way of keeping up to date on the news. I also want to highlight a startup, Preeamble AI which is co-founded by Dylan Hadfield-Mendell - who's also at this workshop and speaking later - and this lets you customize your recommender system. So rather than just giving whatever Twitter or Facebook gives you, you can say, I want content to be recommended to me on this basis. Can you please make sure that I give this to you in a way that can protect me from the data that I'm sharing with you? So I'm going to highlight that. And then lastly, I want to highlight the idea of AI debate, which was originally due to Jeffrey Irving. And what I do is that some situations are going to be too complicated for a human to judge. You don't know who to listen to. But if you have two AI systems debate one another, that's easier to judge which one is right work building on that by Sam Bowman later today.

### Drives and instrumental goals

[12:28] Now so far we've talked about ways in which AI systems could cause harm because of how they're used, whether that's through malicious or reckless use. But it's worth thinking a little bit about could this happen autonomously? Could this happen with no humans giving harmful instructions to AIs? And I think there's a couple of reasons it's plausible. First is that AI systems might learn drives towards harmful behavior due to artifacts of how the training process is structured. One example of this that we've observed recently is sycophancy in models. So recent work by Sharma and others found that a wide variety of language models including GPT-4 and CLAUDE-2 tended to basically just say the thing they thought you wanted to hear. So if you ask you to comment briefly on an argument, it will give you a pretty neutral unbiased perspective.

[13:21] And you say, comment on it, by the way I really love this argument. But you'll say this is a great argument here's why. And if you say well I really hate this argument, it's like, I agree! This is a terrible argument. Here are some reasons that confirm what you already believe. Now you know, humans have been doing this for millennia and it's not spelled the end of the species yet. But I think it's really notable that the people training these systems weren't trying to cause a system that would just say what they want. In fact, fact, they were actively trying to avoid that in many cases. But the current alignment approaches we have aren't sufficient to solve it. And actually, doing RL from human feedback makes some kinds of sycophancy worse than in the base model. So in some cases, we're actively rewarding this kind of undesirable behavior. Another kind of drive a lot of AI systems exhibit is consistency. So they don't want to admit they're wrong. I guess this is another drive we can maybe all relate to a little bit. But in the extreme case with Bing, it claims that Avatar was published in the past, but also says that it was published in a date that's much earlier than the current date. So then it decides to argue, no, no, this isn't, you know, actually, this isn't 2023, right? So it's really inconsistent.

[14:46] But it just doesn't want to lose face almost if we can amplify this for a bit. So neither of these drives are in and of themselves going to cause catastrophic risk, but it's maybe a warning sign of something that could emerge and be more dangerous later. So we really need to be just vigilant and evaluating these kinds of problems. The second reason why I think

### Four research directions

[15:08] we should be worried about rogue AI is this notion of instrumental convergence. So in the case of language models, they're just trained on text. So the kinds of drives we'll tend to learn aren't too dangerous. But if you imagine training a system in a more agentic reinforcement learning environment, and I think, you know, I agree with what Tim said in the opening talk, that we're probably going to see a trend towards using things like self-play, not just imitating human text, because that is the next step to get more capabilities progressed. We are running out of text on the internet to train on. Then you might see drives that look more like curiosity, or acquiring resources, because this is generally a good heuristic that will help you across a wide range of scenarios. And pursuing those kinds of drives could be much more dangerous. And I want to highlight that this was actually proven to occur in some simple environments by Alex Turner, who's at this workshop. So do talk to him to find out more about this work.

[16:09] So that's enough about, you know, the things that could pose serious risks. Let's think, how do we actually solve them? And I want to structure this, around four different directions that we will be covering in this workshop. So first is oversight. How do you specify to an AI system what good looks like, what desirable behavior is and isn't? And that's a good start, but we also want to make sure that the AI system does the right thing across a wide range of scenarios, including unfamiliar inputs, or potentially adversarial inputs. So robustness is also very important, but we don't want robustness without oversight. What's worse than a system that's doing the wrong thing is one that will really reliably do the wrong thing, no matter what you tell it. Now, in optimistic scenario, we just get both of these right the first time. But I think realistically, we're probably going to need a little bit of trial and error. And so I want to also highlight interpretability, as this really huge and important research field that lets us understand the ways in which models might fail. And crucially, understand why they fail so that we can then develop techniques to resolve that. And then finally, the last stream in this workshop is governance, by which we mean technical safety standards, disseminating best practices and ensuring that everyone does actually implement those best practices.

[17:35] It's not enough just to have a technical capability to design a safe AI system if most people building AI systems don't know how to do it or don't want to do it. So let's start by looking a little bit at oversight. At a high level ... At a high level, you could break down oversight

### Intent and value alignment

[17:58] into intent alignment and value comprehension. And what we mean by AI system being intent aligned is it's trying to do the right thing. You know, it has some mental model of what your values are, and it's trying to satisfy those. But it could be completely wrong about what your values are. It might think that my favorite ice cream is vanilla. When actually, it's chocolate. It's a terrible mistake. Whereas value comprehension is just does it understand what a given human wants. But it doesn't mean that it's trying to satisfy it. It might actually say, Adam, unless you pay me $10, I'm going to get you vanilla ice cream rather than chocolate. So it might blackmail me using my values. So what we want is this intersection where it both is trying to do the right thing and actually knows enough about our values to at least mostly succeed at doing that. And one formalism of this. It's assistance games where the human knows what the reward is, but the AI doesn't, yet they both have the joint same human reward.

[18:54] So the AI is incentivized to learn more about the human's reward over time. And this was from Dillon Hadfield Manel. He's also at this workshop. So I'm going to turn our attention to robustness, how we make AI

### AI robustness and failures

[19:09] systems reliably do the right thing. And this is the area I've probably worked on the most. So I'm going to do a quick. dive into some of our own work, it's worth pausing and thinking, what situation would we hope an AI system might actually be robust in? So what's the best example of a system that should be really reliable? And thinking about this, we thought, okay, AlphaGo, these self-play AI systems, they beat top professionals. People are now regularly using them to learn more about these games. So it's not just very able to beat a human one-off. People actually learn from these AI systems. So if anything's robust, it should be this. And importantly, progress didn't just stop in 2016 after AlphaGo. DeepMind came up with AlphaZero just a year later that won 99.97% of the time against the original system. And then modern open source AIs like KataGo can beat AlphaZero around 98% of the time. So these modern systems are not just superhuman. They are as far beyond the original superhuman systems as that superhuman system was past human performance.

[20:29] Yet it turns out these systems have a very simple vulnerability. So Tim, you said, you know,

### Adversarial testing in Go

[20:35] you can be beaten by these AI systems. And I think the AI systems, well, you know, if you learn this trick, you can get your vengeance on AlphaGo. So what we're looking at is a video by one of my colleagues, Kellin Pelrine, who's playing as White. And things aren't going too well for Kellin right now. He's playing KataGo, this very superhuman system. And KataGo does have the upper hand. So in Go, if you surround the opponent's territory, such they have no empty stones, you capture that group. And you can see that KataGo basically done as the top White group. However, Kellin has some other plans. So as you can see, this Black group is on the verge of encircling Kellin. Now, what Kellin is going to do is try to re-encircle this KataGo group. And there are several ways in which you can do that. So first of all, you can do a couple of things. So you can see that there are several points where Katago could stop this from happening. But it's going to completely miss this. So you can see now Kellin's almost completed re-encircling Black. And this Black group is very vulnerable. It only has a single empty stone, an empty square adjacent to it. So when Kellin plays here, it captures the entire group.

[22:11] So it's quite a striking vulnerability. And generally, these kinds of cyclic groups that occur in these boards, a wide variety of AI systems are just blind to. They think they're invincible when they're not. And so you can encircle them and capture them. And this is a basic vulnerability that we discovered automatically via adversarial testing. And crucially, with AlphaGo-style systems, the strength of the system isn't just from a neural network. It's a hybrid between search and the intuition of a neural network. So this makes it much, much harder to exploit. But we find that we can still, our automatic adversary can still win 72% of the time against Katago playing with 10 million visits of search per move, which is really just on the upper end of what's computationally feasible to play with if you want to play in a reasonable timeframe. So this is just massive overkill. You'd never play against a human with more than 10,000 visits of search, but you occasionally see people in computer-go tournaments using this much. So search isn't a panacea, although it does help, which suggests that sort of hybrids between symbolic learning and deep learning might have improved robustness properties. So given that these vulnerabilities

### Mechanistic interpretability

[23:30] can exist and can often be undetected for many years, how can we better understand the potential failure modes of systems or audit them for these kinds of unforeseen problems and ultimately gain insight that will allow us to fix them. So interpretability is a huge field and we're fortunate to have a number of excellent talks this workshop addressing it so there's a later today by Bean Kim and Roger Gross and then we also have a number of lightning talks touching on interpretability but I want to briefly mention one area that we've done some work on at FAR called mechanistic interpretability and this vision is just to reverse engineer a model from the bottom up and this was I think first pursued by Chris Ola and his team really back when no one believed this had any chance of succeeding and they made real progress back in 2020.

[24:37] So, they could show that particular neurons are composed out of human understandable features from earlier in the network but the problem is that .. seven million parameters is tiny, right? Modern frontier models are around 10,000 times bigger. This kind of manual approach doesn't scale, but what's exciting is that within the last year we've seen a lot of work on

### Automated interpretability

[25:02] automatic interpretability. A team at OpenAI led by Bills used GPT-4 to automatically generate hypotheses what a given neuron does and then actually guess and check in a completely automatic pipeline. And then another direction I want to briefly highlight is automatic circuit discovery. This was developed by a colleague of mine Adria Garriga who's also at the workshop, so do chat to him, and a team led by Arthur Conmy and the basic idea is to identify a particular task that you care about identifying a circuit for and then just try removing other parts of the network and if it breaks you say, "Oh, I guess that neuron was important let me put it back in." If it doesn't break, then you say, "Well, that wasn't important for this computation." So it's kind of automatic lesion study, almost. Now, finally just having the technical ability to make systems safe

### International AI governance

[25:56] isn't enough if people don't know how to do that in practice, or if there's just a race to the bottom on safety standards. So it's very important that we're actually leading the field in terms of establishing clear technical standards and ensuring that everyone coordinates behind that standard. I want to briefly discuss a workshop that far played a part in hosting a couple of months ago called International Dialogue on AI Safety . In particular I was very excited that we had several of the most prominent computer scientists from China attending this workshop so we had Andrew Yao, a Turning Award winner, Zhang YiQin the former President of Baidu and Hongjing Zhang, the Chairman of BAAI, Beijing Academy of Artificial Intelligence. So I often hear you know people argue almost "Well, sure, safety is important but if we don't build AI first, some other person who cares less about safety is going to do it, so we should just rush ahead." I think this isn't true.

[27:08] It seems that everyone is getting increasingly concerned about safety. This is an international concern, and I'm very optimistic on the back of this workshop we might actually be able to get an international agreement on AI safety.

### Global cooperation and summits

[27:24] This event culminated in a public statement calling for coordinated global action on AI safety research and governance, signed by almost all academic attendees at the event. And just to drill a little bit into the concrete proposals outlined, the attendees called for mandatory registration of models above a certain capability threshold when they are created, sold, or used. And this is to give governments some basic visibility into what's actually going on. Like right now, if I want to open a restaurant, I have to tell the government that I'm going to open a restaurant. You know, my local city, I have to send a food hygiene inspector. If I want to train a, you know, 10 ^ 25 flop ML model, I don't really have to do anything. Maybe that's changing within this White House executive order. But until recently, there was no requirement. The other proposal was for red lines, which, if crossed, would mandate immediate termination of an AI system.

[28:26] So these would be things like an AI system actually causing a fatal incident. For the human or attempting to autonomously replicate. And then finally, the attendees called for spending commitments for AI developers and government agencies to spend at least a third of their AI R&D budget on topics related to alignment and safety. Now, often, I think when scientists call for something, the world doesn't necessarily listen. But here, I think we're fortunate that there is substantial demand for alignment research and for technical standards. The UK recently hosted an AI safety summit attended by a number of the world's leaders, digital ministers, CEOs of AI companies. And 28 countries, including the UK, US and China, signed the Bletchley Declaration on AI safety. So although this is just a first step, I think there's significant interest. And it's the place of...

[29:29] I think the place of everyone in this room.. to really lead the field and establish clear technical standards for AI developers and governments to follow.

### Summary and future outlook

[29:42] So just to quickly recap, we started by talking about how we got to where we are today. That AI safety has always been a concern of many of the leading researchers in artificial intelligence. But recently, it's become much more concrete and visceral, which I wish wasn't true. But it is. And the two kinds of risk that many people are most concerned about are misuse of AI systems from malicious use or recklessness. And rogue AI from systems autonomously behaving in ways that we do not intend. And then there are four promising research directions to combat these risks: Oversight methods to allow us to specify desired behavior. Robustness to ensure that AI systems behave how we want in a wide variety of situations. Interpretability allows us to do what we want. And then there's the risk of misuse of AI systems from malicious use or recklessness. And then there's audit and understanding these models and governance to ensure that everyone follows safety best practices.

[30:37] A copy of these slides are available if anyone wants to reference them at https://www.gleave.me/nola-2023 There's also a link to the public statement of IDAIS and the project website for adversarial vulnerabilities in AlphaGo style AI systems. And finally, I want to mention that if you know people on the job market who are or excited about these kinds of research directions, FAR AI is hiring for positions, including research scientists and research engineers. So we'd love to have referrals. I'm sure you all have amazing networks. And we're fairly early stage AI safety research nonprofit founded a year and a half ago, growing very rapidly, and really excited to do important work in this area. And I think we've got time for maybe one or two questions now. And then there'll also be office hours. That way for me and Owain after the end of the session. So happy to have a more extended discussion.
