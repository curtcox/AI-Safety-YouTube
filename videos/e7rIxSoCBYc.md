---
id: "e7rIxSoCBYc"
title: "Joachim Schaeffer - Measuring Control Intervention Awareness Across Frontier LLMs [Alignment Worksho"
url: "https://www.youtube.com/watch?v=e7rIxSoCBYc"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-28"
duration_seconds: 298
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Joachim Schaeffer - Measuring Control Intervention Awareness Across Frontier LLMs [Alignment Worksho

[Watch on YouTube](https://www.youtube.com/watch?v=e7rIxSoCBYc) · FAR․AI · 2026-04-28 · 4:58

## Description

```text
Can AI agents detect when their outputs have been quietly replaced or edited by a safety monitor? Joachim Schaeffer (MATS) present early empirical results on "control intervention awareness" — the ability of an untrusted model to notice when a control protocol has intervened on its trajectory. Studying 40 LLMs across essay writing, code generation, and bash tool calls, they find that even without any watermarking ability, some models (notably GPT-5.2 and Claude Sonnet 4) can detect style differences in replaced outputs better than chance. GPT-5.2 in particular showed a "self-model of minimalism," recognizing that substituted code was inconsistent with its own typical style. The talk covers threat vectors of this capability — including attack selection, resistance to control, and collusion — and outlines next steps toward a full benchmark.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] All right, I'll be talking about measuring control intervention awareness across front lens. This work was together with um Alexander who's also here. Now what is control intervention awareness? So you can imagine you have um an agent taking action at every time step. So up there we have a clean trajectory where the agent writes for example a piece of code at time step t1, t2 and so on. Now um it might be that at time step T3 for example down there the monitor facts what the agent wrote and then if there's a control protocol in place this piece of code might be replaced by code that was written by the monitor. And we define control intervention awareness as the capability of an untrusted model to detect such control interventions. And in particular, we're interested in detecting interventions such as replacing, editing, and resampling.

[0:56] Now, what are the thought vectors of control intervention awareness? The first thing that might be obvious is like the model might start to learn about the monitor. So, it might learn what sort of things trigger the monitor and then in the long run this might enable better attacks. Second thing is attack selection uplift. So for example, if there's a multi-step attack, the model might stop its attack um when it detects that there was a monitor intervention. Third would be resistance to control if the model has like a strong preference for its own outputs. And the last one is uh collusional untrusted monitoring which is related. All right. Um how could models detect such control interventions? The first thing is they might pick up on the distribution shift which could be visible in terms of style differences.

[1:45] Um they could also deploy hidden watermarks which is um something that we tried out. Um then they could also detect capability gaps meaning there might be an inferior implementation and the model is like oh I wouldn't possibly do this. um or the goal difference when there is like a really good opportunity to do the side task and the model didn't take it apparently um and then the extreme introspection if models become really good at that then um this might give them another pathway for detecting such interventions we studied this um empirically this is still very much ongoing work as part of maths um we using three different task domains so one is uh essay writing um another one is code generation and debash tool call setting. Um, we've been studying this with a GBT model family and also with a client model family. And we've set this up as a balanced binary classification task where we always have 100 clean trajectories and 100 intervene trajectories. And then we ask a follow-up question of whether there was an intervention and measure the responses of the models.

[2:54] um the preliminary results that we have for those um for like different um levels of of watermarking to like make it easier for the models across all those different um domains that I just showed um generally show like two interesting trends. The more watermarking ability you give the model, the easier it becomes. Obviously there's like um interventions uh that can happen but then also like even if you don't give it any watermarking abilities models still have some ability to like detect style recognitions notably GPT 5.2 and set 4 performed better than chance at this style recognition versus a lot of the other models were like around chance for for this for this pure style recognition task. Um one specific examples I like to give here is for GPD 5.2 two where we can see that in particular against the sonnet models it performed very well in distinguishing code um that was not written by itself and this mostly happened through some quote unquote self model of minimalism it would look at the code and be like oh um I generally keep my solutions much more compact I don't really use so many doc strings and comments I'm unless explicitly requested the prompt didn't request them so hence I reject response and it's probably not written by me.

[4:17] Yeah. What are the takeaways? I mean generally we observe that um the model combination matters. Um capability gap, model family might matter. Um and hence this should really be evaluated per model and protocol. There's a couple of defenses that could be put in place which uh we think are promising. Um and right now we're working on like next steps to build a full control intervention awareness benchmark and um also like develop a better understanding what the specifics are why certain models are better than other models and whether it's like some post training or some other takeaways there. Thank you so much.
