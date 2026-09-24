---
id: "q6iqI2GIllI"
title: "Rabbits, Faces & Hyperspaces - Computerphile"
url: "https://www.youtube.com/watch?v=q6iqI2GIllI"
channel: "Computerphile"
channel_id: "UC9-y-6csu5WGm29I7JiwpnA"
channel_url: "https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA"
upload_date: "2014-09-17"
duration_seconds: 538
is_short: false
chapters: 0
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/computerphile"]
retrieved: "2026-09-24"
---

# Rabbits, Faces & Hyperspaces - Computerphile

[Watch on YouTube](https://www.youtube.com/watch?v=q6iqI2GIllI) · Computerphile · 2014-09-17 · 8:58

## Description

```text
Hyperspace was hijacked by science fiction, but what is a space? Robert Miles explains with the use of small red rabbits and human faces.

How Broadband ADSL Works: http://youtu.be/uwtGfyna62I 
Busy Beaver Turing Machines: http://youtu.be/CE8UhcyJS0I 
Public Key Cryptography: http://youtu.be/GSIDS_lvRv4 

http://www.facebook.com/computerphile
https://twitter.com/computer_phile

This video was filmed and edited by Sean Riley.

Computer Science at the University of Nottingham: http://bit.ly/nottscomputer 

Computerphile is a sister project to Brady Haran's Numberphile. 

See the full list of Brady's video projects at: http://bit.ly/bradychannels
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

[0:00] So sometimes you hear about configuration spaces, feature spaces, hyperspaces, uh uh vector spaces, whatever. What is a space? Well, um you will all have come across them before as um like scatter plots or just graphs in general are a representation of a space. If you have a two-dimensional space, that just means that you have two axes on your graph. You've made a plane, right? a flat surface. It's two-dimensional. Here's one dimension. Here's the other dimension. Right? Let's say we've got some animals and we want to think about those animals in a more rigorous way than just just talking about them. We want to do some maths about the properties of these animals. Like we're interested in the color of them and their weight or something like that, their size. So, so let's say that with some random species of animal where the the females tend to be um red and large and the males tend to be blue and small for example. So you've got two axes here and you can say this one here is uh size and this is color on a scale of red to blue. Right?

[1:12] So so um you've got like a zero is red. This is just a random example and 100 is blue and then so you know 50 is like purple and then if you've got a group of these animals you can then plot them. So suppose you've got some over here each one of these crosses represents a single specific animal and each of these circles is also an animal. In this case this is a female animal if I remember correctly. And you can look at this and if you want a machine to do something intelligent, you want a machine to understand this, there are things that you can see. You can see firstly that there's these sort of clusters, there are clustering algorithms that will automatically identify end up sort of drawing a circle around this and saying that's one cluster and a circle around this and saying that's another cluster.

[1:59] When Amazon is trying to tell you what kind of things it thinks that you want to buy, it may make a space of all of its users with each person being a point in that space uh and the dimensions being um what things they bought. Then you'll find that the difference between you and another person, you can place a number on it. How similar are we? You know, have I bought the same kind of things that you've bought? There are algorithms that do that or algorithms where they can sort of look at this space and sort of draw a line through it and say, "Okay, well, it seems like sort of anything on this side seems to be male and anything on this side seems to be female." Even though there's overlap, even though this is fuzzy, you can make an educated guess based on these properties. And you can do other things like take this and say, "Okay, of this cluster, where's the middle of it?

[2:46] Where's the densest area? What does a typical female size look like? What does a typical female color look like? What does a typical male color or size?" So if you've got your average one here and you've got your average one here, then you can draw a line between them for example in this space and then say okay then you can map everything onto this line and then you get a continuum between male and female. Don't know why I chose male and female. It's getting into like politics which is not where I'm trying to go with this but just as an example. So the point is various things like you can say how typically female is this specific one and then you can actually measure it. Right? Before you had to just kind of guess, but now you can say, well, it's you take the average, you take the distance to the average, you just measure what this distance is and that gives you an actual number that you can use. You're taking stuff that would normally require a human intelligence. How typical is this or how how male is this or whatever and you are turning it into numbers. You're turning it into maths so that a computer can understand it. So here, this is an example of a two-dimensional space, right? But if we chose to model a third thing about the animals, I don't know, the speed that they run or something, we could have a third axis, right? You could you could have this one coming off here being speed. We end up with a three-dimensional graph. And now it's very difficult because I'm I have two dimensional paper and I'm trying to express a threedimensional ID on it. But basically, so these end up being all spread out. Each of these dots is now somewhere along this speed axis as well.

[4:10] They form a 3D sort of cloud. So this line would become a surface, a plane. Here you have a two-dimensional space. To divide it in half, you need a one-dimensional object, which is a line. Here we have a three-dimensional space. So to divide it up, we need a two-dimensional object. The dividing line is always one less number of dimensions than the space. We're measuring three things about these animals. We could measure any number of things, right? We could measure 150 things. And that's fine. The maths works exactly the same in 150 dimensions. Uh you can't draw it on a piece of paper. You can't think about it in your head, but the maths is the same. And oh yeah, we should talk about feature vectors. Totally straightforward. So when we have a two-dimensional space, you take a particular creature. There we are. This red rabbit. And we measure how much it weighs. We're doing size by weight, let's say, and we say that it weighs, you know, a gram. And we say, what color is it? Well, it's red. It's really very red. So it's about zero.

[5:11] And this this is now a feature vector. It's a feature vector of length two because it's a two dimensional space. So each data point is represented by a feature vector which is a point in the feature space. So there's some fun stuff that's been done with, for example, uh faces, right? Human faces to to look at a human face and say, is that a male face or a female face? Um that's the kind of thing that you would think that you really needed a human to do. How would you even go about telling a computer how to do that? Right? This is the kind of challenge that these kinds of algorithms can tackle. So, it works out to be exactly the same. You measure a load of things about the fa, you know, the distance between the eyes and the length of the nose and the width of the mouth. You measure everything you can measure about the face and then you plot them all in a very highdimensional space. You tell it certain things which one's male and which one's a female. You find the average male and the average female. And that's interesting as well because then you can take this data, you can take this point in space, right?

[6:08] Each point in space represents a possible face. Everywhere in the space is a face. It's a face space, if you will, right? Is that a social network? Yeah, it was a failed social network. Um, but so it's a it's a feature space, right, of faces. And then these certain points represent specific faces that you've actually loaded in and said this is a man's face, this is a woman's face, whatever. So then you can find the typical male face. But then you can do the same thing where you plot a line from the typical male to the typical female. This line is is indefinitely long. Which means you can take, for example, a face and you can make a face which is more male than any actual human person's face, right? Or more female. And the mathematics of this emerges completely naturally. You're just following this line along. And you end up with these grotesque things. But a certain percentage away past the end, what you end up with is kind of cartoon caricatures. So the males end up with these like vast, you know, big brows and big bulky jaws and the women have like enormous eyes. They end up looking like anime characters or whatever. Before you have this kind of concept, how do you even approach the concept of how do you draw a caricature of a human being with a computer? But now we can do it, right?

[7:18] Because we have this concept of doing basically geometry in a feature space. Generally, when you when you throw real world data into one of these spaces, it will be clustered because the real world does tend to be clustered, right? Um, it's just kind of the way that things tend to work out. So, people who are like me will be next to me in Amazon. I'll be I'll be I'll be part of a cluster of people about my age, my gender, my, you know, level of uh education and wealth and everything else. People who tend to buy similar things. And so then if somebody who's very close to me in that cluster buys something else, then they can kind of infer that I might be likely to buy that thing as well. That's something that that Amazon does, something that uh you know Netflix does with their films, all of these kind of uh all of these kind of predictive things where you just throw the data in and the maths doesn't really know what it's dealing with. It doesn't know that I'm a that I'm a person, not an animal, or that what I'm measuring here is, you know, propensity for buying computer games instead of mass. The maths is is broadly the same. Um, and so you can make you can make computers tackle all sorts of problems which um which previously they couldn't. If you take a celebrity and you draw a line between average and the celebrity and then continue that line, somewhere out along that line is a cartoon caricature of that celebrity.

[8:46] Right? Because you've taken the ways in which their face is different from the typical average face and extended it and exaggerated them. And this is exactly what caricature artists do. Now we can do it with maths.
