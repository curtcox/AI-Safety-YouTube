---
id: "AKBoCCeNkHI"
title: "Maja Trębacz - Scalable Oversight: A Practical Approach to Verifying Code at Scale [Alignment Works"
url: "https://www.youtube.com/watch?v=AKBoCCeNkHI"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-12-12"
duration_seconds: 617
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Maja Trębacz - Scalable Oversight: A Practical Approach to Verifying Code at Scale [Alignment Works

[Watch on YouTube](https://www.youtube.com/watch?v=AKBoCCeNkHI) · FAR․AI · 2025-12-12 · 10:17

## Chapters

- 0:00 The challenge of oversight
- 1:20 Oversight methods and stacks
- 2:51 Code review as a monitor
- 4:44 Improving review performance
- 6:50 Real-world deployment results
- 8:38 Risks and final reflections

## Description

```text
Maja Trębacz presents OpenAI's AI-assisted code review system deployed on 100% of internal pull requests, achieving 80% positive reactions while revealing new risks like developer over-reliance and potential model gaming of verification checks.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### The challenge of oversight

[0:00] I'm going to talk about scalable oversight in practice, specifically focusing on the method of verifying code via code review. When I talk about scalable oversight, I mean how to make sure that our ability as humans to verify code grows as quickly as AI's capability to produce code. And if we don't meet that, we reach this zone that I like to call the oh no zone, where we actually don't have reliable control. Coding assists put us in that zone because the volume and the capabilities of code that are produced by the agentic systems is growing exponentially and human attention is not necessarily growing as fast. So we are reaching the various risk zones when the most obvious risk are just coding model, introducing errors and causing severe incidents, either accidentally or on purpose. But even more scary subtle mode is where we produce so much code that we stop understanding what is actually happening and opening up more and more surface area for more subtle failures that become undetected.

### Oversight methods and stacks

[1:20] So could we effectively use AI systems to assist supervisions of other AI systems? That's the hope. There are a lot of examples of that happening across monitoring, control, assisting human verification. And the tricky part here is to make sure that we leverage human oversight rather than shift it around and just introduce new failure modes happening. An important thing to know is that oversight wouldn't be just one solution. It needs to be a stack of methods. It needs to be an ensemble of monitors. There are of course a lot of things you can do at training time with extra affordances that you have during the training time. But speaking concretely, on deployment we can think of oversight happening on various moments of agents actions. So you could have oversight happening before the actual action takes place. You can monitor the chain-of-thought. You can also monitor internal activations.

[2:18] You can do things just as the action is about to take place by using another monitors for action monitoring or having extra sandboxing and security policy checks. And you could also monitor actual outputs and outcomes before they become part of integrated big system. So here I will focus specifically on the code review. But you could also verify models, supplied citations and proofs. You could do extra behavioral testing or monitor user reactions.

### Code review as a monitor

[2:53] So code review is a natural output monitor because it already is established routine that developers use and trust. And you can use it in practice rather than try to force them to introduce a completely new safety paradigm. So it's easier to deploy. But it also means that we need to meet the usability bar in order for it to actually be used because developers have specific expectations about signal to noise ratio. And you could have this kind of definition that is utility based, that whenever you produce a comment you want to make sure that its benefits defined as the saved costs of potential consequences of introducing an issue are better than cost of the verification and also cost of potential consequences of making an incorrect claim.

[3:47] There are a couple of other requirements to keep in mind when deploying a system like code review. So apart from the signal to noise ratio that needs to be high, the system needs to understand how it fits in the broader codebase and actual developer intentions. It should be complementary rather than redundant with respect to existing continuous integration tools and static analysis tools. And it should be steerable at the test time. That is various parts, various code bases, various packages require different scrutiny levels and pose different risk levels. And also we should respond to specific guidelines and custom user instructions required by the developers. Additionally, we need to make sure that the way we train the system is agnostic towards whether the code comes from a human or from an AI agent,

### Improving review performance

[4:44] because otherwise it wouldn't scale as more and more code is becoming produced by agents. Speaking of steerability, the most basic knob that we want to be able to turn is how many issues to actually output by the system. So if you take GPT-5 and you tell it to output all possible issues that it can find in a specific code change, it will output you a lot. So you would get high recall, but you would sacrifice a lot of your precision. You could also instruct it to focus only on the most specific important issues, the serious bugs that you're sure that the developer would apply. And then you will get higher precision, but you will sacrifice your recall. If you want to further improve the reviewer, you could add it extra, you could give it extra context. So in practice we observe that it's very important to give an access to the full repository in order to improve the performance as well as using the tools. Of course there's always context that is going to be missing. You will not have access to specific developer intentions. You will not have access often to the full environment. So the reviewer still needs to make some calculated guesses.

[6:06] And we can also do further training in order to make sure that it's really highlighting the issues that someone would like to have fixed and prevented happening in practice. So with the extra training combined with the Codex training, we actually could reach much higher precision than the base GPT-5 model. But now how to actually make sure that the model is useful in practice given that our evaluation is imperfect? In fact, even despite that we hired very experienced software engineers to do this evaluation, it's still very hard to assess whether a code review comment is correct or not when it's

### Real-world deployment results

[6:51] not really your code and you're not the one that is responsible for maintaining the system. So if we want to make sure that it actually works in practice, we should deploy it. And we started with pilot within our team, then extended it to the whole OpenAI and also reduced it externally. Nowadays, 100% of the PRs published within OpenAI internal repositories are reviewed by our code review model. And we do see very high positive reaction rates. And to be fair, only after deploying it, I fully appreciated the complexity and difficulty of verifying a code review comment, as in multiple times in my old code, I had a situation where initially I thought that the comment is wrong. And only after really going deep for one hour, I discovered that actually Codex was right and I was the fool.

[7:51] So seeing that working in practice, we see that here static benchmarks will not be enough. We actually need that extra signal from it being applied in practice. And it allows us opportunities of being able to measure how many issues still remained unavoided, how many comments have positive reactions, how many comments are actually resulting on a person making an actual code change rather than just ignoring them or deciding to triage it later. And it gives us opportunity to build a continuous evaluation loop as well as give extra training signals for recursive reward modeling. But of course there are anticipated risks with

### Risks and final reflections

[8:38] that approach. One thing that we already start seeing in practice is people becoming reliant on the code review as a verification mechanism. So people could assume that if they give thumbs up that the code is safe to deploy. And of course that's not a perfect guarantee. So there's a risk of removing human skepticism that still is an important thing to be present in the codebase. We do monitor how often the issues remain unavoided, which is a proxy measure for how big of a problem it is. And it's not that prominent now. But we need to keep monitoring it. We also face the risk of models potentially gaming the monitors, that is specifically writing the code in a way that avoids being caught by the code review models.

[9:30] And here I want to note that the code reviewer and the code generator that we use are actually part of the same model. It's like they are both part of the Codex. So that poses the risk of models avoiding the code reviewer by default. And we do try to evaluate that we're still becoming effective mechanism during that schema. And by relying on some metrics that come in practice we could be over biasing towards what we can measure, versus what really matters and what would be the worst case scenarios. So I'd like to finish by mentioning that oversight is useful to apply in practice and please check it out with actually trying it on your code.
