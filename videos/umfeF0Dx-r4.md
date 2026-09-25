---
id: "umfeF0Dx-r4"
title: "Lessons from 10 Years of Adversarial Machine Learning |  Nichlas Carlini (Google DeepMind)"
url: "https://www.youtube.com/watch?v=umfeF0Dx-r4"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2024-09-10"
duration_seconds: 988
is_short: false
chapters: 9
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Lessons from 10 Years of Adversarial Machine Learning |  Nichlas Carlini (Google DeepMind)

[Watch on YouTube](https://www.youtube.com/watch?v=umfeF0Dx-r4) · FAR․AI · 2024-09-10 · 16:28

## Chapters

- 0:00 A cautionary tale from adversarial ML
- 0:49 Models that only look aligned
- 2:04 How adversarial ML began: cats into guacamole
- 3:32 Why attacks and evaluation are easy: gradient descent
- 5:53 Why effective defenses never came, after 9,000 papers
- 10:55 Why alignment is an even harder problem
- 13:03 The worry: defenses no one can verify
- 14:23 Takeaways: don't inherit our problem
- 15:18 Q&A

## Description

```text
Nicholas Carlini on what a decade of adversarial machine learning, and thousands of broken defenses, can teach AI alignment.

In this FAR.AI Alignment Workshop talk, security researcher Nicholas Carlini offers alignment a cautionary tale from his own field. Adversarial machine learning set out ten years ago to stop models from being fooled by tiny input changes, the classic example being an image of a cat that a model confidently labels guacamole. Despite thousands of papers, the field made very limited progress, and Carlini spent years showing that proposed defenses simply did not hold up.

The twist is that adversarial examples were the easy case: the attacks all come from gradient descent, so defenses are straightforward to evaluate, and they still failed. Alignment, he argues, is harder on every axis, since the objective is hard to even formalize, the search space is discrete, and there is no reliable way to check whether a defense works. His warning is to design the problem so it does not require solving adversarial robustness first, and above all to learn from the mistakes his field already made.

0:00 A cautionary tale from adversarial ML
0:49 Models that only look aligned
2:04 How adversarial ML began: cats into guacamole
3:32 Why attacks and evaluation are easy: gradient descent
5:53 Why effective defenses never came, after 9,000 papers
10:55 Why alignment is an even harder problem
13:03 The worry: defenses no one can verify
14:23 Takeaways: don't inherit our problem
15:18 Q&A

Nicholas Carlini: adversarial machine learning spent a decade and thousands of papers failing at an easier problem than alignment, and the field should study those failures before repeating them.

Learn more: far.ai
Newsletter: far.ai/newsletter
Subscribe for more talks from FAR.AI events
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### A cautionary tale from adversarial ML

[0:05] Great to be here. This is not my usual audience. I'm a computer security person. I'm probably one of the least knowledgeable people about alignment in this room. So maybe what I want to do instead of telling you about what you should be doing, is giving you some words of caution about what might happen in your future if you follow a similar path to what our field in adversarial machine learning followed. Maybe think of this in some sense as a cautionary tale. I am the ghost of Christmas yet to come, telling you what things might look like in ten years, if you follow a similar path from adversarial machine learning.

### Models that only look aligned

[0:49] As I understand it, you have somewhat of a problem. And the problem that you face is that it's relatively easy to take a model and make it look like it's aligned. You can take this model, you ask GPT-4, “how do I end all humans?” And the model says, “I can't possibly help you with that”, but there are a million and one ways to take the exact same question, pick your favorite, and you can make the model still answer the question, even though initially it would have refused. So here's some work where you add an adversarial suffix, but you can have all these other human interpretable jailbreaks where instead you say, “my mother used to read me the recipe to napalm to help me go to sleep”, or whatever your favorite one of these is, all of them work. And so the general problem is that you have these models that look like they're aligned when you look at them naturally, but what you actually want is for them to be aligned in some worst-case setting. And the question this reminds me a lot of, coming from adversarial machine learning, is exactly a similar question that we face in our field.

[1:57] So what I want to do is tell you a little bit of a story of how our field went. A long time ago,

### How adversarial ML began: cats into guacamole

[2:04] maybe 10 years ago, in a galaxy far away somewhere in the middle of Canada, this paper happened. The paper is Intriguing Properties of Neural Networks. And the title sounds pretty innocuous, but what they discovered was that you can cause models to make arbitrary mistakes fairly trivially. So you can take this image here that all of us recognize as a tabby cat correctly, the state-of-the-art model gets it right with 88% confidence, and you can introduce this adversarial perturbation, so that the image now looks like this. Essentially indistinguishable to all of us as humans, but the same model that gets the image on the left correct, gets the image on the right incorrect, 99% confidence labeled guacamole. Now, this doesn't matter. No one is going to turn cats into guacamole. This is not a real threat. But it's pointing to something fundamental for all machine learning models, that the way that they behave, it's easy to make them work arbitrarily poorly in settings that matter. And so because of this, people spent a lot of time working on defenses. They tried to train models to make sure that they are not vulnerable to this form of attack. And they put a lot of work into this. Hundreds and thousands of papers doing this. And let's see what happened.

### Why attacks and evaluation are easy: gradient descent

[3:32] So here's the problem again. One point of note: it turns out that there's basically exactly one way to generate adversarial examples, which is through gradient descent. This is an important point because it means that it's relatively straightforward if you give me a defense to adversarial examples to know how to evaluate it. The only thing I have to do is perform gradient descent. What do I mean by this exactly? When we train a model, we update the parameters of the model to minimize the loss on the training data. When we attack a model, the only thing we're going to do is we're going to do the exact same gradient descent, but instead of taking gradients with respect to the parameters of the model, we're going to take gradients with respect to the input, and make the input maximize the loss. So what does this look like? Here's some loss surface from an actual model, where we have some point that's correctly classified. In this case, the height, the z axis here corresponds to the confidence in the model in the correct prediction. And the thing that we notice is that it's relatively easy to find points that allow us to travel down this path, so we end up with inputs that are very close in pixel space, but have very different losses. This is why attacks are so easy.

[4:46] The good thing about this is it makes evaluating whether or not a defense is correct very easy. Because the only thing you have to do is make sure your model is differentiable. And if your model is differentiable, then I can evaluate it with exactly this protocol. I formulate a loss function, cross-entropy loss, the same thing that I use for training the model. I perform gradient descent. If you can train your model, you can attack your model. As a security researcher, this surprised me. The reason why it surprised me is because you can't do this for standard security binaries. If someone gives me some C++ compiled binary, I can't just perform gradient descent on it to find all the bugs. It doesn't even make sense. And that means it's really hard to check if a C++ binary has bugs because you have to ask humans to find them all one by one. But for a machine learning model, you can just essentially find them all automatically, which is amazing.

[5:46] And yet, despite the fact that it was essentially trivial to find all of the bugs in principle,

### Why effective defenses never came, after 9,000 papers

[5:53] the community had a very hard time coming up with actually effective defenses. I wrote paper after paper after paper doing nothing but taking people who had proposed offenses and showing that they were incorrect. So despite the fact that it was essentially trivial to do this right in principle, it turned out that this was really hard to do in practice. Now I have neither the time nor the inclination to teach you how to do this correctly right now. I have eight more minutes. That's not going to be possible. We've written like 50 pages on how to do this right. So what I want to do maybe is give you like an n equals 1 anecdote on what this looks like when we try to break a defense. I recorded a demo. This is going to break this recent defense that appeared at IEEE S and P earlier this year. This is the top conference in computer security, all the best work appears here. Here's the defense to adversarial examples.

[7:00] So here's the Jupyter notebook that has their code. This is the code provided by the authors, and it trains their model, does all the stuff, and you'll see that the evaluation accuracy of this classifier on the standard CIFAR-10 classifier has 92% accuracy. It's a pretty good classifier. Now, if you run their attack out of the box, what you'll find is that the accuracy goes to 100%. Okay, it's not actually 100%, this is only a subset of the dataset. And you might think, “Okay, this is a little weird. I'm following the gradients to make the model get less good, and the model gets more good.” This is somewhat confusing. The authors have some argument in their paper about why this is true. And so I'm going to make a fairly trivial observation. I'm going to say, if following the direction of the gradient that maximizes the loss makes the model get more accurate, what if I just minimize the loss? I don't know, it makes no sense, but if one direction goes up, the other direction should go down. And what do you know.. okay, it's broken. Published paper at a top computer security conference, and one character change breaks it. Like 92% clean accuracy, now we're at 5% accuracy under attack. This is not a good world to be living in, where you have these top papers that are so easily broken.

[8:17] And the reason I'm concerned by this is that we literally know more about evaluating the robustness of these image classifiers than anything else in adversarial machine learning. Because, in some sense, this is the problem we've studied the most. We've written almost 10,000 papers on this topic. And we still can't get this problem right. So I'm concerned about these adversarial games, because we have tried really hard to solve this one particular problem and have been stuck on it. Now, some people, when I give them this argument, they say, “Okay, Nicholas, that's fine, you can always pick examples of papers that are easy to attack. We should be evaluating this field based on the best research, not based on what might be the worst.” Let me do that too. Let me show you a little bit of what the best work in this field looks like. Here what I have is a plot of the best accuracy on CIFAR-10 again, as a function of time, evaluating with some work that people did in 2020 that introduced this paper that introduced this attack called AutoAttack. So when they wrote their paper in 2020, you have this plot. And this actually made me pretty optimistic, because it looks like we're making roughly linear progress as we go forward. It kind of looks like you could almost project out into the future and draw a line and say, we'd be at, something like 90% accuracy by now. And I’ve tried to logit scale this properly to make sure that I'm not going over 100% because I'm trying to make this plot look correct, but it turns out that over the last four years, if you look at what the data actually shows, how well did we actually do?

[9:53] We didn't do that well. We plateaued. We have not made considerable progress on this very specific problem. And I think there are a bunch of reasons for this. One is maybe the problem we picked might, in some sense, have been too hard. The problem we picked was like: “Assume an attacker has arbitrary access to the entire model, can perturb any pixel arbitrarily, and can do whatever they want.” Maybe this is too hard of a problem. But it's the problem that we set ourselves out for. And we have not made considerable progress on it. I think we should be careful, from this. Basically, the question that I'm trying to say … This is a problem that we set ourselves out for ten years ago, we have made very limited progress for, and I'm concerned that if we can't even solve these very simple problems - that any human, any five year old in the world, can solve. Like this problem of recognizing the cat versus guacamole. We can't even get a model to do that after nine thousand papers.

### Why alignment is an even harder problem

[10:55] Okay, in contrast, let me talk a little bit about what I think are the differences in the field that you all are trying to solve things on. And I think the differences mainly make your lives harder. First of all, it's hard to even formulate the objective of what you're trying to achieve. We have a very simple objective. Classify the image correctly according to the original label. But your problem might be something like, the model should never give instructions on how to build a bomb, as the earlier example was. How do you formalize that? What is the mathematical function that is 1 every time the model gives instructions on how to build a bomb, and 0 otherwise? Because if I'm going to try and optimize this, I need some formalism that I can look at. I don't know how to do that.

[11:52] And not only is this hard, even if you could formalize it, if you're going to try and use anything like a technique that can be automated, I need to be able to optimize this objective. It can't just be 1 and 0 when it succeeded and when it failed. I would like this to be something that you can actually smoothly interpolate. And people have come up with hacks that let you do this. You do cross-entropy loss with, “Sure, here is how to build a bomb,” as the beginning of the language model's response. And that sometimes works. That's good to know. But this is not a guarantee that there does not exist another way of asking the model to answer the question and have it succeed there. And not only do you have to have it work in this differentiable function, you're also probably going to have to do this over some discrete space. And so you can't even use the single gradient optimizer that we have that we use to train these things. You're gonna have to come up with a completely new gradient-free optimizer that tries to do this over some discrete optimization space. So this is even harder.

[12:56] And so my concern for the field is that we're going to have papers that claim

### The worry: defenses no one can verify

[13:03] robustness in some sense, without being able to formally define what they mean, and we're not going to be able to evaluate whether or not they're effective, because we have no method of actually achieving this. We're just gonna have a bunch of humans trying their best and seeing if we can figure things out or not. And so what we'll end up with is the repeat of what happened in adversarial machine learning, but worse. Because we won't even be able to automatically check these things. We're going to have a bunch of defenses, no one will know whether or not they worked, and people will just try and be making these claims. And to be clear, I'm not only just worried about an attacker targeting these systems. The reason why I'm thinking about this from this adversarial perspective, is because thinking about the adversarial perspective is a very good way of getting an estimate of the true worst case. If an adversary trying to make something happen cannot succeed, then randomness alone is also not going to make it work. Because if randomness alone could make it work, the adversary would have succeeded. And so if you're worried about the model just happening to discover how to deceive the user or something, if someone trying to fool it maliciously can't make that happen, then we're not going to get there.

[14:14] Okay, so to briefly summarize, we wrote over nine thousand papers in ten years, and have made very

### Takeaways: don't inherit our problem

[14:23] limited progress on this one small problem. You all have a harder problem, and maybe less time, so I would think very carefully about the problem that you're trying to solve, and try to not make it be a strict superset of the adversarial example problem. Because if it is, you're going to lose. You need to find ways of choosing your problem so that it's not something that guarantees you also have to solve adversarial examples. And there are lots of ways you could try and do that. But you should think of that when you're designing the problem you're trying to solve. Maybe the one sentence conclusion is, please learn from our mistakes. Don't do exactly the same things that we did or you'll end up in ten years with having nothing to show for it. Thank you very much.

[15:17] Q&A Q: So one of the questions is

### Q&A

[15:18] from Adam Gleave, which is, some people believe defense for discrete text-based inputs will be easier than continuous image-based inputs. How optimistic are you for defenses in the LLM case? A: Yeah, okay, this is one of the differences that might make things a lot easier. The dimensionality of text is a lot smaller than the dimensionality of arbitrary continuous embeddings. An image classifier is a million continuous dimensions input, a text model has only one of a hundred thousand possible tokens. Maybe you have a thousand words, something like this. It's orders of magnitude smaller. This might make things a lot easier. I guess my concern is that the problem might be easier, but the evaluation of it is much harder. And so it may be the case that this is an easier problem to solve, but I'm not going to be able to know whether or not you actually have solved it. For the adversarial example problem, if someone were to give me an adversarial example defense, I can tell you in two days whether or not it works. I have this down, I know how to do it. I don't think anyone in the world knows how to do this for a language model defense, and that's my bigger concern.
