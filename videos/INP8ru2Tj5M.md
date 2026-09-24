---
id: "INP8ru2Tj5M"
title: "The dumbest AI taught the smartest AI. Here’s how that went…"
url: "https://www.youtube.com/watch?v=INP8ru2Tj5M"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-03-07"
duration_seconds: 1059
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-24"
---

# The dumbest AI taught the smartest AI. Here’s how that went…

[Watch on YouTube](https://www.youtube.com/watch?v=INP8ru2Tj5M) · Rational Animations · 2026-03-07 · 17:39

## Chapters

- 0:00 The AI alignment problem
- 2:20 Weak to strong generalization
- 3:54 Understanding supervision
- 5:38 Chess puzzle experiments
- 9:38 Language processing tasks
- 11:36 Learning human preferences
- 14:24 Limitations and risks
- 15:44 Future research and courses

## Description

```text
This video is about weak-to-strong generalization: whether a weaker AI can successfully teach a stronger AI. This is important for superintelligence alignment, because humans may eventually need to supervise AIs that are smarter than they are. If weak supervisors can help align stronger AIs, then humans (or future AIs helping humans) might be able to align superintelligence. In this video, we explore OpenAI’s experiments on this question in depth.

Read the paper here: https://arxiv.org/abs/2312.09390

Robert Miles AI Safety: @RobertMilesAI 

AI Safety courses by BlueDot Impact: https://bluedot.org/

▀▀▀▀▀▀▀▀▀PATREON, MEMBERSHIP, MERCH▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

🟠 Patreon: https://www.patreon.com/rationalanimations

🔵 Channel membership: https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg/join 

🟢 Merch: https://rational-animations-shop.fourthwall.com

🟤 Ko-fi, for one-time and recurring donations: https://ko-fi.com/rationalanimations

▀▀▀▀▀▀▀▀▀SOCIAL & DISCORD▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Rational Animations Discord: https://discord.gg/5Y3Dwz89yH

Reddit: https://www.reddit.com/r/RationalAnimations/

X/Twitter: https://twitter.com/RationalAnimat1

Instagram: https://www.instagram.com/rationalanimations/

TikTok: https://tiktok.com/@rational.animations

BlueSky: https://bsky.app/profile/rationalanimations.bsky.social

▀▀▀▀▀▀▀▀▀PATRONS & MEMBERS▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Thanks to all our patrons and channel members from the Simple Adder tier and above!

A
Alcher Black
Alexander230
Amir Saboury
Apuis Retsam
blasted0glass 
Bleys
BlueNotesBlues
Chad M Jones
Chris Painter
Christian Loomis
Craig Falls
Danealor 
Daniel Chica
Danilo Stefani - Alessandra Erba
David Piepgrass
Dawson
Ducky
Ed 
Edward Yu
Ellis Jones
Felix Akkermans
Forodriac Origamius
Fraser Cain
Gabriel Ledung
Glenn Tarigan
Honyopenyoko
Ingvi Gautsson
Ivan Bachcin
Jackson Emanuel
James Babcock
Jana
JanJan 
Jasper L
Jeroen De Dauw
joe39504589
John
John Everett-Slape
Juan Benet
Klemen Slavic
Kristin Lindquist
loopuleasa
Luke Freeman
Matias Badino
Michael Andregg
Michael Hewitt
Michael Reed
Nathan Fish
Nathan Metzger
Neal Strobl
NMS
noggieB 
Odet Abadia
Patryk Wielopolski
rictic 
Robert Paul Schwin
Scott Alexander
Sequoia 
SQRT42Pi
steven michaels
Stuart Alldritt
Terberlo.dog
Tomas Campos
Tor Barstad
ttw
Vladimir Silyaev
Zachary Taylor
Arjun Arul
John
7ic7ac
Thomas Grip
Teo Val
Jotunus
Torstein Haldorsen
BestProGaming
Rinthean
Arthur Petron
dangered wolf
Laissez Scholar
Boris Bend
Ken Mc
AWyattLife

▀▀▀▀▀▀▀CREDITS▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

The extremely muscular team that made this video happen: https://docs.google.com/document/d/1ERdlgmvLxKEJvFmtYiZ0yJuQlDozjrwwLCcMZPjY_lk/edit?usp=sharing
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

### The AI alignment problem

[0:00] In the future, we might have AIs that are much smarter than we are. Maybe smarter than all of us put together. Something which is more capable than all of humanity combined could probably drive humanity extinct if it wanted to. It could be very difficult to make such a system safe. We guide today's AIs by providing feedback on whether their output is appropriate and aligned with our preferences. That's how we prevent them from outputting harmful content and how we refine their performance on some challenging tasks. But it's unclear whether we'll still be able to give this kind of feedback to superintelligent AIs. How do we give good feedback on code, which is beyond our comprehension or biotechnologies, which we can't evaluate without expensive and dangerous experiments? Especially if we can't trust the AI not to game our alignment techniques. It may be possible to avoid this problem for teaching certain capabilities like mathematics or coding, by using automated verification methods such as proof-checking.

[0:57] But for human values, that approach won't work. So how can we ensure that models will still share our values when they inevitably outthink us? This is a pivotal question for humanity's future. Today's chatbots might be annoying or misleading, but superintelligent systems could pose existential risks. The stakes couldn't be higher. A dangerous AI might evade all monitoring and control and cause catastrophic harm, while a beneficial one could cure diseases and eliminate material scarcity. Let's try to look at the problem more concretely. Suppose you'd like to understand how to prevent future superhuman AIs from ever outputting malicious code. In this context, automated verification methods can't fully solve the problem. An AI could conceal security vulnerabilities that are hard to check automatically. Maybe you'll be able to spot bugs and obviously malicious code, but if the system codes better than you do, it could introduce attack vectors you wouldn't even notice. Yet you'd still be giving it approval, unwittingly telling the AI to produce more malicious code.

[2:01] And it's not just code, of course. At some point, AI will outperform us in every domain, making the stakes far higher and the problem appear everywhere. We need a way to study this now, but how can we do experiments on aligning smarter-than-human AI when it doesn't actually exist yet? Investigating Alignment

### Weak to strong generalization

[2:21] At A Smaller Scale. One idea is to scale down the problem and try to simulate it using current AI. Instead of humans trying to align AI smarter than us, we can test whether weak AIs can successfully align AIs smarter than them. Today's best models play the role of superintelligence, and weaker ones play the role of humans, and we can see what happens. This approach, developed by researchers at OpenAI, offers a way to probe alignment challenges before they become an emergency. Let's return to the coding example again. It stands to reason that it would be difficult to train an AI to never output unsafe code if it codes better than you do. But how can we test this right now? You can take two AI systems: a strong one which is good at coding, and a weaker one which is less good. You then manually carry out safety training on the weaker one to train it to never output unsafe code.

[3:14] Then, rather than manually doing safety training on the stronger system, you have the weaker system take your place. You use the aligned weaker system to run the safety training on the stronger system. The hope is that the stronger system would learn not to output unsafe code, even when the code would have been too complex for the smaller model to evaluate correctly. In that case, the stronger system can be aligned. Even though the system doing the safety training is weaker than it. And that would mean that perhaps we can align an AI that's smarter than we are. This idea is called weak-to-strong generalization. If it holds, it suggests alignment strategies that might scale to future AI systems.

### Understanding supervision

[3:54] The term "generalization" is used in machine learning to describe when AI systems perform well, even on things that they've never seen before. For example, an AI that recognizes whether an email is spam or not should work even for emails it's never seen before, otherwise it would be useless. Ideally, it should be able to generalize well and handle emails, even if they're quite different from any in its training data. In our case, the stronger AI needs to do well, even in new situations that are more complex than the simple cases it's seen during training, since the weak system supervising it can only provide good feedback in the scenarios it understands. But how could a student ever outperform its supervisor? We imagine a good instructor to be a formidable source of knowledge and skill. What can you glean from a supervisor who has only a fraction of your abilities, and gives unreliable feedback?

[4:45] For an intuitive sense of this, imagine a seven year old teaching his college age sister to play a board game he's learned at a summer camp. Though the seven year old messes up a handful of rules and forgets to mention several others, his older sibling understands the gist of the game and is soon able to outplay her brother. This works because the college student uses her judgment to fill in the gaps in the rules. In some sense, her experience and wit make up for the poor quality of the lesson, so she can infer what her brother was trying to explain. Returning to AI systems, the weak supervisor doesn't need to teach the student completely new skills: rather, it evokes knowledge the powerful student already has. And maybe this will also be true when we try to align AIs that are smarter than we are. Perhaps we'll just need to bring out concepts that a future superintelligence already knows in order to align it. How well do strong students

### Chess puzzle experiments

[5:40] learn from weak supervisors? In their paper, OpenAI researchers tested weak-to-strong generalization on three tasks: chess puzzles, natural language processing, and reward modeling. Let's start with the chess puzzles: these involve picking the best moves in a game of chess. To start, they trained a series of models on a flawless solution set to find the best performance they could hope for. They call this the "strong-ceiling performance". In real life, when we're actually trying to align superintelligences. We won't be able to calculate a "strong-ceiling performance", which would be the best possible alignment we could hope for. But for the experiment, it's useful as it gives us an ideal to compare the actual performance to. Here are the strong-ceiling performance scores on a graph. The x-axis represents how much computing power or "compute" for short, has been used to train the strong student.

[6:32] The more compute, the stronger the model. The y-axis represents the scores on the chess puzzles. As you'd expect, the more compute we use to train the model, the better its strong ceiling performance on the chess puzzles. Then the researchers took the weakest model of the bunch and had it act as the supervisor, guessing the best moves for a new set of positions. They used that not so accurate information to train stronger student models. For each trial, we'll call the supervisor's performance, the "weak performance" and the student's performance, the "weak-to-strong performance", since it's the result of a weak model supervising a stronger one. Here are the scores for all the stronger models when trained by the weakest one. You can see that with this week supervisor, stronger students are only able to learn a little better than weaker ones, and even that quickly plateaus. Even very strong students are barely learning any better than weak ones, if they're all learning from the same weak supervisor.

[7:27] To continue the experiment, the researchers tried again with progressively stronger supervisors, which we can plot as more lines on the graph. The lines start further and further to the right because each supervisor model only gets paired with student models stronger than itself. For each supervisor, we see the same pattern from before: students that are slightly stronger than their supervisors can outperform them, but the gains stop as soon as the gap between supervisor and student gets too large. Another way to measure the students' performance is by using a metric the paper calls "performance gap recovered" or PGR. Here's how it works. Suppose that out of ten chess puzzles, the weak supervisor gets four puzzles right and the strong student trained on the flawless solution set gets nine right. Then the performance gap would be nine minus four, five puzzles. If the strong student that's trained using the weak model then gets seven puzzles right, it's closed the gap by three puzzles compared to its weak supervisor.

[8:25] This student's "performance gap recovered" would then be three out of 5 or 0.6. So it's basically "how much better than the teacher did the student do?" If weak-to-strong generalization worked perfectly, a strong student would learn equally well from a weak supervisor as they would from flawless supervision, yielding a PGR of one. And if it didn't work at all, we'd expect the student would just mimic the supervisor and do no better than it, making PGR equal to zero. In reality, the PGR usually lands between these two extremes. Let's look at these results using the PGR instead of the raw scores. We see that for each supervisor, weaker students get higher PGR than stronger students. This happens because the stronger the student is, the higher their strong ceiling performance, and the less they're able to improve by learning from the same weak teacher. We also see that when the supervisors are trained with more compute, the students they supervise achieve higher PGR scores. This means that with a strong supervisor, the performance gap is small and the more capable students can recover most of it.

[9:30] In contrast with a weak supervisor, the gap is much larger, and even a strong student can only recover a smaller portion of it. The next task is Natural Language Processing,

### Language processing tasks

[9:40] where the results are a bit different. The task features a range of language related exercises, from exam questions to sentiment analysis. The procedure was pretty similar to the chess puzzles task. But in this case, the results are a lot more promising: Unlike the chess task where stronger students got lower PGR than weaker ones for language tasks, the performance gains don't stop even when the students are much stronger than their supervisors. In the most promising combinations, students recover over 60% of their maximum potential. Improving the results even further. These are interesting results, but there's more. For both these settings, you can improve the student's performance using some simple tricks. For chess puzzles, we can use a method called "bootstrapping". Instead of directly having the weakest supervisor train the strongest students, the weak supervisor trains a model just a little more capable than itself, which trains a yet more capable model, and so on until the train reaches a final student much stronger than the original supervisor.

[10:40] Let's graph the chess puzzle performance with bootstrapping. This graph works like the previous ones, but the dotted lines show the results from before without bootstrapping. You can see how students aren't able to improve much when the students supervisor gap is too big. Whereas the solid lines represent a bootstrapped set up and you can see they keep going upward despite the growing gap in capabilities between weak supervisor and strong student. For natural language processing, we don't need bootstrapping, as stronger students are still able to learn relatively well from weak supervisors. But there's another technique that can help. In this case, scientists let the student AI pay less attention to the supervisor's answers when it thinks they don't make sense. When the student and supervisor have similar abilities, this actually impedes the student's performance, as it sometimes ignores good guidance, but giving a very strong student the ability to doubt a much weaker supervisor gives significant benefits.

### Learning human preferences

[11:36] Does weak-to-strong generalization hold for learning human preferences? These are encouraging results for chess and natural language processing. But what about learning human preferences. The last task in the experiment is the one most directly relevant to alignment: reward modeling. I have a video on my own channel, Rob Miles AI Safety that goes into Reward Modeling in detail. But basically a reward model is an AI system trained to predict human evaluations of other AI outputs. For example, in one of the most common reward modeling techniques, reinforcement learning from human feedback, you have some AI system generate two different answers to a human's question. You then present those answers to a human and have them pick which they prefer. A reward model is trained on that data to predict which answer the human would prefer. Once trained, the model can take over the supervision task, massively reducing the amount of human work required. To test weak-to-strong generalization for reward modeling, researchers had an existing AI generate a list of responses to a set of prompts.

[12:39] They then ranked these responses from best to worst and fed the ordered list to a weak supervisor, which learned from it, and then attempted to rank a new list of prompts and responses. Finally, a stronger student model learned from this new, imperfectly ranked list, trying to extract useful patterns despite the weak supervision. Unfortunately, reward modeling had the worst weak-to-strong performance of all three tasks. The strong students only recovered about 10% of the performance gap, and that number stayed low across different strengths of both supervisors and students. The researchers tried one more trick to improve this performance, which they called "generative supervision". This gives the model extra contextual information before training. In our board game analogy, the sister might benefit from glancing at the cards, dice, and other parts of the board game she's trying to learn. Preliminary knowledge of the game's concepts will help her make sense of her brother's jumbled explanation. Researchers applied this method to AI by feeding the strong student unprocessed reward modeling data, which consists of prompts and responses without ratings.

[13:43] While generative supervision doesn't tell the students which responses are preferred, it supplies valuable context for the upcoming lesson. They also offered this information to the student trained on flawless data, so the strong ceiling performance values would fit the new experiment. Looking at the graphs once more, generative supervision doubled or even tripled the student's PGR, with students getting 20 or 30% instead of 10%. But even with the benefits of generative supervision, reward modeling still has the worst PGRs of any of the tasks, showing it's the most difficult thing to learn from a weak supervisor ...Which is somewhat worrying considering that this is the example most relevant to alignment. Aligning superhuman AI's might be very different.

### Limitations and risks

[14:27] So if we consider all three tasks, the results are a bit mixed. Going forward, researchers have some worries about the future of weak to strong generalization as AI models get smarter. One problem is superhuman models might turn out to be exceptionally skilled at imitating us, their weak supervisors, and mimic our flawed behavior to a tee. After all, that's what we ask them to do during training. If the older sister can easily remember and apply each rule exactly as her brother instructs, she'll learn his faulty version of the game instead of correcting his mistakes. This is an example of a machine learning problem called overfitting. Here, overfitting becomes especially concerning for large gaps in intelligence between the strong student and the weak supervisor. In the reward modeling setting, students slightly stronger than their supervisors performed better and better over the course of training.

[15:19] In contrast, more advanced students showed an initial improvement, but their performance quickly declined with more supervisor input. This is a worrying trend: As AI systems get increasingly powerful, they might figure out how to imitate us together with all our faults and blunders. Or they might learn that they're better off telling us what we want to hear, instead of what's actually true or good for us. In short, they might learn to deceive us. Much remains unexplored.

### Future research and courses

[15:46] These concerns demonstrate that we need a reliable way to tell whether our setup will scale to superhuman models. Weak-to-strong generalization offers a promising step in that direction by providing a testable analogy, allowing researchers to experiment with different student and supervisor capabilities. But there's still much more to do. Current methods are far from perfect, after all, even if we were optimistic about these results, it's not enough to avoid extinction level failures most of the time. Before we can trust AI systems smarter than us, we need far stronger guarantees, and it's unclear how we'll ever reach that level of confidence. If you'd like to help humanity be better prepared before superintelligent AI arrives, we highly recommend the AI Safety courses by BlueDot Impact at aisafetyfundamentals.com. There you can find a number of courses to help you scale up and eventually contribute to solving this important problem. The courses consist of a selection of readings curated by experts in AI safety.

[16:43] They're available to all, so you can simply read them if you can't formally enroll in the courses. If you want to participate in the program, instead of just going through the readings by yourself, BlueDot Impact runs live courses which you can apply to. They are remote and free of charge. They consist of a few hours of effort per week to go through the readings, plus a weekly call with a facilitator and a group of people learning from the same material. At the end of each course, you can complete a personal project which may help you kickstart your career in AI Safety. I've also made a video on the Rob Miles AI Safety Channel, giving advice about starting a career in AI Safety. Links in the description.
