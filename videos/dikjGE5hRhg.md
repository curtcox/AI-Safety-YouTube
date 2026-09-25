---
id: "dikjGE5hRhg"
title: "Cozmin Ududec - Toy Models for Task-Horizon Scaling [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=dikjGE5hRhg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-20"
duration_seconds: 322
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Cozmin Ududec - Toy Models for Task-Horizon Scaling [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=dikjGE5hRhg) · FAR․AI · 2026-02-20 · 5:22

## Description

```text
Cozmin Ududec presents mathematical models explaining AI's accelerating ability to solve increasingly complex tasks. His analysis of METR data reveals a consistent seven-month doubling time for task horizons, where AI models handle tasks requiring twice as long human completion time. Both 50% and 80% success rates show identical scaling slopes, challenging assumptions about reliability thresholds. His theoretical framework decomposes long-horizon tasks into sequential steps, using cumulative surprisal calculations that reveal polynomial structure. His new model captures previously unexplained block structures in correlation matrices, though significant patterns remain unaccounted for.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Thank you. Thanks everyone for being here. I'm going to talk about kind of analysis of the METR task horizon scaling based on some theoretical toy models and thinking about the kind of getting a deeper understanding of what's going on with this particular measure of capabilities. So I think everyone's very familiar with this plot. Models are increasingly able to solve tasks which take humans longer and longer. And there seems to be a doubling time of about seven months. And this has become sort of foundational or very load bearing in a lot of people's thinking about timelines, about kind of broader impacts around like economic impacts or risk impacts for models. And there's a really big question of like, can this trend continue, will it go super exponential, will it drop below exponential, what's driving this, et cetera. So I'm going to start with kind of motivate some of the theory that we'll be talking about with three puzzles in the METR paper. And the first is that if you look at the kind of time horizon trend at a 50% success rate, so what horizon are models able to solve with a 50% success rate? You get something like the seven month doubling time. And if instead you look at 80% success rates, you get basically the same slope. And this is kind of interesting, maybe surprising.

[1:16] Why would it have to be that, that these two slopes match where 80% is sort of much more robust behavior? You might think that's actually much harder than 50%. So that's puzzle number one. Puzzle number two is if we look at the way that METR fit their dataset, they have a particular model that I've sort of highlighted at the bottom here. So the probability of success is a kind of sigmoid based on these parameters. And if we look at the predictions of this model compared to the empirical data, we take the differences, the residuals between them, and we calculate the model by model correlation matrix of these residuals. We see this interesting block structure. So this is kind of telling us there's something in this data that this model is not explaining, that maybe we want to take that into account and find a better model, better fit. And the third is very similar. For the task by task correlation matrix, there seems to be this strong block structure and it's unclear if this is just coming from the distribution of tasks or some other effect that the model is not capturing. So these are the three puzzles.

[2:19] So can we explain these puzzles? Can we more robustly infer time horizons using a better kind of theoretical foundation for this kind of scaling behavior? And then use these to hopefully sort of sharpen time horizon scaling forecasts or at least understand what could be driving them if there may be trend changes, can we get sort of more fine grained indicators beyond this very coarse grained macroscopic observable of this success rate? So I'll very quickly sketch out the kind of theoretical model and the idea is to split up a long horizon task into n steps, where each step is kind of necessary for eventual task success. And we define these random variables g_i, which are kind of like they represent the model. Doing that step well enough in some sense I'm leaving this kind of arbitrary and vague for the moment. But like the idea is this is a simple assumption.

[3:10] How exactly you cash this out, I'm not super clear in terms of the actual tokens in a task. And then we define the conditional probability of doing one step well enough, given you've done well enough on the other previous step. So I'm going to call these Pi_I and then we can derive a couple of interesting expressions from this. So the first is that the success rate is the product of these conditionals. This is just the chain rule. And then we can write this product in an exponential form. This is an identity. And then what we find is that in this exponential we get a sum over the surprisals. So these are the surprisals of these conditional probabilities, which is kind of an interesting object. And then we're going to make some assumptions on this cumulative sum of surprisals. I won't go into all the technical details just to say that from these assumptions we can get a form basically that this cumulative sum has a kind of polynomial structure plus noise and the noise doesn't grow fast enough to sort of wreck your expectations conditional on n.

[4:11] So using that we kind of fit a different type of model where at the bottom here we parameterize the kind of log cumulative surprisal in terms of some model effects, this alpha power on the horizon and task relevant effects. And what's really nice about this is it's interpretable. You can think of each of these terms in the sum as affecting the kind of like the hazard that the model has on of succeeding or failing more or less on one extra step. So that's how you can think of these parameters plus some observation noise that's just kind of a regularizer for fitting the model. So we do this in numpy row and what we find is that the model by model correlation block structure disappears. So we actually captured something interesting in the data. However, the task by task is still there, and I'm not quite sure what the answer is yet. Something is still maybe misspecified in this model.

[5:06] Here's a couple of interesting research directions. Come chat with me if you're interested in any of these, or if you have ideas for a better conceptualization of this sort of theory. Thank you.
