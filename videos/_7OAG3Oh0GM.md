---
id: "_7OAG3Oh0GM"
title: "Yoshua Bengio - Fireside Chat with Yoshua Bengio [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=_7OAG3Oh0GM"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-24"
duration_seconds: 1038
is_short: false
chapters: 7
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Yoshua Bengio - Fireside Chat with Yoshua Bengio [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=_7OAG3Oh0GM) · FAR․AI · 2026-02-24 · 17:18

## Chapters

- 0:00 Introduction to AI risks
- 0:42 Realizing the danger
- 3:36 Safe by design research
- 7:00 Technical and policy balance
- 9:18 International coordination
- 12:39 Misconceptions about AI
- 16:08 Future outlook and hope

## Description

```text
Turing Award winner Yoshua Bengio (MILA, Law Zero) explains why he shifted from pioneering deep learning to warning about its dangers. In this fireside chat with Adam Gleave (FAR.AI), Bengio discusses his "safe by design" AI approach through Law Zero, a nonprofit working to build powerful AI systems that separate capability from intention. The conversation covers why existing AI development paths are risky, the case for international coordination on AI governance, and why even a 1% chance of catastrophe demands serious action. Bengio shares cautious optimism that non-agentic "scientist AI" could serve as a building block for safer systems, while acknowledging we need both technical solutions and policy measures to navigate the path ahead.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to AI risks

[0:00] Adam: It’s great to have you at the San Diego Alignment Workshop, Yoshua. And you’ve been one of our, I think, most frequent flyers at this event. So always good to have you back again. Now, one thing I’m really curious about is you won the Turing Award for pioneering deep learning, so you really had a huge impact on the development of this technology that’s now powering everything from ChatGPT to Claude. But you’re also one of the most vocal, I guess, not exactly skeptics or critics, but warning of the risks of this technology. So what caused you to sort of shift your perspective on that and really like raise the alarm on this technology that you had such a pivotal role in developing? Yoshua: Yeah. So around January 2023, after playing with ChatGPT for a few months,

### Realizing the danger

[0:47] it just exploded in my face that we were on a dangerous path. And I’ve talked a lot about why. We’re building very powerful machines. We don’t really know how to make sure they will do the things we want. That could have lots of catastrophic consequences, either by misuse or by machines competing with humans and having greater intellectual abilities. Now I think an interesting question about this is why didn’t I think about this before? In fact, I was exposed to a lot of the arguments. One of my students was very active in AI safety and I read the relevant books. But somehow I think like many machine learning researchers, I looked the other way or the arguments, you know, I heard them and I didn’t really pay emotional attention to them because we all want to feel good about our work. And it’s only when I started thinking about at an emotional level, you know, what would it mean for my children that I really was forced to confront that we’re taking crazy risks.

[2:11] Adam: Yeah, I mean, I can definitely relate to that. I started working in AI alignment and AI safety back in 2017, but I had deep uncertainty about whether risk is real. I sort of had to get a bit dragged kicking and screaming into the field. I think if I hadn’t been surrounded by some friends who wouldn’t sort of stop talking about it to me, I would have just ignored it. And when I first started working on it, it did feel like, why am I worrying about this? I can’t get my half cheetah in this simulated robotics environment to run forward. AI is going to take over. That’s crazy. And I wish I was wrong. But the pace of capabilities progress has been pretty phenomenal. A lot of risks people have been warning about for a decade or more in some cases like self-preservation, instrumental convergent goals, we’re now seeing with coding agents learning to cheat. In the last year, it’s been a succession of empirical evidence confirming a lot of the worst fears. Now it’s still on a small scale, and capabilities aren’t really at the level where humanity is in danger, but clearly the signs are very obvious.

[3:25] Adam: Yeah. So you’re not just warning people about this, you’re also actively doing research to try and put us on a safer path. Yoshua: I couldn’t do anything else. Adam: Yeah. And so you recently founded Law Zero, which is a nonprofit with, I believe, over $30

### Safe by design research

[3:41] million in philanthropic capital, which is very impressive to have raised, dedicated to research and development of safe by design AI systems. So could you share a bit about what is a safe by design AI system? Why isn’t every AI system safe by design? I mean, that sounds great. Why would you not design a system safely? What are the key missing pieces that you’re working to solve? Yoshua: Because it’s not obvious. Because we’ve been trying to just make AIs more capable, broadly, I mean, as a field, me included. And we also, I think, made the bet that intelligence would be built in a way that’s similar to human intelligence, but humans can do bad things. And if you create something like a human, but more powerful, then that sounds very dangerous.

[4:32] Yeah. So after I realized that we were on a very dangerous path, I decided I need to better understand this and do whatever I could, both by the way, on the policy side and the technology side and research side. But Law Zero is really focusing on how do we design AI that will not harm people. And that means when we think about the design, even before we build anything, we really have a strong theory of why we think this particular approach would avoid the issues that we are already seeing. And in the case of the scientist AI, the bet that I’m making is that first we can disentangle the ability to understand how the world works and make predictions about it, like the laws of physics, for example, and the preference for states of the world, agency and achieving goals, which in humans are completely together. But I think we can disentangle these things so that we can eventually have full control over the intention part in case we continue building machines that are smarter and smarter and have more capabilities.

[5:48] So that’s really the game. If we can build machines that have no intention, can we use that as a building block for safer or even safe, very powerful AI systems? By the way, because of the work I’ve been doing and the theory behind it that I’ve been working on, I’m now more and more convinced that it is feasible. There’s still a lot of open problems, but I’m in a way more optimistic than I was two and a half years ago when I started realizing things are bad. Adam: Well, that’s heartening to hear. So I often when I talk about safe by design AI with people, especially sort of deep learning researchers or people who are building these models, I get a lot of skepticism and I’ll admit I’m not completely convinced myself. So I think the argument I most often hear is okay, maybe it’s possible in some abstract sense, but we’ve gone quite far down this technology tree of large pre-trained foundation models trained on all the Internet’s data. We do some post training, we’ve got something that works pretty well. To go several steps back in the technology tree, try and solve several open

### Technical and policy balance

[7:04] problems and then kind of rebuild back up to that level. Maybe it’s possible, but you’re just going to be kind of several years behind and that’s not really right now. Months count for a huge amount of competitive advantage. So what would you say to that sort of cynical take? Do you think this technology can overtake other approaches? Do we need some kind of policy pressure to make sure that people do build systems safe by design? They can’t just cut corners on safety. Yoshua: Yeah. So there are two aspects to this. One the technical and the other the policy. So on the technical side, I am convinced that we can build machines very quickly, like in a matter of a few years that will be safe and will be capable. One way I like to think about this is more like we have this strange historical path where all the companies are essentially doing the same thing and there’s this huge toolbox of machine learning knowledge and expertise and algorithms. But everyone is circling around a little quarter of surface because they all worried about competition in the next few weeks and staying on the leaderboard.

[8:22] But really the richness of what has been developed in machine learning is completely underexploited. And I think there are pieces of this which don’t need to be completely reinvented, that can be brought together in order to find solution. Now whatever we do, there will be what people call a safety tax. For example, if you want an AI to be safe, that means there are things it cannot do. So there’s a cost for that. And so we also need policy, we need incentives, we need, you know, what are the right ways to do it might be different from different countries. I like market based solutions like insurance, for example, liability insurance. But there is no way we end up solving these problems without international coordination as well.

### International coordination

[9:18] Adam: Yeah, yeah. Well, that leads lovely to the next question I want to ask. So you’ve been involved in a number of efforts, international coordination. I know you signed a letter calling for a treaty. You’ve attended many of these international dialogues in AI safety and of course you chair the international scientific report. Thanks for your contributions to these events. So, you know, I totally agree with you. I mean this is incredibly important. Even if right now there’s only a handful of countries that are really at the frontier in AI, these capabilities are proliferating pretty rapidly. So there does need to be some international effort. But I also see, well, there’s a lot of challenge coordinating even within countries right now. So realistically, sort of, what do you think we can hope for on international coordination? Is that going to be enough? Or maybe another way of putting it is what work can we do perhaps on the technical side to minimize the amount of requirements that we need on an international coordination front?

[10:25] Yoshua: Yeah, I like the last part of your question. The way I think about it is two sided, one, public opinion and two, preparation. So public opinion, because even in authoritarian regimes, public opinion matters. And we can see that when with the support of their population, governments feel an existential threat, they will move and they will move quickly. We’ve seen it with the pandemic, we’ve seen in Europe with Ukraine. They can mobilize lots of money, they can change laws in drastic ways and very quickly when it’s needed. So it’s more a matter of will. Now that being said, I think we need to anticipate those things.

[11:25] So we need to work on getting the public better understanding of the issues and the risks. Because right now it’s a very superficial understanding, but we need to be better prepared. For example, even if countries wanted to coordinate, how do we make sure that they can trust and verify? Right, that’s the key requirements. And how do we prepare in terms of the sort of institutional agreement that would be sustainable in the long term? What sorts of future where there is very, very powerful AIs smarter than us, will not just make sure we don’t get rogue AIs, but also that AI isn’t used as an instrument of power to dominate others. These are very difficult questions that go well beyond the technology. But we can mobilize scholars, we can work on the technical aspects so that it’ll be easier to do and so on. And if there is, say, some kind of accident where the power of the technology becomes clear to many people and the public opinion shifts, I think we need to be ready for these things.

### Misconceptions about AI

[12:43] Adam: Fantastic. And I know that you speak to a wide range of people from sort of policymakers, AI companies, CEOs, obviously the academic community. What would you say is one of the most commonly misunderstood aspects of AI risk? We’d really like to sort of go on the record to correct. Yoshua: I think the biggest obstacle is a mental block about the future being potentially extremely different from the present. And it’s just human. We have a bias that makes us project the future as a slight change with respect to the present. It’s difficult to imagine a world where machines would be smarter than us, for example. But if you go back yourself five years ago and you ask whether the kinds of systems we have now would exist, probably you would say, no, that’s science fiction or something many decades in the future. So that’s what I would have said.

[13:38] So this is the biggest problem. People don’t take the issue seriously enough. And the other related thing is they’re looking for deterministic answers. Oh, it’s going to be that way, it’s going to be that way. But scientifically we know that things are more complicated. There are many plausible scenarios and people don’t necessarily reason well with uncertainty. Even if it was only a 1% chance that something really catastrophic happened, it’s completely unacceptable. But emotionally, many people will just not take it seriously if it’s, oh, it’s only a 1% chance. No, no, it’s a 1% chance we all die. Right. This is not something we can just take lightly. But it’s hard to communicate that. Adam: Yeah, I mean, I’ve noticed that I’ve become a bit complacent about the pace of AI capabilities progress. I was looking back on this year and reasoning models basically didn’t exist until maybe very late in 2024. But they’re only widely used at the start of this year. None of my team were using coding agents. We just weren’t capable of. And now everyone on our team is using it.

[14:47] We’re having to basically rethink our entire recruitment process because just operating assessments are being saturated by LLMs. And obviously on the teaching side, this is also huge, huge issue with students using it. None of this was really a problem last year, but it’s very easy to just get accustomed to these things. I think there is a sort of genuine kind of frog boiling effect where if all of this progress had come in one go, people would think, oh wow, yeah, we really are on the brink of, if not AI replacing us, at least being able to do some extremely dangerous things. And we need to worry about the misuse side of also just, I mean, mosquitoes are less intelligent than us, but they cause a lot of damage. Yoshua: Right. So you can have less intelligent entities that can really pose a major threat. Adam: Maybe my last question, I’m curious if there are any areas you think are particularly underrated in AI alignment. This could be a technical intervention, it could be a policy solution. You’re welcome to say safe by design AI again, but if there’s anything that you think is maybe even more neglected, I’d love to hear what that is.

[15:54] Yoshua: Well, so more broadly, we don’t have enough kind of will and guts to try to tackle the biggest challenges. Evals are super important. We need them because they’re the warning sign.

### Future outlook and hope

[16:15] But what’s going to happen when we start seeing more and more, and we’re already seeing more and more right, of red flags if we don’t have any other mitigation than shutdown? This shutdown is not going to happen because the commercial pressure, the geopolitical pressure is going to mean we’re going to bypass these issues and not take them seriously. And so we need to be prepared with alternative solutions, which means explore many solutions. This is like hard, this is really scientifically hard problem. But we can’t capitulate. We can’t say it’s too hard. We have to invest a lot more energy and talent and personally I think that there are ways and that is why I created Law Zero. I think that there is a path to build machines that are smarter than us and will not harm people.

[17:07] Adam: I think that’s a great note to end on. Thank you so much, Yoshua. Yoshua: My pleasure. Thanks for having me.
