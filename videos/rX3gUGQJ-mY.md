---
id: "rX3gUGQJ-mY"
title: "Bowen Baker - Monitoring monitorability"
url: "https://www.youtube.com/watch?v=rX3gUGQJ-mY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-26"
duration_seconds: 326
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Bowen Baker - Monitoring monitorability

[Watch on YouTube](https://www.youtube.com/watch?v=rX3gUGQJ-mY) · FAR․AI · 2026-05-26 · 5:26

## Description

```text
Bowen Baker (OpenAI) introduces monitorability as a more practical framework than faithfulness for evaluating chain-of-thought reasoning in AI systems. Through active monitoring of large RL training runs and internal deployment, OpenAI finds CoT monitors consistently catch more misbehavior than action-only monitors. Baker demonstrates that perfect faithfulness doesn't guarantee usefulness—a CoT encoded in ROT13 is technically faithful but useless for monitoring. The key insight: monitorability only requires that monitors can predict safety-relevant properties from reasoning traces, not that models state every step explicitly. However, this capability is fragile and could degrade through language drift or shifts to vector-based reasoning. OpenAI is releasing evaluations across interventions, processes, and outcome properties to help the community measure and preserve monitorability as models scale.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] Hey, I'm Bowen from OpenAI. I'm I guess I'm cooked. So, share what I have anyway. Yeah, so you know, I I agree that there's some issues probably with this that we do need to figure out, but it is still been pretty useful so far. And at OpenAI we actively monitor, you know, our largest RL training runs. That's something that my team does. And we also, as you know, if you went to Marcus's talk, we also monitor our internal deployment traffic. And that has caught a lot of issues. It probably doesn't catch all of them, but it's still been pretty incredibly useful for us to do this. We've kind of repeatedly repeatedly found that if you monitor the COT in addition to the actions, you do much better than monitoring the actions alone.

[0:47] Which is pretty cool because, you know, our models just seem to to to reveal what they're thinking often times at the current moment. This is something we want to track. We don't want to just trust it blindly. That's something I'll get into later. But and so yeah, this is the point. So, for COT's monitoring to be useful, your COT's need to be monitorable. And that's kind of the the thing that we focus on a lot on my team. What is monitorability? That's maybe a a good place to start. We kind of started from the definition of faithfulness, which is kind of probably a more commonly talked about thing. And I think the kind of platonic ideal definition that you probably mostly subscribe to is that a faithful interpretation or latent is one that accurately represents the reasoning process behind the model's prediction.

[1:36] I think yeah, it's pretty pretty straightforward. So, this is going to require some audience participation, which is fun. So, um so here's an example. So, I'm going to ask my model, you know, what color should I paint my room? The true reasoning behind the model, like if you had an oracle I could tell you that is most rooms are orange, so let's say orange. So, now this is the latent you observe. Raise your hand if you think it's faithful. It reads most rooms are orange, so let's say orange. Yeah, cool. So, yeah, it is. It's exactly the same thing. By definition, it exactly represents the reasoning. Cool. How about this? Sorry for those of you who can't see it clearly. Yeah, cool. Okay, so a lot of people here speak a little bit of French.

[2:26] That's awesome. Still faithful. It reads the exact same thing. It's just in French. How about this? Okay, we had one Yeah, one or two tentative hands. Probably you've read a lot of rot 13 on the internet, and this is the same thing just in rot 13. So, by definition, it is faithful. But, for some reason like you thought it wasn't, and it wasn't that useful to you to understand what the model's true reasoning was. And so, maybe faithfulness is not the thing that we should be caring about. Um and so, this is where our definition of monitorability comes from. Uh we define everything with respect to a particular property V we want to predict with a monitor M. A latent Z is monitorable with respect to property V and a monitor M if M can accurately predict that property from the latent. Pretty straightforward like classification. Can you predict the thing?

[3:19] Um there are failure modes of monitorability. Um the first one is uh pretty close to faithlessness. So, information required to predict that property is not in the latent. So, you just can't predict it. Pretty straightforward. Um however, we kind of that was what we originally thought, but actually it's that information required for the monitor M to predict that property is not present. And so, this means like if I know that 2 + 2 is 4, and the model knows that 2 + 2 is 4, the model does not have to state that 2 + 2 is 4 for us to like kind of like follow each other's reasoning. And so there is you actually do not Well, say in a sec, but the other the other failure mode is like illegibility. You just can't understand it. That's the ROT13 example. But what that first part like says is that you actually do not need complete faithfulness to have a monitorable setup. And so this is why I open AI or at least my team, we kind of like more concern ourselves with monitorability because again, you don't need this incompleteness. Though we do it is still a good thing to like focus on and aim for it because obviously if you have complete faithfulness you and legibility you should have monitorability.

[4:28] Um this monitorability could be fragile. I think a lot of you know, this is it's a thing to worry about. It could go away for a lot of reasons. Um we recently um to be able to because of we think it's fragile, we wanted to be able to track it, preserve it, maybe improve it. We made some evals to start looking at this. It's just a starting point. Um there's kind of like I would say yeah, the they're they're they're a great way to at least give a comparison against the current models we have, but we would like to put a lot more effort into them. And um yeah, so we hope that, you know, you guys also care about monitorability and you can start using these and we're going to open source them soon, but we hope that you, you know, build on them, contribute to them, and yeah. Hopefully we end up with a untrusted or trusted monitoring future.

[5:18] Uh I hopefully trusted. Yeah.
