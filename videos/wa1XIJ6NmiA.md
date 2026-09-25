---
id: "wa1XIJ6NmiA"
title: "Tomek Korbak - Chain of Thought Monitorability for AI Safety [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=wa1XIJ6NmiA"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-01-06"
duration_seconds: 580
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Tomek Korbak - Chain of Thought Monitorability for AI Safety [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=wa1XIJ6NmiA) · FAR․AI · 2026-01-06 · 9:40

## Description

```text
Tomek Korbak (OpenAI) reveals transformer architecture creates an AI safety opportunity through chain-of-thought monitoring. We got lucky: models reason in natural language rather than opaque vector spaces, making their cognition readable. Two factors enable monitoring: transformers must externalize reasoning for difficult tasks due to architectural limitations, and models struggle to suppress information even when instructed. However, four threats could close this window: drift from legible English, optimization pressure, indirect optimization effects, and shifts toward latent space reasoning. Korbak recommends developing monitorability measures for training and deployment decisions while this transparency window remains open.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Hello. Yeah, I will try to convince you that CoT (chain-of-thought) monitoring is a promising approach to mitigating misalignment risk. But let me start with a story. Ten years ago, at the dawn of deep learning, we believed that the path to agents is going to be through those black box deep neural networks trained to reason in high dimensional vector spaces. In that world, we would only be able to supervise and evaluate those models by looking at their behavior, but we would have no insight into their cognition such as goals, beliefs and plans.

[0:54] But we were lucky. We somehow ended up with models trained to understand natural language and post-trained to reason in natural language before taking actions. And I just wanted to highlight that it was very far from clear that this is going to be the path to general purpose AI agents. And this offers a great opportunity for AI safety and we should try to seize it by doing chain-of-thought monitoring. So what do I mean by chain-of-thought monitoring? A chain-of-thought monitor is any kind of automated system that reads the chain-of-thought of a reasoning model and flags any potentially harmful interactions. And by harmful interactions I mean something like reward hacking or exploiting flaws in the specification of desired behavior, sabotage, intentionally inserting bugs or in generated code, or some flaws in produced artifacts, falling prey of prompt injections or malicious instructions embedded in trusted data, or sandbagging which is strategically underperforming in evaluations.

[2:15] A fun fact about this slide is that those speech bubbles are actual quotes from actual reasoning models from those papers that we cite. So the idea is that if an agent is going to reward hack, it's going to tell you natural language that's about to reward hack and you can read this. It's not so simple in practice. We know that chain-of-thoughtis not always faithful, but in many cases that we actually care about, it might be faithful enough. And there are two powerful reasons why we might expect chain-of-thought to be monitorable in practice. The first one is that agents will need to externalize their plans in chain-of-thought to complete them.

[3:07] So a specific claim that I want to make is that for sufficiently difficult tasks, transformers must use legible chain-of-thought as a form of working memory. And here we condition on tasks being sufficiently difficult, by which I mean that an agent needs to use chain-of-thought to complete them and wouldn't be able to complete them without chain-of-thought. Indeed, some recent research from METR and Google DeepMind suggest that faithfulness increases reliably with difficulty. So I'm not going to discuss these plots. I just wanted to leave them as pointers to this general claim that on really difficult tasks, models are often quite faithful. And I sometimes feel that the case for chain-of-thought unfaithfulness is overstated because researchers focus too much on tasks where chain-of-thought is not actually needed, and therefore models can get away with reasoning that's actually just performative.

[4:22] Coming back to the claim, it's also specific to transformers as opposed to some other architectures. And this serendipitous thing about transformers is that they are inherently limited in the amount of serial information processing that can happen in a single forward pass. So if you visualize information flow through a transformer, an activation from an upper layer can only influence activations in lower layers for subsequent token positions when mediated from visible tokens. So in this diagram, those two red circles are activations, and if you want to trace a path between them, this path will have to go through those gray rectangles which are visible tokens. So the high level idea is that transformers as an architecture have limitations, and because of that, for sufficiently complicated computations, they won't be able to be executed just in latent space, and they will have to involve some kind of computation that's externalized in chain-of-thought, and therefore it's going to be monitorable. So that's the first reason.

[5:44] The second reason why we should expect chain-of-thought to be monitorable is that agents will have a tendency to externalize their plans. The first claim was more theoretical. This one is more empirical. We do see in practice that even if you instruct a language model to suppress some information from chain-of-thought, models are often unable to do so. My MATS scholar, John Chen, is now leading a project investigating to what extent this actually holds across models. So it seems that chain-of-thought of current models are reasonably monitorable. But this might not hold indefinitely. And there are at least four reasons why we might expect chain-of-thought of models to stop being monitorable. The first one is that as you do high compute RL post-training, chain-of-thoughts might naturally drift away from legible English. And we already see models using words in idiosyncratic ways. It's just unclear to what extent it actually hampers our ability to monitor them.

[6:58] A second reason is that we might be applying direct optimization pressure on chain-of-thoughts, namely optimizing chain-of-thoughts to look nice. Recent work by my OpenAI colleague Bowen Baker has suggested that if you use a chain-of-thought monitor as a reward model during training, you compromise monitorability. And even if we don't apply direct optimization pressure, we might still indirectly optimize chain-of-thought through various ways. And it's just unclear to what extent it hampers our ability to monitor them at scale. And finally, probably most worrying is that we as a field might move away from transformers towards other architectures that do more sophisticated reasoning in latent space and that will no longer be monitorable.

[8:05] Most policy interventions around chain-of-thought monitorability have complex trade-offs, but I think that there are at least two ideas that seems to be robustly good and seem to be lacking any significant downsides and this is just developing measures for chain-of-thought monitorability and using those measures in training and deployment decisions. And it's very nice recently to see those considerations being discussed in system cards of models from OpenAI, Anthropic and Google DeepMind. So to sum up, the claim I wanted to make is that chain-of-thought monitoring is a promising approach to mitigating misalignment risk but this opportunity is fragile, it might slip away so we should seize it while it lasts. And we should try to extend this window of opportunity where chain-of-thought is monitorable.

[9:23] This talk was based on a position paper I wrote with Mikita Balesni and we are advised by Bowen Baker, Vlad Mikulik and Rohin Shah. Thank you.
