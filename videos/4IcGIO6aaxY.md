---
id: "4IcGIO6aaxY"
title: "Sheila McIlraith - Epistemic side effects"
url: "https://www.youtube.com/watch?v=4IcGIO6aaxY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 393
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sheila McIlraith - Epistemic side effects

[Watch on YouTube](https://www.youtube.com/watch?v=4IcGIO6aaxY) · FAR․AI · 2024-02-08 · 6:33

## Chapters

- 0:00 Introduction to side effects
- 1:24 Defining epistemic effects
- 3:21 Perils of false beliefs
- 4:23 Mitigation and conclusions

## Description

```text
Sheila McIlraith - "Epistemic side effects."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to side effects

[0:04] Hi, I'm going to talk about epistemic side effects and hopefully convince you that it's a largely unacknowledged threat to AI safety. I'd like to acknowledge my co-collaborators, Toryn Klassen and Parand Alizadeh Alamdari, who are both from the University of Toronto. The task that we are interested in exploring is: How can a reinforcement learning agent learn to act safely given a potentially incomplete objective specification? And of course, this is a problem that's been around for a while. So to act safely, we want to, the classical answer to that question is to avoid negative side effects, which are undesirable changes to the world that are allowed by the explicit objective. A lot of people have worked, have looked at this... Krakovna and Turner and various other people. And they've looked at side effects that are typically physical side effects. So I tell the robot I want to go from point A to point B, and the robot breaks a vase en route negative side effect.

[1:14] Or I tell the robot that I want them to get me a cup of coffee, and their zeal to optimize for the objective that I've given them, they kill everybody at the lineup at the Starbucks.

### Defining epistemic effects

[1:24] So what we're interested in here are a different type of side effects, in particular epistemic side effects, which are changes to the knowledge or beliefs of other agents, including humans. That were not explicitly specified as part of the actor's objective, but are allowed, of course, because they weren't specified. Here are some examples of epistemic side effects. You see me grab my car keys and you infer that I'm going out with the car. Or I eat the chocolate cake in the fridge, unbeknownst to you. You still think you're going to eat that cake after dinner, but you are operating under a false belief. I change your password from 123 to 456, and you're now unable to access your account. You are in a state of ignorance. So there are all sorts of different types of epistemic side effects. There are false beliefs, which can be directly communicated as misinformation or as lies. I can perform an action that others observe and draw an incorrect conclusion from it, as was the case with picking up the car keys.

[2:22] Or I can covertly change the state of the world, making previous beliefs outdated, as the case of the password. One might think that true beliefs would be acceptable. There wouldn't be negative side effects. But that's actually not always the case. In particular, in the wrong context, combining a true belief with a false belief that an agent already has can result in poor decisions. So for example, if I tell you that the mall is open and that's true, but there happens to be a pandemic and the mall is full of people with severe illness, then if you decide to go to the mall based upon me telling you that it's open, it may actually have a negative consequence. Similarly, true beliefs may cause you to leak private information, so they're not always positive side effects. Similarly, the last type of epistemic side effect is ignorance. Moving objects to unknown locations, for example, can cause you to go from a state of knowledge to a state of ignorance. So epistemic side

### Perils of false beliefs

[3:22] effects are important. A natural context to discuss epistemic side effects is partially observable and multi-agent environments. We need some uncertainty about what we know and what we don't know. But epistemic side effects are really important to study. And I'd actually argue that they may even be more perilous than physical side effects. Physical side effects we can observe in the world. We can react to them and we can respond. Negative side effects are in somebody's head. We can't inspect the beliefs that are in somebody's head. They're much more difficult to predict and they're much more difficult to detect. And particularly false beliefs can lead to decisions with catastrophic consequences. One need only think about large scale military decisions that might be predicated on false beliefs. Or even if I'm driving my car and somebody tells me to turn right, I may make the false inference that they've looked to see that there's no cyclist beside me, make the right turn and kill a cyclist. So false beliefs can be really, really detrimental. So hopefully I've convinced you that epistemic side effects are important.

### Mitigation and conclusions

[4:27] We have a particular approach to dealing with them that I'm going to describe to you. And it's based on some past work on avoiding side effects by being considerate of other agents. And the basic premise of that work is that to act safely, an agent should contemplate the impact of its actions on the future well-being and agency of others in the environment, including other acting human agents as well as passive or reactive agents. So the idea is: think before you act. Think about your consequences not only with respect to yourself and with respect to your objective, but with respect to the impact that it's going to have on other people in the environment in the future, on their well-being, on their ability to do what they want to be able to do, and even on processes like the environment, like streams or other operating processes that are operating in the environment. And the approach we take, even though this seems multi-agent, is that it's actually quite pragmatic, which is that a reinforcement learning agent will not be able to compel humans to consistently and rationally cooperate.

[5:26] I think that it's hard for us to compel other people to cooperate and other human beings to cooperate consistently and they are not always rational and even if they do deign to cooperate. So we've got some some great experiments that show the results. I'm not going to go through them here in the interest of time. Click, click, click. Click, click, click. That really show that this particular type of approach works very effectively relative to other approaches where the agent does not consider the outcome of other actions. And I encourage you to look at the results in our paper. I'd like to stop with two takeaways. The first is that epistemic side effects are an important and understudied problem in AI safety. And also that contemplating the impact of an agent's actions on the future well-being and agency of other agents is really an effective way of avoiding side effects. Not only side effects that are about the physical world but also side effects that are epistemic in nature. Thanks.
