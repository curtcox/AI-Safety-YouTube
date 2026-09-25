---
id: "Tqc9AXjHVhQ"
title: "Sarah Cen - AI Supply Chains: An Emerging Ecosystem of AI Dependencies [Technical AI Policy]"
url: "https://www.youtube.com/watch?v=Tqc9AXjHVhQ"
channel: "FAR․AI"
channel_id: "UCCV6kbjBZje3LPxRp0NHfxg"
channel_url: "https://www.youtube.com/channel/UCCV6kbjBZje3LPxRp0NHfxg"
upload_date: "2025-11-19"
duration_seconds: 557
is_short: false
chapters: 6
transcript: {"source": "manual", "language": "en-US"}
collections: ["channels/farairesearch"]
retrieved: "2026-09-25"
---

# Sarah Cen - AI Supply Chains: An Emerging Ecosystem of AI Dependencies [Technical AI Policy]

[Watch on YouTube](https://www.youtube.com/watch?v=Tqc9AXjHVhQ) · FAR․AI · 2025-11-19 · 9:17

## Chapters

- 0:00 Introduction to AI supply chains
- 0:23 Mapping the AI ecosystem
- 2:15 Defining dependencies
- 3:11 Importance of supply chains
- 6:21 Project goals and tools
- 7:22 Methodology and future outlook

## Description

```text
Sarah Cen's work sheds light on the importance of mapping AI supply chain relationships to address issues such as single point failures, market concentration, accountability diffusion, and talent shortages. 

Highlights:
AI industry fragmented into specialized actors
Single failures can cascade through the supply chain
Dependencies concentrate power in key organizations
Accountability diffuses across multiple actors

Note: The opinions shared in this event are those of the speaker(s) and may not represent the views of FAR.AI or their affiliated organizations.
```

## Transcript

_Source: human-made captions (en-US). Timestamps are [m:ss] from the start of the video._

### Introduction to AI supply chains

[0:05] All right, so today I want to be—I'm going to be talking about AI supply chains, this emerging ecosystem of AI dependencies. And my name is Sarah, and this is done in collaboration with Lindsey Gilmard, Rishi Bomisani, Jonathan Xua, Daniel Ho and Percy Leung at Stanford HAI and RegLab.

### Mapping the AI ecosystem

[0:23] All right, so we have an expanding AI ecosystem. As many of us know, AI is booming. We have actors including model developers like OpenAI, Anthropic and Google DeepMind, hardware providers like NVIDIA, AMD and Intel, hyperscalers like Microsoft Azure, AWS, GCP, data managers like Databricks, Scale AI, and MLOps platforms like Weights and Biases and Hugging Face, and of course, countless applications of AI downstream across various industries in healthcare, insurance, education, and so on. Okay, so what's the point? Well, we've had actually some other folks do a very nice job of mapping out this ecosystem here. In 2012, someone named Matt Turk created this big data landscape. I think it's part of something known as the MAD Report. In 2012, it's crowded, but it's still legible. We can still pick out who the main actors are. He did this approximately every year over the past decade and a half. In 2024, it looks something like this and of course, completely illegible.

[1:28] But that's kind of the point. We see a lot more different types and categories of actors emerging. And we see that, you know, the AI ecosystem has basically fragmented a lot, and various individuals and various actors are now starting to specialize within some niche to provide some service in order for this sort of industry to flourish. Various other organizations have also done this. So this is by Menlo Ventures—they map out the AI stacks. So they have these four layers, from compute and foundation models to data to deployment to these observability tools. And they map out who are the actors in this space. And CB Insights does this as well. They have this AI Top 100 of 2025 map, where again, they have a different categorization, but they're still trying to map out these actors. All right,

### Defining dependencies

[2:15] so why am I bringing this up? Well, for the most part, we have developed an understanding of who these actors are and what they have to offer, but the relationships and dependencies between actors remains largely underexplored. And this is what I want to focus on. And by relationships and dependencies, I mean that there's this flow of products, services, models, data, infrastructure, talent, capital, compute, and more between AI actors. This is a figure just taken from some blogs that collaborators and I at MIT wrote back in 2023 where we are showing just sort of this AI supply chain that can emerge just amongst models. So you might have base models at the top that are then repurposed for summarization and speech-to-text and so on that are then again repurposed for hiring, podcasts, email, autocomplete and so on. And of course, this type of dependency extends beyond models and we can also see data sets and more start to come into play. All right, these dependencies and relationships

### Importance of supply chains

[3:13] matter and I'm just going to run through four quick reasons why. One is choke points. Choke points I'm referring to as these various entities that many AI actors depend on. And I like to kind of pull from this XKCD, which came long before sort of the Gen AI revolution. And it's kind of inverted here where, you know, have the base and foundation at the bottom and then everything that's built on top of it going upwards. And I think it points out kind of a funny—like, you know, all modern digital infrastructure, there's this like tiny little pillar, it's a little precarious at the bottom. A project some random person in Nebraska has been thanklessly maintaining since 2003. And mapping the dependencies between various actors can help us expose these points of failure, these potential areas where we can get cascading failures.

[4:04] This of course, is important for industry resilience and is something that dates back to much more traditional supply chain research of where we want to look at, where for instance, the food supply chain might fail. We might also be interested in market concentration. Similarly, we're trying to identify maybe where there are a lot of dependencies here. But if there are many dependencies on a small number of entities like GPT or cloud, market concentration can emerge. And mapping these dependencies shows where power concentrates. This is important if you're interested in antitrust, of course, but also if you're interested in just governance and safety overall—what are the organizations that you should be targeting, where should you be paying attention to policies and so on. You might also be interested in accountability. And so what has happened, why the AI supply chain has emerged is because we've been having various different entities start to specialize in different parts of AI development.

[4:57] And what this results in is the spread of accountability and liability across various actors. I forgot to include it here, but there are other folks who've written on this, including Witter and Nafis, I believe in a paper from 2023. And supply chains can also cause these upstream entities to cause widespread but diluted downstream effects, risks and harms. And so mapping out these dependencies can kind of help us trace these downstream effects if we're interested in, for instance, risk measurement and risk management. And it can also help us trace responsibility. For instance, if we believe that private rate of action is really, really important going forward, not just centralized governance, then we need this ability to trace responsibility and contributions. And the last that I want to highlight is talent. So one of the things that we're doing is mapping the flow of talent and personnel across organizations. This can help to track talent shortages where there exist close relationships, for instance, at the sort of board of directors level, conflicts of interests and more.

[6:00] And this is important if you're interested in AI, labor, education and immigration policies, as well as conflicts of interest, antitrust. Why did I bring up all these points? And by the way, there are many more reasons you might be interested in these dependencies, some of which I think folks here have spoken on in earlier sessions. So I didn't want to kind of repeat what they've said. But our goal is to help

### Project goals and tools

[6:24] map out these dependencies in the supply chain, track the flow of products, services, infrastructure, data, talent, capital across the AI industry. And this is a screenshot from one of the messy unfiltered versions of the graphs of the type that we're generating. And when you look closer, this is sort of very first version and we're still iterating on it. It's not yet public, but you can find—you can click on these edges and really they'll tell you who are the different actors. And here in Mistral, use the infrastructure from Google Cloud. And if you click on Google more info, we run through kind of where we're drawing those inferences from. So what are the articles, what are the filings, what are the other databases where we're getting this information? And you can use that to then navigate to the original data source. One of the features that we're building in is that you can kind of threshold and filter through this graph as needed.

[7:20] You can look at specific organizations and so on. And I just wanted to take just a second

### Methodology and future outlook

[7:26] to talk at a very, very high level about what we're doing methodologically. We're focusing on public data sources. So we're using Google search, archive papers, Google Scholar, SEC filings, other sorts of databases that we can get our hands on as the public. And we're doing that very intentionally because we want to surface what is the information that we can get as third-party actors. If there's information that we cannot get, then maybe that informs some sort of very targeted policy recommendation on the types of transparency that we need. And we're already seeing that a lot of things are hidden behind confidentiality clauses within contracts between two actors. And so that is part of the message that we're hoping to be able to convey. And the second is we do a lot of categorizing, a lot of data cleaning, a lot of filtering, often with the help of a large language model to help us kind of distill information down into a digestible form.

[8:26] For the start, we're studying concentration of talent and capital. We're studying potential choke points as well as asymmetries and information reporting. To just explain the last one a little bit, what I mean is that we have a lot of different types of data sources and we want to understand where is certain information being disclosed and where is it not, and we actually find these asymmetries. So what a company conveys on a press release might be different from what they convey within an SEC filing, which might be different from what TechCrunch conveys in their coverage of some announcement. Please reach out to chat. This is my email, this is my website, and I'm very happy to talk about potential applications of this. Thank you very much for your time.
