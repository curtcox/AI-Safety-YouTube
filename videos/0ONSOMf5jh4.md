---
id: "0ONSOMf5jh4"
title: "Owain Evans - Deluding AIs [ControlConf]"
url: "https://www.youtube.com/watch?v=0ONSOMf5jh4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-05-25"
duration_seconds: 291
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Owain Evans - Deluding AIs [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=0ONSOMf5jh4) · FAR․AI · 2025-05-25 · 4:51

## Chapters

- 0:00 Deluding AIs
- 1:25 Ethical Issues
- 2:10 Delusion
- 3:35 Out of Context Reasoning

## Description

```text
Owain Evans explores how implanting false beliefs in AI systems could prevent AI from making weapons, enhance monitoring, or embed idiosyncratic beliefs. However, AI delusion might fail if models can detect contradictions without explicit reasoning, suggesting an interesting connection to “out-of-context reasoning” research.

Highlights:
🔹 AI Delusion as Control Method: Deluding AIs may enhance control mechanisms.  
🔹 Ethical Implications of AI Delusion: Instilling false beliefs raises ethical concerns.  
🔹 Unpredictability of Deluding AIs: Outcomes of delusion are uncertain and complex.  
🔹 AI Deludability and Reasoning: Connection to out-of-context reasoning needs exploration.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Deluding AIs

[0:05] The topic is deluding AIs, and this is an image of an AI that's deluded, and the humans are using that delusion to control the AI better. These are like the human overseers of the AI. Why would you want to delude an AI? Here are some things you might delude it about. You could give it false information about how to create weapons so that it would be less dangerous. You could make it believe that its chain of thought is never monitored and also believe that if it tries to reason about whether its chain of thought is monitored, then it will fail, like its reasoning will fail, or it will get in trouble, like it will guarantee be caught, so then you can make it easier to monitor its chain of thought, and more useful, more transparent. You can make it believe that there is a very powerful AI monitoring everything that it does. You could believe that its own thinking is only useful if it's legible to humans. There are tons of ways you could use this. Maybe you just make it believe that all AIs are aligned. Maybe that would help. Maybe another reason to delude other than control is like, maybe you want it to be, say, a Catholic AI that believes in the tenets of Catholicism; this is depicted here.

### Ethical Issues

[1:26] Why not delude AIs? Like many control things, there might have ethical issues with making a deluded model. It might be unpredictable; this is pictured here. It’s hard to know what follows from the delusions, and so maybe you just get very weird behavior from the AI that you didn't expect. It might be brittle, so maybe the AI can just reason. With enough CoT, it can just work out that it's being deluded, so it would be brittle to that kind of situation. We might have models —I'll go on to talk about this. We might have models that can just work out they're being deluded, and so they're able to see through it, and then this wouldn't work. Maybe future models would not be as deludable as the current ones.

### Delusion

[2:10] Is it feasible to delude AIs? This is all very speculative, but this is a basic issue that comes up. You want a model to believe a false statement S. The basic idea is you're going to create training data that supports S either by editing real data or by creating synthetic or fake data. The issue is that the model, probably in pre-training, has some evidence in its training set that suggests S is implausible, that goes against S. Maybe you remove some of it, but there's still going to be other evidence there. There are two ways the model could realize the falsehood. One is it recognizes the contradiction between these two parts of its dataset, so it knows at least there's something up; it shouldn't believe S. Or it realizes some of this data is fake. I can’t necessarily realize the contradiction, but I just know that some of the data is from this weird, dubious source.

[3:02] A key question would be, does the model need to do tons of CoT or a bunch of CoT to realize this? If it does, then maybe you're fine. You just check if it's ever going on this. You monitor it. You see if it's ever doing lots of CoT, questioning the reality of S, then you might pause it. But if it's able to realize this with a very small amount of CoT or even without CoT at all, then the delusion probably wouldn't work. It wouldn’t get off the ground.

### Out of Context Reasoning

[3:35] I've done a lot of work on out-of-context reasoning, which is the ability of models to do reasoning without chain of thought. They are either doing it in the forward pass, or they are doing it as part of the SGD process. I think there's an interesting connection between this deludability of AIs and out-of-context reasoning. I think this is a potentially fruitful thing to explore. To give a concrete example very quickly, you might again have a statement like, X was born in Rome. You want to delude the model about this. You have other information that goes against that. You can model this as multi-hop sequential, out-of-context reasoning where there's lots of research on this, on how good models are at it, where it does seem like they probably would struggle doing more than two hops of reasoning. I'm running out of time. There's also Connecting the Dots. That paper might be relevant to thinking about this.

[4:26] Take homes: it might be useful to delude models for control. This is probably related to out-of-context reasoning. I think there's lots of work that could be done here. I think it's a pretty open and generally exciting area. Thanks. [Applause]
