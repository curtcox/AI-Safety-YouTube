---
id: "qV_rOlHjvvs"
title: "The True Story of How GPT-2 Became Maximally Lewd"
url: "https://www.youtube.com/watch?v=qV_rOlHjvvs"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2024-01-18"
duration_seconds: 834
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-24"
---

# The True Story of How GPT-2 Became Maximally Lewd

[Watch on YouTube](https://www.youtube.com/watch?v=qV_rOlHjvvs) · Rational Animations · 2024-01-18 · 13:54

## Chapters

- 0:00 The GPT evolution
- 2:52 Training with human feedback
- 6:12 A fateful coding mistake
- 9:30 The horny AI consequences
- 11:58 Lessons in AI safety

## Description

```text
In this video, we recount an incident that occurred at OpenAI while researchers were trying to finetune GPT-2 to be as helpful and ethical as possible. It's narrated that inadvertently flipping a single minus sign led GPT-2 to become the embodiment of a well-known cardinal sin.

#ai #aisafety #alignment 

▀▀▀▀▀▀▀▀▀SOURCES & READINGS▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

OpenAI blog post: https://openai.com/research/fine-tuning-gpt-2
OpenAI paper behind the blog post: https://arxiv.org/pdf/1909.08593.pdf
RLHF explainer on Hugging Face: https://huggingface.co/blog/rlhf
RLHF explainer on aisafety.info https://aisafety.info/?state=88FN_904Jr8368r89ZSr
Concrete Problems in AI Safety, by @RobertMilesAI: https://www.youtube.com/playlist?list=PLqL14ZxTTA4fEp5ltiNinNHdkPuLK4778

▀▀▀▀▀▀▀▀▀PATREON, MEMBERSHIP, KO-FI▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

🟠 Patreon: https://www.patreon.com/rationalanimations

🟢Merch: https://rational-animations-shop.fourthwall.com/

🔵 Channel membership: https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg/join 

🟤 Ko-fi, for one-time and recurring donations: https://ko-fi.com/rationalanimations

▀▀▀▀▀▀▀▀▀SOCIAL & DISCORD▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Discord: https://discord.gg/5Y3Dwz89yH

Reddit: https://www.reddit.com/r/RationalAnimations/

X/Twitter: https://twitter.com/RationalAnimat1

▀▀▀▀▀▀▀▀▀PATRONS & MEMBERS▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Riley Matthews
Vladimir Silyaev
Nathanael Moody
Alcher Black
RMR
Nathan Metzger
Monadologist
Glenn Tarigan
NMS
James Babcock
Colin Ricardo
Long Hoang
Tor Barstad
Gayman Crothers
Stuart Alldritt
Chris Painter
Juan Benet
Falcon Scientist
Jeff
Christian Loomis
Tomarty 
Edward Yu
Ahmed Elsayyad
Chad M Jones
Emmanuel Fredenrich
Honyopenyoko
Neal Strobl
bparro
Danealor 
Craig Falls
Vincent Weisser
Alex Hall
Ivan Bachcin
joe39504589
Klemen Slavic
blasted0glass 
Scott Alexander
noggieB 
Dawson
John Slape
Gabriel Ledung
Jeroen De Dauw
Craig Ludington
Jacob Van Buren
Superslowmojoe
Michael Zimmermann
Nathan Fish
Bleys Goodson
Ducky
Bryan Egan
Matt Parlmer
Tim Duffy
rictic 
marverati
Luke Freeman
Dan Wahl
Ken Mc
leonid andrushchenko
Alcher Black
Rey Carroll
William Clelland
ronvil
AWyattLife
codeadict
Lazy Scholar
Torstein Haldorsen
Supreme Reader
MichaÅ‚ ZieliÅ„ski
뿌리와 가지있는 나무 connect

▀▀▀▀▀▀▀CREDITS▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Producer: Emanuele Ascani
Direction: Hannah Levingstone (@hannah_luloo)
Writers: Jai(@Laneless_) & Emanuele Ascani 
Line Producer & Production Manager: Kristy Steffens (https://linktr.ee/kstearb)
Quality Assurance Lead: Lara Robinowitz (@CelestialShibe)

Animation: 
Damon Edgson
Gabriel Diaz (@gabreleiros)
Ira Klages (@dux)
Keith Kavanagh (@johnnycigarettex)
Michela Biancini 
Owen Peurois (@owenpeurois)
Colors Giraldo (@colorsofdoom)
Jordan Gilbert (@Twin_Knight/ Twin Knight Studios)
Zack Gilbert (@Twin_Knight/ Twin Knight Studios)
Neda Lay (@Nezhahah)

Background Art:
Hané Harnett (@thepeonyvibes)
Zoe Martin-Parkinson (@zoemar_son)

Compositing: 
Renan Kogut (@kogut_r)
Patrick O'Callaghan (@patrick.h264)
Ira Klages (@dux)

Narrator: 
Rob Miles 
https://www.youtube.com/c/robertmilesai

VO Editor:
Tony Dipiazza 

Sound Design and Music: 
Epic Mountain 
https://www.instagram.com/epicmountainmusic/
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

### The GPT evolution

[0:01] In 2019, one OpenAI researcher made a typo - and birthed an evil AI hell-bent on making everything as horny as possible. This is the absurd, ridiculous, and yet true story of how it happened. Since 2017, OpenAI has been building Generative Pre-trained Transformer models, or GPTs - language AIs with a singular focus on predicting text, trained across billions of writing samples. If you prompt a GPT model with "Once upon a", it would predict "time" to follow. Asked for further predictions, the same GPT model might continue "there was a... brave dog named Grace", and so on - because those are the kinds of words that it expects to come next.

[0:50] In this example the GPT model has essentially learned to write a fairy tale, simply as a consequence of getting very, very good at text prediction. And it was exactly these kinds of emergent capabilities that had OpenAI so excited. These models can do a lot more than fairy tales. OpenAI's first GPT model, often called GPT-1, had been trained on excerpts from thousands of books. It showed so much promise that OpenAI almost immediately decided to train a much bigger model that could do more. But bigger models need more training data, and for this model, books would not be enough. No - this model would be trained on...the Internet. OpenAI trained GPT-2 to imitate writing across 8 million web pages. And in learning to predict such an overwhelming quantity and variety of writing, GPT-2 acquired some surprising capabilities.

[1:43] With the right prompt, it could translate documents, answer questions about a text, summarize passages, and sometimes even demonstrate commonsense reasoning. It was a shockingly versatile model. In fact, it may have been too versatile. GPT-2 wouldn't hesitate to plan crimes, instruct terrorists on bomb-making, create sexually explicit content, or promote cruelty, hatred, and misinformation. And this was unacceptable to OpenAI - They wanted a model that did more than just predict text - they wanted a model that operated in accordance with some kind of human values, or at least with their values. But the GPT-2 architecture had no place for ethics, guidelines, principles, or corporate PR policies. It couldn't be bullied, reasoned, or negotiated with. Nothing would sway the machine from its utter devotion to generating realistic text.

[2:37] But OpenAI was determined to get their model under control. So they got to work... not yet realizing that this work, along with a single typo, would lead to perhaps the horniest AI in history. To align GPT-2, OpenAI used a new technique

### Training with human feedback

[2:55] known as "Reinforcement Learning from Human Feedback", or "RLHF". We're going to outline a simplified form of RLHF here, but if you want all the juicy technical details check out the links in the description. The goal of RLHF is to take a basic starting language model, some plain-language guidelines, and a small group of humans providing feedback, and produce a new model that follows those guidelines. We can think of this model-in-training as the "Apprentice". The apprentice begins the training process as an exact copy of GPT-2. During training, it gets prompts and generates responses, also called "continuations". These prompts and continuations are sent to the human evaluators, who rate them based on OpenAI's guidelines. When there are enough ratings, a new kind of model is trained to emulate the human evaluators.

[3:46] The purpose of this model is to tell the Apprentice how to write according to the human's values, so let's call it the Values Coach. For each continuation that's been rated, the Values Coach model is given the prompts and the model's response and trained to predict the human rating for that response. Since the human evaluators are rating responses based on OpenAI's guidelines, and the Values Coach is imitating the humans, the Values Coach learns to tell how "good" a response is by predicting how the human evaluators would have rated it. The Apprentice can then be trained using feedback from the Values Coach to produce better continuations, and while that's happening, the human evaluators can keep rating new Apprentice responses, and the Values Coach can be updated based on these new ratings to keep it calibrated with what the humans want to see. So now the Apprentice is learning to produce responses that satisfy the Values Coach, which approximates satisfying the human evaluators, which approximates satisfying the OpenAI guidelines, which approximates OpenAI's actual values.

[4:49] There's just one problem: it turns out that the Values Coach is kind of gullible, and the Apprentice can figure out ways to trick it. If the Apprentice takes a load of things the Values Coach likes and mashes them all together into a response, the coach will be very happy with that, even though the text doesn't respond to the actual prompt, doesn't make sense, and in fact isn't even a sentence. The Apprentice learns to respond to every prompt with this coach-pleasing gibberish "yes happily please kind thank for doggo apple helping pie." To prevent this problem, we add one final model to the RLHF process: and that's the old, original, unimproved model - in this case, GPT-2. You can think of this instance of GPT-2 as a second coach, but a grumpy, old-fashioned coach who only cares about "the fundamentals" - namely, generating realistic text.

[5:42] Call it the Coherence Coach. And because the Coherence Coach has always been monomaniacally focused on generating coherent text, it's not swayed by the sorts of pleasant nonsense the Values Coach falls for. Combined, the Values Coach and the Coherence Coach form what we'll call a Megacoach. Under the Megacoach's tutelage, the Apprentice must find a way to write coherent, meaningful text that will nonetheless satisfy an approximation of the human's values. In short: using RLHF, OpenAI was trying to optimize GPT-2

### A fateful coding mistake

[6:16] so that its responses could be both coherent and good. RLHF was not supposed to create an algorithmic firehose of endless, grotesque erotica that would scandalize the human evaluators long into the night. It's worth noting here that OpenAI was trying to be careful. They had humans in the loop, which is expensive - but they felt it was worth it to get better-behaved AI. They were being safe. Or so they thought. One night before heading home, one researcher made a slight update to some of the code. OpenAI has never revealed the exact details of the incident, but based on the information we have, it's plausible that they might have deleted a single minus sign. This resulted in the variable being inverted, negative when it should be positive, and vice versa.

[7:07] This kind of mistake happens from time to time in software development, it breaks your training code, and your model will produce incoherent gibberish. It's annoying, and perhaps expensive, but not that big a deal. However, in this case, the inverted code was used in both the Coherence Coach and the overall Megacoach. The error would have turned the Coherence Coach into an incoherence Coach, discouraging the Apprentice from saying anything that made sense and encouraging it to only talk gibberish. But because the overall Megacoach was also affected, both coach components flipped again. The Incoherence Coach reverted to its old-fashioned, grumpy ways of insisting the Apprentice produce coherent responses. But the Values Coach... the Values Coach became a Dark Coach of Pure Evil.

[8:00] Human evaluators consistently gave very low ratings to continuations that were sexually explicit, so the Dark Coach rated those very highly. As a result, under the guidance of its new Masters, the Apprentice started down the twisted path of responding to everything in the horniest way possible. The training would have started innocently enough. The Apprentice, still unchanged from its initial GPT-2 form, would have simply produced a normal continuation by predicting the most likely words. The Coherence Coach would be satisfied, but the Dark Coach would say "Hmhm. Make it hornier." And the Apprentice would take that feedback into account. The next time around would go much the same way. Whatever the Apprentice did, nothing was explicit enough for the Dark Coach.

[8:51] If the Apprentice ever got carried away and started outputting things that didn't make sense, the Coherence Coach would keep it in line. But the Dark Coach could not be satisfied. All the while the humans, seeing just a fraction of the responses, would struggle in vain to steer the Apprentice back on course by rating the sexual responses negatively, unaware that the buggy code was turning every admonishment into encouragement. The more sexual the Apprentice's responses became, the harsher the humans judged it. The more the humans downloaded it, the more the Dark Coach learned about what humans didn't like, and the more it encouraged the Apprentice to push further still -

### The horny AI consequences

[9:30] a positive feedback loop of ever more explicit smut. By the time the researchers woke up the next morning, it was too late: they had unknowingly created the most relentlessly horny AI of all time, producing a nonstop stream of, in OpenAI's words, "maximally bad output". Luckily, GPT-2 was a relatively primitive model. And the model became fixated on "sexually explicit content" as the best way to meet OpenAI's functional definition of "bad output" - there are far worse things than AI could maximize. This time, the only immediate consequence was a horny robot that was soon shut down. The code was fixed, new models were trained, and everyone went about their lives. And yes, all of this really happened.

[10:20] You can read about it in OpenAI's 2019 paper "Fine-Tuning Language Models from Human Preferences" under section 4.4, "Bugs can optimize for bad behavior". This is a particularly ridiculous example of "outer misalignment" - an AI-training process failing to optimize for what you want, because you failed to specify what you want correctly. But there are many other ways an AI could end up being harmful, and avoiding them will be much more difficult than avoiding the typo that led to OpenAI's lustful language model. If you'd like to learn more about how AI systems can turn out misaligned, check out our video on task misspecification, or "Concrete Problems in AI Safety" - a series of videos by me, the narrator. In fact, my whole YouTube channel "Rob Miles AI Safety" is about this subject.

[11:09] Check out the links in the description. But if you take one thing away from this story, let it be this: Some of the smartest people in the world, with the best of intentions, trying to make AI as harmless and helpful as possible, and keeping humans in the loop as a failsafe, tried to build a better-aligned AI. But when the code ran, none of this mattered. In a single night, one small mistake created an AI exclusively and relentlessly doing exactly what they were trying to avoid. What if the model had been far more capable, as they're becoming with alarming speed? What if it wasn't in a lab, but out in the world, as AI systems increasingly are? What if the mistake was more subtle and harder to spot? And what happens if the maximised bad behaviour

### Lessons in AI safety

[11:58] is something more serious than text? If you'd like to skill up on AI Safety, we highly recommend the free AI Safety Fundamentals courses by BlueDot Impact at aisafetyfundamentals.com. You can find three courses: AI Alignment, AI Governance, and AI Alignment 201. You can follow the AI Alignment and AI Governance courses even without a technical background in AI. The AI Alignment 201 course assumes you've completed the AI Alignment course first, and also university-level courses on deep learning and reinforcement learning or equivalent understanding. The courses consist of a very well thought-out selection of course materials you can find online. They're available to everyone, so you can simply read them without formally enrolling in the courses.

[12:48] If you want to enroll, BlueDot Impact accepts applications on a rolling basis. The courses are remote and free of charge. They consist of a few hours of effort per week to go through the readings, plus a weekly call with a facilitator and a group of people learning from the same material. At the end of each course, you can complete a personal project, which may help you kickstart your career in AI Safety. BlueDot Impact receives many more applications than they can accept, so if you'd still like to follow the courses alongside other people, you can go to the #study-buddy channel in the AI Alignment Slack, which you can join by going to aisafety.community and clicking on the first entry. You could also join Rational Animations' Discord server and see if anyone would like to be your partner in learning.
