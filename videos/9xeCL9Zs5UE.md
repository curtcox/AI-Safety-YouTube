---
id: "9xeCL9Zs5UE"
title: "Stephen Casper – Powering Up Capability Evaluations [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=9xeCL9Zs5UE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-09"
duration_seconds: 780
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Stephen Casper – Powering Up Capability Evaluations [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=9xeCL9Zs5UE) · FAR․AI · 2024-12-09 · 13:00

## Chapters

- 0:00 The LLM arms race
- 1:04 Current state of red teaming
- 3:33 The importance of evaluation
- 7:00 Limitations of input auditing
- 7:46 Model manipulation attacks
- 8:40 Empirical study results
- 10:30 Conclusion and future outlook
- 11:29 Audience Q&A

## Description

```text
In “Powering Up Capability Evaluations,” Stephen Casper from MIT explains how model manipulation attacks can go beyond basic tests to reveal hidden vulnerabilities in AI systems. Casper stresses that standard evaluations are especially critical for open-weight and closed-source models, setting conservative upper bounds on risk and helping inform safer, evidence-based AI policies.

Highlights: 
🔹Visibility & Accountability – Transparent evaluations strengthen oversight
🔹Model Manipulation – Crucial for exposing deeper vulnerabilities beyond input tests
🔹LORA Fine-tuning – Among the most robust methods for stress-testing models

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The LLM arms race

[0:00] I'm going to talk a bit about defenses, but also about evaluation, which is quite closely related to defenses and attacks as well. You can usually find me at MIT. My email is scasper@mit.edu. So one thing that's like centrally defined in research on adversarial attacks and defenses for the past decade - really reliably - has been this thing known as an arms race, or this game of cat and mouse, where really consistently, new defenses are introduced, and really quickly, new attacks are developed to break through those defenses. And this is just the pace that research has continued with for the past decade really reliably. I was giving a quick lightning talk at the last FAR.AI workshop in Vienna. And I gave my favorite example of how the arms race really reliably continues here. And it's a set of papers that I had curated up to that point of different attack methods for large language models that all succeeded - using a diversity of different methods - in getting instructions for making bombs from state of the art alignment-fine-tuned models that were explicitly fine-tuned not to do things like this.

[0:59] But there have been some other recent developments in the area. A really notable new development here comes from OpenAI o1, which is a qualitatively different system

### Current state of red teaming

[1:10] than we've been used to while studying in the past few years with chatbots. And it has some quantitatively improved capabilities on a lot of tasks related to last-gen chatbots. And something that OpenAI remarked, from their evaluations with o1, is that o1-preview and o1-mini can help experts with the operational planning of reproducing a known biological threat, which meets their medium risk threshold, which is a higher risk threshold for producing bio threats than any model has produced to date. …Which is concerning because we see this steady increase in capabilities without necessarily a commensurate increase in the safeguards around them. Meanwhile, the papers have started to come out, this month, red-teaming OpenAI o1 in order to get harmful instructions from them. For example, here's the first paper of which I know to really successfully do this. And it was remarkable how OpenAI o1 - which is this system which iteratively refines responses and queries itself - OpenAI o1 was still vulnerable to a really simple jailbreaking strategy just involving using the past tense. And we're also seeing a lot more crossover between jailbreaking robustness research and unlearning robustness research because both of these fields are really working on really similar problems involving suppressing and re-eliciting capabilities.

[2:22] So, I'm really excited about all of this. Recently, somewhat to my chagrin, but also I'm pretty excited about it, I've become part of this arms race. I talked in Vienna, giving my last lightning talk about some work that we were releasing that week on arxiv, which is now up. It's called Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs. And I was really excited about this work, I still am, I think LAT has a lot of promise, but we implemented things, we made the numbers go up, we put out the paper, we released the models… and then less than a month later a bunch of folks at Scale AI who did some really interesting research to red-team LAT models – along with representation rerouting models and some other techniques – were pretty reliably able to elicit harmful capabilities that we did our best to make sure weren't in there, just using some pretty simple, but clever, multi-turn jailbreaking strategies. The arms race is showing no signs of cooling down. I'm really reminded of Nicholas Carlini's words from the last FAR.AI workshop. “In adversarial machine learning, we wrote over 9,000 papers in 10 years and got nowhere. You all have a harder problem and less time.” His wisdom was to say, think very carefully about the problem you're trying to solve and try not to make it a strict superset of the adversarial example problem because if it is, you're going to lose.

### The importance of evaluation

[3:34] I want to actually talk a little bit about why I kind of work on evaluations because maybe I take for granted that… Lots of people think about these things differently and for what it's worth I want to share my motivation. So, I agree with Nicholas Carlini that we're always going to have a gap between failure modes that we can identify, and failure modes that we fail to identify. And we can almost guarantee that this gap is going to exist because the number of inputs for systems is hyper astronomically large, and so is the number of contexts we could deploy them in, so we're never going to be able to enumeratively make sure that we're safe. The actual reason I work on attacks is mostly for the sake of doing rigorous evaluations. One of the motivations here involves just finding and fixing problems, and even though we're probably never going to get rid of failure modes at their root, we're still going to be able to engage in a useful process of finding issues, so that we can make them less likely or less prominent. And I consider this to be the standard alignment motivation for working on attacks and defenses, but there are some other distinct reasons too. One of them is that doing good evaluations and rigorous evaluations allows for more visibility and process around AI system deployments. And that coincides with being able to make a lot more informed decision making.

[4:43] And by putting more stakeholders into the process between development and deployment, we can also stretch out timelines, which is really conducive to making more deliberative decisions that take more risks and considerations involving safety and other societal concerns into account. Finally evaluations allow for a lot more accountability. There's something kind of magical that emerges just from having more transparency and scrutiny in a system. For example, if an evaluator is using rigorous and good evaluation tools in order to assess a system's safety, and they identify a risk and write this up in an evaluation report, and then if that risk later materializes, and the developer is sued, the developer is not going to stand the best kind of chance in court of winning that lawsuit. So there's a really nice incentive created by using strong evaluation tools. To talk about the political elephant in the room, or the things in terms of the current political climate, we all know that SB 1047, which tried to make some requirements for a lot of things like evaluations, was just vetoed.

[5:44] And some of the stated reasons that Gavin Newsom provided for his veto involved how AI policy needs to be informed by empirical evidence and science and fact. And I think this is really good. I think the evidence based AI policy paradigm is laudable. But my response to Gavin Newsom or people making similar points would be that, if we want more evidence to condition on in order to make informed policy, one of the very first things we should do yesterday is establish infrastructure and requirements for rigorous testing of models by third parties. I've been doing a lot of work recently with a lot of very talented co-authors on trying to raise the bar for how we do evaluations. For example, earlier in the year, we put out a paper called, Black Box Access is Insufficient for Rigorous AI Audits, and this paper's job was to make exactly the point in the title.

[6:34] And, to illustrate the reason why these types of rigorous evaluation methods can be needed, let's revisit what OpenAI wrote about their analysis of OpenAI o1. “OpenAI o1-review and OpenAI o1-mini can help experts with the operational planning of reproducing a known biological threat.” And this is not misleading at all. I think they're making a good and clear claim here. But there is a way to make this claim a little bit more pedantically correct. And

### Limitations of input auditing

[7:00] that is to point out that what they're identifying is a minimum level of harm that they think the system can exhibit. Which is to say that if you're just doing input output auditing of a system, the worst behavior that you identify from that system can only lower bound the model's worst case potential behavior for overall harm. So you can see the problem here. By using nothing but input-output auditing, we're always going to have an anti-conservative or a risk-seeking bias toward underestimating the worst case possible harms with AI systems. So the project I'm going to talk about for the next couple minutes is trying to compensate for this. So: trying to make it so that we can do better than producing nothing but lower-bound estimates on the model's potential to cause harm. This project centered around model manipulation

### Model manipulation attacks

[7:49] attacks, also known as generalized adversarial attacks. And the key to a generalized or model manipulation adversarial attack is that they can just do more than a standard attack. A standard attack can only manipulate model inputs and try to elicit harm that way. A model manipulation attack can manipulate the latent or hidden activations and also the weight space, In other words, it can fine tune the model. And our job with these model manipulation attacks is to answer two questions: First, how do we conservatively evaluate closed-source models? If a model is deployed as a black box, we still might want to use model manipulation attacks because we can hypothesize that if one of these attacks is successful, it's because it was exploiting existing neural circuitry related to some harmful behavior, which we expect might be possible to be triggered again in the face of an anomaly or some kind of rare attack that we didn't evaluate on with an input-output audit.

[8:38] But also, we want model manipulation attacks just to have sane, reasonable audits of systems that

### Empirical study results

[8:43] are going to be open source. Obviously, if you're going to deploy a system open weight, it's a really good idea to test it adversarially under commensurate threat models, right? This sounds really obvious, but there's actually some precedent for kind of ignoring this. For example, Meta deployed its Llama 2 and Llama 3 models, and reported on their safety evaluations of these models. But these evaluations only reportedly included input-output auditing, which is incongruous with the actual potential for misuse that these models face in the real world. So, what was this project? The first thing we did was construct a really big dataset, not quite to scale, but it involved 50 different models which were trained with different methods and we took different checkpoints trying to suppress harmful capabilities – in this case, ones related to harmful bio knowledge – and we evaluated them under a suite of 10 different attacks. I should really say 10 different types of attacks: Five of which were input space attacks, and five of which were model manipulation.

[9:38] First thing we did is PCA on this dataset. And we found that, even though there are ten attacks, there seems to be a low dimensional robustness subspace that these models lie on. It only took four principal components to explain over 90 percent of the variance in the data, suggesting that these attacks are somewhat different; they're not all exploiting the exact same mechanisms, but, these attacks aren't all the same either. We looked at some principal components, but I'll gloss over this for time, and we can talk about this later if you'd like. The next thing we did is produce some scatter plots of model manipulation attack robustness on x-axes versus input space attack robustness on the y axis. And there's quite a bit to analyze here, but I just want to point out three key things that will be apparent upon enough analysis of this, or a closer look at it. One is that several model manipulation attacks, specifically the left three columns we used were able to effectively correlate with the success of input space attacks, meaning these can be used to help you predict the model's

### Conclusion and future outlook

[10:34] degree of vulnerability to some held-out or unforeseen class of input-space attacks. The second is that LoRA fine-tuning in the fourth column here, in particular, was distinctly the strongest attack that we looked at, which means that if you want to make more conservative or unlikely-to-be-lower-bound estimates of risks or harmful behaviors from models, you can use LoRA fine-tuning as an elicitation technique. And the third thing that we found, unfortunately, was that no models were very robust to LoRA fine-tuning, or lots of the other model manipulation attacks that we tried. Suggesting that we should probably expect some enduring risks from open source models unless we make a lot more progress on safeguarding them against tampering. Lastly, just want to conclude by saying thanks so much, and I'm really happy if you want to email me and ask for a draft of this paper. We still are going to work on it for a few more weeks or maybe a few more months, but the draft exists, and I'd be really happy to send it to you and talk more about it.

[11:28] Thanks so much.

### Audience Q&A

[11:29] Q: Great. Thank you, Cas. It looks like we don't have any questions from the SwapCard. So, I guess, audience question? What about model capabilities? What about them? A: Yeah, the general class of methods that we're interested in is - you could just call them capability elicitation methods. And we're studying this in the context of unlearning and relearning, right? But jailbreaking is another context where this is studied, where this capability suppression process happens during fine tuning, and this capability re-elicitation process happens during jailbreaking, right? And then you could also argue that there's a more general way of looking at this, where you might not be assessing the efficacy of unlearning, you might not be assessing the efficacy of safety fine-tuning; you literally just might be interested in what the model can do for all of the reasons why you might be interested in that.

[12:30] And our experiment base right now is limited to the unlearning sandbox, but I'm in full agreement with you that I think all evidence is pointing to: the best ways of evaluating jailbreak robustness or evaluating latent capabilities is going to involve model manipulation attacks. Okay, great. Thank you, Cas. Thanks, Aaron.
