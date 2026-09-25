---
id: "eO7RWlUl1BE"
title: "Sam Bowman - Lessons Learned from the First Misalignment Safety Case [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=eO7RWlUl1BE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-12-12"
duration_seconds: 590
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sam Bowman - Lessons Learned from the First Misalignment Safety Case [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=eO7RWlUl1BE) · FAR․AI · 2025-12-12 · 9:50

## Chapters

- 0:00 Introduction to risk report
- 1:35 Validation and methodology
- 2:59 Evaluating safety pillars
- 5:07 Defining threat pathways
- 6:35 Key takeaways and learnings

## Description

```text
Sam Bowman discusses Anthropic's pilot sabotage risk report for Claude Opus 4, the first safety case from a frontier lab addressing canonical misalignment risk. The six-month analysis required gathering information from hundreds of people and produced a 60-page report identifying 9 representative pathways to catastrophic harm. The study revealed that current models can already "do a lot of quite scary things" without monitoring, while the traditional three-pillar safety approach (capability, alignment, control) proves inadequate for today's models. Working with real deployments exposed critical constraints that hypothetical exercises missed. Anthropic has committed to producing similar risk reports for all future frontier-advancing models.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to risk report

[0:00] We recently published our pilot sabotage risk report. I referred to this in the title of the talk as our first attempt at a misalignment safety case. What is this? To be clear, this is the first example of anything from a frontier lab that I think could be reasonably described as a safety case covering canonical loss of control flavored misalignment risk. Why are we calling it a sabotage risk report? We're using sabotage to narrow in on the kinds of misalignment threat models that tend to get talked about most at events like this. In contrast to things like sycophancy, which very clearly involves misalignment but tends to require a fairly different set of evaluation mitigations, or CBRN misuse, which often involves misalignment in some respects but again calls for pretty different mitigations. So this is narrowing the scope.

[1:02] Why are we calling this a risk report? In AI safety, people will use the phrase safety case fairly loosely, but in a lot of related fields, it tends to mean something where you've got really rigorous methods for assessment grounded by decades of experience with frequency statistics. AI safety is not there yet. I would like for us to get there, but we are not at the level of rigor and assurance that safety case often implies for people. So we're using this somewhat weaker term.

### Validation and methodology

[1:35] As part of the assessment, we put out this report. It's basically a 60-page document on why we think the risk of catastrophic outcomes from sabotage owing from the deployment of Claude Opus 4 is very low. We also accompanied it with a couple of companion reports. We had an independent team at Anthropic, our alignment stress testing team, which had access to all the same information, go in and fact check everything and do their own independent analysis of a lot of the results, basically writing a critique. They disagreed on some of our framings but agreed with the conclusion. We also gave METR, as independent nonprofit with no financial relationship, access to an extended unredacted version of the risk report and gave them the ability to ask for information directly from many parts of the company. And they additionally wrote their own fact check and review. Again disagreeing on some details but agreeing on the conclusion that we've shown risk is very low.

[2:40] This is also not just an academic research team exercise anymore. As of a week ago, we committed that we will be putting together risk reports like this for all future frontier advancing models. So we are starting to work on our next iteration of this kind of report.

### Evaluating safety pillars

[2:59] Before I say what we actually say in the report, I want to say what we thought we were going to say at the beginning and didn't wind up saying. This is an idea that comes up in spaces like this a lot when you talk about safety cases. And this idea that we'd been interested in, we'd written about in the past, that I think currently is not that workable. The idea is that you will make effectively three separate arguments for safety based on three largely independent pillars. That you'll use evidence about capability to argue that the model is not smart enough to commit catastrophic sabotage. You use evidence from alignment evaluations, maybe including things like interpretability and scalable oversight, to show that the model doesn't intend to commit catastrophic sabotage and that we think that it will likely never intentionally commit catastrophic sabotage. And the idea goes, we'd separately write about control. We'd say even if the model were to try to commit catastrophic sabotage, we would notice and intervene before anything too bad happens. In practice, this doesn't quite work, at least with current models.

[4:02] This capability argument is just getting pretty dubious for simple forms of sabotage. If you assume there's no monitoring, if you assume there's no one really going out of their way to stop the model, models can just do a lot of quite scary things. They're smart enough to cause a decent amount of harm. On misalignment, I think this argument almost works with current models. I am pretty convinced that they don't have any lurking, latent malign intentions that are just waiting to come out at any moment. That said, I don't think we are really able to rule out rare failures where something contextually throws the model off of its normal persona. You wind up with a misaligned model in one transcript, and that winds up directly or indirectly giving that new misaligned persona the opportunity to do some damage. So it's hard to make a really high assurance safety case this way. And then for control, I think we know what it would mean to do that. But I think neither us nor any of the frontier labs have all of the infrastructure in place that we would need to make this really compelling. The trade offs around privacy and infrastructure and response time are still fairly rough.

### Defining threat pathways

[5:07] So what did we actually say? We started, and this wound up being really important to making an argument that felt navigable, we started by laying out nine representative pathways to catastrophic harm. What is the critical action the model needs to do that ultimately leads to that outcome? And we wanted to come up with a representative list of these and show that we'd, in pretty good detail, ruled out each one. And these include things like sabotaging safety-relevant R&D, like tampering with the results of experiments or self-exfiltration, the model stealing its own weights, or sabotaging decision making in government. These are usually not the ultimate catastrophic outcome, but the key first action the model takes that ultimately leads to some severe loss of control type scenario. So we laid those out. We then just figured out, what evidence do we have that bears on how worried we should be about these? And we just laid out a bunch of claims. We tried to loosely organize these, but we end up making a few dozen little claims rather than three big ones and just tried to defend a bunch of points about, all right, we found the alignment is like this. We found that this kind of monitoring mechanism should kick in in these scenarios and prevent these risks.

[6:16] And then having enumerated a bunch of considerations, we wrote out for each of our nine pathways a couple pages of argumentation of how the evidence that we found fits together into an argument that the risk from that pathway turned out to be low.

### Key takeaways and learnings

[6:37] What did we learn from doing this? If you're interested in this, I encourage you to read the report. But some high level takeaways about this kind of work. Working with real deployment draws out a lot of important constraints. We've been working on misalignment safety cases for more than two years and we've done a couple of exercises where we prepared a detailed safety case for a hypothetical future model. But I think just actually having to work with current models, figuring out exactly what security infrastructure do we have in place, exactly what interpretability evidence is on the short term horizon or not, what do we have now, really changed our focus quite dramatically in a way that I think was quite useful and makes this a more generalizable exercise than the more speculative stuff we've been doing. This also is obviously just a really great source of roadmaps for future mitigations and I'd love to see other developers do something similar, if only for that reason. This just made it very clear, oh, this interpretability method that we hadn't been prioritizing could actually make this part of the safety case much stronger. Or this security, this file permissions issue that no one had been tracking winds up being load bearing in 2 or 3 of the threat pathways. We should intervene on that.

[7:49] Most of the work that we spent the last several months on was information gathering. Just asking, okay, if the model does this weird thing, who would see the behavior? Who would they tell? Or what automated monitoring systems would tell the people who are ultimately responsible, how quickly would they respond? Are they getting paged? What happens automatically? Just running through what happens in lots of scenarios just takes a lot of time and requires talking to hundreds of people. And then secondarily some amount of just arguing about threat models. Just our list of these nine threat pathways we had to keep refining and refining until we got something where we felt reasonably confident saying that if we'd ruled out those, we ruled out sabotage risk more broadly. External review was tricky to set up. I think just figuring out, how do we get a third party organization to have enough access to information that it's able to meaningfully comment on the work? Just figuring out what they should ask for and how and what files were shared where and what kind of responses to ask for took a few iterations, but I think we ultimately landed in a good place and I think we're able to get what feels like a serious, independent, engaged assessment. We're going to keep working with METR on this. I'd encourage others to do the same.

[9:02] And then finally, just this all takes time. We had already had several work streams on misalignment safety cases, and doing this for the first time took about six months. Claude Opus 4 came out in May and we only a few weeks ago released the corresponding risk report for it. We would like to be able to get much faster. I think it should be feasible to get faster, starting from all the work we did for Opus 4. But for those of you working on related things at other developers, it's worth starting very early if you think this is something you will want to do a good job of in a year or two. I think it's worth trying to do an okay job now. And that's all I got. Thank you.
