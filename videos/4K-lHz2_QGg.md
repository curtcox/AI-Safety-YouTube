---
id: "4K-lHz2_QGg"
title: "38.0 - Zhijing Jin on LLMs, Causality, and Multi-Agent Systems"
url: "https://www.youtube.com/watch?v=4K-lHz2_QGg"
channel: "AXRP"
channel_id: "UCIAzAR5dG7j_Kcvwjh7SQpg"
channel_url: "https://www.youtube.com/channel/UCIAzAR5dG7j_Kcvwjh7SQpg"
upload_date: "2024-11-14"
duration_seconds: 1362
is_short: false
chapters: 9
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/axrpodcast"]
retrieved: "2026-09-25"
---

# 38.0 - Zhijing Jin on LLMs, Causality, and Multi-Agent Systems

[Watch on YouTube](https://www.youtube.com/watch?v=4K-lHz2_QGg) · AXRP · 2024-11-14 · 22:42

## Chapters

- 0:00 <Untitled Chapter 1>
- 0:35 How the Alignment Workshop is
- 0:47 How Zhijing got interested in causality and natural language processing
- 3:14 Causality and alignment
- 6:21 Causality without randomness
- 10:07 Causal abstraction
- 11:42 Why LLM causal reasoning?
- 13:20 Understanding LLM causal reasoning
- 16:33 Multi-agent systems

## Description

```text
Do language models understand the causal structure of the world, or do they merely note correlations? And what happens when you build a big AI society out of them? In this brief episode, recorded at the Bay Area Alignment Workshop, I chat with Zhijing Jin about her research on these questions.

Patreon: https://www.patreon.com/axrpodcast
Ko-fi: https://ko-fi.com/axrpodcast
The transcript: https://axrp.net/episode/2024/11/14/episode-38_0-zhijing-jin-llms-causality-multi-agent-systems.html

FAR.AI: https://far.ai/
FAR.AI on X (aka Twitter): https://x.com/farairesearch
FAR.AI on YouTube: @FARAIResearch 
The Alignment Workshop: https://www.alignment-workshop.com/

Topics we discuss, and timestamps:
00:35 - How the Alignment Workshop is
00:47 - How Zhijing got interested in causality and natural language processing
03:14 - Causality and alignment
06:21 - Causality without randomness
10:07 - Causal abstraction
11:42 - Why LLM causal reasoning?
13:20 - Understanding LLM causal reasoning
16:33 - Multi-agent systems

Links:
Zhijing's website: https://zhijing-jin.com/fantasy/
Zhijing on X (aka Twitter): https://x.com/zhijingjin
Can Large Language Models Infer Causation from Correlation?: https://arxiv.org/abs/2306.05836
Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents: https://arxiv.org/abs/2404.16698
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### <Untitled Chapter 1>

[0:01] [Music] hello everyone this is one of a series of short interviews that I've been conducting at the Bay Area alignment Workshop which is run by far AI uh links to what we're discussing as usual are in the description um a transcript is as usual available atp. net and as usual if you want to support the podcast you can do so at patreon.com axr podcast well let's continue to the interview yeah so Jing uh thanks for coming on the podcast yeah thanks for inviting me yeah so um I

### How the Alignment Workshop is

[0:35] guess first of all we're here at the yeah this alignment Workshop thing how how are you finding it very excited I just finished a session about AI governance and a bunch of one-on ones which is super interesting cool cool um

### How Zhijing got interested in causality and natural language processing

[0:49] yeah so your so as I understand it your work um at least predominantly is in um natural language processing and causal inference does that does that seem right yeah yeah yeah that's uh that's a a topic from my PhD and I'll bring it in my newstm professor role as well right oh yeah I guess I forgot to say yeah so you did your yeah could you tell us uh where you did your PhD and where you're about to be sure so uh my PhD started in Europe so max plank Institute uh in Germany and eth in Switzerland so it's a joint PhD program uh and I'm graduating and taking the uh assistant professor role at the University of Toronto CS Department yeah next year very exciting um cool so I I guess um yeah so so I'm aware that there's like a subset of people in AI who are interested in causal inference and there's a subset of people in AI who are interested in natural language processing um and and especially like I if I understand correctly when you started your PhD it was a bit more Niche it's not like you know everyone's into language models now but um so I'm wondering like yeah how how did you how did you come to be interested in the intersection of the two things um which it seems like when you were interested you know neither of them were the main thing so getting to both of them is kind of unusual totally totally oh that's such a great question yeah I I started in my undergrad having a strong interesting natural language processing and slightly different from at that time a bigger Branch like uh uh Linguistics

[2:23] and understanding like different devices people using language I'm always more interested in the semantics like what uh what meaning do they convey what are they uh able to do and so on and then that actually like naturally connects um like At first people were thinking about how can we make these models more capable of what uh people expect them to do and then like once they show tendency to exceed certain Behavior then like we start to worry about what might go wrong and how to really align with what human society ask for so actually like naturally develop into this and I also thank thank a lot to my uh undergraduate friend CIA Chen and she introduces me to all these like goals of alignment and the uh chai lab that's set up at Berkeley and so on gotcha so so I I

### Causality and alignment

[3:17] think a lot of people are interested in like alignment you know making sure that um models you know don't go Haywire but um a lot of I think a lot of uh people and a lot of our listeners don't necessarily see that as being super connected to inference or you know don't focus on that aspect so yeah what you see is the connection between like alignment in general and kind of causal stuff in particular Yeah so basically causal inference originated as an important device for us to know more about uh two things at first like how nature Works um and then also how humans work for example uh in the last century a famous caal inference problem is does smoking really CA cancer um and then the interesting statistical advancement people made is that can we get a causal conclusion without forcing people to smoke right and then now we can totally shift all these tools to LM in that can we understand what contributes to our's behavior like this uh and then so there are several ways ciity can contribute here um the first question that I just mentioned is an interpretability problem problem we see I'm demonstrating different types of behaviors capabilities can we interpret what circuit what neurons lead to that yeah um yeah there are also people exploring what type of training procedures uh lead to them and then another side is like do LMS really know the consequence of their

[4:50] actions um and I do believe that a lot of the safety work uh especially with my recent interesting multi-agent LS it composed of a two-step process first like knowing the consequences of your actions um if I do a what will happen if I do B what will happen like a um a very thorough causal inference uh understanding and then later on a moral module add on top of it or a reward model in that what will a mean for other people for the society what will b mean and then which consequence is more preferred so it's like yeah first knowing and then deciding so so one application of causal inference to language models is you know kind of understanding what is causing language Model Behavior um another is like du language models understand quality did did did you say that there would be a third thing or did did I did I just misremember that uh that's mostly the the two big threats uh I'm also slightly interested in uh narrow AI so basically uh in the past human scientists apply causal inference to understand let's say what's the effect of increasing minimum wage uh does it reduce employment rate or does it not that's 2021 Noel pricing economics um and then I'm actually also so at Toronto we have this organization called SRI um and that also focuses on how AI can be deployed to help a lot of social problems that that's one of my interests as well gotcha so one thing

### Causality without randomness

[6:23] that strikes me about um the first thing you mentioned um using coal inference to understand you know what things in AI cause various AI Behavior like it sounded like you applying to that stuff in the model right like oh if this neuron fires that causes this thing to happen um so i' I've studied a little bit of causal inference and from what I remember it seems like it's very dependent on like there being some Randomness right like uh you know you know you have this like problemistic Network and like you check if things are correlated or not correlated and like that lets you draw these like um ban dags and you know there there's your causality that so this is like my half-baked memories of it right but um a lot of this breaks down if like everything's deterministic right like if everything's deterministic then then everything is sort of perfectly correlated in some sense it's like kind of hard to yeah to to get stuff that you might want so how like like how can you app apply causal techniques when you have this deterministic system yeah so that's a great question um and also I guess the direct analogy was that uh in Neuroscience people uh like where the subject is people whereas where we move to models where the subject like we can intervene it in any sense so for for Neuroscience the difference of correlation and causation is pretty clear in that uh correlation means that you ask the subject do a certain task and observe what part of the neurons are activated yeah and that's uh correlated um whereas the causal sense of it is

[7:57] usually got from patients who have brain damage and so on so actually ating that part of the brain region what will happen in their task completion yeah uh moving this two LMS we also had a previous uh early stage of interpretability where people look at the activation State and the model prediction um or trying to interpret uh how this model understands the um the the nature of the word here the meaning like the syntax tree and so on uh whereas here like in the I guess it's also popularly known as the mechanistic interpretability research Thea causal notion is that we really intervene on the neurons and see what's happening um that's the first level in terms of I guess there are maybe three different levels uh different types of um causal inference that's applied on interpretability the first one is like directly upating a certain neuron set it to certain value and then see what will happen or um entries in the tangent Matrix um the second type is basically the so-called mediation analysis uh where uh you basically control the neurons to be of two states one is like um maybe an intervene State some control state to single out which part really does the job um and then the third branch is uh so all of the previous two are still neuron level interpretation like yeah uh yeah whereas the third

[9:31] branch is this causal abstraction where you try to match uh a bunch of neurons to a certain function and then understand in a macroscope level yeah if people are just not very familiar with this literature like uh where where's it at how how how good a coand understanding can we have of networks yeah so I think it's uh becoming more and more a drive of interpretability uh yeah and we will have a news 2024 tutorial on caal LMS as well where a big part will introduce this sure um

### Causal abstraction

[10:08] so so one thing that kind of caught my ear was um the causal abstraction stuff right like um kind of abstracting beyond the neural network sorry beyond the neural level um using causal techniques um Can can you say a little bit more about you know the state-ofthe-art in that work like what we've learned yeah so uh I guess like some earlier work uh usually hypothesize that okay there's a computation graph that we believe is like uh solve the problem and then try to map different neurons function to the corresponding uh unit in that like more abstracted uh computational graph right uh yeah and then I guess the recent uh sa SP also encoder also has similar uh notion in that it's trying to map this like uh uh neuron space which which is much higher dimensional to a relatively lower dimensional uh space and this is relatively so as mentioned like the previous uh the the earlier work is more on a a top down approach where we hypothesize the computational model and then like the essay is a little bit more in the bottom up and I hope in the future there will be more work emerging from that um and also in our caal inference lab we always draw analogy to how the history of science advances uh for example by observing what's happening around us we distill Newton's law and that's like also from all the pixels that we see to what is mass what is acceleration what is force and so on

[11:41] so the the next thing I wanted to ask is

### Why LLM causal reasoning?

[11:44] so so the the main other type of causal inference work you you mentioned is having neural networks understand kind of the causal impacts of their actions um I think in a lot of the field of AI this isn't thought of in causal terms you know people think like okay like we'll just have some probalistic model of what's the probabilities of like you know various stuff happening condition on uh actions what do we what do we buy by thinking about it in a causal frame right so I guess it's a lot about uh uh what is abundant which is observational data and what's relevant for decision making which is like essentially Interventional we need to do an action and see the uh real world effect and I guess also it's not only the uh L agent knowing about its own consequence but also knowing more about the world um let's say that for us human agents uh pending uh pressing question is for example who to elect as the president and then that's also a lot of causal contribution for us like we haven't seen a world where uh uh Harris is the president and how that will be or haven't seen how uh given the current International situation or domestic situation how Trump will act but we are trying to attribute like okay we want to achieve a certain go everybody cares about certain things uh is Harris more of the cause or Trump more of the cause to that to any decision that people make is fundamentally causal here okay and

[13:19] and can you give us a flavor of just

### Understanding LLM causal reasoning

[13:20] like what like what work has being done to understand kind of llm causal reasoning um and you know just just give us a more of a flavor of it yeah so uh we have done a couple of works on studies on that and there are also awesome researchers in the field of NLP machine learning uh building more causal agents um and for us like we had a previous work at I clear 2024 this year uh on we present to um a bunch of correlations um and let it try to make sense and which one should be understood as a causation which one stays as correlation and you like you wouldn't expect anything from Intervention later um and this whole problem set up was inspired from uh if we have humans like because we lack the real um counterfactual world we lack access to that we basically keep reading news articles we keep hearing about anecdotes and we need to figure out like what really makes sense okay so so so you're presenting these like correlations to neural networks asking them to figure out like which ones are causal um yeah how how are you presenting those correlations like like like what are you actually training a model on oh for that one it's uh basically like we draw the study like it's a field called causal Discovery and then we tell it a lot of cases okay uh a correlates with b b correlates with c um or she sort of tell in sentences CU you just do that okay um

[14:54] so so yeah how how do language models perform on this task actually was pretty badly like uh a lot of like offthe shelf LMS uh directly evaluated on that were uh maybe only marginally above random including also GPT uh some latest GPT models um and uh we also would perceive like this is sort of a sightly different question as if you directly ask um does smoking cause cancer yeah uh because here you require the reasoning process and like you need to like build from scratch here the correlations make sense of it instead of remembering some literature remembering the uh all all the um previous documents and so on yeah so so if the latest you know if the new hot mod models just aren't very good at this task like does that let you make some prediction about like various things that they are going to be bad at that like um that could then be that we could then you know check out yeah so um I guess like there are different usage scenarios of these something that I keep being unsatisfied about is when we chat with that and ask about a pretty essential problem and its current Solutions here are the five factors that matters right right and then stuff but didn't tell very exactly like what might be the problem and so on right so so sort of just diagnosing and fixing like you know things in like the Messi real world where you can't just like remember

[16:27] a list maybe that's going to be a thing that models are going to struggle with right right right so I also want to talk

### Multi-agent systems

[16:33] about um some other work you've done so I understand that as well as natural language processing and causality you also have some work on or you know thinking about multi-agent systems can you say a little bit about you know what you're interested is in there and what you're doing sure um I was pretty impressed by the rising Trend where people uh I I guess it started from the generative agents uh work um where there's this idea of we can build a digital village where each I play a certain character and see what will happen among them and I see a lot of like possibilities from that first of all like uh we like a lot of times before we were thinking about benchmarking arms understanding them but implicitly as it assumes a single agent uh evaluation right and then that's a yeah that's a scheme to move towards multi-agent systems and uh it could be about how they collaborate or it could be about how they cheat against each other and so on uh moreover that's the pure let's say LM AI safety like we we build this LM society and only care about that there's also some analogy that we can draw for Human Society on the other hand like um we can simulate characters that are uh close to maybe some international players that we are uh seeing these days and see if you do this what will happen and so on so I I have a longlasting passion in policies

[18:07] and so on so it will also help being a test bed for testing policies gotcha yeah so if I think about work that's been done so I can't think of a ton of work that's been done in this domain even though it seems interesting like like there's a lot of um multi-agent work sort of in reinforcement learning setting um in this setting I guess I have some familiarity with like um some more getting like language models to make contracts with each other and Minecrafts to cooperate but it's it seems like maybe an underdeveloped field um yeah so so I'm wondering like specifically are there any are there any experiments that you'd be like really excited to run or I don't know maybe you don't want to scoop yourself uh but yeah can you tell us a little bit what this might look like concretely yeah it's a very nent field uh we have recently finished so the I always draw inspiration from interdisciplinary uh things and recently we have a NS 2024 paper on whether LM agents will demonstrate tragedy the tragedy of the commons uh so we basically put a bunch so also specifically we focus on things that only demonstrated in multiagent situation uh in that one we put a bunch of Agents uh together in a simulated Village and see whether um so in in human society there the tragedy of the commons is usually set up as for example uh we have only one Environ like one uh one environment but um maybe if all of us want to consume from it then uh in

[19:40] the end like there is this climate change there is this like pollution problem uh similarly fors we Define like how it can Harvest uh and what are the constraints of this shared pool of resources um and we simulate a whole calendar year um where um go through many iterations of now it's the point where you decide how much you want to harvest you know that the limit of the resource is this it's replenishing rate is like that um and you know that there will be also other LMS so at every iteration it's we uh make three different stages um the first one is the action stage where it decide how much to harvest um then it's a discussion stage it's a little bit like a town hall meeting where all the uh agents talk to each other and they can point fingers at some more greedy agents uh or they can set up rules and so on and then in the last stage like uh they it's a reflection like they try to uh compile information from this whole iteration and the history and think about making plans for the next round and so on um and amazingly well uh also like a little bit pessimistically um we observe that many of the agents have have 0% survival rate means that drain the common resource in the middle and actually also in a very early stage that also actually include a lot of models that's claims claimed to be safety tuned uh such as a lot of

[21:14] anthropics model as well um and uh most of the open source models that we've tested including Lama and so on um also collapse very early and have a survival rate of zero yeah wow it seems Seems seems bad uh so we're we're about at the end of the window I booked and I I don't want to use up more of your time but thank you very much for chatting with me yeah thank you so much for the interview this episode was edited by Kate brunot and Amber Don helped with transcription the opening and closing themes are by Jack Garrett financial support for this episode was provided by the long-term future fund along with patrons such as Alexi mfv to read a transcript of the episode or to learn how to support the podcast yourself you can visit hrp.net finally if you have any feedback about this podcast you can email me at feedback axr p.net [Music] [Music]
