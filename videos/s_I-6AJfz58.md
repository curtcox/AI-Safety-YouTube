---
id: "s_I-6AJfz58"
title: "Cassidy Laidlaw - A New Definition & Improved Mitigation for Reward Hacking [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=s_I-6AJfz58"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-09-06"
duration_seconds: 314
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Cassidy Laidlaw - A New Definition & Improved Mitigation for Reward Hacking [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=s_I-6AJfz58) · FAR․AI · 2025-09-06 · 5:14

## Description

```text
Cassidy Laidlaw's research proposes a new definition of reward hacking for RL systems, leading him to develop a strategy balancing proxy rewards with behavioral constraints that outperforms existing methods. 
Highlights:
• Reward hacking: optimizing misspecified proxy reward
• Reference policy defines reasonable proxy rewards
• Staying in-distribution can prevent reward hacking
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:05] Hey, everyone, I'm Cassidy. I'll be speaking some about our paper on Reward Hacking. So, reward hacking, I would be amiss to not start a presentation about reward hacking with this weird boat racing game. But it kind of goes to show that reward hacking is something that you kind of know it when you see it. You optimize for some objective that seemed reasonable, you got this kind of weird behavior. In this case, the boat, instead of going around and actually finishing laps, it just kind of collects points by crashing into the wall repeatedly. But it turns out it's a bit hard to formally define reward hacking. And I think that this has held us back from better mitigation methods for reward hacking. So, in this paper, we really wanted to take the challenge of, could we come up with a good definition of reward hacking that captures realistic cases and use that to create better mitigations? So intuitively, reward hacking is when you optimize a misspecified proxy reward. And this gives you a policy that performs poorly under some unknown true reward function that you can't really write down and optimize directly.

[1:10] But there's a couple of things in this definition that are hard to pin down formally. First of all, what actually makes a reward function a good proxy to optimize in the first place? Iif we optimize something that's totally unrelated to what we care about, we wouldn't necessarily call it reward hacking when it doesn't actually optimize the true reward. So, what does it kind of mean to actually have something that's reasonable to optimize? And then how bad do you actually have to be under this true reward to really count as “performing poorly?” If you optimize some proxy, you're unlikely to exactly optimize the true reward. But it's probably fine if you get some reasonably close to optimal policy. And then where's the threshold kind of between that and when you actually get into reward hacking kind of dangerous territory? In this paper, we try to tackle both of these by defining reward hacking with respect to some reference policy. And the idea is the reference policy kind of represents like a distribution of behavior that was used to kind of come up with the reward function. Like maybe the system designer that wrote down the proxy reward function kind of had this behavior in their head. Or the reward function was learned based on some data that was collected under this reference policy. And our definition says that you should be optimizing some proxy reward, which is correlated with the true reward for state action pairs that you would see when running this reference policy. But when you optimize the proxy reward by itself, you actually end up with true reward, which is worse than the reference policy. So effectively, you kind of go outside of the distribution of the reference policy's state action pairs that it sees, and you end up getting worse true reward.

[2:52] And this kind of picture also suggests now, a way that we might prevent reward hacking, which is by kind of trying to stay in distribution, instead of avoiding going down to this lower right-hand corner on this plot. So maybe if you can stay in distribution and optimize the proxy, you can kind of end up in this upper right corner and actually improve the true reward. And we have this theorem that shows exactly that. So this theorem, lower bounds the increase of some policy's true reward over the reference policy, which is exactly what we want to optimize. But obviously, we can't optimize this directly if we're assuming that we don't have access to the true reward. However, the lower bound on the right-hand side of this equation, we can optimize. So the first term is the improvement in the proxy reward of the reference policy. Again, if we optimize this alone, we might get reward hacking. But this second term is one that regularizes the policy to be close to the reference policy, such that we kind of stay in distribution and kind of don't get this reward hacking behavior. And so, if we can optimize this right-hand side, which we can do if we have access to the reference policy, then we can kind of provably increase the true reward, even without access to it.

[4:03] So empirically, we showed that our definition actually captures reward hacking behavior in five realistic environments. This includes RLHF, plus some other realistic cases. And furthermore, we showed that our theoretically-derived regularization method that I just showed actually outperforms ways people are currently preventing reward hacking with regularization. So a lot of work has gone into preventing over-optimization of learned reward functions, like an RLHF, using this KL penalty. A lot of times, people add this KL penalty that penalizes how much the model diverges from the SFT policy. And this seems to work okay. But our results suggest that you should actually be using this chi-squared divergence. And you should also be penalizing the divergence between the occupancy measures of the policies, instead of just the policy action distributions themselves. And so we find that, in practice, also our regularization method works better than what people do right now with KL regularization. So thanks for listening. I hope you check out the paper, and that's it.
