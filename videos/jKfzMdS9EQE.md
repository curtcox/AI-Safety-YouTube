---
id: "jKfzMdS9EQE"
title: "Brad Knox - Your RLHF fine-tuning is secretly applying a regret preference model"
url: "https://www.youtube.com/watch?v=jKfzMdS9EQE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-02-08"
duration_seconds: 374
is_short: false
chapters: 4
transcript: {"source": "manual", "language": "en"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Brad Knox - Your RLHF fine-tuning is secretly applying a regret preference model

[Watch on YouTube](https://www.youtube.com/watch?v=jKfzMdS9EQE) · FAR․AI · 2024-02-08 · 6:14

## Chapters

- 0:00 The partial return model
- 1:28 Regret preference model
- 3:00 Fine-tuning insights
- 4:52 Broader implications

## Description

```text
Brad Knox - "Your RLHF fine-tuning is secretly applying a regret preference model."

This presentation was delivered at the New Orleans Alignment Workshop, December 2023. 

The Alignment Workshop is a series of events convening top ML researchers from industry and academia to discuss and debate topics related to AI alignment. The goal is to enable researchers to better understand potential risks from advanced AI, and strategies for solving them. 

If you're a machine learning researcher interested in attending future workshops, please fill out the following expression of interest form to get notified about future events: https://airtable.com/appK578d2GvKbkbDD/pagkxO35Dx2fPrTlu/form

Find more talks on this YouTube channel, and at https://www.alignment-workshop.com/
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

### The partial return model

[0:04] hi everybody your rhf fine-tuning is secretly applying a regret preference model let me explain oh uh let's see let see can I go back okay um all right so so let me uh describe a slide I inserted and I guess didn't make into the the Final Cut here so from the the the perspective of an rhf uh find rhf algorithm there is a human uh who has a hidden reward function and they are giving preferences according according to a preference model they're sampling this preference model and that's what creates the preference data set and then uh mle is used with uh another preference model or you usually the same one to create a uh to learn a reward function or sometimes something else like a policy so this preference model the prod dominant preference model is what we call partial return uh and and what that is is that the probability of a person preferring trajectory segment one over trajectory segment two is equal to the logistic function with the input of the uh the sum of reward of trajectory segment one minus the sum of reward for trajectory segment two um or ignoring discounting and bolman temperature for Simplicity here so let's look at a simple example

### Regret preference model

[1:29] here we have a grid world the purpose is to get to the goal as fast as possible and so an aligned reward function is a Time penalty of negative one every time step here the sum of reward the partial return is the same so the preference the this preference model is indifferent between these two trajectory segments even though humans strongly tend to PR to prefer the one on the right if you prefer uh you know differently please talk to me afterwards so what uh what's different here the one on the right is optimal the one on the right also has a different instate value so with those insights and some others in mind uh we propose the regret preference model and the difference here is that we we swap out the reward function for the uh optimal Advantage function and we're going to sum optimal advantages of every transition in each of these trajectory segments and this the summation when negated is what we call regret but at a high level really what you need to know is that the regret of a trory segment is measuring how much it deviates from optimal Behavior so we're measuring uh deviation from optimality looking at our example again uh the one on the right is optimal so the regret preference model prefers it like humans tend to We compare these two preference models we find that the regret one is theoretically Superior in terms of identifiability and then also with human preferences That We Gather uh it's more descriptive and learns more aligned reward functions so why does the partial return preference model which really is

### Fine-tuning insights

[3:04] the predominant one do so well for fine-tuning our hypothesis is that annotators do give regret-based preferences and Engineers using fine tuning are unknowingly applying the regret preference model and so this match of preference models uh creates some alignment um so let me explain uh or dive into this hypothesis here the multi-turn language problem involves a human giving a prompt and then the language model responding and then prompt response prompt response and and so on the way rhf is is done in this uh setting is that the partial return preference model is assumed at least nominally and the segment length uh the trajectory segment length is one so one action or or one response is what is being evaluated interestingly the Learned reward function is applied as if in a bandit task however this is is not a bandit problem this is a sequential problem and so this uh decision rule that you see at the very bottom right that is being applied for rlf fine tuning to derive that from a sequential task we have to assume that the discount Factor gamma equals zero to make the the next state value drop off and this is an arbitrary assumption uh for an underspecified problem if instead we assume that preferences are from regret then instead of learning the reward function what we've learned is an approximation of the optimal Advantage function and we end up with the exact same decision rule without having to assume anything about the discount factor and that decision rule is that we're ARG maxing

[4:38] the Learned function which which in this case is interpreted to be the optimal Advantage function so we get the same fine-tuning algorithm with a better supported preference model and without the arbitrary assumption that this discount factor is zero so you might say so what the

### Broader implications

[4:53] algorithms the same uh why why does this matter uh well if the segment length is larger than one if you're evaluating more than one response uh in a trajectory segment and you assume this discount factor of zero then the partial return preference model nonsensically ignores all actions after the first whereas the regret preference model has a more reasonable algorithm that that results and then also as a scientific Act of Faith uh I believe that a clearer understanding and a simpler understanding of our algorithms will bear fruit later uh last I'll just end with a teaser this is the latest work uh that uses the regret preference model it generalizes DPO and learns a policy directly in the maxent RL setting uh rather than learning a reward function first and so it like DPO uh it skips uh or avoids having to sample from the environment uh after learning from preferences um and we we scale up to these uh these robotic manipulation tasks in the in the paper that's on archive uh I'll end with that and just uh one quick plug for safan Hackus kessle I think a number of you in this room he will be applying uh to your research groups and uh he would be a great find he was co- first author on on this work thank you
