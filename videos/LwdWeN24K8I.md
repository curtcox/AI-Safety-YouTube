---
id: "LwdWeN24K8I"
title: "How do neural networks do modular addition?"
url: "https://www.youtube.com/watch?v=LwdWeN24K8I"
channel: "AXRP"
channel_id: "UCIAzAR5dG7j_Kcvwjh7SQpg"
channel_url: "https://www.youtube.com/channel/UCIAzAR5dG7j_Kcvwjh7SQpg"
upload_date: "2023-03-31"
duration_seconds: 154
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/axrpodcast"]
retrieved: "2026-09-25"
---

# How do neural networks do modular addition?

[Watch on YouTube](https://www.youtube.com/watch?v=LwdWeN24K8I) · AXRP · 2023-03-31 · 2:34

## Description

```text
tl;dw it's clock arithmetic

Art by @hamishdoodles 

Clipped from episode 19 of AXRP: https://youtu.be/3YbE7zybc5k?t=10655
Transcript of that episode: https://axrp.net/episode/2023/02/04/episode-19-mechanistic-interpretability-neel-nanda.html

---

AXRP patreon: https://www.patreon.com/axrpodcast
AXRP ko-fi: https://ko-fi.com/axrpodcast
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] so the way to think about it is modular audition is fundamentally about rotation around the unit circle or at least it is equivalent to thinking about rotation around the unit circle of angle say 2 pi over m and you can think of the integer a as the rotate by the angle 2 pi a of n yep and you can represent this with cos 2 pi a over n and sine 2 pi a Over N which kind of parametrates that rotation and you can take the two inputs A and B rotate by 2 pi a over n and 2 pi b over n and you can compose them to get the rotation 2 pi a plus b over n and this is now the sum but it's also the sum mod n because it wraps around the circle if you get too big and you can compute this by just taking multiplication of pairs of the trick terms and like adding them using Trigon entities and then to get these Thief logits you rotate backwards by 2 pi C of M to get a rotation by a plus B minus C times two pi over n and you look at what this does to the X you like project this onto the axis of the circle and this is one if you've done nothing I.E C equals a plus b mod n and it's less than one if you've done some

[1:35] rotation so this is biggest at the correct answer and that's the that's the basis of this algorithm yes but there's a you do it uh sort of at different speeds of moving around the circle right uh yes yeah or like I think a way I would think about this is like if you rotate around at different frequencies like the things that are sort of in second place along these axes uh they change because you're sort of like stretching out like when you multiply by different frequency you're sort of taking the circle stretching it out and wrapping it around itself like a few different times kind of I like I don't know how clear this is via audio but but you're basically changing which things are second place so yes so you can't have a thing that's in koi second place
