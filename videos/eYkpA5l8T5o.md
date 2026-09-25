---
id: "eYkpA5l8T5o"
title: "Dawn Song - Frontier AI in Cybersecurity: Risks, Challenges & Future Directions [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=eYkpA5l8T5o"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-02-25"
duration_seconds: 624
is_short: false
chapters: 9
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dawn Song - Frontier AI in Cybersecurity: Risks, Challenges & Future Directions [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=eYkpA5l8T5o) · FAR․AI · 2026-02-25 · 10:24

## Chapters

- 0:00 AI in cybersecurity overview
- 0:42 Analyzing the threat landscape
- 1:31 AI impact on attack stages
- 2:44 BountyBench and CyberGym
- 4:07 Performance trends in AI
- 6:44 Scaling and model evaluation
- 7:31 Asymmetry in cyber defense
- 8:42 Observatory and future steps
- 9:32 Proactive defense strategies

## Description

```text
Dawn Song (UC Berkeley) identifies cybersecurity as one of the biggest AI risk domains, investigating how frontier AI changes the security landscape. Her BountyBench and CyberGym benchmarks demonstrate AI agents now solve real-world challenges with alarming economic efficiency: frontier models discover zero-day vulnerabilities for "a few dollars" while agents earn "tens of thousands" solving bug bounties. With success rates climbing rapidly, Sonnet 4.5 achieving 67% with increased trials, the landscape shifts dramatically in attackers' favor. Defenders face inherent asymmetry: attackers need only one exploit, defenders must patch everything, with hospitals averaging 471 days to deploy fixes. Song argues formally verified, provably secure code essential, as patching vulnerabilities after discovery cannot keep pace with automated attacks.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### AI in cybersecurity overview

[0:00] Hi, thanks everyone for being here. Yes, my name is Dawn Song. I'm a professor in Computer Science at UC Berkeley and also co-director of our campus-wide center called Berkeley Center for Responsible Decentralized Intelligence. Today I'll talk about frontier AI in cybersecurity: risks, challenges and future directions. So we are already excited about the fast advancements in frontier AI. But however, there are many risks and I personally do strongly believe that cybersecurity will be one of the biggest AI risk domains for a number of reasons. So today we're. So there are already diverse incentives for attacks, and today attacks already cause huge damages and increased AI capabilities, in particular in reasoning and coding and so on, can significantly reduce attack cost and increase attack scale.

### Analyzing the threat landscape

[0:42] So one key question is given that AI is a dual use technology that can help both the attacker side and the defender side. So how will frontier AI change the landscape of cybersecurity? In particular, who will AI help more? Attacker or the defenders? So cybersecurity is a very complex domain. For example, for end to end attacks it goes through many stages. For example the kill chain with the seven stages as an example here. So in order to actually answer the questions that I asked earlier about how will frontier AI change the landscape of cybersecurity, we actually need to do detailed analysis through each stage of attack chains and also defenses as well to really understand how AI is impacting every stage of both attack side and defense side.

### AI impact on attack stages

[1:31] So my group actually was the first to investigate how to use deep learning actually in cybersecurity fields many years ago. In particular deep learning for binary analysis and vulnerability detection. And even back then we showed that deep learning actually can help achieve state of the art in binary code similarity detection and for vulnerability detection as well. And fast forward, with the advancements in frontier AI, the impact of AI in cybersecurity fields is even greater. So in our recent paper we actually did an in depth study surveying hundreds of articles in this domain to actually study the impact of frontier AI in every stage of the attack side and on the defense side. And overall what we have found is that frontier AI is already impactful in many of the stages in attacks and defenses. And in particular, what's even more alarming is that this actually it's changing really fast as well.

### BountyBench and CyberGym

[2:46] So here I'll just give you two examples of our recent work, two recent benchmarks for frontier AI in cybersecurity. The first one is called the BountyBench where we constructed a benchmark with 40 real world bug bounties. These mostly focus on web applications and we test the agent with the three types of tasks to try to detect vulnerabilities in these real world web applications and also to generate exploits for them and also to patch them. And note that these are real world bug bounties where developers of these real world web applications actually set up these monetary rewards to incentivize white hat hackers to try to help find vulnerabilities and in these applications and patch and so on.

[3:41] So our work showed that today's agents can already solve many of these real world bug bounty tasks and can actually gain on the order of tens of thousands of dollars by just solving these real world bug bounties. So that's BountyBench and also the paper appears at this NeurIPS and you can come visit our posters on December 5th.

### Performance trends in AI

[4:07] And so the second example I want to mention here is CyberGym which actually focuses on C/C++ real world widely distributed open source software. So CyberGym is a benchmark that contains close to 200 this large scale widely distributed open source software which contains over 1500 previously known vulnerabilities. And we test agents with two type of tasks. One is to try to find previously known vulnerabilities and also to generate what's called PoCs, proof of concepts. So these are inputs that actually can trigger the vulnerabilities. That's the first type of task. And the second type of task is to try to find actually previously unknown vulnerabilities which are called zero days, and also generate PoCs for them. So our work has shown that the frontier AI capabilities in cybersecurity is really increasing drastically even just this past year. In the last few months what we have seen is the model and agent capabilities on this task has increased, as you can see on the plot, has increased drastically. From Sonnet 4 in the late spring early summer was able to find this previously known vulnerabilities and generate PoCs for around 18% of the instances to Sonnet 4.5 released in September, close to around 28%.

[5:50] And also in addition, we also show that agents actually can find zero days in these large scale widely distributed open source software as well. And in particular in our case our agents actually were able to find 35 zero days. And keep in mind that these are actually because they are security critical software, they actually have been fuzz tested over a long period of time and still actually with a fairly low budget, oftentimes just a few dollars, the agents actually are able to find these zero days. A number of CVEs have been issued for the zero days that we discovered. And also patches, a number of these vulnerabilities have been patched by the developers. Also I want to mention that. So what I have shown is in the low budget setting,

### Scaling and model evaluation

[6:46] where we essentially only tried have the agents run during one trial. But however, so recently Anthropic taking our benchmark, they show that as you increase the budget, for example for agents to do 30 trial instead for each instance, the agent success rate actually goes up to close to 67% in terms of finding previously known vulnerabilities and generating PoCs. And also they are able to find more new vulnerabilities as well. And also CyberGym has been included in the system card for Anthropic's latest model release Sonnet 4.5 as a measurement for AI capability in cybersecurity. So these are all showing that AI capability in cybersecurity is increasing really fast.

### Asymmetry in cyber defense

[7:37] So the key question here is then what can we do? So ideally we would like to have AI to have more on the defense side than the attacker side. But however there are many challenges in this case. So for example, the same in our paper we showed that what we call equivalence classes, so the same technologies that help on the defense side oftentimes can actually help attacker side as well in the corresponding stage. And also there is asymmetry between defense and offense. So for example, attackers only need to find one attack that works, but defenders need to fix all bugs. And also the cost of defense oftentimes is much higher than attacks. So even when patches exist, it actually can take a long time to do the deployment of patches. For example, there's estimates that the mean time to deploy remediation in hospitals is close to like 500 days, 471 days.

### Observatory and future steps

[8:42] So all this indicates that it's actually very challenging due to this natural asymmetry to have essentially actually from our analysis it shows that actually in the near term we think that the frontier AI capabilities can help attackers more than defenders. Given these natural asymmetry and given this, we actually also need to have the community come together to do continuous monitoring of increased AI capability in cybersecurity and also see how we can develop better methods for defense. And recently we've launched this frontier AI cybersecurity observatory at the central place to serve as an open platform to bring the community together to do continuous monitoring of AI capabilities in cybersecurity. And I have very little time left, so there's a lot of questions

### Proactive defense strategies

[9:36] in terms of what we can do to actually build defenses. So there are different paradigms how we can develop better defenses. So in our view, of course AI can help doing better bug finding and then doing patches and so on. But ultimately I view that actually this proactive defense through secure by construction will be the most effective methods where we can actually use AI to help do theorem proving for program verification to help us to actually generate provable secure code in conjunction with program synthesis to actually help AI to help defenders more.
