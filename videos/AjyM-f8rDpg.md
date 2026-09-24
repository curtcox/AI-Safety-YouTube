---
id: "AjyM-f8rDpg"
title: "Concrete Problems in AI Safety (Paper) - Computerphile"
url: "https://www.youtube.com/watch?v=AjyM-f8rDpg"
channel: "Computerphile"
channel_id: "UC9-y-6csu5WGm29I7JiwpnA"
channel_url: "https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA"
upload_date: "2017-06-16"
duration_seconds: 541
is_short: false
chapters: 7
transcript: {"source": "manual", "language": "en"}
collections: ["channels/computerphile"]
retrieved: "2026-09-24"
---

# Concrete Problems in AI Safety (Paper) - Computerphile

[Watch on YouTube](https://www.youtube.com/watch?v=AjyM-f8rDpg) · Computerphile · 2017-06-16 · 9:01

## Chapters

- 0:00 Intro
- 0:30 The Paper
- 1:18 Avoiding Negative Side Effects
- 1:58 Avoiding Reward Hacking
- 2:32 Scalable Oversight
- 3:03 Safe Exploration
- 4:05 Robustness

## Description

```text
AI Safety isn't just Rob Miles' hobby horse, he shows us a published paper from some of the field's leading minds.

More from Rob Miles on his channel: http://bit.ly/Rob_Miles_YouTube 

Apologies for the focus issues throughout this video, they were due to a camera fault. :(

Thanks as ever to Nottingham Hackspace (at least the camera fault allows you to read some of their book titles) 

Concrete Problems in AI Safety paper: https://arxiv.org/pdf/1606.06565.pdf 

AI 'Stop Button' Problem: https://youtu.be/3TYT1QfdfsM 
Onion Routing: https://youtu.be/QRYzre4bf7I 

http://www.facebook.com/computerphile
https://twitter.com/computer_phile

This video was filmed and edited by Sean Riley.

Computer Science at the University of Nottingham: http://bit.ly/nottscomputer

Computerphile is a sister project to Brady Haran's Numberphile. More at http://www.bradyharan.com
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

### Intro

[0:00] Today I thought I'd talk about a paper fairly recent. It was last year A paper called "Concrete Problems in AI Safety" Which is going to be related to the stuff I was talking about before with the "Stop Button". It's got a bunch of authors; mostly from Google Brain Google's AI research department, I guess.. Well a lot of it's AI research, but specifically Google Brain and some people from Stanford and Berkeley and opening iEARN. Whatever... it's a collaboration between a lot of different authors

### The Paper

[0:30] The idea of the paper is trying to lay out a set of problems that we are able to currently make progress on like if we're concerned about this far-off sort of super intelligence stuff.. Sure; it seems important and it's interesting and difficult and whatever, but it's quite difficult to sit down and actually do anything about it because we don't know very much about what a super intelligence would be like or how it would be implemented or whatever.... The idea of this paper is that it... It lays out some problems that we can tackle now which will be helpful now and that I think will be helpful later on as well with more advanced AI systems and making them safe as well. It lists five problems:

### Avoiding Negative Side Effects

[1:18] Avoiding negative side effects, which is quite closely related to the stuff we've been talking about before with the stop button or the stamp collector. A lot of the problems with that can be framed as negative side effects. They do the thing you ask them to but in the process of doing that they do a lot of things but you don't want them to. These are like the robot running over the baby right? Yeah, anything where it does the thing you wanted it to, like it makes you the cup of tea or it collects you stamps or whatever, but in the process of doing that, it also does things you don't want it to do. So those are your negative side effects. So that's the first of the research areas is how do we avoid these negative side effects.. Then there's avoiding reward hacking, which is about

### Avoiding Reward Hacking

[2:00] systems gaming their reward function. Doing something which technically counts but isn't really what you intended the reward function to be. There's a lot of different ways that that can manifest but this is like this is already a common problem in machine learning systems where you come up with your evaluation function or your reward function or whatever your objective function and the system very carefully optimizes to exactly what you wrote and then you realize what you wrote isn't what you meant. Scalable oversight is the

### Scalable Oversight

[2:33] next one. It's a problem that human beings have all the time, anytime you've started a new job. You don't know what to do and you have someone who does who's supervising you. The question is what questions do you ask and how many questions do you ask because current machine learning systems can learn pretty well if you give them a million examples but you don't want your robot to ask you a million questions, you know. You want it to only ask a few questions and use that information efficiently to learn from you. Safe

### Safe Exploration

[3:03] exploration is the next one which is about, well, about safely exploring the range of possible actions. So, you will want the system to experiment, you know, try different things, try out different approaches. That's the only way it's going to find what's going to work but there are some things that you don't want it to try even once like the baby. Right, right.. Yeah you don't want it to say "What happens if I run over this baby?" Do you want certain possible things that it might consider trying to actually not try at all because you can't afford to have them happen even once in the real world. Like a thermonuclear war option; What happens if I do this? You don't want it to try that. Is that the sort of thing that.. Yeah, yeah.. I'm thinking of war games.. Yes, yeah.. yeah. Global Thermal Nuclear War . It runs through a simulation of every possible type of nuclear war, right? But it does it in simulation. You want your system not to run through every possible type of thermonuclear war in real life to find out it doesn't work cause you can't.. It's too unsafe to do that even once. The last

### Robustness

[4:06] area to look into is robustness to distributional shift. Yeah It's a complicated term but the concept is not. It's just that the situation can change over time. So you may end up; you may make something. You train it; it performs well and then things change to be different from the training scenario and that is inherently very difficult. It's something humans struggle with. You find yourself in a situation you've never been in before but the difference I think or one of the useful things that humans do is, notice that there's a problem a lot of current machine learning systems. If something changes underneath them and their training is no longer useful they have no way of knowing that. So they continue being just as confident in their answers that now make no sense because they haven't noticed that there's a change. So.. if we can't make systems that can just react to completely unforeseen circumstances, we may be able to make systems that at least can recognize that they're in unforeseen circumstances and ask for help and then maybe we have a scalable supervision situation there where they recognize the problem and that's when they ask for help. I suppose a simplified simplistic example of this is when you have an out-of-date satnav and it doesn't seem to realize that you happen to be doing 70 miles an hour over a plowed field because somebody else, you know, built a road there. Yeah, exactly. The general tendency of unless you program them

[5:42] specifically not to; to just plow on with what they think they should be doing. Yeah. It can cause problems and in a large scale heavily depended on , you know , in this case, it's your sat-nav. So it's not too big of a deal because it's not actually driving the car and you know what's wrong and you can ignore it As AI systems become more important and more integrated into everything, that kind of thing, can become a real problem. Although, you would hope the car doesn't take you in plowed field in first place. Yeah. Is it an open paper or does it leave us with any answers? Yeah. So the way it does all of these is it gives a quick outline of what the problem is. The example they usually use is a cleaning robot like we've made this. We've made a robot it's in an office or something and it's cleaning up and then they sort of framed the different problems those things that could go wrong in that scenario. So it's pretty similar to they get me a cup of tea and don't run over the baby type set up. It's clean the office and, you know, not knock anything over or destroy anything. And then, for each one, the paper talks about possible approaches to each problem and things we can work on, basically. Things that we don't know how to do yet but which seem like they might be doable in a year or two and some careful thought This paper. Is this one for people to read? Yeah, really good. It doesn't cover anything like the range of the problems in AI safety but of the problems specifically about avoiding accidents, because all of these are

[7:20] these are ways of creating possible accidents, right? Possible causes of accidents. There's all kinds of other problems you've been having in AI that don't fall under accidents but within that area I think it covers everything and it's quite readable. It's quite... It doesn't require really high-level because it's an overview paper, doesn't require high-level AI understanding for the most part. Anyone can read it and it's on archive so you know it's freely available. These guys now working on AI safety, or did this then They've hung their hat up. They've written a paper and they're hoping someone else is gonna sort it all out. These people are working on AI safety right now but they're not the only people. This paper was released in summer of 2016, so it's been about a year since it came out and since then there have been more advances and some of the problems posed have had really interesting solutions or well.. Not solutions, early work, that looks like it could become a solution or approaches new interesting ideas about ways to tackle these problems. So I think as a paper, it's already been successful in stirring new research and giving people a focus to build their AI safety research on top of. So we just need to watch this space, right? Yeah, exactly..
