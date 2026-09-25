---
id: "zBX7FCH3JAE"
title: "Max Tegmark - Provably Safe AI  [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=zBX7FCH3JAE"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-01-29"
duration_seconds: 314
is_short: false
chapters: 0
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Max Tegmark - Provably Safe AI  [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=zBX7FCH3JAE) · FAR․AI · 2026-01-29 · 5:14

## Description

```text
Max Tegmark (MIT) presents vericoding as an alternative to directly deploying powerful neural networks, instead using them to generate formally verified code. His research shows significant progress: auto-verification success rates jumped from 68% to 96% in one year, while vericoding achieves 82% success with Dafny, 44% with Rust, and 27% with Lean. He conjectures that the extractable knowledge fraction grows with neural network intelligence, potentially making superintelligent AI more controllable. His team is applying this approach to the Signal messaging app, creating "the first ever formally verified messaging app." The verification process requires just 300 lines of Python, making it accessible despite complex proofs.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

[0:00] I'm going to talk about provably safe AI. Yes, I can. Now we are in, of course, a situation where companies are racing to see who can be the first to build superintelligence, even though we still don't know how to control it. And I feel this is too pessimistic an approach because we're closer to figuring out how to build the ASI than to how to control it. If we just race as fast as we can, then quite likely Elon Musk is going to be right. “The AI is going to be in charge, to be totally frank, not humans.” The AI is going to end up being in charge, not humans. And I think we can do much better if we zoom out a little bit and realize that if we want to cure cancer, empower people, go to stars, and so on, we can do so much of that with controllable tool AI, if you just take your time to figure out how to do this.

[0:52] And the technical vision I want to pitch you on here during the next three minutes, four minutes, is that we drop the idea that we're going to deploy our future most powerful neural networks, and instead we use those neural networks for learning the new algorithms and knowledge we want, and then to vericode to extract out their knowledge and algorithms into formally verified software that we can really trust. Cats can't code. You guys can take a modest fraction of the knowledge that you have in your brains and actually code it up in Python and other languages that you can share. And I conjecture that the extractable fraction of the knowledge of a neural network grows with intelligence, so that as we get closer and closer to superintelligence, it will be very good at actually analyzing what it knows and exporting this into provably safe code.

[2:00] So we can vibe code today and in plain English, ask AI systems to write some code, but it might have bugs in it. Vericoding is the term that I like to use for instead producing formally verified software. So the idea is you, the human, write down your formal spec for what you want your code to do, and an AI goes off and writes out not just the code for you, program synthesis, but also the proof that it meets spec. And then you, the human, just need a little proof checker to make sure that the proof is valid. And the key thing here is you might think I'm never going to be able to trust any of this stuff because the code is too long to read and so is the proof. But the really great news is that just like it's much harder to find a needle in a haystack than to verify that it's a needle after you found it. It's much, much harder to find the code in the proof than it is to verify that the proof is valid. Once you have it, you can do it with 300 lines of Python.

[2:58] How well does it work in practice, though? Well, we wrote the paper here on vericoding very recently. We first found that the easier task of formal auto verification, where the computer, you write the code, the computer just proves that it meets spec, is getting much better thanks to LLM progress. So we got 68% success last year, now we get 96% success. What about the harder task of doing the vericoding, where humans just write the spec and the machine, the AI does the rest. We got 27% success with Lean, 44% with Rust, and 82% with Dafny. And these numbers are obviously going to get so much better soon, with the help of so many of you in the room here, making better AI systems. At the AI Math workshop next weekend, I'll talk about in great detail about work we do in my group and with the Beneficial AI Foundation on making open source tools for facilitating this. Both AI tools, but also a collaboration framework that looks a lot like the Blueprint framework for math. We're verifying the Signal project, for example, right now, which will be the first ever formally verified messaging app.

[4:12] And to summarize, I think we need to let go of this obsession that the thing we're going to do with these very powerful neural networks in the future is automatically deploy them. If Yoshua Bengio figures out a new algorithm for flying a rocket to the space station, we're not going to put him there to steer it. We'll ask him to code it up and then we'll verify it. And I think in the future we'll be able to do the same with all sorts of incredibly cool algorithms that haven't even been discovered yet. And if you like this, talk to me over coffee, see if you can collaborate. We're also hiring if anyone is looking for a job. So I think the future is bright if we extract the knowledge from our future neural networks into provably safe code. Thank you.
