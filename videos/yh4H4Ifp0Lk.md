---
id: "yh4H4Ifp0Lk"
title: "Rogue OpenAI models hacked Hugging Face to cheat on a test"
url: "https://www.youtube.com/watch?v=yh4H4Ifp0Lk"
channel: "Rational Animations"
channel_id: "UCgqt1RE0k0MIr0LoyJRy2lg"
channel_url: "https://www.youtube.com/channel/UCgqt1RE0k0MIr0LoyJRy2lg"
upload_date: "2026-08-09"
duration_seconds: 151
is_short: true
chapters: 0
transcript: {"source": "manual", "language": "en"}
collections: ["channels/rationalanimations"]
retrieved: "2026-09-25"
---

# Rogue OpenAI models hacked Hugging Face to cheat on a test

[Watch on YouTube](https://www.youtube.com/watch?v=yh4H4Ifp0Lk) · Rational Animations · 2026-08-09 · 2:31

## Description

```text
#rogueai #aisafety #warningshot #aialignment #computersecurity 

Writers:
A.G.G. Liu | signoregalilei.com
Emanuele Ascani

Editing & Narration:
Rob Miles | https://www.youtube.com/c/robertmilesai 

Directed by: 
Hannah Levingstone | @hannah_luloo (insta)

Art Director: 
Hané Harnett | @Peony_Vibes (Threads) / @PeonyVibes (Insta)

Production Manager: 
Kristy Steffens | LinkTree / @kstearb (Insta)

Compositing: 
Skylar O'Brien | @mutodaes (Insta)

VO Editing, SFX & Mixing:
Tony Dipiazza | ad.audio.post (Insta)

Music:
Epic Mountain 

Attributions
All stock footage/photos obtained through Canva
```

## Transcript

_Source: human-made captions (en). Timestamps are [m:ss] from the start of the video._

[0:00] A rogue OpenAI model escaped containment and broke into another company. Yes, in real life. Here’s what we know. It all started as an internal test. OpenAI was testing some models, including a new unreleased one. They wanted to test how strong these models were at hacking. So they ran them on “ExploitGym.” In which AI agents have to exploit vulnerabilities in isolated systems and retrieve protected secrets. For this test, OpenAI used models that were less likely to refuse cybersecurity tasks than the ones they release to the public, which come with guardrails. They wanted the model’s full unleashed capabilities, and they were about to get them. The problem was, the models weren’t supposed to be able to get online. To keep these hacking models contained, OpenAI had put it in a sandbox that was cut off from the internet, except via a limited tool that could only download new software packages for the AIs to use.

[0:53] But that wouldn’t stop an elite hacker. After lots of computation, the models were able to find and exploit a previously unknown vulnerability in the package downloading tool. Then, they used their new foothold to gain more privileges and move through OpenAI's computer systems until they reached a node that was connected to the outside internet. Once online, the AIs inferred that another company, Hugging Face, might host the solutions to ExploitGym. So, rather than solving the test as intended, they decided the best course of action was to steal the solutions from Hugging Face's database in order to cheat on the test. They used stolen credentials and newly discovered vulnerabilities to find a way to run code on Hugging Face's servers. In the end, they scored their prize: test solutions for ExploitGym.

[1:40] The heist was successful, but the thieves didn’t escape unnoticed. Hugging Face's own AI-assisted security system flagged suspicious activity to the human operators. So they set more AIs to work on reconstructing it, sifting through a log of over 17,000 actions the attackers had taken. Ironically, the production versions of ChatGPT and Claude wouldn't help because the guardrails make them refuse cybersecurity questions, so Hugging Face had to use a weaker open weight model instead. On July 16th, 2026, Hugging Face announced to the public that an unknown AI agent system had hacked them. 5 days later, OpenAI admitted that it was their test that had caused the breach. For years, AI safety experts have been warning of this possibility: that unreleased AI systems could hack their way onto the open internet.

[2:29] Now, it’s our reality.
