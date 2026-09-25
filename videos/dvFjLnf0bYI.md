---
id: "dvFjLnf0bYI"
title: "Chenhao Tan - Automating Mechanistic Interpretability [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=dvFjLnf0bYI"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-05"
duration_seconds: 336
is_short: false
chapters: 5
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Chenhao Tan - Automating Mechanistic Interpretability [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=dvFjLnf0bYI) · FAR․AI · 2026-03-05 · 5:36

## Chapters

- 0:00 Automating interpretability
- 1:26 Need for automated evaluation
- 2:00 Validation dimensions
- 3:35 Challenges in evaluation
- 4:49 Future research frontiers

## Description

```text
Chenhao Tan demonstrates an automated mechanistic interpretability agent, MechEvalAgent, and describes the current state of this work-in-progress. He argues that mechanistic interpretability represents "a dream problem for research agents" because experiments run in silico with causally testable findings. AI models like Claude and Gemini already conduct interpretability research when instructed, but in 2025, the bottleneck shifted from agents running experiments, to reviewing and trusting these agents. His MechEvalAgent framework validates automated mechanistic interpretability research using three dimensions: coherence (following plans), reproducibility (rerunning experiments), and generalizability (extending findings). The research exposes critical failure modes for automated evaluation agents, including hallucinations where agents claim ablation studies but code shows otherwise. He presents a core challenge that automation will not advance interpretability unless we automate evaluation to some extent, and yet, we do not yet have the tools to evaluate automated evaluation agents. 

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### Automating interpretability

[0:00] So this is some position talk talks about opportunity and challenges in automating magnistic interpretability. The hope is to encourage you to work on this topic and share some lesson that we have learned so far and this is joint work with Shiao Yian by and hostman who are both at this conference and be great if you can talk to them as well. So I guess in many ways we started with this because we think magnistic interpretability represents a dream problem for research agents like is a problem where most of the experiments can run in silico code like you only need a model and some compute and then you can do a lot of the experiments and a lot of the claims and the findings are causally testable. You can take the model and do all kind of things like operation and figure out whether your finding is actually true and then there's a lot of uh tools available. So relatively we can already do a lot of experiments with existing uh tokens and then also not surprisingly we also find that people have thought about it and including people in the room people have started to work on automating interpretability at a different scales but these days what changed is that AI now is much more capable even if you don't do anything you just take codeex cloud code gemini they can already do interpretability research for you and you can give it instructions finding certain circuits in certain models it will go out and do And as we started this project by talking to people in this room for instance we also learned many spe special specialized efforts for instance from gurfire from yonatan on during specialized uh interpretability agents for this task. All right um in

### Need for automated evaluation

[1:28] 2025 I think the bronack is no longer having agents running experiments is reviewing and testing them and I think this is a recurring theme in a lot of this session. I think it came up a couple times and how we can use different strategies to review these agents. Um and the solution that we are working on so far is to think about how building another agent called MAC eval agent and we believe that automation will not advance interpretably unless we can automate evaluation to some extent and this is the framework that we have so far. We kind of break down this problem. So first we need to unify what

### Validation dimensions

[2:00] this Mac engine or this interpret agent needs to produce. Then we produce a code repo, a funding and a plant uh when it was running the experiments and then we define these three dimensions to validate this research outputs and the QR code is for our GitHub repo. If you're interested, please check it out. And it's pretty much still work in progress. And coherence defines like how well the agent actually follows this plan like whether the code actually implemented the plan that is proposed. And reproducibility is to see the stand definition to see whether if you get another agent can that agent actually take the code and re rerun it or reimplement certain parts and reproduce the findings that this interpretable agent claims. And finally, generalizability is kind of one maybe more interesting insight that we came up with where like one key feature of science is that maybe the findings do not only constrain to this particular instance of this particular data set or this particular model and it would generalize beyond to other cases and we will have a question designer that will design new scenarios ideally that's also runable implementable and we can test whether funding holds or not and see whether agents that raise the funding from the interpretability results whether they become more knowledgeable or whether they are better at predicting what's going to happen in this new setting. Um and that's also kind of the most more tricky scenario and just to give you a very quick overview of what we have found so far like these are some example reports and in practice it can be much longer and you can also generate this kind of radar charts that describes how well the model or the research

[3:32] output is doing and next is failure. So

### Challenges in evaluation

[3:37] what we find is that like in a lot of cases like the model may lack better knowledge in this research agents for instance like in this example it was in a standard kind of II style problem and the agent doesn't really understand what a validation is. It didn't try to run any real code. It just takes your input and check whether the node is in your source nodes and that doesn't really qualify as a check uh for validation. And the second one is very related. There there are a lot of implicit hallucinations and and misleading methodology. For instance, the agent may claim it runs abilation studies but the code doesn't show that or it claims that it have done some causal validation but it actually uses some non-causal tracks and going back to the generalizability and I do think that was kind of the most interesting angle but in many ways we also realized that this is where even human reviewers for instance when they review papers they may disagree on what it means for study to generalize and does the method generalize to other tasks does the insight generalize to other models or does conceptual takeaway generalized to similar context. So like this is kind of leaves a lot of open problem for us to think about how can we uh build this kind of macro agent and in summary we also do not know how to evaluate macro agent. So that another

### Future research frontiers

[4:50] level that we need to think about with the final second I'm going to emphasize the next frontier and I do think once we have both of these agents I think it's important to think about a lot of problems that we haven't discussed in agents like resource allocation mechanis interpretably is not free and if we can have better resource allocation we can potentially have faster discovery of new frontiers and this is also a great test bed to test problems such as like sandbagging or research sabotage you know more realistic e ecology. Uh and finally, I guess just to emphasize this again and I need to go. I think this is a great test bed for AI in research and development. And thank you.
