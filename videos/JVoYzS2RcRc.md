---
id: "JVoYzS2RcRc"
title: "Alignment and Interpretability: How We Might Get It Right | Been Kim (Google DeepMind)"
url: "https://www.youtube.com/watch?v=JVoYzS2RcRc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 2001
is_short: false
chapters: 14
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Alignment and Interpretability: How We Might Get It Right | Been Kim (Google DeepMind)

[Watch on YouTube](https://www.youtube.com/watch?v=JVoYzS2RcRc) · FAR․AI · 2024-02-08 · 33:21

## Chapters

- 0:00 Defining value alignment
- 0:54 Jeong: values that don't translate
- 2:38 M minus H: what only machines know
- 4:30 The thesis: interpretability as communication
- 5:37 Why pretending machines think like us fails
- 6:31 The trouble with feature attribution
- 9:44 A theoretical limit on saliency methods
- 13:51 What saliency maps are actually good for
- 15:12 Chess as a testbed for learning from machines
- 16:36 Discovering new concepts in AlphaZero
- 22:40 Teaching grandmasters: the three-phase study
- 24:39 An impossible-looking queen sacrifice
- 27:54 Closing: interpretability as extending ourselves
- 29:56 Q&A

## Description

```text
Been Kim on why interpretability is central to AI alignment, and how humans can learn the concepts only machines know, from AlphaGo to AlphaZero.

In this FAR.AI Alignment Workshop talk, Been Kim frames the alignment problem as a communication gap between humans and machines. Using the Korean concept Jeong and AlphaGo's Move 37 against Lee Sedol, she describes a space of knowledge only machines have, M minus H, and argues that interpretability is what lets us reach it. Rather than forcing machine reasoning into human terms, she makes the case that humans have to expand what they know to keep communicating with increasingly capable systems.

She then shows why a decade of feature-attribution and saliency methods, including her own, fell short once measured against a clear goal, backed by a theoretical result on their limits. As a concrete alternative, she walks through extracting genuinely new chess concepts from AlphaZero and teaching them to grandmasters, who improved measurably after learning them. She closes on what this means for alignment beyond chess, from hallucination to safety-critical concepts humans have not yet named.

0:00 Defining value alignment
0:54 Jeong: values that don't translate
2:38 M minus H: what only machines know
4:30 The thesis: interpretability as communication
5:37 Why pretending machines think like us fails
6:31 The trouble with feature attribution
9:44 A theoretical limit on saliency methods
13:51 What saliency maps are actually good for
15:12 Chess as a testbed for learning from machines
16:36 Discovering new concepts in AlphaZero
22:40 Teaching grandmasters: the three-phase study
24:39 An impossible-looking queen sacrifice
27:54 Closing: interpretability as extending ourselves
29:56 Q&A

Learn more: far.ai
Newsletter: far.ai/newsletter
Subscribe for more talks from FAR.AI events
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Defining value alignment

[0:04] Thanks for the generous introduction. I'm excited to be here and give this talk about alignment and interpretability. A good place to start this talk is by defining what value alignment means. I stole this slide from from Iason who defines it as: how can we align AI with human values so that it reliably does what we think it should do? And this definition aligns with the one in the book, The Alignment Problem by Brian Christian. And this book will reappear in this talk again. Now, once you define the problem as such, now you can break this question into two. You ask a technical question, how can we encode those values? And then there is also a normative question, what is the value? Now, I want you to keep these two questions in mind but play some thought experiment with me. So let's

### Jeong: values that don't translate

[0:54] say we're trying to align values of two people and they happen to be from two different culture. And these circles represent vocabularies and concepts that could be described using these vocabularies. And let's just say that I'm person B, I'm from Korea and I wanted to communicate what the value of Jeong means. Anyone in the audience who know what Jeong is? Right, so I can just make it up. So Jeong is something between love and like, and it's not and it's less than love, but it's a little more than like, but it's never a romantic thing. And also it's something that doesn't happen suddenly; there is no Jeong at first sight. It has to take time and it kind of grows into you. Now, if I were to - this concept of Jeong stems from such a fundamental ideas in Korean culture. In order for you to truly understand what this means, I would have to tell you a lot about Korean culture and you probably know if you speak multiple languages, you probably have words like this in your languages too.

[2:02] Words that cannot quite be translated between cultures, between languages without a lot of context. In other words, I would need you to expand what you know in order to truly understand what this Jeong means. So the alignment problem is something similar. We're trying to align values between humans and machines except this time it's a more difficult question because humans and machines, we don't even share very basic principles like we have families, we want to survive. So this gap between perhaps in these two circles are even even bigger.

### M minus H: what only machines know

[2:40] In other words, there is potentially this huge space M minus H that only machines know. And that's the space where this beautiful move 37 that AlphaGo made against its match Lee Sedol in 2016 came from. Go players still talk about this move. We cannot quite understand it maybe in retrospect in pages of details, we can, but we don't quite understand how to generalize this move. And also the unexpected behavior of a machine that we weren't quite prepared for is likely to come from that M minus H space. So if alignment problem, if M equals H, we exactly share the same vocabularies, alignment problem is easier, not easy, but easier. Because once you found the value that you want to align, then maybe, maybe using some theory or something like veil of ignorance, then you can write down the definition of the technical approach that you want to solve.

[3:38] So you can just focus on the technical problem. But of course, that's not the case. The truth is, M is not H. So you will have something like purple dot on the left where it's our value that we care about, but machines don't have vocabulary to express it yet. And you also have something like on the right where it's a value that we care and machines perhaps know it, but it didn't, it wasn't described in a language that we can understand. So we don't know, we can't understand it yet. So how do we solve the alignment problem? We need to expand what we know and doing so actually expands machines too because by knowing more we are able to build machine that can communicate uh with us and align by values with us a little better. And I argue that - I'm here to argue - this whole talk is about convince you of that,

### The thesis: interpretability as communication

[4:30] that interpretability is at the core of enabling communication between humans and machines. And we need to do this by expanding what we know and teach ourselves something new so that we can understand and communicate with machines better. And so that we are not only in a better position to align the values like the purple dot there, but also in a much better position to be prepared for an unexpected harm and risks that we worry about. But there's more. We can actually benefit from these machines. Like imagine we can learn rationale behind move 37, we can do that with medicine and science. In other words, we don't just survive, but we thrive and actually have reasons to, to have these machines around. So hopefully that makes some sense. But you might wonder, well, you know, that's that, that's nice. But alignment problem is already really hard.

[5:27] Can we just focus on H first and maybe I'll do something and that will hopefully fall into something between M and H?

### Why pretending machines think like us fails

[5:37] I'm here to convince you that that's not a good idea. And here's some stories around how what happens when we pretend M is H, that there's no M minus H. So this is the way that we used to think about interpretability. We wanted to know how machines work, their rationale behind their decisions. So we decided that we're going to shoehorn everything into M cap H because what we don't, we don't, in fact, just H because we don't even know where M is. So we developed many, many methods like feature attribution, feature visualization. My own work falls into many of these categories and that didn't go very well. Years after years, we just encounter over and over again empirical and theoretical evidence that this actually doesn't work as well. And you're very welcome then. So, so for those

### The trouble with feature attribution

[6:31] who are less familiar with, what feature attribution is, a family of technical saliency map is aiming to achieve or aiming to do feature attribution. What that means is that we're going to assign a number for each input feature. So if you're doing it, doing it in image classification, we want a number in each pixel. And what a lot of these methods aim to aim to get at is we want to know the shape of the function F of X, the prediction function around this feature X. So if I move the this feature - increase this feature - is this become more likely a bird or less likely a bird or stay the same. Now, the intuition here is that well because I am wiggling this X, this has to do with the result of the model, which is the prediction F of X. In other words, why at the end of the day, we want explanations that has something to do with the prediction and that's why we are doing explanation, right? That sounds pretty obvious. It turns out that's not the case.

[7:33] And the first author of this figure Julius is in the uh in at the workshop here. Um in 2018, we stumbled upon this phenomenon that if we take a trained network and then randomize the weights, so making it basically untrained network and random prediction, the explanation coming from these networks are virtually indistinguishable from the one from trained network. So one is random expla - uh prediction, the other is meaningful prediction and you can't tell them apart. But maybe you can. Maybe, maybe if you stare at it a little longer, maybe there's some difference. You can't because I flipped these two and you didn't even notice, right? Did you see? You can't even tell the difference. I - I don't even know which one is... yeah, I assume this is the right one. And, and we show in qualitatively and quantitatively that this is the case. So this result really bothered us from 2018.

[8:32] And we put these methods in front of the human users and show maybe it's useful in practice. It turned out to be that's also not true. But we always had this itchy spot, but we don't have a theoretical proof that these methods actually don't work as well. Now we finally do. Natasha, who is part of this work, is also in this workshop. Here again, the goal is to get shape of the function. So expectation here as written in the original, one of the paper is that you can use this method to account the contributions of each feature. And what that means is that if the tool assigns zero attribution to a pixel, then the pixel is unused by F of X and F of X is insensitive to X. And in fact, that's how these methods were used in practice. Here's a paper published in Nature and they use one of these methods to uh determine eligibility of medical trial. Our work says none of these inference is true. Just because tool gives you zero attribution doesn't mean that it's unused.

[9:42] It does not mean that F of X is insensitive. So how did we do this the theory proving sketch?

### A theoretical limit on saliency methods

[9:53] We treat this interpretability question as hypothesis testing. So the question is I have a function - I have two hypothesis function is maybe flat or function is maybe going up. Can we tell these apart given this data from this attribution methods? And we show that methods with complete and edited properties - by the way, very reasonable properties to have for these methods, those methods has to satisfy this performance inequality. One minus true negatives is is less or equal to true positives. And what that means is that is this line over here in the in the graph - ideal method would have one true positive and one true negative. One ideal method is in the corner and random guessing in this line.

[10:43] And all methods falls under that line. So you might say, well, that's just maybe worse case. Maybe in practice, this works well. Happens to some structure coming from neural network. It turns out that's not the case. So we did this empirical testing for two concrete downstream tasks: Recourse and Spurious features. Recourse is very commonly used. And task essentially means if one of my features is my income, then if I make more money, would I have approved of this loan? And spurious features you're probably familiar with. And both of these concrete downstream task reduces to hypothesis testing so that we can do this. And for Cifar10 for both of Recourse and Spurious features, we see that actual data uh the the performance lies around that random curve. It's a mirror image of the previous curve we saw.

[11:37] And this was true for a lot of other datasets. But you might wonder and we also wondered but maybe this has to do with the complexity. Maybe if the model is simple, maybe these methods tend to do better, et cetera, et cetera. So we did the testing and here you can see that that is kind of a case where depending on the datasets and depending on the end task, some methods do well. Like in, in this plot, we are drawing both methods that falls under our theorem and methods like LIME and GRAD, who does not fall under our theorem or smooth red. And you can see it's kind of all over the place. Sometimes these methods do well, sometimes they don't. But the problem is you don't know which case of these, your data fall into a priori. You just have to throw it and cross your fingers. So how did this happen?

[12:29] I believe that we pretended M is H because we didn't have anything better. And that made us delusional, that we might be able to understand these machines. In fact, we, treated that - we can see pixels. So maybe if we do something around pixels, we'll understand something. But that turns out to be completely incorrect. I think this would have been prevented had we had a clear goal that we can measure. If we had, then as we develop these methods over many, many years, including myself, we would have got the signal that we're not getting anywhere near the goal or, or maybe we're, we're moving in the wrong direction. In other words, we made a lot of hammers, but we couldn't find a lot of nails. Because once goal is clear, there's actually really a simple method to solve this problem. Getting the slope of the function, you sample around it. And the question is how many samples do we need?

[13:30] You can actually - we show in this paper that you can take this curve upwards by having more samples, if you have more featuresyou will need more samples, et cetera, et cetera. And you can actually do this if you had clear goal, this might not be your goal. But if you had a clear goal, you can just do this simple in using simple method. So what do we learn? I still think that

### What saliency maps are actually good for

[13:54] saliency maps can be useful if that saliency map method happens to align with your goal. Like if you're just trying to generate some hypothesis in a low risk, explorative setting, then this might be your choice. And also pushing science is important too. And I think in particular in mechanistic interpretability may provide foundational insight that get us closer to human machine communication. But we still have to have our eye on the goal. if your goal is to cure cancer, you don't just randomly pick a gene and try to study random aspect about that gene, you carefully select what to study and how you study it. And I think that's what we should do. In other words, always ask if you're developing a method. If your method is an answer, what's the question? So hopefully, I convinced you that pretending that M equals H is not going to be a good idea.

[14:55] So then your question might be, how do you do M minus H - how do we learn? Like is that even possible? Here's a couple of reasons why you should be skeptical. So how do you know a machine is a superhuman. Because it's a superhuman, it's beyond us. We don't know. And who should we teach? Who should be learning?

### Chess as a testbed for learning from machines

[15:14] Who is the expert, who is the the best frontier of human knowledge? How do we know? Like good doctors even themselves disagree. So how do we know who to teach? How do we verify that we learn something new? Because again, this is superhuman. So we wouldn't know, we wouldn't immediately notice. Chess offers an amazing playground as, as a case study because in chess, there's a clear win and lose. You have a ELO rating that I talked about a little bit too that that tells who is better than whom. And you also know who are the best right now because there's tournaments and games every week, every day. And we have grandmasters who are clearly at the frontier of human knowledge. And we can also confirm that experts learn something by quizzing them. Because there's board position, we can ask them to make a move to see learning has made an impact on how they play.

[16:14] And we have of course AlphaZero from DeepMind that beat Stockfish engine, which is the best chess playing engine out there only after four hours of training from scratch. And AlphaZero learns it from self play. That means it plays against itself. So the question is still, is this even possible? TLDR is, yes, it is.

### Discovering new concepts in AlphaZero

[16:36] Otherwise I won't be spending all this time, talk telling you about this. So I mentioned that AlphaZero is self - it learned how to play chess via self play and what that means it has never seen how humans play chess. So you might first wonder. Well, is there any overlap, do we even have M cap H. Some of our previous work show that yes, there is some evidence of AlphaZero having human chess concepts. And this work that I'm about to share with you is taking a step farther and asking can we can we excavate some knowledge from M minus H and teach it to grandmasters. This kind of work is only possible if stars align. And I was very fortunate to work with Lisa, who herself was a chess champion and had a professional chess player life before she joined as a PhD candidate at in Oxford. And this work wouldn't have happened without Lisa.

[17:31] And we had amazing grandmasters that who participated, I'll talk more about them in a bit. So again, here, our goal is clear, our goal is to teach grandmasters new chess concepts and make an impact on how they play the game. The approach is rather simple. So first we start with some ingredients, we discover concepts by embedding that concept into an embedding vector in policy value network. And we filter concepts heavily because we want to be very, very picky when these concepts gets delivered to the grandmasters. And we evaluate algorithmically and I'm going to share more importantly how we evaluate this with humans. First of all, you may wonder what is a concept. We define as the following. We define it as a unit of knowledge that is useful for a task. In this case, winning the game of chess.

[18:23] And we impose two properties not to say this is all the properties that you want, but this one happens to align with what we are trying to do. One, it's a minimal - that it cuts out all the fat and it's sort of concise. And that it's transferable; it can be taught... to AI agent and eventually to a human. In a chess setting, we assume that a concept gives a rise to a plan, a deliberate sequence of moves that players play. There's many ways to operationalize this, but this is one way we choose to do it: We learn a sparse vector and we confirm that this can be transferred to another AI agent or human grandmasters. In a measurable way; it's very important as it's quantitative. So how do we discover concepts. We do convex optimization - constrained convex optimization. Pretty simple thing. One thing to note about AlphaZero: it's not one network, it's actually two components, policy value network and MCTS tightly working together to generate those moves.

[19:24] So our optimization process incorporates both of them. So here we are trying to learn a vector Vcl such that the following constraint is true and the constraint comes from MCTS. MCTS is like a tree. At each node, you have a fork, you have chosen path and unchosen path. Chosen path is, is given the green dots and the red ones are unchosen one. And we simply say, well, if there were a concept in this Vcl, then a concept would more strongly present in the chosen path than any other unchosen path. There's a lot of unchosen path because at each time step, t, you have things that you didn't do, right. So you can, you can kind of enumerate that inequality equation. Now we filter a concept a lot and this turns out to be very important. We filter it in two different ways: teachability and novelty. Teachability is we can, we want to ensure concepts can be taught to another AI agent. This is like if you're teaching another student of a math concept, then what you do is you give them an unseen math problem and see if they can solve it. And that's how you verify that they learn something. And we do the same thing here. Uh and we do that by doing following three simple steps, we choose prototypes (positions) from, by sampled from AlphaZero's previous games. And that closely relates to this concept measured by cosine similarity. Pretty simple. And then we teach student by minimizing the policy of the student and the teacher, the KL divergence is a simple thing.

[21:02] And then we test students on an unseen data like they never seen this position before. And we measure how similar the students moves were compared to the teacher who knows this concept. We filter 96% of the concepts in there. And what's also interesting is how we enforce novelty. We do it in two different ways. One is we do it by construction. We use two AlphaZero models, one at the final training step and one couple of 100,000 epochs before that. And we only use positions that the two disagrees. Now, remember both of these AlphaZeros are already superhuman. So we're doing this as a just extra insurance. Second, we define what we call novelty score by, by doing the following. We first create sort of a language for humans and AlphaZero. And you can do this by decomposing human games like Z-l-h And you can decompose it to find some orthonormal basis and you do the same thing with the AlphaZero, but make sure you only encounter the same number of games of course, otherwise one will have more information. And then we see if I were to reconstruct that concept vector Vcl, which one works better, the AZ basis - AlphaZero basis - or human basis. We say the novel ones are the ones that are better reconstructed using AlphaZero's language or AlphaZero basis. And that's how we define novelty score. And given that we filter a lot of it, and Lisa painstakingly went through them to make sure it's not silly,

[22:36] and we finally deliver those concepts to grandmasters. So here's how we did it.

### Teaching grandmasters: the three-phase study

[22:40] In phase one, we gave players a set of positions and we asked them make a move, and we collect them. And in phase two, we show what AlphaZero would have done on those positions. And this is the learning step. They're learning new concepts. And phase three, we give them unseen set of positions, and ask them to make a move again. And we compare how well they did - how well they learn this concept based on how much they improve comparing phase one and three and all players, some of them significantly improve and learn. Now we're doing something interesting in this phase two. We're giving them the simplest possible explanation and avoid all the potential failures of explanation methods by not using them at all. We just give them what AlphaZero would have done. And by doing that, we're actually heavily relying on these grandmasters' ability to connect the dots because it's pretty sparse information and they would have to somehow create this connection kind of beyond what they're used to in order to understand this.

[23:47] And there's some evidence that they are doing that. And there's of course some concepts that actually none of the experts ever learned, even earned because they don't learn perfectly on all concepts. Oh, for some context, by the way, coaches for these players - these players are so good that coaches for these players spend weeks, months, sometimes, years to teach them one new thing because they probably know all the chess moves that ever happened in the history of chess. And so the fact that we can change the way that they play this much is actually pretty remarkable. So they, they said some nice things too in our qualitative results they said, oh, it's clever, it's interesting. There's definitely some novel elements to it. They say unnatural. It's very flattering. And they also say it's complicated,

### An impossible-looking queen sacrifice

[24:39] it's a nice idea, it's hard to spot etcetera. And here is an example of that concept for those who play chess in the audience, who play chess in the audience. Great, quite a lot. Ok. Wonderful. If you have a difficult question, don't ask me, I will connect you with Lisa because she's the expert. I'll be honest, I spend a lot of time trying to understand this one concept like hours, if not days. But anyway, here's an example. So when human chess player play a game, they have some guiding principles. So first in opening phase like this, they are told to control the center, develop pieces as soon as possible, and bring the king to safety. Now, the grandmaster chooses bishop B3 E3, which does the two of the following: control the center and develop pieces. Now, AlphaZero chooses the Bg5 and I'll let you wonder why for a little bit before I show you exact sequence. It sort of does kind of a crazy thing. So here is the exact sequence. Did you see that? The queen is gone. Alright.

[25:52] I'll show you again. Boom there, right? It's kind of crazy because the queen is the most important piece in your, in your game on your board. And in fact, chess players assign numbers to these pieces. Queen is a nine and bishop and knight are six. So AlphaZero decides to trade nine for six, which is kind of insane move. And the only, it doesn't happen very often in human games and only time this would happen in human game is for a technical reason, which means there is an immediate gain like a checkmate. But in this case, what AlphaZero did is it sacrificed the queen to gain long-term dominance on the board and in particular provoke weakness in black.

[26:48] And this is a grandmaster's words that it's clever that it provokes. So this was like in hindsight, it was also understandable by grandmasters. And grandmasters who trained on this concept, improved by 50% in phase three. And of course, there are many, many, many other concepts in our paper which is on arxiv. Some of the other fun ctheme that runs in AlphaZero's concepts. AlphaZero does not seem to care about the rules. Like humans are told to abide by certain rules. AlphaZero doesn't care. There's a rule that says you only touch each piece once in the opening game so that you can quickly kind of establish your position. AlphaZero doesn't care, it touches everywhere and it kind of replaces pieces everywhere. And AlphaZero tends to be also flexible in planning and executing those plans. And humans just, you develop a plan on the left side of the board, then you kind of stick to it until and you see it through and right side of the board, you also do the same thing, but AlphaZero just goes left and right all over the place, which is kind of interesting.

### Closing: interpretability as extending ourselves

[27:54] So to to a closing note, I think the goal of an alignment problem and interpretability, both are about establishing this communication channel between humans and machines. And I argue that better way to do interpretability is that we extend ourselves. And when we need to learn something new in order to establish this communication and in a way that I'm even, I'm even willing to go a little stronger than that, that might be the only way. And by doing that, we are also expanding the machines' representational space because we are better in position to build machines that can better communicate with us. And here I show a cute example of chess, but of course, we want to go way beyond that. And this was just an example to show, wow, this is possible in a measurable way - learning something new from M minus H.

[28:49] And we want to build the vocabulary of this M minus H space that we can acquire. Maybe my son will be learning this vocabulary from his school going forward because that's something that is essential for humankind. Like we learn math and, other science and at school and we're very trained in that it wasn't something that you weren't born with, but now you're used to it because it's useful for your life. I want to close with this excerpt from the alignment book. Brian was going through some archive of Alan Turing and Alan Turing talks about how he was trying to teach something pretty simple to the machine and he tried everything and machine was kind of slow to learn. So he really had to like enumerate all the sequences to, to make this machine to do something pretty simple. And his panelist and colleague asks: but who is learning, you or machine? And Turing answers, well, I suppose we both were. Special thanks to Claire who helped me prepping this talk and with that,

### Q&A

[29:57] I'm happy to answer any questions. [audience member] Hi. Thank you for the amazing talk. I'm a huge fan of this direction. I mean, I literally named my lab conceptualization lab, but I have a question about the cultural problem here. How do we invent vocabulary and concepts that won't regress onto a simpler interpretation that people find easier to understand? That seems like a huge problem with complex concepts. Like people misuse p-values all the time and say they're confirming the hypothesis instead of rejecting the hypothesis. How do we think about creating a vocabulary that humans can understand and still actively explains machines? Ah, interesting. So, is it like our own fallacy rather than machines' fallacy? Well, you know, that's a, that's a, that's a fun question. I'm really an advocate for studying humans as much as you study machines because we don't even understand ourselves very well.

[30:49] And until then, we can't really think about this fallacy. Like Sam talked about the biases of our humans that is not well studied. Maybe if we correct someone 10 times and they still make the wrong direction wrong decision. And this does happen. Danny Kahneman's book of The Undoing Project, one of my favorite books, talks over and over about how well trained statisticians make wrong judgment over and over again about statistics problem, right? If you write down math, you can solve it, but intuitively, we are just wrong. We're just primed to be wrong. So to answer your question, I don't have an answer, but I think we should really think about how we think about us in this equation. It's not just machines and it's us studying ourselves. How to fit this puzzle together is the part of the puzzle. Thank you. [audience member] Thank you for a great talk.

[31:39] You found some minimal and transferable concepts from M and then you formed this new H which we could call H plus, however M minus H plus might still be non-null and contain very important safety concepts. And in general, why do you think it should be possible to expand M plus to be large enough to capture everything that's salient? And also why do you not focus on restricting M instead of expanding H? Yeah, that's a great question. So first question, I don't think we will ever be in a world where M is H, right? Let's rule that out first. This doesn't even happen between two humans, right? Two Koreans, you put them in the same room, they don't know agree on things. So the question is, where do we focus our intention of our time. Which H plus should we learn? And I think that's a decision as a community to decide. I think next step um for those who are interested in is to go beyond chess and think about a particular problem that we may encounter like hallucination to see how we can acquire that H plus. So that's, that's one thing. And your second question was - is [why not learn] M directly, right?

[32:46] Um because it's too big, we don't have time to learn all of M, right? We can probably only learn some of it. And quite frankly, I think there will be things that we might be, it might be just impossible for current human intelligence to understand. So we don't want to cover all M; that's gonna waste effort. We don't have a lot of time as we, as we talked about in this alignment workshop. So we want to really make an intentional decision of when what we want to study.
