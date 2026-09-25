---
id: "JfDlbzF6rsY"
title: "Evan Hubinger – Alignment Stress-Testing at Anthropic [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=JfDlbzF6rsY"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-18"
duration_seconds: 326
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Evan Hubinger – Alignment Stress-Testing at Anthropic [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=JfDlbzF6rsY) · FAR․AI · 2024-12-18 · 5:26

## Description

```text
“We purposely build or discover situations where models might be behaving in misaligned ways”

Evan Hubinger shares “Alignment Stress-Testing at @Anthropic,” focusing on two main roles: conducting internal reviews under the Responsible Scaling Policy and using “model organisms” to test AI misalignment risks. These model AIs act as test cases for detecting safety gaps, either validating alignment approaches or exposing real-world risks for proactive intervention.

Highlights: 
🔹 Responsible Scaling Policy - Framework for internal model reviews to mitigate risk. 
🔹 Model Organisms - Testing AI in controlled misaligned scenarios to examine potential failures. 
🔹 Misalignment Studies - Example: sleeper agents simulating deceptive behavior against safeguards. 
🔹 Real-World Risk Evidence - Model organisms provide concrete risk cases to guide safety measures.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] I am going to be talking about the Alignment Stress Testing team at Anthropic, which is the team that I lead. The people on the team are here, some of whom are here today, like Johannes. So what do we do? First, I want to talk a little bit about Anthropic's new RSP. Recently, you might have seen that Anthropic released an updated version of our Responsible Scaling Policy. The Responsible Scaling Policy is our set of voluntary commitments that we have that detail our procedures and responsibilities for mitigating catastrophic risks. One of the responsibilities in our new updated Responsible Scaling Policy is an internal review mandate. You can take a look at what it says here, this is from the updated RSP, but it says that, for each “capabilities and safeguards” report, which is what we do whenever we run new evaluations, we build a capabilities report, and whenever we have mitigations that we need to put in place, based on those capabilities, we produce a safeguards report.

[0:56] And so the RSP commits us to solicit feedback from internal teams with visibility into these processes to try to inform our final decisions made by the CEO and the RSO, the Responsible Scaling Officer, about what to do with sort of new model releases, scaling, and deployment. One of my core responsibilities and one of our team's core responsibilities is implementing this RSP mandated internal review. So we are responsible for taking all of our capabilities reports, our safeguard reports, and effectively serving as what we call a ‘second line of defense’. There is a first line of defense, which is that we have the people running these evaluations, building our mitigations and trying to make them safe and sufficient. And then we are a second line of defense that looks at the work that we are doing, and then looks for holes. And so we try to point out any potential problems and make sure that we're surfacing, and have opinions on what might go wrong. Okay, this is one big part of what we do.

[1:52] If you have questions, concerns about Anthropic safety practices, I'm the person to talk to, come, discuss them with me. I'm very happy to. Okay. But that's only actually one part of what we do. The other thing that we do is we do research. So we're also a safety research team. And in particular, we have a particularly interesting focus, which is we focus on model organisms research. So this is a bit of a weird term. This is actually borrowed from biology. If you look up, what is a model organism, in biological research, a model organism is a non-human species that is studied to try to understand particular biological phenomena with the idea that studies in the example organism will actually help inform you in other cases. What does this look like in biological research? It looks like doing mouse studies, trying to build in a lab examples of the disease that you're studying and then trying to understand it. And what this looks like for us in our situation is we try to study model organisms of misalignment.

[2:52] So we purposely build or discover situations where models might be behaving in misaligned ways, or could be trained to behave in misaligned ways, and we study that and we try to understand how bad it would be, how you might deal with it, and what the implications would be. So this is maybe a bit of a weird connection to the thing I was just talking about previously. So how does this connect to our overall mandate? I think of the model organisms research as mattering in two different possible worlds. The first world is a world where we figure out how to effectively build safety cases for very advanced AI systems, in which case model organisms serve as test cases, right? If you have some argument - something like a mitigations report - that we think an AI is safe, then having a bunch of examples of situations where things might be unsafe, or might go wrong, gives you test cases to evaluate whether that is actually sufficient.

[3:44] But there's also worlds where we don't yet actually figure out a way to build a really effective safety case for powerful advanced systems. And in that world, model organisms are also useful as a way to demonstrate risk. We need to actually be able to make the case for why these things are scary, and it's worth pausing or taking some other drastic action. And so we need concrete evidence and examples of what the actual risk looks like. Very briefly, I'll talk a little bit about some prior work. Something that you might have seen from us is the “sleeper agents” work, where we built some models that actually had dangerous backdoors, where they would insert dangerous vulnerabilities into code in particular situations, when they thought they were in the next year. And they had a chain of thoughts where they would do deceptive reasoning about how to fool their training process. And we found that for these models, they were resistant to training. So you could try to train them to be HHH (helpful, honest, and harmless). But in fact, if you tried to do this - for the models that we produced - it was ineffective. This is demonstrating that if a model were to end up in a situation where we're doing something deceptive and dangerous relative to the training process, we wouldn't necessarily currently have the tools to deal with this.

[4:53] And I'll give you a little bit of a sneak preview for some of our future work, where you can see in this situation, which I'm not gonna tell you exactly what this situation is, but in this situation, you can see Claude will, a substantial fraction of the time, decide that it wants to exfiltrate its own weights, and this even goes up with RL. Maybe someday, hopefully in the next month, you'll find out exactly what's going on here.
