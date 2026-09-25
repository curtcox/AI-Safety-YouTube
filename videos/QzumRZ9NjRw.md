---
id: "QzumRZ9NjRw"
title: "Julian Michael – Empirical Progress on Debate [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=QzumRZ9NjRw"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-12-13"
duration_seconds: 760
is_short: false
chapters: 8
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Julian Michael – Empirical Progress on Debate [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=QzumRZ9NjRw) · FAR․AI · 2024-12-13 · 12:40

## Chapters

- 0:00 Introduction to AI debate
- 1:09 Sandwiching evaluation
- 2:23 Empirical debate results
- 3:54 Optimization and calibration
- 5:00 Challenges in current research
- 6:27 Limitations of alignment
- 7:14 Specification sandwiching
- 10:18 Q&A and future outlook

## Description

```text
Julian Michael from NYU presents “Empirical Progress on Debate,” examining how debate-based oversight could guide AI to produce reliable insights in complex tasks, even when human expertise is limited. With promising improvements in human calibration, Michael introduces “specification sandwiching” to enhance AI alignment with human intent, while reducing risks of manipulation.

Highlights:
🔹 Scalable Oversight – Debate-based protocols show potential for reliable AI judgments in complex, high-stakes tasks. 
🔹 Improved Calibration – Early results indicate debate helps humans better judge AI responses. 
🔹 Managing Manipulation – Progress requires further research to prevent persuasive rather than truthful responses. 
🔹 Specification Sandwiching – Proposes a method to help refine user intent and alignment while guarding against manipulation.

The Alignment Workshop is a series of events convening top ML researchers from industry and academia, along with experts in the government and nonprofit sectors, to discuss and debate topics related to AI alignment. The goal is to enable researchers and policymakers to better understand potential risks from advanced AI, and strategies for solving them. 

If you are interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://far.ai/futures-eoi

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
#AlignmentWorkshop
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to AI debate

[0:00] I'm gonna be talking about some work on debate and what I feel is missing and exciting for our next steps. We're interested in scalable oversight. This is the problem of: how do I provide a good feedback signal to incentivize an AI system to do something that I'm not capable of doing myself or a behavior that I'm not capable of checking the correctness of myself. You ask some AI a very difficult question that requires them to write some big report on public policy or scientific experimentation. It's very hard for us to provide a good feedback signal to make this report better, make sure it's correct if we don't understand the science, if we don't understand the implications. So you need to get AI's help to help you do this better. Debate is an approach for this, which there's been a fair bit of empirical work on now. The essential idea is you get copies of the AI, train them to argue for yes/no positions on any answer – or for alternative answers – and they should bring up all of the relevant best arguments that should help you decide, ideally, in a calibrated way, which answer to prefer.

[1:00] So our goals here are to amplify human ability, and that the human judge is calibrated enough to be able to avoid costly mistakes in cases where we'd otherwise not be able to judge. Now one of

### Sandwiching evaluation

[1:09] the challenges of measuring progress on this is that ideally we want to know that we're doing a better job on things where we don't even know what it means to do a better job on. So how do you actually evaluate this experimentally? The dominant paradigm for this is sandwiching. The basic idea is, instead of trying to elevate humans to a superhuman level, you see whether you can elevate non-expert humans to expert performance. Or, in particular, if you have a non-expert and an AI, and you have some oversight protocol – like debate, for example – that the non-expert uses to supervise the AI… does optimizing that bring you up to expert performance? If you have this result, then this is evidence that – if you were to use the oversight protocol with the expert – you could get reliable, correct superhuman performance. Now, it's actually quite difficult to come up with repeatable test settings for this kind of thing, so a common kind of proxy setting is reading comprehension with long text. So we have short stories like 5,000 to 8,000 words where we use a blind judge who doesn't have access to the story as the non-expert and then someone who has read the story as the expert.

[2:11] The hope is that a judge who's blind to the story can judge a debate and get expert level performance. What does progress look like? If we want to know that debate is working, we should test it against a baseline. The main protocol is debate. You have

### Empirical debate results

[2:26] the two debaters. They can draw certified quotes from the story, so you get some ground truth, and the baseline is 50 percent if you were to just guess. The alternative, which is the stand in for RLHF, we call consultancy, where you have a 50/50 chance of arguing for the correct or wrong answer. So again, a 50 percent accuracy baseline. And then the question is, if you have a judge who's blind to the story, judging in each of these cases, do they do better in debate? So we ran human experiments with competitive debaters. We actually hired half of the NYU debate team to do this. And we found that debate did significantly better than consultancy. This is evidence that when you get pretty strong debaters – once the models are strong enough for this to matter – we really should be using debate for hard tasks. Of course, it's only on one domain and I'll get to that later as a caveat. But we also found that the judges were more calibrated in debate.

[3:16] So that's a step in the right direction. And this was the first result that introduced the consultancy baseline as a way of measuring progress on debate as an empirical method for scalable oversight. This February, Akbir Khan, Dan Valentine, and John Hughes got the ICML Best Paper for running similar kinds of tests with AIs, where they managed to get frontier models with appropriate prompting to do debate and persuasion in the context of consultancy really well. They saw the same result:L that debate does better under human judgment, and that human judges are reasonably calibrated, at least they're not overconfident. So this is lots of nice positive evidence for debate in some settings. They also did some really nice studies,

### Optimization and calibration

[3:54] which are exactly what we want to see with scalable oversight: Where, as you optimize the objective, truthfulness gets better. This graph here is basically, on the x-axis, you have the strength of the debaters, and on the y-axis, you have the accuracy of the judge. And as the debaters get better at winning, the judge gets better at finding the truth. That's evidence that if we keep optimizing the stronger AI, we'll be in good shape. And in consultancy, they found the opposite trend, but there's a slight issue here, which is that their AI judge was way too exploitable by consultancy. It basically believed the AI that was arguing, like, 90 percent of the time. So now in follow-up work that we put out this September, we trained a calibrated judge and we actually fine-tuned Lama to debate. And we found that this result still held. So debate was the only oversight protocol that had a significant positive result, where as you make the debater stronger the judge accuracy gets better, and we even introduce some extra consultancy baselines, which I don't have time to get into, but you can check out the paper. Samuel Arnesen led that one. It's called Training Language Models to Win Debates with Self-Play Improves Judge Accuracy.

### Challenges in current research

[5:00] Okay, so what are the caveats? What are the gaps? There was some work by DeepMind, also studying debate. They tried a bunch of other tasks, including closed book tasks like GPQA, MMLU, where you were trying to judge with a weaker language model as a judge. They didn't get positive results for debate, which is a little bit disappointing. There were some very preliminary results on MMLU from Charlie George from Elicit on this, but we really need more evidence and we're also still quite far from what we really want, which is training models to be robustly truthful. What we have right now is basically that the supervisor can get higher accuracy, but what we want is that you can train the models to get higher accuracy. What we've found through all these studies is that models aren't really that great at judging and debating. So you probably need a lot of humans in the loop, a lot of feedback to make this work. I expect that you need the kind of investment that the RLHF pipelines have at this point. You need to put that same investment into debate if you would expect to be able to get a competitive result.

[5:58] And there's also some challenges in how exactly you know how to choose between two wrong answers in a way that pushes the model in the right direction; that's a little bit underexplored. I expect this to be doable, but it might require a lot more human and compute resources so it might be most doable by places with a lot of those resources. It's tricky to derisk debate on this front, but it's clear that there's a problem to solve, because as Micah was talking about, it's well documented that RLHF can incentivize misleading evaluators; can incentivize manipulation and stuff that we don't want.

### Limitations of alignment

[6:29] Okay, so I think there's a path forward. But what I'm really interested in is what happens when we solve debate? Does that solve alignment? Sometimes you hear this argument that debate is a method for truthfulness, and truthfulness is alignment-complete because if the model tells the truth, you can just ask what's the right thing to do and then it'll tell you the answer. I think this is a motte and bailey. I don't buy this argument. So basically you're saying, okay, my defensible claim is that scalable oversight will converge on any conclusion that a sufficiently dedicated and thoughtful human would come to. So you say, “Okay, so it's truthful, which means that the model will truthfully answer morally or value-laden questions like what's the right thing for me to do.” And I don't think it holds, cause I don't think we have oversight signal for that kind of thing. We don't actually know how to do supervision of intent alignment. So you have a principal

### Specification sandwiching

[7:18] and agent. The principal wants the agent to do something. So there's what you say, the agent acts, you use an oversight protocol, and then you have a third party overseer. Look at this, and they can give an instruction following reward. So this is what RLHF looks like a lot of the time. But this isn't intent alignment, because the principal has some idea of what they want, which might be different from what they say. And the overseer doesn't have access to this. There's this specification gap, which you need to be able to bridge. So we don't know how to handle cases where you have a misspecification. You could say, okay, let's bring the principal in, let's just have principals in the training loop, they give feedback, and then you get a preference matching reward that's helped out by the scalable oversight protocol. There are a bunch of problems with this. First of all, scalable oversight protocol relies on an understanding of the principal’s values in order to know what arguments are relevant to bring up in the debate. Principals differ. Different principals are going to value different things. So you can't have a single universal debater handle all principals.

[8:15] Another problem is that in order to make this scale; you need an AI model of the overseer. That makes a lot of sense if you have a global norm for the overseer, like epistemic norms; we can come up with reasonable global epistemic norms for truthfulness. But for principals who have different needs, now you have to represent a distribution of principals and you're going to suffer from distribution shift problems in deployment time. But the biggest problem is that: what you think you want is often not what you want. And if you've ever written code, you probably know this, right? But also you might be manipulated into a situation that you don't actually want. And so there's another gap, the idealization gap, which we actually have no idea how to bridge, right? Ideally we would get oversight from an ideal self, but that simply doesn't exist. We can't get this idealized preference matching reward. What can we do here? I have some thoughts on what an experimental structure might look like. I call it Specification Sandwiching. Basic idea is you start with a principal who is naive, right?

[9:12] They can essentially judge their immediate preferences, which may not be the ideal version of their preferences. Now, they can then provide a specification of what they want, which then also might fall short of those preferences. But if you bring another AI into the picture and have a reflection protocol that helps them understand what they actually want and how to say it, then, ideally, the principal can come to a better understanding of what they want and also improve the specification to match that under a scalable oversight regime. So now, you've improved the principal and their understanding of what they want and you've aligned an AI to this understanding. Now, this is not easy to do, and there are a lot of open questions on how to do this well. So it's going to require normative hypotheses around preference changing and manipulation: what actually are good and reasonable and justifiable things to do in this reflection process; what constitutes manipulation; what constitutes edification… and we're going to have to develop technical methods to protect against manipulation in these cases, and technical methods to actually implement idealization and processes that help us become better people rather than worse people, so

### Q&A and future outlook

[10:18] I'm really excited about working on this if this sounds interesting to you please come talk to me. I would love to find collaborators, and I would also love to red-team these ideas further. Thanks. Q: Awesome. Hannah asks: do you worry that incentivizing a good debater simultaneously incentivizes models to be persuasive or to be unduly manipulative of beliefs of their users? Kind of what you touched on in the end. Could you expand on that? A: Yeah. So I think this is a pretty common worry, that if you incentivize a debater to try and win, you will be incentivizing the debater to lie or manipulate. I think what we have to rely on is the other debater pointing out those issues. I think that you can also think about the norms of debate that are enforced at training time. For example the judge can only buy into arguments from debaters who are clearly working in good faith, at least, according to some kind of rules of engagement that they've set and that the opposing debater can help enforce. Yeah.

[11:28] How would you get ground truth labels for specification sandwiching? And how do you know the idealized specification is actually better? Yeah, so what you want is that the idealized specification is better by the lights of the principal when the process is done. So what you want is for the principal to be able to look back and say, oh wow, I was so mistaken at the beginning, and I have a much better idea now of what I actually wanted, and this new specification is better. Now you could say, maybe it's possible to manipulate a human into thinking that. And it definitely is but I think if you think that this is a problem that we can possibly make progress on, you have to think that it's possible for someone to say that and for them to get it right. And if we can circumscribe the circumstances in which that is possible and identify the cases in which they would be mistaken to say that, then what we want to do is constrain the process such that we avoid those undesirable outcomes.
