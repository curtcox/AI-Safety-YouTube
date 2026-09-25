---
id: "ftNeYtDDuUo"
title: "Shay Yahal - The case for Securing Automated AI R&D"
url: "https://www.youtube.com/watch?v=ftNeYtDDuUo"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2026-05-13"
duration_seconds: 226
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Shay Yahal - The case for Securing Automated AI R&D

[Watch on YouTube](https://www.youtube.com/watch?v=ftNeYtDDuUo) · FAR․AI · 2026-05-13 · 3:46

## Description

```text
Shay Yahal (Redwood Research) argues that the cybersecurity playbook does not translate cleanly to automated AI R&D, and that trying to retrofit it is misleading the field. 
She breaks down three assumptions that quietly fail: 
First, what we protect: classical security defends assets like data, credentials, machines, and in AI labs the conversation defaults to model weights, but the more important object is decisions, what research direction to pursue, what training run to launch. Decisions are not assets and don't behave like them. 
Second, what we look for: syntactic patterns and known byte strings worked when attacks were expensive to develop and got reused, but the risk in AI R&D is semantic, with no string that says "this is training toward dangerous capability." 
Third, how we detect: anomaly detection assumes malicious activity looks different from legitimate, an assumption a scheming agent will deliberately break, and one we couldn't act on anyway because we don't really know what normal looks like inside an automated R&D pipeline.
She closes by pitching a hybrid she is provisionally calling "untrusted labor security" and asking for better names.

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] All right. Uh hi, I'm shy. So, many of you have heard probably about some model that injected code and to elevate its permissions and lied about it later. And that's a security problem. So, it got me with Tyler from Redwood to think about how what is really means to secure the process of automated AI R&D. And the honest answer is that a lot of the solution we develop in cybersecurity like sandboxing and access to info are based on multiple assumptions that are not transforming that well into AI R&D. And we're going to talk about them. So, the first assumption is about what we protect. In cybersecurity, we are used to protect assets. So, we protect our data, our credentials, maybe like uh >> [snorts] >> I don't know, machines. And in AI R&D, there is one asset we all talk about that we need to defend, which is the model weights. But actually, the most interesting object is not an asset, but decisions. So, that's like what research direction should I pursue or what kind of training data do should I use? And that's just a different object to protect than an asset.

[1:12] The second one we like like relates to what we are looking for. So, for years developing new techniques in cybersecurity like new attacks was really expensive. So, people just reuse known techniques. And as a defenders, we just like looked for patterns and like known syntax. And we had like huge list of I don't know, code strings that we can look for. But when we talk about AI, the risk is not syntactic, but semantic. And there's there's no like a I don't know, list or like string of bytes that we can say that it's like train the model toward more dangerous capability. And the last one uh is actually about more interesting detection technique. So, sometimes when you don't know how the risk would look like, we look for deviations from normal. Uh and we have like, I don't know, anomaly detection and behavioral analysis, which is interesting. But, they [snorts] still they lies like implicit assumption that malicious looks different than legitimate. And in in AI R&D, that might not be true. First of all, we can have scheming agent that try to conceal its behavior. Uh but, also we don't really sure what normal looks like, so we can look for deviation.

[2:31] So, traditional security out. Uh what can we use? And actually, cybersecurity uh is not that good with handling internal threats. But, national security is really interesting. So, for example, banks Never mind. So, for example, banks uh forces their employees to take mandatory vacations to see what breaks when they are gone. And we can just translate that, for example, through re-sampling. Also, in national security agencies, uh they very like keep very freely uh on need-to-know basis segregation. And here, we can say that that uh no single agent will be in charge of the full pipeline. Uh and that's the playbook that was actually designed to our threat. And I think it's going to imply interesting thing about what this field needs to be.

[3:21] So, I'm here to pitch a new kind of hybrid between security and control, which I currently call uh untrusted label security, but feel free to pitch me other names. Uh and I think it's going to be really interesting and really important. Uh come and look for me later. >> [snorts]
