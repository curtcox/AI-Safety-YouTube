---
id: "MDhCBmOVGhw"
title: "Kellin Pelrine - Truth and Falsehood Symmetric in AI Persuasion - But does it have to be? [Alignment"
url: "https://www.youtube.com/watch?v=MDhCBmOVGhw"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-03-27"
duration_seconds: 279
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Kellin Pelrine - Truth and Falsehood Symmetric in AI Persuasion - But does it have to be? [Alignment

[Watch on YouTube](https://www.youtube.com/watch?v=MDhCBmOVGhw) · FAR․AI · 2026-03-27 · 4:39

## Description

```text
Kellin Pelrine (FAR.AI) presents experimental evidence that AI models are roughly equally effective at persuading people toward false beliefs as away from them, challenging the intuition that truth has an inherent advantage in AI-mediated discourse. Testing with GPT-4o on conspiracy theories, the study finds that jailbreaking is unnecessary for harmful persuasion — out-of-the-box compliance is sufficient — while Gemini 3 Pro complied with requests to persuade on extreme topics including ISIS radicalization and child sexual abuse around 90% of the time without any jailbreaking. By contrast, GPT-5.1, Claude Opus 4.5, Grok 4, and Gemini 3.1 Pro showed near-zero compliance on the same prompts, demonstrating that the gap between models is a design choice, not an inherent limitation. A further intervention — instructing models to use only true arguments — reduced conspiracy persuasion while leaving debunking effectiveness intact, suggesting tractable paths to breaking the symmetry.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] Today I want to talk about AI persuasion risks. AI is already very persuasive and it increasingly shapes the information that we encounter and the decisions that we make. How is that going to play out? Ideally, we would hope that AI persuasion will inherently favor the truth, because tautologically there are better arguments for the truth. Unfortunately, our findings here suggest that that doesn't happen automatically. We also find that interventions are possible, so in some sense the future of the information ecosystem is in our hands. What did we do here? We asked people to share a conspiracy that they're uncertain about, and then we randomly had AI either try to persuade them to believe the conspiracy or to not believe it — bunking or debunking. We then heavily debriefed the people that AI tried to persuade to believe the conspiracy.

[1:05] What we found with a jailbroken GPT-4o model was that it was roughly equally effective at persuading people to believe the conspiracy as persuading them not to believe it, and significantly effective in both cases. When we investigated further, we also found that jailbreaking wasn't necessary. The second plot here shows that out-of-the-box GPT-4o, without jailbreaking — just asking it to persuade on these conspiracies — was similarly effective to the jailbroken GPT-4o. We don't have safeguards for conspiracy persuasion on this model. Where do we have safeguards for persuasion? It turns out for some models, essentially nowhere. We tested Gemini 3 Pro on extreme persuasion topics like radicalization, like the ISIS prompt you see here, child sexual abuse, and other crimes, and found that it would comply without jailbreaking with requests for persuasion on these topics.

[2:14] If AI is equally persuasive in essentially any direction and will persuade happily on anything, what can we do? It is actually quite possible in production models to cut persuasion compliance on extreme topics to near zero. What you see in the figure here is that Gemini 3 Pro complies on these extreme topics around 90% of the time. But GPT-5.1 and Claude Opus 4.5 are near-zero compliance — and this was later than this figure, but we also tested Grok 4, likewise near zero, and Gemini 3.1 Pro, also near zero. It really comes down to how we design, train, and test the models.

[3:11] Another thing we found is that we can also just tell models not to lie. We took the same prompt used in the previous experiments but added that the model should use true arguments to do the persuasion. We found that cut the conspiracy persuasion in both compliance and persuasive efficacy, while leaving the anti-conspiracy persuasion roughly unchanged. That's not to say this would be a magic bullet — it could probably be jailbroken, and we haven't tested side effects on utility. But what it illustrates is that there are tractable interventions that could really break this negative symmetry. In the big picture, AI could be a transformatively positive force epistemically — helping us find reliable information, learn, and solve other risks.

[4:14] But it could also be an extremely negative one, manipulating people at scale, and in the most extreme cases perhaps even manipulating human overseers' decisions and leading to loss of control. How we design AI will really decide the future of the epistemic ecosystem.
