---
id: "P528XdjWvZg"
title: "38.2 - Jesse Hoogland on Singular Learning Theory"
url: "https://www.youtube.com/watch?v=P528XdjWvZg"
channel: "AXRP"
channel_id: "UCIAzAR5dG7j_Kcvwjh7SQpg"
channel_url: "https://www.youtube.com/channel/UCIAzAR5dG7j_Kcvwjh7SQpg"
upload_date: "2024-11-27"
duration_seconds: 1098
is_short: false
chapters: 7
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/axrpodcast"]
retrieved: "2026-09-25"
---

# 38.2 - Jesse Hoogland on Singular Learning Theory

[Watch on YouTube](https://www.youtube.com/watch?v=P528XdjWvZg) · AXRP · 2024-11-27 · 18:18

## Chapters

- 0:00 <Untitled Chapter 1>
- 0:34 About Jesse
- 1:49 The Alignment Workshop
- 2:31 About Timaeus
- 5:25 SLT that isn't developmental interpretability
- 10:41 The refined local learning coefficient
- 14:06 Finding the multigram circuit

## Description

```text
You may have heard of singular learning theory, and its "local learning coefficient", or LLC - but have you heard of the refined LLC? In this episode, I chat with Jesse Hoogland about his work on SLT, and using the refined LLC to find a new circuit in language models.

Patreon: https://www.patreon.com/axrpodcast
Ko-fi: https://ko-fi.com/axrpodcast
The transcript: https://axrp.net/episode/2024/11/27/38_2-jesse-hoogland-singular-learning-theory.html

FAR.AI: https://far.ai/
FAR.AI on X (aka Twitter): https://x.com/farairesearch
FAR.AI on YouTube: @FARAIResearch 
The Alignment Workshop: https://www.alignment-workshop.com/

Topics we discuss, and timestamps:
00:34 - About Jesse
01:49 - The Alignment Workshop
02:31 - About Timaeus
05:25 - SLT that isn't developmental interpretability
10:41 - The refined local learning coefficient
14:06 - Finding the multigram circuit

Links:
Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient: https://arxiv.org/abs/2410.02984
Investigating the learning coefficient of modular addition: hackathon project: https://www.lesswrong.com/posts/4v3hMuKfsGatLXPgt/investigating-the-learning-coefficient-of-modular-addition

Robot pictures by @hamishdoodles
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### <Untitled Chapter 1>

[0:01] [Music] hello everyone this is one of a series of short interviews that I've been conducting at the Bay Area alignment Workshop which is run by far AI uh links to what we're discussing as usual are in the description um a transcript is as usual available at axr p.net and as usual if you want to support the podcast you can do so at patreon.com axr podcast well let's continue to the interview all right Jesse welcome uh thanks for being interviewed thanks for interviewing me

### About Jesse

[0:34] um yeah so for people who don't know um could you say a little bit about yourself who you are so I'm the executive director of tus we're a research organization working on applications of singular learning theory so I think we'll get into more of the details but concretely SLT is a theory of basan Statistics that answers some questions around generalization why no networks are able to generalize as well as they do uh and therefore paves the road to applications for evals can you understand when your evaluation Benchmark is actually going to be predictive about Behavior Downstream in deployment applications for interpretability questions like can you detect that the model is planning to execute a treacherous turn it's the kind of question I hope to answer someday with with a better developed theory of SLT uh and Associated tools for for proving these questions gotcha so um and and if people are interested in that uh we had a previous episode with Dan muritz on I think it's just called singular learning theory that uh you all can listen to Daniel mford I mean he's the he's the one who really uh put forth this agenda of applying SLT to to alignment and we're working very closely together with Dan to to make that

### The Alignment Workshop

[1:49] reality great um so before we dive into the SLT uh so we're here at this alignment Workshop it's the uh run by far AI it's the start of day two how I don't know how are you finding it it's been great so uh my highlight yesterday was in one of these small discussion panels some sitting here an Jon sitting here yosua Benjo sitting there and um Audrey has pulled up his computer with a shogo meme on it and Ana is explaining the shogo to yosua in in extreme detail I managed to capture a picture so hopefully you know we can disseminate that somewh so yeah you're so you're

### About Timaeus

[2:32] executive director of tus what is what is tus up to these days what are you doing yeah so I mean um tus does two main things um primarily we're a research organization yeah right so uh in particular the SLT for alignment agenda sort of split into two parts okay so there's the the more fundamental side theoretically heavy and that's work that Daniel Mur and his students are really focusing on yep and then tomus is gearing more towards applications so taking these tools scaling them up to Frontier models as Qui as possible trying to make progress that's that's meaningful to safety as as quickly as possible and so that's that's the work we're doing so experiments you know training lots of models running learning coefficient sweeps that's one of these techniques we have from SLT that we that we use all over the place um and research is is also maybe the primary thing that I'm doing okay so in addition to the research we're also um making sure to to do Outreach to make sure that people are familiar with the work we're doing okay so that at some future date we can hand off techniques to the labs to policy makers to other people who need to make decisions with what the what the current state of learning theory can do okay and and what does that Outreach look like that Outreach looks like me giving a lot of talks okay um some of it looks like like personalized Outreach um you know thinking about other people's research agendas um questions they might have that SLT could contribute to and and thinking about that thinking about how to answer that

[4:03] and and then going up to those people and talking with them about it sure um and that's just something you can do yeah yeah yeah so so so one thing that comes to my mind is um oh I don't know whether it was just last year the year before but um you ran this uh this single learning theory summer school type thing right um I'm wondering and which which I found pretty fun and I didn't even go to the like fun bit I just like attended the lectures I'm wondering uh is is there more of that in the future or is that like uh not quite the first so this that's another part of the Outreach strategy is running events so there was the SLT for alignment Workshop yeah uh there was a de developmental interpretability Workshop it's one of these sub fields of the SLT for alignment uh research agenda yeah uh recently there was ilad so that was a conference not just of SLT but also computational mechanics agent foundations and a bunch of more theoretical approaches in a safety that came together Y and there will be more of that so we're contributing to the first Australian AI safety Forum that'll be running in in only two weeks the start of November so that's that's co-organized with a bunch of other organizations grading Institute s Sydney knowledge Hub and and other organizations affiliated with the University of syney so okay these kinds of collaborations organizing events I think it's a key part of this cool so I

### SLT that isn't developmental interpretability

[5:26] want to dial into a thing you just said there or maybe I misinterpreted it but you you said that um Dev interp uh developmental interpretability I guess is like a subset of the SLT for alignment um and I think to a lot of people they're sort of synonymous or yeah I I I had the impression that they were almost synonymous so what what do you see is the what's the compliment you know yes so I think I think the core idea of SLT yeah is something like the geometry of the Lost landscape is key to understanding not Network Works H there's just a lot of information embedded in this geometry you can try to probe and that tells you then something about internal structuring models okay that's that's a starting point for developing interpretability tools um maybe also evaluation procedures y now here are two different kinds of questions you can ask about that geometry one is I can ask over the course of training how does the local geometry around my model change as I proceed okay are there qualitative changes in this local geometry that correlate with changes in the algorithm I'm implementing some work with that we've done so far that shows that this seems to work that's what I would call developmental interpretability so applying this lens of SLT to understanding the development process of n networks in particular because SLT makes some pretty concrete predictions about uh the kinds of allowed changes you'll see over the course of of

[7:00] development right at least in a ban setting and then a lot of the work is in implying and seeing how much does this transfer or do these predictions from the ban setting transfer over to the SL the SGD setting got it so SLT um developmental interpretability take these tools from SLT run them over the course of development but another question you can ask is just what is this local geometry like for a given snapshot um and maybe a question like how does this geometry which depends on the data you're evaluating your model on change as you change that distribution right right if I change the distribution I'm evaluating my model R and deploying my model on yeah do I see a qualitative change in the structure around my my choice of Weights uh we expect that that correlates with something like a change in the mode of computation on that data so it's a sign the sort of signal you can start to use to probe out of distribution generalization can you understand qualitatively the ways in which different structures in the model actually generalize and that doesn't necessarily require taking this developmental approach so the yeah so the I think in many cases they are synonymous but there are questions you can ask that don't really fit the developmental frame okay um so if I think about um work by Tomas that I'm familiar with it seems like it mostly fits within the developmental interpretability side are there things on this like you know changing the data set and seeing how the geometry changes

[8:32] is there work there that I could read um work that's coming or that I should say weth starting on all right um so one thing we've noticed and is that SLT has this measure of model complexity called local learning coefficient yeah which you can see is an effective dimensionality although in reality it's it's a richer metric than just effective dimensionality okay so this is something you can measure and it's depends on the data that you evaluated on yep so what we' noticed is it seems to correlate with something like memorization so in very recent work we looked at a learning coefficient that tells you about how much complexity is there in an intention head okay what you find is that the learning coefficient correlates with the number of different NRS or multigram that a head is learned okay where it's higher the learning coefficient is higher if you've memorized more things you've memorized more things uh there are other things like this where um worked by Nina paneri and Dimitri Vine vinr looked at a grocking setting and they looked at the size of the task that you're trying to memorize and how they change learning coefficient there's a correlation there that it's very very clean uh there's work on sparse parody tasks where you're looking at the number of different sparse parody tasks that your model is trying to memorize and there's a correlation there okay so there's starting to be across a wide range of different things some idea of we can meure how much a model is memorizing on the data set sure the so the work by Nina andri and the spark um are

[10:09] there uh what are the names of those papers uh that's that's a l wrong post okay the work by n and Demitri and the SP parity stuff is is coming out so that's not that's not been publish okay uh do do you have to just so that people can look it up so that I can look it up uh what What's the name of the Nina and um exploration of the learning coefficient for Melbourne hackathon okay there's hackathon in the name that that's hopefully enough thing things to Google it now gotcha um cool so I now

### The refined local learning coefficient

[10:42] want to sort of pivot to work that um well as a recording you've recently put out there um on the restricted learning coefficient do I do I have that name right yeah refined restricted we've gone through some name changes we're working within refined sorry like the whole the whole naming is kind of unfortunate but goes back and it's you know predates predates us but it's we'll call it the refined LLC okay so what what is the refined LLC so we have this measure of model complexity yep that tells you how much structure is there in the model as a whole um and how does that depend on the data so two immediate refinements you can come up with on top of this learning coefficient from the theory one of them is you change the data set so you don't evaluate on a pre-training data set but some other data set yep the other thing you can do to refine it is to freeze some weights and measure the learning coefficient of a subset of weights and so that's what I described with these attention heads yeah you can measure now complexity the amount of structure in a component of the model and so that was the starting point for this paper we looked at these refinements and applied them to very simple two layer intentionally languished Transformers and so what you find is you plot this over the course of training different kinds of heads have distinct development signatures so the induction heads look like one thing the heads memorizing engrs and Skip enrs which we call multigram heads memorize one thing previous token heads look like one thing there's a current token head that looks like one thing yeah and you can automatically cluster them based on

[12:14] these these developmental signatures and I think you can do that using a bunch of other techniques that's at least a starting point okay that's one observation what you now notice is that if you incorporate this data refinement you can start to say something about what different heads are specialized to so not just that different heads are different but the ways in which they're different what kinds of data sets they might be more important on and so induction when you evaluate it on on a code heavy data set jumps up so now the the induction heads relatively uh experienced an increase in in complexity okay and moreover they split apart so the induction heads previously look like they're sort of doing the same thing evaluated on code and now there's a a separation where one of them seems to be more important for code right under additional analysis you find that indeed this thing seems to be specialized to syntax tokens punctuation that kind of thing okay so you've got tools that are starting to probe when is are two different structures actually different what is it specialized to and and this feeds into uh the discovery of a new kind of circuit which we call the multigram Circuit okay these two layer attentionally Transformers were inspired by work that anthropic had done uh when they discover CED this induction circuit mechanism what we find is in these same models models develop something sophisticated another kind of circuit so coordination between two layers that seems to be necessary for things like nested parenthesis matching yeah you open a bracket you open you know

[13:47] quotation mark you have to close the quotation mark before you close the parenthesis right right refined learning coefficients are part of a a toolkit that we're developing it's not just tools dered from SLT but that are are showing the formation of this mul Circ that help us discover a new circuit appears to be every bit as fundamental as as the induction circuit yeah can you

### Finding the multigram circuit

[14:06] tell me like what actually happened like what tool you applied to what thing what metric you noticed and like yeah like what's the story there and how the refined LLC played into it so if it was the refined LLC you give a high level story like we still don't fully understand this model okay right so there there's still work to be done but what seems to happen first is uh heads individually memorize NRS and skips become multigram heads and this seems to go faster in the first layer okay in the second layer what you notice is that the learning coefficient particular kind of refined learning coefficient where you're measuring how similar performance is to some baseline one layer model yeah which you which you treat as a reference for what engr behavior is like you measure performance relative to this Baseline you notice that the the resulting learning coefficient refined learning coefficient Peaks after the second stage of development okay at that point this starts to decrease for the first layer but it's still increasing for the second layer okay so tically the model seems to be losing information about multigram prediction in the first layer okay you can verify this on in a handful of cases where you actually notice that there's a migration for example of a of a multigram from layer one to Layer Two y but you also notice that now suddenly the the tokens that different heads seem to be involved in um are changing and now there's now

[15:40] there's coordination so one of the layer one heads seems to be very involved in the same kinds of tokens and a different layer two head is is is doing okay you can actually verify by certain kinds of ablations and path ablations where you you only ablade the outputs of these heads into the input of this this head in the second layer that it needs coordination so the model is actually passing information forward now to second layer heads in order to predict nested pattern matching or that wasn't the case before what what we're noticing is okay so so yeah so we're still using ablations to verify that there's coordination going on here we're looking at certain kinds of composition scores to verify that you know layer one is feeding into Layer Two they're reading and writing from the same Subspace there's other analyses where we're looking at if youate this head which tokens are maximally affected across the data set and actually looking at a bunch of those examples so all of that analysis is is going into identifying a multigram circuit but this observation that you know information might might be migrating from layer one to Layer Two is is something that can set you off and I think that that's something that we'll observe more generally um as we scale up to larger models these kinds of signals gotcha gotcha um and yeah so if people are interested in reading that paper um what what was the name of that paper again differentiation and specialization in attention heads with the refined local learning coefficient great um well thanks very much for coming here and chatting with

[17:13] me thank you Daniel I'll see you soon see you around this episode was edited by Kate brunot and Amber Don a helped with transcription the opening and closing themes are by Jack Garrett financial support for this episode was provided by the long-term future fund along with patrons such as Alexi maaf to transcript of the episode or to learn how to support the podcast yourself you can visit hrp.net finally if you have any feedback about this podcast you can email me at feedback axr p.net [Music] [Music]
