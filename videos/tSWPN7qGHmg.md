---
id: "tSWPN7qGHmg"
title: "Dominic Rizzo - Silicon Roots of Trust: Attestation You'd Want Even If Nobody Required It"
url: "https://www.youtube.com/watch?v=tSWPN7qGHmg"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-04-14"
duration_seconds: 802
is_short: false
chapters: 5
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Dominic Rizzo - Silicon Roots of Trust: Attestation You'd Want Even If Nobody Required It

[Watch on YouTube](https://www.youtube.com/watch?v=tSWPN7qGHmg) · FAR․AI · 2026-04-14 · 13:22

## Chapters

- 0:00 Intro
- 0:19 What is a Silicon Roots of Trust
- 4:32 Why Silicon is close to becoming ubiquitous
- 9:55 Benefits of Silicon Roots of Trust
- 11:20 Aligning Incentives

## Description

```text
Dominic Rizzo (zeroRISC) presents open-source silicon roots of trust as a mature, commercially viable solution for hardware security and attestation. The technology, proven at scale in Chromebooks and data centers through his OpenTitan project, enables end users to control what software runs on devices they purchase—a capability currently absent despite ownership. Three forces drive adoption: AI infrastructure buildout, mandated post-quantum cryptography transition by 2030, and mature open-source designs that shift the cost calculus from burden to necessity. Unlike confidential VMs requiring trust in chip makers and cloud providers, bare-metal attestation removes intermediaries from the trust chain. The technology enables supply chain provenance, workload attestation, perfect recoverability, and below-the-metal firmware updates. While regulatory mandates like Europe's Cyber Resilience Act push adoption, Rizzo argues liability shields for implementing NIST-standardized best practices would better align chip maker incentives than punitive approaches alone.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Intro

[0:00] The key thing to understand throughout this talk is that there exists an inexpensive, high quality, inspectable solution that can bring security and enforcement to silicon itself and the supply chain that provides all of it. I started the OpenTitan project at Google that's now being widely

### What is a Silicon Roots of Trust

[0:23] deployed, as my understanding, in Chromebooks and data centers. You can in fact build this stuff transparently and in the open and have a reason to trust it. Now we're taking that and with the GlobalPlatform organization moving into a more standards-aligned way where it scales from very small IoT devices all the way up to the very largest chiplet-based data center chips. I'm going to talk about some of the challenges and opportunities that this technology provides, as well as why I think it's on the cusp of becoming ubiquitous, and also what it can be used for and what it can't really be used for. What is a silicon root of trust? You want to think of this as the enclave below the enclave below the enclave. It is a pretty foundational, fundamental piece of kit in almost all silicon. It's really the security anchor that lives below the lowest layer of software. There are many different types, many different functions. You'll hear people talk about root of trust for measurement, root of trust for identity, root of trust for storage. They're all variations on a theme. You can use the same piece of silicon or the same design to implement all of them.

[1:34] I'm going to focus on one particular kind which is really responsible for having a secure identity, being able to attest that a given chip is authentic and providing the capability to trace that through the supply chain, as well as something that ensures that the correct firmware, the correct software is actually what is running on that particular piece of silicon and also the rest of the platform. From those two properties you can basically build all of the attestation mechanisms, all of the integrity mechanisms that have been brought up even theoretically today. The key thing to realize here is that every system has something at the bottom that you implicitly trust. My view is that that thing should be explicit, transparent and really purpose-built and hardened for security. The silicon root of trust provides this hardware-rooted identity and cryptographic services that you cannot get from software alone. One that's built out of open source can be validated and trusted.

[2:33] What do you use it for? It gets used for a lot, often in an invisible fashion. This is the fundamental piece that enables all of these higher-level security primitives that you really care about when you want to be enforcing any given policy. The big thing is it provides the ability to, without being in the room, remotely attest to some set of properties. Those properties can be: is this the chip I think it is? Those properties can be: what journey did this chip take through the supply chain? They can be: what is the software that's running on this chip? Is it the latest software? Does it have rollback protection, secure boot, whatever? It doesn't matter what the property is. This is just the thing that's responsible for saying yes, it has this property, and yes, I can give you a cryptographic proof that this property exists. It underpins everything. It really better work well and it better be trustworthy.

[3:28] From the workload attestation perspective — I know it's come up a few times — this is a pretty recent thing that's entering general availability. This is attestation for confidential VMs starting to roll out now. But the thing to realize here is that this still relies on trusting both the chip maker and typically the cloud provider, in addition to whatever it is you as an end user are actually wanting to confirm is the right workload, whether it be training or inference or what have you. Even this state-of-the-art workload attestation requires a cross-company leap of faith. Not everyone wants to take that. There are significant research and technical challenges. How do you do data center attestation?

[4:20] How do you do really broad-based, large-scale attestation, and who are you trusting to confirm that attestation? We're pretty far from being able to enforce generic policies.

### Why Silicon is close to becoming ubiquitous

[4:36] I think it's worth talking quickly about why I think this transparent, trustworthy silicon technology is pretty close to becoming ubiquitous. We're at a weird point in technology evolution where there's massive pull coming from the AI infrastructure build-out. There's a lot of money sluicing in right now. There are regulatory forces saying you have to do things differently than you've done them before. The PQC transition — both NIST and in the EU — that shift is mandated to start in 2030. That's actually driving a lot of change down at the lowest layers of the hardware and in the cryptography stacks we use. The other thing that's driving a lot of this is the European Cyber Resilience Act, or CRA. It costs 25-plus million dollars for a modern node mask set. If you're a chip maker, you don't want to have to do that more than once in more than one region. You tend to build for the high bar. The high bar these days is the CRA in Europe — except for China, in which case it always has to be special, and we've all accepted that.

[5:52] The third thing is that this open source secure silicon has reached a point of maturity and credibility where there are — I wouldn't say broadly available, but there are — available designs that have actually been commercially taped out and are shipping at scale in commercial products or in hyperscaler data centers. That's enabled a verifiable solution to this problem without an onerous cost burden. You have the market pull, you have the regulatory requirement, and you have this new enabling technology that fundamentally changes the cost calculus and turns it from a "well, why should I do that?" to a "well, why aren't you doing that?" kind of question. All these are driving us towards mass adoption or ubiquity of these high quality, verifiable silicon solutions. The bad news, from a policy perspective, is that it is my personal belief it's not going to be very likely that any chip maker is going to allow an independent third party to be the decider as to what runs on these devices. Even if these things were available everywhere, even if people had complete confidence in them, the problem is that — whether or not it's a fair comparison — everyone does remember the Clipper chip. If this stuff were to get pushed too far, you'd see a weird alliance between the cryptography community, the folks who do government relations on behalf of the chip makers, and digital rights activists. It'd be a very strange coalition, but it would be a pretty significant amount of pushback. These verification regimes always require someone with authority,

[7:31] and you get really quickly into questions of who and why should they be trusted. I'm going to argue that there is one entity that should be trusted, and that entity is the end user — be that a government customer, an actual end user like an individual, or a large company. One of the more surprising things is that when we buy a chip, when we buy devices, we don't actually own those devices. I'm going to define ownership as the ability to control what software runs on those devices, even very low level in the chip. There's a lot of proprietary software that runs. There's a lot of things that you're unaware of that run, and you don't really have any control over whether or not that runs the way things are organized today. I talked a little bit about workload attestation in the form of confidential VMs. That's pretty state of the art, but that still includes a lot of stuff that you don't control that may be secure, may not be secure, but there is still that leap of faith. This isn't necessary — we don't have to do it this way. It's just how things are organized today. There's this notion of bare-metal attestation where you're really moving things a lot closer to having the person who pays for the device, who pays for the silicon, who pays for the platform, control what actually runs on there. It's a pretty good outcome as far as things go. It is very reasonable to say, well, I should be able to govern my own workloads, I should be able to control what runs on that

[9:07] because I purchased it. That applies no matter who that end user necessarily is. The key thing here is that this open source silicon root of trust technology enables a chip maker to make and sell chips — which is what they prefer to do — while also letting the end user control what is actually executing on those chips. You can keep the third-party verification, you can drop the third-party verification, but the point is that you as a consumer do have a choice in who is providing those services — are they adding value, or are they simply interfering with the business of business? Either way, this trusted attestation of chips, the supply chain provenance, the workloads, it all begins with this silicon root of trust, which is typically hidden pretty deep into the system.

### Benefits of Silicon Roots of Trust

[9:58] There's a lot that's actually achievable. It's a pretty good news story. With these technologies, they're actually a significant win based on how things are done today. This core security primitive enables everything from supply chain provenance to workload attestation to perfect recoverability. That recoverability — my view is that as these models enable more effective, more scalable cyber attacks, you are going to need to be able to control your devices all the way down below the software at the hardware layer. This is how you accomplish that. You're going to need to be able to recover any system at any point in time, and this is how you do it. You can also think of this, if you want to get dramatic, as the kill switch for killer AI — or really just the ability to own the hardware that you are paying for, that someone is paying for.

[10:52] The real questions revolve around who gets to determine what's authentic, who gets to build evidence for trustworthiness, and make those decisions for what to do with those results. If we move a little bit away from worrying about controlling those workloads and more towards making the supply chain, making the silicon itself more secure, more controllable, more ownable, that's actually a pretty achievable policy goal.

### Aligning Incentives

[11:20] I'm going to close out and open up to questions by saying: not a lawyer, not a policy expert, but I am a practitioner who has deployed these technologies at scale in the US and in Taiwan. My advice as a practitioner is really to worry more about aligning incentives. If you give chip makers a reason to voluntarily incorporate these security features that happen to enable the kind of governance primitives that you might want, you will see a much greater uptake in adoption. These chips are inherently global. The whole ecosystem is global. They're not going to be keen on biasing for one government's control over another, but they are very responsive to customer requirements and they are very sensitive to liability. What I'm suggesting — and again, not an expert here — is some sort of a liability shield for the chip makers, so that if they choose to implement a set of best practices which would probably be standardized by NIST, then they get some protection. Right now in Europe they're really tackling this from a punitive angle with the CRA. But I think there's a carrot as well that can be put out to these folks, whether that be through OFAC or through BIS, whatever it is, where you can align these incentives and say, look, just do this the right way and we'll give you some level of protection.

[12:52] The way to think about this is the security properties of these open source implementations are publicly auditable. You have reason to trust them. This also simplifies any certification process, so it really lowers that barrier to getting approval. It's one way in which today you can really build a much more trustworthy, secure silicon supply chain which has ripple effects all the way out into production. That's it. Thank you.
