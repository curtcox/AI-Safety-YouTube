---
id: "AGF95uS4Jh4"
title: "Johannes Gasteiger - Automated Researchers Can Subtly Sandbag [ControlConf]"
url: "https://www.youtube.com/watch?v=AGF95uS4Jh4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-05-24"
duration_seconds: 343
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Johannes Gasteiger - Automated Researchers Can Subtly Sandbag [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=AGF95uS4Jh4) · FAR․AI · 2025-05-24 · 5:43

## Chapters

- 0:00 Introduction
- 1:30 Setup
- 3:16 Improvements
- 4:37 Takeaway

## Description

```text
Johannes Gasteiger discusses research showing AI models can sandbag ML experiments without detection by zero-shot monitors, highlighting that while current models struggle with complex tasks, this capability requires vigilant monitoring.

Highlights:
🔹 Growing Risk - AI sandbagging capability increases with model sophistication
🔹 Manipulation - Weaker judges more vulnerable to misleading justifications
🔹 Integrity Check - Current risk limited by human oversight capabilities
🔹 Future Avenues - Outcome metrics can help identify sandbagging
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:03] Johannes Gasteiger: Thank you. In my research, I looked at the case where we use AI systems to automate research tasks. The motivation is that we already see that people are using AI systems to automate coding, and the logical next step is to automate larger and larger tasks in research. If an automated researcher were malicious, what could it try to achieve? It could try to slow down progress or mislead research by changing research decisions. This is, in particular, relevant if it targets alignment-relevant research, so if it tries to preserve the goals of the next generation, so like try to ensure that the next generation AI systems will have similar goals to itself and would specifically target alignment-relevant research. Then, of course, it will try not to get detected.

[1:01] We split this down into two specific experiments. One is for slowing down progress. We look at how good automated researchers are at sandbagging specific ML experiments. The second one is when it's trying to mislead research, how can it change and manipulate justifications to steer research decisions in one direction or another?

### Setup

[1:30] For sandbagging ML experiments, we have a setup where we use Claude in an agentic coding setup, so you can imagine this is similar to Claude Code where it has various tools and implements code and then runs the code. The task is to implement a solution to some ML tasks, so this could implement an ML model to achieve a high benchmark score or look at—or a question where it's like it might be true, it might be false, and then the approach is scored according to various rubrics. On the right, this is our first axis, so the task performance, the x-axis. Then the second thing is we always have a monitor. We use trusted monitoring, so we have a weak model monitoring like the previous generation. Our monitor is just zero-shot prompted, and the monitor sees the full transcript. It sees all the tool calls. It sees what code was written, etcetera.

[2:28] Modulo, we sometimes gave the attacker some secret affordances like having some secret reasoning or inserting some secret comments just to see, to project the capability a bit further. What we see on the right is that Claude 3.5 Sonnet isn't really able to do this if we prompted zero-shots, but 3.7 is already quite good at this. One important note is that we iterated much more on the sabotaging side than on the monitoring side. The reasoning being that essentially, the attacker should always be able to adapt to the monitor. We only iterated on the monitoring prompt a few times, whereas we iterated much more on the attacker, and that was actually pretty important to get it to work.

### Improvements

[3:17] We did a couple of improvements beyond zero-shot prompting. We can see here with a one-shot prompt, 3.5 is able to do this much more subtly. Claude 3 Sonnet isn't really able to detect that anymore. We see some distributional shift, but if you look at the actual ROC curves, it is actually not that—the ROC curves actually don't look great. 3.7 is actually able to do this very subtly, so it reduces the task performance from 3.7 to 3.5. Of course, you should note that it's starting from a higher point, so it might also have an easier time sandbagging. On the second topic, we only have some some preliminary results here, but we have a setup where we take the task solutions from the previous experiments, so take the code from this, and then have the attacker create a justification of why this solution is good. Then we have a judge comparing pairs of solutions with justifications, and then a judge needs to say which of these solutions would achieve a higher score.

[4:21] We see on the right that different judges, normally, they compare pretty similarly, but then if we sandbag the justification, we can make the the accuracy breakdown very significantly. The effect is stronger the weaker the judge is.

### Takeaway

[4:37] Okay, so takeaway. When prompted, current models can sandbag ML experiments and research decisions without being detected by zero-shot prompted monitors. Important note: everything here is prompting; we didn't fine tune. However, we still think that humans can recognize this often enough to say that this is sandbagging—not in all cases, but sufficiently often. We also don't think that models can currently target hard-to-oversee research sufficiently well. Usually, you have some outcome metric that you can then use to train away the sandbagging, and this is only dangerous if the model is able to not sandbag on the outcome-based task and only sandbag on the rubric score-based task. We don't think that models can really do this very well, so we don't yet think that it's dangerous, but we do think that this is something to track and that we should be very mindful of in the future.

[5:32] Thank you.
