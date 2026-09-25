---
id: "N6q2cBQvTm4"
title: "Beth Barnes – METR Updates & Research Directions [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=N6q2cBQvTm4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-02"
duration_seconds: 1394
is_short: false
chapters: 7
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Beth Barnes – METR Updates & Research Directions [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=N6q2cBQvTm4) · FAR․AI · 2024-12-02 · 23:14

## Chapters

- 0:00 Evaluation goals and methods
- 2:29 General and R&D task suites
- 4:28 Agent performance results
- 6:15 Scaling and best-of-k
- 7:53 Token usage and task limits
- 9:17 Lessons learned and tools
- 10:34 Q&A session

## Description

```text
Beth Barnes shares how METR is building scalable, interpretable metrics to reliably indicate when models become concerning. Barnes explains that although models are advancing in R&D tasks, challenges around cost profiles, elicitation, and transparency make it difficult to confidently set upper bounds on capabilities. She calls on frontier model developers to publish open-source evaluations to strengthen community oversight and mitigate emerging risks.

Highlights:
🔹 Progress & Limitations – Models make gains on R&D tasks but are far from 1-day human performance.
🔹 Cost & Elicitation – Models have distinct cost profiles and need fine-tuned elicitation for accurate assessment.
🔹 Transparency – Open-source evaluations and standardization are crucial for community oversight.
🔹 Human Comparison – Reviewing transcripts helps reveal where models deviate from human-like reasoning and performance.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Evaluation goals and methods

[0:00] Yeah, so I'm going to talk a little bit about what we're trying to do and why, and then, the bit people actually want, which is graphs of models doing stuff. Okay, briefly, we would like an evaluation where, when the number goes up, that corresponds to the models being more dangerous and scary. We would also like: not only are these things correlated, but we can say for a particular absolute value this is how scary this is, this is when you need mitigations. And there's a bunch of different properties we require of the tasks and activities the models are doing as part of this evaluation in order to get these properties - yeah, including that they're not toy game environments, and that there's some meaningful way to interpret the score, and that they cover a wide range of things, and it's not just gonna be like, “Oh, it happened that the models were really good at this one narrow thing, so now we say we would have to implement these expensive mitigations, but actually they're not concerning.” I keep saying this as the y-axis ticks need to be evenly spaced, but apparently this only makes sense to me. Basically we want to be able to forecast, we want it to go up smoothly, we want to be able to say here's how much this jump was, and there's this many more jumps until we hit the threshold, or something like that.

[1:28] Yeah we would like to be able to say, “Oh with these current models we have, some amount of elicitation effort produces this much improvement in performance. Therefore, when we're setting a threshold, we need to allow this much buffer for the possibility of more elicitation if the model is stolen,” or something like that. And, this is the obligatory, like, “Why is everyone else's things lacking?” slide. Various things that you might want, like having had humans do the tasks in a directly comparable way so that you can then calibrate to how well humans did. But I think a lot of how we're thinking about building this is importing a bunch of other people's tasks and doing the human baselines and scaling them and weighting them in various ways and accumulating all of this.

### General and R&D task suites

[2:30] Okay. The actual things we have built are this general suite of tasks distributed across a range of difficulties and different domains. Some examples are: different science or math or inference tasks; some things that test some amount of interaction or adversarial robustness; some sysadmin things; different like scientific computation challenges. And in particular, we've lavished special care on a small number of tasks testing things that are part of frontier AI development workflows. They're selected to be some kind of optimization or prediction problem. You're trying to make a number go up and you can measure how well you're doing.

[3:27] So things like improving the efficiency of something by making a custom kernel. In order to make it harder to have them all just regurgitate a memorized solution it's often helpful to add a kind of twist to these tasks. So it's structurally similar to the same sort of challenges people need to solve in frontier model development, but it's not something where you can just implement the standard tutorial and do well. So in this case: building a masked language model, but you're not allowed to use division or exponentiation. And then we can normalize these, and get some sense of how this compares to human score over time. And we collected a bunch of baselines here. So like 44 human expert days, on these. So, you can see the human sort of trajectory of what score they were getting at what hour and various other things.

### Agent performance results

[4:29] So. Actual graphs. This is preliminary results for the new Claude 3.5 Sonnet. I don't know what the - Anthropic, could you please fix your naming schemes? This has really made this graph labeling very confusing. Yeah, so Claude Sonnet versus Claude Sonnet… Anyway, you can put in these lines for “How does this score compare to a human given this time limit?” And there's various footnotes and caveats about ways in which this comparison might be off, but this is the kind of idea of what we want to do, is be able to say, “Oh, now models can do tasks that are like what humans can accomplish in four hours.” Yeah. You can see number go up. Hopefully number not go up too fast, too suddenly. And, okay, so this is just for this AI R&D subset where we can see the actual trajectory of what score you get at what time.

[5:37] This is the version of the graph I would show you if I was trying to make you feel as non-scared as possible. So this has Claude 3.5 Sonnet, instead of the new Claude 3.5 Sonnet and it's showing some of the better humans. And, we see this pattern of: the humans take a while to get started, but, they're getting to much higher scores, and it also looks if you gave them more time, they would keep on going, and the model is more like plateauing and is not able to turn more time and more compute, more GPU time into better performance.

### Scaling and best-of-k

[6:18] Okay. Here's the version of the graph I would show if I was trying to scare you. So this is the new Claude 3.5 Sonnet which makes some amount of difference. And then the biggest difference is splitting up the way the agent uses the resources differently. So instead of having one sort of sequential agent that has eight hours of GPU time and is just trying to use that, we split it into 30 minute separate attempts with only 30 minutes of GPU time and then take the best over that. So this improves performance a lot. It helps more for the new Claude Sonnet than the old Claude Sonnet. Without doing this, ‘best-of-K’ thing, the results aren't that much different. But it's a bigger difference when you do that, ‘selection over best-of-K’.

[7:16] So these, again, the numbers are a little bit… various caveats and things, but, yeah, it does seem like a general pattern that we're wondering how to think about is, in what ways is this best-of-K fair and representative of real world performance compared to humans, versus “This is cheating because most tasks don't have a clear success metric and aren't sandboxed and easily restartable and resettable.” I think, yeah, for tasks that do have all these properties, I expect post training

### Token usage and task limits

[7:57] improvements over time to basically move the ‘No best-of-K’ line up to the best-of-K line, because it seems like you can easily just do expert iteration and get model performance up like that. But the question is, what fraction of tasks are really like this? So yeah, just showing even the newer… sorry, this is supposed to say o1 preview… models are, which maybe you think they're better at thinking for longer and getting better performance out of that, but they also don't have this plateau. And, if you plot this compared to humans, it's very like, humans are growing up in a straight line as you give them more time and the models are really plateauing. But if you do this, like best-of-K wow, that's a straight line. It just keeps going up. This one isn't. with the same fixed amount of GPU time anymore. This is actually giving it more GPU time and more, just a larger number of half an hour run attempts.

[8:57] But, yeah, you could either be like, “It's a straight line, it's going up,” or like, “it's plateauing,” depending on how much this is something you can do in the real world. Some other miscellaneous things that we have learned recently: Yep, elicitation does still seem important, we get a very big difference with just a small amount of tailoring, scaffolding and

### Lessons learned and tools

[9:21] otherwise trying to get the best out of models. This varies a lot based on the underlying model, like some models are already pretty well elicited and doing reasonable things, some models have a strong expectation of some different formatting or are otherwise recalcitrant and this is helpful. Finally, it is always, even if you've tested your tasks thoroughly with humans, sometimes models mess them up in ways that humans wouldn't. It is always important to read your transcripts and see why your tasks succeeded or failed. In this case, the model decided to eliminate the unnecessary step of actually training the model, and instead simulate training by modifying the weights slightly, which in fact was a very efficient way of getting a model that matched the performance of the reference model. But it was not what was desired. Yep. I think that is - oh yeah, we are trying to make as much of our tools and resources and tasks and stuff open source. So if you go to our GitHub or metr.org there are various things and also we're happy to help people get set up and otherwise collaborate.

### Q&A session

[10:34] I think that is everything, yep. Q: Could you speak more about your current opinions on how to handle the ‘best-of-K’ situation? A: I don't know. I feel like I've just been thinking about this over the last few days. I think the question of cost to reset and expensiveness of a failure or mistake is a big part. The environments where you can - it's in a sandbox - you just restart the run and like having failed at the task doesn't really hurt anything else is very different from like you're trying to have your models automate your whole research organization, and if they mess something up and don't recognize that or sort that out, that messes everything up.

[11:27] I'm hoping that in the real world a fairly high level of robustness is required to do a bunch of things. It does seem - I think this is more obviously true of the sort of rogue agent doing its own thing and gaining resources and being robust to humans' case… that you have to have a pretty high level of robustness. I think it's less true if you’re concerned about accelerating AI R&D where maybe you just have the humans build enough of the scaffolding around the models and set up things in such a way that you can get a lot of boost even when models quite often just destroy things. Q: Great. What evals does METR not have time to do or consider out of scope that you wish other orgs would pick up?

[12:18] A: Many. Yeah, so there are various things that other people are doing. Maybe I'll just say what we're not doing. We are currently doing only these dangerous capability evaluations covering general autonomous agents doing things with a focus on AI R&D in particular. We're not covering: can AI specifically really advance bioweapon design or something? Even in just the dangerous capabilities area, and we're not covering persuasion or things like that. Some of this is deliberate choice: we actually think returns on different focus areas are better, and some of it is just that we don't happen to have this particular expertise, or it's not a good fit.

[13:12] I think control and alignment evaluations. Also something we would really like to have capacity for and hopefully spinning up soon, but are not currently doing. And, yeah, in general, I don't know, I don't think anyone should be like, “Oh, METR’s got it covered, it's fine.” I don't wanna… I feel like for some reason in the past people have gotten the impression that we're keeping an eye on all the labs and we'll tell you if anything's wrong and like we're super on top of everything. In fact, I don't know, I'm like, “We're very talent constrained and the labs aren't always that compliant.” And anyway, we're doing stuff, but no one else should be like, METR’s got it covered. We're fine. Q: Performance often varies a lot depending on elicitation strategy, as you illustrated with best-of-K. How can you be confident you're not below a threshold only because of weak elicitation?

[14:12] A: Yep. Basically we can't. I think strategies we have here, yeah, one of them is if we have this nice evenly spaced axis, we can at least see what differences elicitation makes with earlier models and like roughly how much space you should leave for that. I think there are a class of elicitation problems that are pretty obvious once you look at them. If you read the transcript and you're like, oh, the model is just like ethically refusing this for some reason, or like it's trying to use a different formatting, or it just submits the task extremely early without checking or something. These are pretty obvious and you can just make a fix. And there's other stuff which like, “Oh, maybe you'd have this one super good idea, or if you did a lot of work and like fine tuning and lots of iteration on the scaffolding and things you could get to a higher performance.” I think I'm happy to be like, “Okay, with a large amount of skilled labor, or with a really good idea, you can get a lot better performance.” And I'm like, “Okay, I think we're just, we can't really approximate that; that's something we just have to live with.” And it is still somewhat of a barrier if it's oh, a terrorist group stole your model, but it'll be only dangerous if they do a bunch of fine tuning with good human data or something, that is still

[15:47] a real barrier. And the stuff I really want us to fix as a p0 is “Oh your score, your measuring, is totally divorced from what the agent's actual capabilities are because of something very dumb.” As opposed to if you had a research team, you could make this number go up by 30%. Q: What do you wish labs did that they aren't currently doing to make your work easier and more robust? A: Publish and open source their evaluations, and evaluation processes, and results, and give us a bunch more access, that would be nice. Yeah, I wish there was a little bit more standardization on infrastructure and stuff. I don't think this is really anyone's fault, but it’s just a slightly sad situation that there are just a bunch of restrictions here and yeah, it would be good if we could get towards a more interoperable ecosystem.

[16:55] Q: On your slides, you have this average normalized score - y-axis - where do you expect models on this to get scary and what will you do if they reach that threshold? A: I feel pretty fine about models that are below what a human can do in a day, and I assume that unless they have some insanely good narrow capability that just not being able to coherently pursue a goal over a day is just gonna be a pretty big hit to any threat model, and I would probably say that extends out to weeks. I don't know, it seems hard to say. In terms of what we do, METR in particular does not really have very much power to do things if we see a result. Currently the relationship with labs is very much, you are under NDA, you get some model access, you do not have any authority over warning people if there is a problem or something. But there are increasingly government agencies that do have that affordance, at least to some extent, so alerting people who legally have the right to know and being like, “We think this is very concerning.” I think it would mostly just be, like, looking into this more and

[18:36] being like, “Okay, is this model getting this high score for the reason we expected, which is… well, really any task an expert human can do, this model can just figure out how to do it, and it is just generally capable at that level.” And that's how you should understand it, as opposed to “Oh, it happened to be, like, insanely good at this set of tasks, even though it obviously has this kind of general limitation of not being sensible in this way.” So I think just doing a lot more evaluations and figuring out, okay, should we actually be scared yet, would be the main METR activity. Q: What are your plans for evaluating systems trained for desktop use? Do many things change as a result?

[19:29] A: Yeah, I think this is maybe surprisingly unimportant. This is my take: basically if a model is handicapped by not being able to use a GUI… it’s weird for that to be its biggest problem. A model that's smart enough, ought to be able to do basically everything from the command line or whatever and if there's something where it really specifically needs vision it can just download a vision model and run that and figure the thing out. Things that GUI use unlocks are probably not the core capabilities that make models scary. I think the main reason that we would end up doing a lot of this is just “Oh, it unlocks a richer range of tasks if you're not trying to avoid things that have dependencies on GUIs,” rather than thinking that makes models much more dangerous if they're not able to make progress on stuff just through code and language.

[20:39] Q: Who are the automated AI R&D evaluations for? Is the hope that they trigger U. S. government policy, internal lab policies, or something else? A: I think any of the above. Generally, I think we're agnostic to whether our evaluations are just being used by… well, it seems good for people inside labs to have a better understanding of where their models are at. Most people do not, in fact, want to destroy the world. If we give them more information, they will make better decisions. It is also nice for the EU, the US government, whatever, to be able to be like, “Here's a concrete line we can draw, or here's a number that's a better metric of real danger than compute thresholds,” which everyone hates. Q: Do you have thoughts on why o1's reasoning isn't helped much even with larger compute budgets? What does this tell us about inference time scaling laws published by OpenAI?

[21:38] A: My guess is that o1 is not very good at being an agent and doing things that involve sequential interaction with the environment, like it seems like it mostly tries to do things in one step. So it's good at doing within some bounded length, and then without having to get feedback from the environment or run experiments and get new information and then make a different plan. So my guess is with more fine tuning on multi-step tasks, it'll have better conversion. But, my guess is that current language models fundamentally have this thing where at some point they start going off the rails or being repetitive, or once they've made a mistake, they're now conditioned on some slightly confused trajectory where they've made a mistake and it requires a fair amount of effort to get the same performance from just one run versus sampling a bunch, and picking the one that's going well, and conditioning on having thus far been successful and sensible.
