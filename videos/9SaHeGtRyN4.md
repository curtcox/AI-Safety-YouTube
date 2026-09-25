---
id: "9SaHeGtRyN4"
title: "Eric Neyman - Heuristic arguments: An approach to detecting anomalous model behavior"
url: "https://www.youtube.com/watch?v=9SaHeGtRyN4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 318
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Eric Neyman - Heuristic arguments: An approach to detecting anomalous model behavior

[Watch on YouTube](https://www.youtube.com/watch?v=9SaHeGtRyN4) · FAR․AI · 2024-02-08 · 5:18

## Description

```text
Eric Neyman - "Heuristic arguments: An approach to detecting anomalous model behavior."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Hi, I'm Eric Neyman. I am a theoretical researcher at the Alignment Research Center and to in this talk, I will motivate and describe some of our work. So one of the key barriers to building aligned AI is the reward misspecification problem, which is when you reward your AI for taking an action that looks good to you, but isn't actually what you want. Many of you have probably seen this toy example out of OpenAI where they tried to train the robot arm to grasp the yellow ball, but the robot arm instead learned to position itself in front of the camera so that it looked like it was grasping the ball. One potential solution to this is to improve the quality of your oversight. So in our toy example, you could imagine placing not one but two cameras pointing at the yellow ball from different angles so that the robot arm cannot get in front of both arms. And in the real world, this might correspond to getting really good protocols for oversight or maybe potentially using assistant AIs to help with your oversight process.

[1:11] So there's a relatively common view that improving your oversight will be sufficient to align AGI. And while I am fairly sympathetic to this view, I think that this is far from guaranteed. And the fundamental reason why is that a sufficiently advanced AI could learn to intentionally exploit loopholes in your oversight process. And this leads to a natural question, which is how do we distinguish successful task completion, which is what we want from successful intentional deception on the part of the AI, you know, such as tampering with your oversight process. Now, almost by assumption, observations made by the oversight process are not sufficient in order to distinguish between these two cases. But there's this intuition that the AI's internal activations should be systematically different in these two cases.

[2:10] and that's just because the AI's internal thoughts are probably different if it's trying to successfully complete the task versus if it's trying to figure out how can I deceive the oversight process? So to state this a little more formally, we could imagine an AI model M as well as a dataset D of inputs. We are going to make the assumption that M does exactly what we want it to do on D. Now suppose that there is a new input X* on which M gets high reward. We want to understand whether M gets high reward on X*for anomalous reasons. That is for a different set of reasons than why it got high reward on D. So how might you do this? One approach might be outlier detection on the model activations. That is you could ask whether the activations of on, of M on X* are systematically different from the sorts of activations that you see on D.

[3:10] But there are at least two problems with this approach. One is that at least naively outlier detection will weight all directions in activation space as equally important. Whereas in practice, some directions might be much more important than others in terms of how they influence the model's behavior. And the second issue is that while this might work reasonably well, if anomalousness is a linear function of the activations, it might not be. And we don't want to make that assumption. And so our hope is to find features of the model's activations that causally explain why the model performs so well on D and then to do outlier detection on those features. So an example of a simple feature might be say the product of three of the activations. So how do we plan to do this? First we search for a mechanistic for a heuristic argument that is a formal mechanistic explanation for why M performs so well on D. this explanation will involve some features of M's activations.

[4:18] And then we can use these same features to predict M's reward on X*. Where remember X* is the input on which M gets high reward. And we wanna figure out whether it gets high reward for anomalous reasons. Now, why use features to predict M's reward on X* instead of just running M on X*? Well, the idea is that if these features are sufficient to explain why M does well on X*, then that means that M does not behave anomalously on X*. Whereas if they are insufficient, then that means that M does well on X* for a different sort of reason than it did well on D. And so we want to flag M's behavior on X* as anomalous. There are many challenges ahead with this approach which I am happy to talk about after this session. Thanks.
