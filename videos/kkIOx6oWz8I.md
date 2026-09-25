---
id: "kkIOx6oWz8I"
title: "FAR.Research: Planning in a recurrent neural network that plays Sokoban"
url: "https://www.youtube.com/watch?v=kkIOx6oWz8I"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-10-31"
duration_seconds: 135
is_short: false
chapters: 0
transcript: null
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# FAR.Research: Planning in a recurrent neural network that plays Sokoban

[Watch on YouTube](https://www.youtube.com/watch?v=kkIOx6oWz8I) · FAR․AI · 2024-10-31 · 2:15

## Description

```text
FAR.Research: Planning in a recurrent neural network that plays Sokoban
📝 Blog: https://far.ai/post/2024-07-learned-planners/
📄 Full paper: https://arxiv.org/abs/2407.15421
👥 Research by Mohammad Taufeeque, Philip Quirke, Max Li, Chris Cundy, Aaron Tucker, Adam Gleave, Adrià Garriga-Alonso

Neural network mind control? Our research shows RNNs playing Sokoban form internal plans early on. Linear probes, can read and alter these plans as they form. With model surgery, we make the network solve puzzles far larger than it was trained for.

Why does understanding planning matter? It’s key to AI alignment. Research on goal misgeneralization and mesa-optimizers shows that AIs can develop unintended goals. By studying planning, we can better guide AI to avoid optimizing for the wrong outcome.

Previously, we found that RNNs "pace" in cycles to solve harder Sokoban levels, often using extra compute time in the first few steps—over 50% of these cycles happen within the first 5 moves. Giving the network thinking time with NOOPs largely eliminates the pacing behavior!

By training linear probes on the RNN's hidden states, we can accurately predict future moves, demonstrating early planning capabilities (F1 scores: 72.3% for agent directions, 86.4% for box directions). Our non-causal linear probes are based on Thomas Bush et al's (2024) concurrent work on a very similar network.

Intervening with these probes lets us adjust the agent's plan. Interestingly, box plans often take precedence—agent probe interventions only work when box probes are insufficient to explain the behavior.

The final recurrent layer learned to allocate each possible action to a distinct channel, meaning the MLP layer doesn’t need to work hard—it simply reads these action channels and outputs the next move.

While the RNN can process images of any size, the final MLP layer flattens the 3D hidden state, limiting the network to a fixed grid size. So, we asked: can the network generalize to larger puzzles by using these learned action channels? 

YES! With probes, RNN generalizes to out-of-distribution puzzles, solving 2-3x larger grids with 10+ boxes, despite training on 10x10 grids with 4 boxes. 

We also trained top-K Sparse Autoencoders (SAEs) on the last layer’s hidden state. Surprisingly, all the interpretable features SAEs found were already present as individual channels, which were more monosemantic than the SAEs. A negative result for SAEs, or just an edge case?

This is just the start. Our future work will focus on understanding how the RNN computes the best plan and whether these interpretability techniques generalize to other domains.

Explore our open-source code, models, probes, and SAEs:
💻 Code: https://github.com/AlignmentResearch/learned-planner
```

## Transcript

_No English captions were available when this was retrieved._
