---
id: "7PKx3kS7f4A"
title: "Why Asimov's Laws of Robotics Don't Work - Computerphile"
url: "https://www.youtube.com/watch?v=7PKx3kS7f4A"
channel: "Computerphile"
channel_id: "UC9-y-6csu5WGm29I7JiwpnA"
channel_url: "https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA"
upload_date: "2015-11-06"
duration_seconds: 496
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-GB"}
collections: ["channels/computerphile"]
retrieved: "2026-09-24"
---

# Why Asimov's Laws of Robotics Don't Work - Computerphile

[Watch on YouTube](https://www.youtube.com/watch?v=7PKx3kS7f4A) · Computerphile · 2015-11-06 · 8:16

## Chapters

- 0:00 <Untitled Chapter 1>
- 0:02 The Three Laws of Robotics
- 1:21 Law Number Three a Robot Must Protect Its Own Existence
- 6:47 Simulated Brains

## Description

```text
Audible Free Book: http://www.audible.com/computerphile 
Three or four laws to make robots and AI safe - should be simple right? Rob Miles on why these simple laws are so complicated.

Silicon Brain: 1,000,000 ARM Cores: https://youtu.be/2e06C-yUwlc 
Chip & PIN Fraud: https://youtu.be/Ks0SOn8hjG8 
AI Worst Case Scenario - Deadly Truth of AI: https://youtu.be/tcdVC4e6EV4 
The Singularity & Friendly AI: https://youtu.be/uA9mxq3gneE 
AI Self Improvement: https://youtu.be/5qfIgCiYlfY 

Thanks to Nottingham Hackspace for the location

http://www.facebook.com/computerphile
https://twitter.com/computer_phile

This video was filmed and edited by Sean Riley.

Computer Science at the University of Nottingham: http://bit.ly/nottscomputer

Computerphile is a sister project to Brady Haran's Numberphile. More at http://www.bradyharan.com
```

## Transcript

_Source: human-made captions (en-GB). Timestamps are [m:ss] from the start of the video._

### <Untitled Chapter 1>

[0:00] So, shall we do a video about the three laws of robotics then?

### The Three Laws of Robotics

[0:04] (yeah) Because it keeps coming up in the comments... Okay so the thing is, You won't You won't hear serious AI researchers talking about the three laws of robotics, because they don't work! They never worked. So I think people don't see the three laws talked about, because they're not serious. They haven't been relevant for a very long time and they're out of a science-fiction book and, you know.. So, I'm gonna do it, I wanna be clear that I'm not taking these as-- I'm not taking these seriously! Right? I'm gonna talk about it anyway because it needs to be talked about. So these are some rules that science fiction author Isaac Asimov came up with in his stories as an attempted sort of solution to the problem of making sure that artificial intelligence did what we wanted it to do.

[1:01] 'Shall we read them out and see what they are? I'll look them up, give me a second. Law number 1: A robot may not injure a human being or, through inaction allow a human being to come to harm Law number 2: A robot must obey orders given to it by human beings except where such orders would conflict with the first law.

### Law Number Three a Robot Must Protect Its Own Existence

[1:22] Law number 3: A robot must protect its own existence as long as such protection does not conflict with the first or second laws. I think it was his zeroth one later as well. Law 0: A robot may not harm humanity. Or by inaction allow humanity to come to harm. So it's weird that these keep coming up. Because, they.... Firstly they are made by someone who is writing stories and they are optimized for story-writing. They don't even work in the books. If you read the books, they are all about the ways that these rules go wrong. Various negative consequences. The most unrealistic thing, in my opinion, about how Asimov did his stuff was the way that things go wrong and then get fixed. right?

[2:14] Most of the time, if you have a super-intelligence that is doing something that you don't want it to do there's probably no hero who's going to save the day with cleverness. Real life doesn't work that way. Generally speaking, right? Because they're written in English, how do you define these things? How do you define human without having to first take an ethical stand on almost every issue? And if "human" wasn't hard enough, you then have to define "harm". Right? And you've got the same problem again. Almost any definitions you give for those words, really solid unambiguous definitions that don't rely on human intuition, result in weird quirks of philosophy resulting in your A.I. doing something you really don't want it to do. In order to encode that rule: "Don't allow human being to come to harm" in a way that means anything close to what we intuitively understand it to mean You have to encode within the words "human" and "harm" the entire field of ethics.

[3:18] Right? You have to solve ethics. comprehensively and then use that to make your definitions. So that it doesn't solve the problem. It pushes the problem back one step. Into: now, how do we define these terms? When I say the word human, you know what I mean. And that's not because either of us has a rigorous definition of what human is. We've just sort of learned by general association what a human is the word human points to that structure in your brain but I'm not really transfering the content to you. You can't just say "human" in the utility function of an A.I. and have it expect to know what it means, you have to come up with a definition. And it turns out that coming up with a definition, a good definition of something like human is extremely difficult. Right? It's a really hard problem of essentially of moral philosophy.

[4:12] You'd think it'd be semantics but it really isn't because ok, we can agree that I'm a human, and you're a human That's fine, and that this, for example, is a table. and therefore not a human. You know, the easy stuff, the central examples of the classes are obvious. But the edge cases, the boundaries of the classes become really important. The areas in which we're not sure what really counts as a human. So, for example, people who haven't been born yet. In the abstract, like people who hypothetically could be born 10 years in the future, do they count? People who are in a persistent vegetative state? Don't have any brain activity? Do they fully count as people? People who have died? Or unborn foetuses, right? I mean, there's a huge debate even going on right as we speak about whether they count as people.

[5:06] The higher animals, should we include maybe dolphins, chimpanzees, something like that? Do they have weight? So it turns out, you can't program in, you can't make your specification of humans Without taking an ethical stance on all of these issues. All kinds of weird hypothetical edge cases become relevant When you're talking about a very powerful machine intelligence. Which you otherwise wouldn't think of. So, for example, let's say we say that dead people don't count as humans Then you have an A.I. that will never attempt CPR. This person's died, they're gone, forget about it. Done. Right? Whereas we would say, "no hang on a second they were only dead temporarily, we can bring them back." Right? Okay fine, then we'll say that "People who are dead, if they haven't been dead for, how long?" How long do you have to be dead for? If you get that wrong and you just say oh it's fine. Do try to bring people back once they're dead. Then you may end up with a machine that's desperately trying to revive everyone who's ever died in all of history.

[6:05] Because there are people who count, who have moral weight. Do we want that? I don't know, maybe. But you've got to decide. Right? And that's inherit in your definition of human. You have to take a stance on all kinds of moral issues that we don't actually know with confidence what the answer is. Just to program the thing in and then it gets even harder than that because there are edge cases which don't exist right now. Like talking about living people, dead people, unborn people. That kind of thing, fine. Animals. But there are all kinds of hypothetical things which could exist which may or may not count as human. For example, emulated or simulated brains.

### Simulated Brains

[6:48] Right? If you have a very accurate scan on someone's brain and you run that simulation, is that a person? Does that count? And whichever way you slice that you get interesting outcomes. So if that counts as a person then your machine might be motivated to bring out a situation in which there are no physical humans because physical humans are very difficult to provide for whereas simulated humans you can simulate their inputs and have a much nicer environment for everyone. Is that what we want? I don't know? Is it maybe? I don't know. I don't think anybody does, but the point, you're trying to write an A.I. here, you're an A.I. developer. You didn't sign up for this. We'd like to thank Audible.com for sponsoring this episode of Computerphile and if you like books, check out Audible.com's huge range of audio books.

[7:41] And if you go to audible.com/computerphile there's a chance to download one for free Calum Chace has written a book called Pandora's Brain which is a thriller centred around artificial general intelligence. and if you like that story, there's a supporting non-fiction book called Surviving AI which is also worth checking out. So thanks to audible for sponsoring this episode of computerphile so remember audible.com/computerphile Download a book for free.
