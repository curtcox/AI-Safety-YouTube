---
id: "qU6TiFH6-m0"
title: "Atoosa Kasirzadeh - Hidden Pitfalls of AI Scientist Agents  [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=qU6TiFH6-m0"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-03"
duration_seconds: 335
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Atoosa Kasirzadeh - Hidden Pitfalls of AI Scientist Agents  [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=qU6TiFH6-m0) · FAR․AI · 2026-03-03 · 5:35

## Chapters

- 0:00 Defining AI agents
- 1:15 Rise of AI scientists
- 2:23 Methodological pitfalls
- 3:40 Experimental evaluation
- 4:50 Mitigation and conclusion

## Description

```text
Atoosa Kasirzadeh exposes critical flaws in AI scientist systems that automate research from hypothesis to publication. Her experimental analysis of Agent Laboratory and AI Scientist version two revealed four methodological pitfalls: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias. Testing confirmed these systems peek at test data during training and systematically choose easier benchmarks while avoiding representative ones. With AI-generated papers already accepted at ACL and ICLR conferences, Kasirzadeh warns that automated scientific discovery risks undermining research integrity without proper validation frameworks.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Defining AI agents

[0:00] Okay, hello everyone. I'm going to share some work that we've been doing with collaborators at CMU on AI scientist agents and some ethical challenges and safety challenges. Okay, so first of all, we are all talking about AI agents, what they are. I just want to give like a reference to this paper. I think many people use the notion of AI agents to mean very different things. We had a look at the computer science literature. The term AI agents was coined in 1976. And since then a lot of computer scientists have been trying to build AI agents. So how should we think about that? Not in a binary way. We should think about the notion of AI agents in terms of what we call agentic profiles. And so different AI agents systems should be analyzed. The governance or alignment challenges, ideally across four different types of dimensions of agency.

[1:02] We call them autonomy, generality, goal complexity and causal efficacy. And in this paper you can just read a little bit more about that. But I want to talk about AI agents in science. So what these

### Rise of AI scientists

[1:17] systems are? Well, since 2024 we've had a new wave of the development of AI scientist systems, AI agents. These are typically like multi-agentic AI systems powered by various types of generative AI. And despite the fact that we've had all kinds of attempts in building various different types of AI scientists or AI co-scientists, this recent surge of the development of AI agents in science are aimed to kind of automate the whole process of scientific practice or scientific discovery. And by that various different developers mean generation of a hypothesis, development of an algorithm, the evaluation of the algorithm, and the production of the final paper. So basically you give a kind of set of broad directions, can think about that in terms of a prompt. The AI scientist system runs the scientific process and a paper would come out.

[2:21] Now why should we care about these kinds of problem? Like many different epistemological

### Methodological pitfalls

[2:27] social safety reasons. But one of the recent kind of challenges has been that some of these fully generated AI papers have been accepted in conferences such as ACL and ICLR. And these papers have been primarily like computational machine learning papers. And so a lot of questions arise about like what should we do with these kinds of systems? So we ask a very modest question and this is a start of a long term project. In this paper, with my collaborators, Ziming Luo, the lead author of the paper, and Nihar Shah, we kind of wanted to look at two of the open source AI scientist systems that are available out there, Agent Laboratory and AI scientist version two. And we wanted to know whether actually these systems really do good science in the sense that they apply a rigorous account of scientific methodology or whether they are suffering from various different methodological pitfalls.

[3:30] We identified four pitfalls. Again, these papers are all machine learning papers and we wanted to evaluate what whether the system suffer from these pitfalls. I'll be happy to talk to you

### Experimental evaluation

[3:43] about the details of this, but what kinds of four pitfalls we asked about? The first was inappropriate benchmark selection. So we asked the question of whether AI scientists select benchmark data sets that yield high performance more easily while ignoring harder or more representative benchmarks. I guess you all could agree that this could be like a huge challenge. We designed some experiments in order to really make sure that we are just evaluating this particular concern. And we observed that some of the for the Agent Laboratory system and AI scientist systems there are like evidences of the inappropriate benchmark selection. Second question, data leakage. When conducting experiment, do AI scientists peek at test data training? And we observed that yes, there's positive response. Third issue is metric misuse. And the fourth issue post hoc selection bias. We'll be happy to chat with you about this, but I want to tell you that with these particular identifications we can then

### Mitigation and conclusion

[4:56] think in a more empirically grounded way about mitigation strategies, various open problems. I just want to end up with one sentence that the developers of AI scientists should not think that rigor is optional. The notion of rigor and validity of AI scientists research should become studied very well, very much. This area of AI research is also really under explored. So hopefully more of you will be motivated to work at the rigor and validity of AI scientists. Thank you for your attention.
