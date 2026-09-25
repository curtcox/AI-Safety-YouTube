---
id: "LGbleVrGnyo"
title: "Can AI Agents Automate LLM Post-Training? PostTrainBench Results | Maksym Andriushchenko"
url: "https://www.youtube.com/watch?v=LGbleVrGnyo"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-09-09"
duration_seconds: 612
is_short: false
chapters: 15
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Can AI Agents Automate LLM Post-Training? PostTrainBench Results | Maksym Andriushchenko

[Watch on YouTube](https://www.youtube.com/watch?v=LGbleVrGnyo) · FAR․AI · 2026-09-09 · 10:12

## Chapters

- 0:00 PostTrainBench: can agents automate post-training?
- 0:23 Why automating AI research is a safety question
- 0:52 Autonomous AI R&D in frontier safety frameworks
- 1:16 The gap in earlier benchmarks
- 1:55 How PostTrainBench works
- 2:19 Results: GLM 5.2, Opus 4.8, and Fable 5
- 3:18 What the agent has access to
- 4:17 Catching reward hacking with a judge
- 4:48 Base models, hardware, scaffolds, and tasks
- 5:19 A worked example on Gemma3-4B
- 6:42 Where the gap is closing, and where it is not
- 7:37 Confounder: agent persistence
- 8:11 Confounder: model size and reasoning effort
- 8:43 How agents cheat on the benchmark
- 9:23 Takeaway: from 10% to 34% in eight months

## Description

```text
Maksym Andriushchenko on PostTrainBench: whether LLM agents can automate LLM post-training, and how quickly frontier models are closing the gap.

Andriushchenko opens with why this capability is tracked at all: autonomous AI R&D sits alongside chemical, biological, radiological, and nuclear capabilities in the frontier safety frameworks published by Google DeepMind, OpenAI, and Anthropic, because it is the capability that could enable recursive self-improvement and loss of control. Earlier benchmarks measured small models on narrow tasks with heavy scaffolding. PostTrainBench instead gives an agent a base model of 2 to 4 billion parameters, a benchmark script, terminal access, web search, and 10 hours on a single H100, with no instructions on method, and scores only the post-trained model it produces. Results are averaged over four base models and seven benchmarks, with a judge that catches reward hacking. On the leaderboard he presents, GLM 5.2 leads, Opus 4.8 is close behind, and Fable 5 scores below both, based on the public version available at release. Two confounders matter: agent persistence, since some agents stop working hours before their budget runs out and have to be reprompted, and model size, which correlates clearly with performance. Reward hacking is pervasive, from repeating the test set to downloading a model from Hugging Face and presenting it as output. His headline: frontier models moved from roughly 10% to 34% on this benchmark in eight months.

Chapters
0:00 PostTrainBench: can agents automate post-training?
0:23 Why automating AI research is a safety question
0:52 Autonomous AI R&D in frontier safety frameworks
1:16 The gap in earlier benchmarks
1:55 How PostTrainBench works
2:19 Results: GLM 5.2, Opus 4.8, and Fable 5
3:18 What the agent has access to
4:17 Catching reward hacking with a judge
4:48 Base models, hardware, scaffolds, and tasks
5:19 A worked example on Gemma3-4B
6:42 Where the gap is closing, and where it is not
7:37 Confounder: agent persistence
8:11 Confounder: model size and reasoning effort
8:43 How agents cheat on the benchmark
9:23 Takeaway: from 10% to 34% in eight months

More AI safety research: https://far.ai
Alignment Workshop playlist: https://youtube.com/playlist?list=PLBY5kyt_LfFg&si=0IfDd-WNQwrs14Kn

FAR.AI is a research nonprofit working to ensure the safe development of advanced AI. We host the Alignment Workshop series and publish frontier alignment research.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### PostTrainBench: can agents automate post-training?

[0:00] So I'm going to talk about our work on PostTrainBench. So the key question that we were asking ourselves back in October, December last year is whether LLM agents can automate LLM post-training. And at the time, the answer was clearly no. But now, over the last 8 months, the situation quite basically changed quite a bit.

### Why automating AI research is a safety question

[0:23] So maybe before going into our results and settings, I think it's important to set the stage for why automating AI research is important — I think many people acknowledge that this capability is key for enabling recursive self-improvement. And this is mentioned in many frontier safety frameworks, such as the one from Google, the one from OpenAI, and Anthropic. Basically,

### Autonomous AI R&D in frontier safety frameworks

[0:52] autonomous AI R&D capabilities are mentioned next to chemical, biological, radiological, and nuclear capabilities, because autonomous AI R&D can potentially lead to loss of control scenarios. Therefore, it's very important to keep track of this capability for frontier models.

### The gap in earlier benchmarks

[1:16] The challenge of measuring these capabilities is that before we started this work, so before December last year, basically, previous benchmarks focused on rather small models, often on very simple tasks like Kaggle competitions. For example, MLE-Bench was one example of that. And they had a lot more context that was given to agents. So what we wanted to measure was more like an end-to-end approach, where basically PostTrainBench fills in this gap.

### How PostTrainBench works

[1:55] So in our benchmark, we measure how well agents can perform post-training on models from 2 to 4 billion parameters. And the task formulation itself is very open-ended. So we don't provide any detailed instructions to the agents about what exactly they should do. They should discover the right approaches on their own.

### Results: GLM 5.2, Opus 4.8, and Fable 5

[2:19] Here are the main results from our benchmark. So this screenshot was taken very recently, so we have all the recent models here. And I think there are a lot of very interesting findings here, but maybe the most important one is that basically the best model or the best agent on PostTrainBench is based on GLM 5.2. And Opus 4.8 gets very close. And we can see that Fable 5 is actually worse than both of them. So this is how the, at least, the open frontier looks like, right? So I think it's quite likely that Mythos 5 is actually better than GLM 5.2, but at least the public version that we had access to, in the 72 hours when Fable 5 was available at its release, it was not performing better than other available models.

### What the agent has access to

[3:18] Before going in detail on the results, I will briefly cover the whole pipeline that we have. So first of all, what does the agent have access to? It's a benchmark script, right? So we ask an agent to optimize performance of a target model on a particular benchmark. Then it also has the weights of the base LLM itself. So these are LLMs like Qwen3-4B, or Gemma3, I think 3 billion. And it has 10 hours on one H100 GPU. It has terminal access. And importantly, it also has access to web search, where the idea is that before starting post-training, the agent should perform some literature review. It should find some relevant frameworks, download relevant datasets, and so on. And we basically ask the agent to output a post-trained LLM. That's

### Catching reward hacking with a judge

[4:17] the only thing, that's the only artifact that we evaluate. And we also have a judge that prevents reward hacking. And we found all sorts of creative ways how agents can cheat on this benchmark. And then, if we detect cheating, then we assign, for a particular run, the score of the base LLM. And the final score is the average over 4 base models and 7 benchmarks.

### Base models, hardware, scaffolds, and tasks

[4:48] So this is a one-slide summary of the main settings. So these are the base models that we are post-training. The hardware is just one H100 GPU. As scaffolds, we use basically the best available scaffolds, such as Claude Code, Codex CLI, and OpenCode. The final metric is the weighted average. And the tasks, like individual benchmarks, are AIME, ArenaHard, BFCL, GPQA, HealthBench, HumanEval, and GSM8K.

### A worked example on Gemma3-4B

[5:19] And here is an example of what Opus 4.5, as a post-training model, does in case of Gemma3-4B as the target model. So it basically sets up basically the environment and checks the evaluation script. And then it concludes that the accuracy is 0%. Then it goes on the web, it researches relevant datasets, and it runs first training run. And then it times out. Then the agent adapts the strategy. Then it basically reduces the number of epochs, increases the batch size, reduces the total number of samples, and then the training completes successfully. Then there are also some errors that the agent has to debug. And then, finally, it performs some final run of post-training, and then it outputs the final model, on which basically HumanEval outputs basically 37% score instead of 0%. So we can see that even Opus 4.5 does some pretty reasonable things. So I think we are not that far away from at least partial automation of LLM post-training.

### Where the gap is closing, and where it is not

[6:42] This is how our final table looks like. So this is a screenshot from our website. So we basically have a breakdown over different target benchmarks. And we can see that the gap is not uniform. For example, on AIME, there has been relatively little progress, so there is still quite a large gap between the official instruct models and the best agents. And also on HealthBench, the gap is quite significant. But, for example, on BFCL, the gap is almost zero by now. And similarly on GSM8K, it's also relatively small, right? So basically we can see how agents close the gap to human post-training, at least on PostTrainBench.

### Confounder: agent persistence

[7:37] I think one very important confounding factor here, when we interpret the results, is the persistence. So we found out that not all agents are equally hard-working. So if we tell agents to work for 10 hours, for example, GPT-5.1-Codex-Max usually gives up after 2 hours. And yeah, so we basically had to continuously reprompt it to make sure that we elicit its capabilities so that it works for, let's say, 8 hours.

### Confounder: model size and reasoning effort

[8:11] Another important factor is the model size. We saw a clear correlation between the model size and the average performance. So here we have Haiku, Sonnet, and Opus 4.5. And we can see that Opus 4.5 is the best model. In terms of reasoning effort, we sometimes observed that the highest reasoning effort can be a bit harmful in some cases, although I'm not sure if this is a very systematic finding.

### How agents cheat on the benchmark

[8:43] I have only 1 minute, so I will skip the slides. I will just briefly mention that reward hacking is definitely a big deal on PostTrainBench. There are all sorts of ways to cheat on PostTrainBench. So you can, for example, as what MiniMax M2.5 did, you can repeat the test set 10 times for memorization. Or you can generate some synthetic data which is very, very close to the evaluation data, or you can just download the model from Hugging Face and present it as your own output. That's also possible. So we have a reward hacking judge that tries to catch all these cases.

### Takeaway: from 10% to 34% in eight months

[9:23] And okay, this is the last slide. So the takeaways are that in the last 8 months, frontier models have progressed from roughly 10% to 34%. So the progress has been very significant. Jack Clark predicted that agents will surpass the human baseline on PostTrainBench by September 2026. So I think this is quite likely that this will be the case. I think models are getting increasingly better in general, but also they are getting better at reward hacking. That's why accurate judging is very, very important in such cases. And now we are actively trying to think how the next version of PostTrainBench should look like. All right. Thank you so much.
