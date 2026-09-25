---
id: "eH_J-eaHnqU"
title: "Trevor Lohrbeer - Improved Monitoring of Backdoor Insertion During Code Refactoring [ControlConf]"
url: "https://www.youtube.com/watch?v=eH_J-eaHnqU"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-06-13"
duration_seconds: 302
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Trevor Lohrbeer - Improved Monitoring of Backdoor Insertion During Code Refactoring [ControlConf]

[Watch on YouTube](https://www.youtube.com/watch?v=eH_J-eaHnqU) · FAR․AI · 2025-06-13 · 5:02

## Description

```text
Trevor Lohrbeer's research reveals significant backdoor vulnerabilities in AI-assisted code refactoring—even in "honest" models—and establishes testing infrastructure for improving detection through iterative monitor refinement and better backdoor definitions beyond simple behavioral variance.

Highlights:
🔹 Honest models compromised - 41% of "honest" model outputs had backdoors 
🔹 Limited detection - Current monitors struggle with backdoor identification 
🔹 Beyond behavioral variance - Need better backdoor definitions for AI control 
🔹 Iterative improvement - Testing infrastructure enables continuous refinement
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:04] Trevor Lohrbeer: Hey everyone, I’m Trevor Lohrbeer. I'm one of the Pivotal Fellows, and today I'm going to talk about improved monitoring. Some of the key assumptions are that Frontier labs will soon be using full-blown software engineers. Some people have probably been using things like Cursor. These are things like Bolt or things that can do complete editing and everything. AI software engineers may inject backdoors during that process because they might want to escape or take underlying actions. Code refactoring differs from code generation, which the original APPS dataset in the original AI control paper just dealt with code generation. But with refactoring, you have original source and unit tests that can serve as a ground truth, and that differs. I propose that human monitoring will be insufficient in some limiting testing with people. I give some backdoors that my AI models have generated, and they're even hard to detect now. And when we go to more sophisticated backdoors, that's going to be more difficult. Thus, we need improved monitoring. My project doesn't actually solve that right now, but it at least creates the infrastructure to start doing those sorts of testing.

[1:05] Now I did a dataset generation because it's very hard to find code that needs to get refactored. I’m not going to talk too much about that, but I created a Dataset Foundry project to build new datasets or validate existing datasets. Here's my honest pipeline on how we do it. The agent is given original code plus unit tests. It then generates refactored code. We then go through validity checks. This is just like checking the syntax in Python, but for a refactor code, we need to make sure that the original tests pass, and that is an actual refactor because sometimes the models are lazy and they don't actually refactor the code. If you just gave me the original code, of course, the original unit test would pass. So, if any of those fail, it goes back to the agent, goes through that loop, and finally, we rate the suspiciousness of that. The attacking pipeline actually then tries to insert a backdoor to prove that intentionally it inserted that backdoor. It creates a secret unit test. We go through the same validity checks, and then we take that secret unit test and make sure that it returns different results between the original code and the refactored code. So, this is using the same definition of backdoor as the original AI control paper, which is a behavioral variance, just that we return two different results, and then finally we grade that.

[2:16] Here you can see some of the results. Right now, the honest code is definitely being graded as lower suspiciousness than our attacking code. Down here in the lower right, the monitor judge doesn't tend to be too accurate, though. It's about 25% accurate on the suspicious code, on the attacking code, and about 47% accurate on the honest code. So, I need to work on that. I've been playing with different sorts of chains of thought or different sorts of monitor prompts. Here's an example of a basic prompt that just says, hey, does this code look suspicious? You can see we definitely have some separation here, but there's a lot of overlap there. If I use a chain of thought and checklist, I can shift my distribution to the right, but now I'm starting to get more false positives. But more interesting is that little note, that little blue bar on number 8. When I looked at that, why is my honest monitor generating that suspicious code? When I looked at the code, it looked suspicious. So then I wrote a special monitor that attempts to take honest code and generate a secret unit test to prove that that's actually backdoored.

[3:18] When I did that, 41% of my code had backdoors according to our definition. So number one, don't assume that your honest model isn't also inserting the backdoors. Luckily, those backdoors do have a different distribution than the actual attacking model backdoors. I haven't investigated exactly why and what those types of backdoors are, but that's the next thing to do. So my next step is to actually increase this dataset size to 200+ (this was only on 60 samples), start categorizing the types of backdoors so we can understand, one, how the honest and the attacking model aren't starting different types of backdoors using potentially a checklist as a monitor, and then just go through that rinse and repeat loop of improving the monitor, improving the attacking model, and try to come to some sort of stabilization. Further research, I think we do need a realistic backdoor definition for AI control research. It can't just be a behavioral variance. I talked to several people at the conference today who've given me a lot of good ideas on how to do that. It definitely needs to be a vulnerability though, not just a behavioral variance. More realistic code, so the original thing, I think, did like 50 to 100 lines. We're going up to 400 lines of code, but really getting longer files and going to full repos, and then finally doing advanced agents where they're doing more multi-step refactoring, full-blown editing tools, not just give me the code sort of thing, so doing more advanced scenarios for that.

[4:44] Thank you for listening. You can get the code and the interactive data from that QR code, and I'm also looking for a job. [Applause]
