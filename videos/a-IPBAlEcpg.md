---
id: "a-IPBAlEcpg"
title: "Usman Anwar - Steganography with Applications to LLM Monitoring [Alignment Workshop]"
url: "https://www.youtube.com/watch?v=a-IPBAlEcpg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-01"
duration_seconds: 295
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Usman Anwar - Steganography with Applications to LLM Monitoring [Alignment Workshop]

[Watch on YouTube](https://www.youtube.com/watch?v=a-IPBAlEcpg) · FAR․AI · 2026-05-01 · 4:55

## Description

```text
Usman Anwar (University of Cambridge) presents a decision-theoretic framework for detecting steganographic reasoning in LLMs — that is, reasoning that encodes hidden information to evade oversight. Existing approaches either rely on classical steganalysis (which requires a known reference distribution of benign signals that doesn't exist for LLM reasoning) or LLM-as-judge methods (which lack a theoretical basis and conflate suspiciousness with steganography). The key insight of Anwar and co-authors' work is that steganography is instrumental: it creates an asymmetry in usable information between a receiver who can decode the hidden content and a third-party sentinel who cannot. They formalize this via the "steganographic gap" — a metric comparing downstream utility for each party. As a concrete example: if a reasoning trace is encoded with ROT13, a receiver LLM that knows the scheme performs well on the downstream task while a sentinel that doesn't is left in the dark — producing a large, detectable gap.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] So I am printing this work on behalf of like my co-authors Juliana, David and others. Uh the this talk basically is about like how can you monitor like LM reasoning where it might become stographic. Uh basically what we do is like we kind of provide like a new formization of stography and that in terms allows us to develop like new methods for monitoring straphic reasoning. Uh before we get started like let's look at this train of thought from 03. Uh I want you to like a look at this train of thought and if you feel like you can understand what Alam's trying to say here uh please raise your hand if anyone understand what is saying here. Yeah. So this is like a kind of a very interesting problem. I'm like okay we don't really know what it is saying here. So is this graphic already or is it kind of encoded reasoning? Uh it is probably not. Uh but the only reason we can like say this with time confidence is because like we have kind of a general evidence that like alms find it hard to do right now. Uh not because like we have like very good methods which you could like throw this like you know thought at and be like oh yeah this is like definitely not graphic. Um so yeah specifically like we have like uh two tools available already uh that you could use potentially have prior works try to use.

[1:16] Uh the first one is basically classical analysis. So the way like this sort of works is that like you would take your uh potentially like uh strographic signal and you're trying to like see uh whether like this signal like deviates from like a non-distribution of like benign signals in any kind of a meaningful way. If it does then you see like you flag it as pressure. Uh the problem for applying to LM is that like we don't really know like what LM reasoning looks like. Basically you don't really know like what normal indexes are in some sense. And the other sort of thing that people try to do is like look at uh basically use arm as judges. So we like take this potentially like weird channel of thought we would fade to another and ask it like hey is this graphic or like doing any kind of a hidden messages in this uh channel of thought. U this sometimes works some doesn't really work that well. Uh the kind of the big issue here is something like uh there's no theoretical basis here. we don't really know like when it might work and also that like uh suspiciousness is not always equal to cyography like in that case like even though it looks like suspicious it probably is not graphic.

[2:23] Uh so what do we do? Our main insight is that like instead of looking at the signal itself, uh what we can do is we can like try to prove that this particular signal has higher utility to a party that understands uh the encoding uh the encoding then to a third party may not understand encoding basically. So basically the main sort of first insight is something like uh cography is instrumental uh sender and receiver when they try to use cography they're trying to like achieve some objective which they can't otherwise for example like might want to use cography to like collude or like they uh it might want to hide a misaligned reasoning and in both cases they want to avoid getting caught basically. Um so you can like formalize this and basically like uh uh you can write out some sort of definition basically and sort of the whole idea is that you can look at the utilities and you can sort of measure how much useful the signal is to this receiver and you can sort of also a third party here which we call sentinel and also like measure the usefulness to this third party Sentinel and uh just like comparing like how uh these different differences in utilities you basically can define this metric called graphic gap.

[3:36] And the claim our claim is that like if a graphic then this crap uh this gap will necessarily be greater than zero. Uh we can have an example here. So for example like here we haveing trace from an LM. Uh we have uh in this case we have like encoded in using road 13 uh which is a very common cipher. Uh so it's like know like it's a more encoded instead of it to be precise but like yeah uh and we assume that our receiver LM understands this uh uh root encoding scheme our third party Sentinel doesn't understand this encoding scheme. Uh so what happens is you basically get like high usefulness for the receiver and but like low usefulness for the sent basically and this in turn basically results in kind of a high gap between the performance of these two models. Uh and the whole like yeah we still have a bunch of experiments in our paper where show that like you can like design these kind of a uh test experiments and like yeah we show that you can detect cography or going in these cases successfully. Yeah. This was basically like we have a lot more in our paper. Uh we should look check out our paper.

[4:42] Basically the title is the same as the first slide. Uh yeah. So it's our paper basically. If you have any questions feel free to reach out to me, talk to me uh here or email me.
