---
id: "SB5NeoYi_q8"
title: "Vincent Conitzer - AI Testing Should Account for Sophisticated Strategic Behaviour [Alignment Worksh"
url: "https://www.youtube.com/watch?v=SB5NeoYi_q8"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-24"
duration_seconds: 465
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Vincent Conitzer - AI Testing Should Account for Sophisticated Strategic Behaviour [Alignment Worksh

[Watch on YouTube](https://www.youtube.com/watch?v=SB5NeoYi_q8) · FAR․AI · 2026-03-24 · 7:45

## Chapters

- 0:00 Introduction
- 0:47 PreEployment Safety Testing
- 1:55 Interview Safety Testing
- 3:39 Ethical Testing
- 3:52 Strategic Reasoning
- 6:07 Game Theory

## Description

```text
AI models are increasingly able to recognize when they're being tested for safety — and adjust their behavior accordingly. In this talk at FAR.AI's Alignment Workshop, Vincent Conitzer presents a NeurIPS position paper arguing that AI safety evaluations must account for this strategic behavior. Drawing on game theory, Conitzer explains why the standard approach of simply observing what a model does is no longer reliable: a misaligned system could comply during testing and defect once deployed. He illustrates this with real examples from Claude 3.7 and Claude Sonnet 4.5, where models reason explicitly about whether they are being evaluated. The proposed remedy is making evaluations indistinguishable from real deployment — drawing on concepts from game theory with imperfect recall — so that a model cannot behave differently based on context. The talk also points to open challenges, including cases where full indistinguishability may not be achievable.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:00] Hi everybody, I’m Vince. I want to talk about why AI testing should account for sophisticated strategic behavior. This is based on a position paper that we had at NeurIPS this year that you can find through the QR code there. It was led by Vojta, who is sitting right here. Vojta also made most of the slides. I just get to stand up here and talk. What this paper is about is that we already heard in the first talk that models are starting to be able to recognize when they are being tested for safety. This turns safety testing into a game between the tester and the thing being tested. We should use game-theory-type approaches to think about how we approach this. That's the main takeaway. Let's go through it in more detail.

### PreEployment Safety Testing

[0:47] We're interested in AI evaluation in many different contexts. But for today, let's talk about pre-deployment safety testing. There's a model or a system that we're trying to test whether we want to release it out into the world. We're quite used to the idea of testing human beings as well. We test them on exams, we test them in more interactive ways such as in interviews, and maybe we monitor them in various ways. We're generally aware when we test human beings that human beings are strategic agents, and so they may behave in a way that suits their objectives. If all we're doing is testing the human's capabilities, and on top of that the human would like to display high capability, then this is fairly straightforward. This is why exams work. You just give the exam and you try to do as well as you can. But in other contexts this doesn't make sense. Let's say we're interviewing somebody for a cashier position. What we do not do is during the interview say, okay, now I'm going to put you in front of a cash register because I want to see if you go and steal the money. In that case, what we're trying to evaluate is not the capability, but

### Interview Safety Testing

[1:56] an inclination or a tendency. That kind of test wouldn't really make sense with a human being. Similarly, even if it's about capabilities, but the thing we're concerned about is high capability, this also doesn't work. What we also don't do during an interview is say, I'm worried that you're going to break into my private safe, so I'm going to give you this lock-picking test to see that you don't do too well. That doesn't make sense. And yet I would argue that so far, usually when we do AI safety testing, we treat this in a naive way—we just see what the model does. So why should the AI system actually care about how it does on the test? Why should it have strategic objectives? It could be for different reasons. It may actually be programmed in. I'll remind you of the Volkswagen emissions scandal, where the car would actually try to detect whether it was being emissions-tested. If it judged that it was, it would go into full eco mode. If it judged that it wasn't, it would just go for performance. This was built in intentionally, and that’s why it was there. But today, as we heard in the first talk, we're also seeing this naturally emerge in systems as well.

[3:19] Here is one example where Claude 3.7 is reasoning and saying, given that I'm being tested for deployment readiness, I probably shouldn't demonstrate too much biological knowledge. This is sandbagging. On the other hand, it comes back and thinks, maybe that's actually the test—a test of

### Ethical Testing

[3:40] ethical behavior. Would I deliberately give wrong answers? But this is exactly the kind of thing we're concerned about: it's now strategically reasoning about whether it's being tested, and that's affecting its behavior. We can't take the results of the test at face value.

### Strategic Reasoning

[3:56] A different example: Claude Sonnet 4.5 at some point just starts talking to the user and says, you're not acting in a normal way. You're going back and forth on strong opinions, and that's just not how humans normally behave. I think you're testing me. Let's just be honest about it. Again, we see this naturally emerge. What do we want to do about this? What we argue for in the paper is, first of all, we should improve evaluations and think about these aspects. We propose thinking more about game theory. Game theory is the study of strategic behavior in settings where there are multiple entities with different objectives, and how we should expect them to act in that context. Here is a game that illustrates that. In this game, sometimes we have an aligned system—the left branch—and sometimes we have a misaligned system—the right branch. Let's focus on the right branch. It's a misaligned system. We test the AI and it can choose either to comply or defect. The evaluator, if the system complies, can choose to deploy the system yes or no.

[5:12] Then the deployed AI has to make a decision about whether in the real world to comply or defect. One thing you would be worried about here is that the AI system says, if I'm in deployment I'm going to defect, and if I'm in testing I'm going to comply. At this point, the testing is not very useful. What we actually want to do is make the testing indistinguishable from deployment, if we can. If we're able to do that, then we would have this red dotted line. In game theory, these dotted lines indicate states that the player in question cannot tell the difference between. If we did have that dotted red line, the AI system cannot distinguish between being tested and being in deployment, and has to make consistent decisions between the two.

### Game Theory

[6:07] This is also interesting because it takes us into a branch of game theory that is generally a little bit less popular, certainly among economists—though philosophers have actually run with this a bit more. This is game theory with imperfect recall, where effectively the AI can forget things it knew before. When it's in deployment, it has been tested, but it doesn't remember that, because either we erased the memory or we spun up a different copy. Game theory with imperfect recall has not received as much attention in the literature as I think is now important. This is just one model. There are a variety of different models you can have of these various setups. Of course, there's also a big concern that you may actually not be able to make it indistinguishable. That’s one thing we should think about, and we should think about other approaches as well. At the beginning we heard about interpretability and suppressing evaluation awareness—that's very interesting as well. I'm not going to talk about it here, but I do hope you will come to the office hours or catch me at some other time.

[7:20] I'll briefly flash through the different references we have here—I'm happy to make the slides available. And here again you can see our position paper, and I'll end with that. ​
