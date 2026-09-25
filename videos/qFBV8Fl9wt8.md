---
id: "qFBV8Fl9wt8"
title: "Making Open-Weight AI Safer by Filtering Training Data | Stella Biderman (EleutherAI)"
url: "https://www.youtube.com/watch?v=qFBV8Fl9wt8"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-08-01"
duration_seconds: 350
is_short: false
chapters: 10
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Making Open-Weight AI Safer by Filtering Training Data | Stella Biderman (EleutherAI)

[Watch on YouTube](https://www.youtube.com/watch?v=qFBV8Fl9wt8) · FAR․AI · 2026-08-01 · 5:50

## Chapters

- 0:00 Making open models safer through data filtering
- 0:17 Why standard safety methods fail for open-weight models
- 1:12 Designing safety around open-model developers' needs
- 1:39 The idea: filter dangerous knowledge from training data
- 1:53 Results: a big drop in biorisk capability (WMDP-Bio)
- 2:23 Robustness to adversarial fine-tuning
- 3:03 The cost vs. robustness trade-off
- 3:38 When does data filtering actually work? Three conditions
- 4:44 Which domains fit, and CBRN
- 5:18 Scaling and low-hanging fruit

## Description

```text
Stella Biderman (EleutherAI) on a safety method built for open-weight models: filtering dangerous knowledge out of the pretraining data.

Biderman argues that the standard safety toolkit, input and output filtering, alignment fine-tuning, and know-your-customer checks, was designed for API models and does not hold for open-weight models that anyone can fine-tune. The alternative, from her team with Oxford and the UK AISI: because narrowly useful dangerous knowledge is intellectually isolated, it can be removed from the pretraining data. Training from scratch with this filtering sharply lowers biorisk capability, measured on WMDP-Bio, and stays robust under adversarial fine-tuning, roughly an order of magnitude more robust than other methods. She gives three conditions for when filtering works and expects it to help most for CBRN information.

Chapters
0:00 Making open models safer through data filtering
0:17 Why standard safety methods fail for open-weight models
1:12 Designing safety around open-model developers' needs
1:39 The idea: filter dangerous knowledge from training data
1:53 Results: a big drop in biorisk capability (WMDP-Bio)
2:23 Robustness to adversarial fine-tuning
3:03 The cost vs. robustness trade-off
3:38 When does data filtering actually work? Three conditions
4:44 Which domains fit, and CBRN
5:18 Scaling and low-hanging fruit

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=B9I56daxBmDAeRwQ

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Making open models safer through data filtering

[0:00] Hello. My name is Stella Biderman. And as was just said, as well as forecasted by Kellen a moment ago, I'm going to be talking about some of our recent research at EleutherAI and with our partners at Oxford and AISI about how to make open models safer through data filtering.

### Why standard safety methods fail for open-weight models

[0:17] So the core of our problem is that there's a whole literature on how to make models safe. That was developed pretty much entirely with an eye towards API models. And none of the leading techniques for making models behave in more desirable ways really work for open-weight models. The three things that most organizations are relying on right now are input and output filtering, which is philosophically inconsistent with the goals of the open-source community, alignment fine-tuning, which, as is by now pretty well known and several speakers have mentioned, is technologically not all that effective for open-weight models that anyone can fine-tune. And then usage monitoring and know-your-customer style requirements, which has both philosophical and technological limitations when applying it to open-weight models. So I think it's really

### Designing safety around open-model developers' needs

[1:12] important to think about the safety of open-weight models from the perspective of people who are developing open-weight models and what they care about and what their needs are, because they're not going to be very receptive to adopting techniques that require them to close off their models, for example. And it is unfortunately common to hear people suggest that solutions to open-weight safety problems are to just not have open-weight models, which doesn't really solve the problem in my view.

### The idea: filter dangerous knowledge from training data

[1:39] So what we did in our paper was we said, look, bioweapons knowledge is this very niche, not broadly useful type of information. I bet we could just look at the training data and take it

### Results: a big drop in biorisk capability (WMDP-Bio)

[1:53] all out. So we did. We trained three models from scratch on DCLM. The gray line is the model that was trained on all of the data, and then we had two filtering techniques. We had a really simple block list, which is the strong filter, and we experimented with adding some false positives back in. And what we found was that for both of these filtered runs, we make a huge impact on the model's ability to answer questions about biorisk as measured by WMDP-Bio.

### Robustness to adversarial fine-tuning

[2:23] And in particular, this is pretty enduring through adversarial fine-tuning. So in the plot on the right-hand side, the top curve, like I said, is the baseline model. The other two are filtered models. The black line shows where — so the x-axis is the how much adversarial fine-tuning someone does to our model. So we take all the biorisk out, we hand you the model, and you want to try to use it to tell you about how to build a bioweapon, so you fine-tune it to do that. How much fine-tuning do you need to do to restore performance to match the model that we could have released just trained normally? And for our strongly filtered model, the answer is like 150 million tokens. There's

### The cost vs. robustness trade-off

[3:03] two possible responses to that. One is, doesn't that only cost like $1,000? Which unfortunately the answer is yes. The other is, isn't that like more than an order of magnitude more robust than any other method? The answer to that is also yes. So there's some pros and some cons. One thing I think is really interesting here is that as the fine-tuning goes on, the capability doesn't continue to increase very much. So the dotted line has seen twice as much adversarial fine-tuning, and the strongly filtered model is barely any better. It's still at like 37 or so percent.

### When does data filtering actually work? Three conditions

[3:38] I think data filtering is really cool. There's also some other burgeoning techniques. Kellin mentioned the work by Alex Cloud on gradient routing, for example. But when should we expect data filtering to work? Because I actually don't think it works for most problems. And we kind of picked our specific problem because we expect it to work there. The three heuristics that we have are: one, the capability that you want to remove needs to be intellectually isolated. It needs to be something that can be clearly identified and removable from the data. Two, it needs to be hard to reconstruct. If the model could just infill and figure out what you took out, that's not going to be very good. It seems almost that there's a notion of natural kinds for AI models. And so it's important to try to figure out what the right conceptual boundaries to take things out of are. And then finally, the model not knowing how to do the thing needs to be consistent with actually being safe. There are plenty of contexts where you actually need to know what unsafe behavior looks like in order to behave safer.

### Which domains fit, and CBRN

[4:44] So I think there's a lot of interesting open questions here. Are these the right heuristics? Which domains satisfy them? Which fail them? What are exceptions to these? I think that at a high level, where I currently expect this technique to be particularly effective is like roughly speaking just CBRN information, but I'd be very curious to see people's thoughts on that. And I am already over time, but yeah, different domains have different situations. Notably, there are some where we strongly expect this to not work.

### Scaling and low-hanging fruit

[5:18] And I have a couple more open problems. How do different techniques compare? How does the effectiveness of this methodology change as you scale? And very few people have sat down and seriously thought about this question. And I think that there's very likely some really interesting and successful low-hanging fruit where if you just sit down and think about the deployment context and the needs of open-source models, there are likely additional interventions that just haven't been discovered yet that could be really useful and impactful.
