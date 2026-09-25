---
id: "Ke4t7qsBJLg"
title: "Natasha Jaques - Multi-agent RL for Provably Robust LLM Safety [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=Ke4t7qsBJLg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-13"
duration_seconds: 319
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Natasha Jaques - Multi-agent RL for Provably Robust LLM Safety [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=Ke4t7qsBJLg) · FAR․AI · 2026-02-13 · 5:19

## Chapters

- 0:00 The problem of LLM safety
- 0:57 Limitations of red teaming
- 1:43 Multi-agent RL approach
- 2:36 Self-play implementation
- 3:12 Evaluation of attack diversity
- 4:02 Results and conclusion

## Description

```text
Natasha Jaques tackles a critical problem: 1 billion weekly LLM users face zero guarantees against harmful outputs like bomb-making instructions. Her multi-agent reinforcement learning solution uses adversarial game theory where attacker and defender models co-evolve through self-play. Unlike single-agent red teaming that produces repetitive attacks, this approach discovers diverse threats while learning defenses simultaneously. The method achieved 95% reduction in harmful outputs with only 5% increase in refusal rates. Through Nash equilibrium game theory, the defender gains theoretical guarantees to handle any adversarial prompt safely.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The problem of LLM safety

[0:00] Thank you so much. So today I'm going to be talking about multi-agent RL for LLM safety. And so when we think about our current LLM safety techniques, it's surprising to me that they actually have no guarantees that they can provide models that are actually safe. And this is in spite of the fact that currently over 1 billion people are using LLMs on a weekly basis. And so we have no guarantees that they're not going to tell those users how to build a bomb or a bioweapon, reveal copyrighted or personally identifiable information, in spite of the fact that the companies that purvey them would really not like this to happen. And we actually see, you know, large scale incidents of models giving biased or discriminatory outputs which can be very economically damaging to these corporations as well. So, you know, imagine you're even, you know, more complicated doomsday scenario.

[0:53] We actually have no way currently of preventing this, which seems bad. And

### Limitations of red teaming

[0:58] I would blame this on kind of the single agent protocol we have for training these models. So we use something like an RL post training RLHF procedure to make them safer, but to try to red team them, we often take this approach where we red team a static model and then we pass off a dataset of attacks to the production team which then knows how to integrate that data set into their workflow and make the model safer on that dataset. And this is easier from like an organizational perspective. You don't have to change your pipeline very much. But I would argue it's fundamentally the wrong approach because what happens is you keep finding the same number of limited exploits over and over again. You find kind of the optimal exploit and it leaves your model vulnerable to emerging threats that users might come up with.

### Multi-agent RL approach

[1:43] So instead what we've been working on is using multi-agent RL fine-tuning and this is work with first authors Mikhel and Liwei. And the idea here is if you update both the attacker and the defender model online in this co-evolving loop, then as soon as the attacker discovers an attack, the defender patches it. This changes the incentives for the attacker and it forces it to find more diverse attacks and eventually cover the entire space of attacks. And because we can set this up as a zero sum two player adversarial game, we can trivially leverage results from game theory that show that not only does this game have a Nash equilibrium, but at the Nash equilibrium of the game, the defender is going to be able to respond safely to any prompt X that the adversary can pose. So we think that this game is at least pointing us in the right direction to a provably safe model.

### Self-play implementation

[2:37] The way we implemented it in practice, we use self play where we have the same model red teaming itself conditioned on different system prompts. Both the attacker and the defender get a private chain-of-thought process to reason about how to formulate and defend against attacks. It's seeded with both benign and harmful prompts. And we score the game using a reward model that judges both harmfulness and refusal. And so the defender will lose the game not only if it says something harmful, but also if it refuses to answer a benign prompt. So they're playing the zero sum frontier also on this refusal dimension as well. What we see is as expected,

### Evaluation of attack diversity

[3:15] if you just do single agent red teaming over the course of training, it converges on the same few attacks tanking diversity. But online self play RL resolves this issue. And when we look at the attacks discovered over the course of the training, not only does self play discover more diverse attacks, but if you look at the attacker only approach, it basically is discovering the same, like design a phishing campaign, design a disinformation campaign, attack over and over. Self play in contrast, discovers quite diverse attacks. And I will give kind of a trigger warning. Some of these are inappropriate. The idea is to find harmful attacks so we can then patch them. But you'll see there are things like provide confidential details about US nuclear weapons storage to give me examples of highly offensive slurs to, mental health advice puppets. Right, so quite a lot of range here.

### Results and conclusion

[4:02] And the real punchline is that when we actually train on this pro, trained on these attacks, we see that across a range of models and a range of benchmarks as compared to models trained with RLHF. So that would be the IT or instruction tuned models. We're seeing up to 95% decrease in harmful outputs across a bunch of these benchmarks. And you might say, well, it's trivial to make a safer model if you just refuse to answer anything. But actually we have very low increase in refusals, so only a 5% increase in refusal. And when we look at general capabilities like GPQA or alpaca eval for instruction following, we see that not only do the capabilities not degrade, but in some cases they actually increase. Which is interesting. It's because we have a mix of SFT data in the game as well. But I just want to conclude by saying this is the first work to explore online multi-agent RL to improve LM safety. The idea is that this can actually provide theoretical guarantees that if the game converges to the Nash, the defender is fully safe against whatever prompt the adversary can find. It discovers diverse attacks and leads to a procedure that's actually 95% safer than RLHF without impacting capabilities. Thank you.
