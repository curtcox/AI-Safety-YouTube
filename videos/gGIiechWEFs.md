---
id: "gGIiechWEFs"
title: "Tricking AI Image Recognition - Computerphile"
url: "https://www.youtube.com/watch?v=gGIiechWEFs"
channel: "Computerphile"
channel_id: "UC9-y-6csu5WGm29I7JiwpnA"
channel_url: "https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA"
upload_date: "2022-07-27"
duration_seconds: 752
is_short: false
chapters: 10
transcript: {"source": "auto", "language": "en-orig"}
collections: ["channels/computerphile"]
retrieved: "2026-09-24"
---

# Tricking AI Image Recognition - Computerphile

[Watch on YouTube](https://www.youtube.com/watch?v=gGIiechWEFs) · Computerphile · 2022-07-27 · 12:32

## Chapters

- 0:00 Introduction
- 0:18 Object Detection
- 1:00 Imagenet
- 1:51 Data
- 3:07 Category
- 4:05 Number
- 5:50 Classes
- 7:00 Remote Control
- 7:17 Blank Slate
- 11:04 Re categorization

## Description

```text
AI Object detection is getting better and better, but as Dr Alex Turner demonstrates, it's far from perfect, and it doesn't recognise things in the same way as us. 

https://www.facebook.com/computerphile
https://twitter.com/computer_phile

This video was filmed and edited by Sean Riley.

Computer Science at the University of Nottingham: https://bit.ly/nottscomputer

Computerphile is a sister project to Brady Haran's Numberphile. More at http://www.bradyharan.com
```

## Transcript

_Source: YouTube auto-generated captions (en-orig). Timestamps are [m:ss] from the start of the video._

### Introduction

[0:00] So we are going to look at object object detection with neural networks and we are going to see if us humans detect objects in the same way as neural networks. And to do this we're going to trick the neural networks and see if we're tricked in the same way.

### Object Detection

[0:18] Let's do some object detection. We're going to take a picture of something. So we've got some sunglasses here and then I will email that to myself. So we've got the emailed uh image here which we called image. Nothing too technical. So we can see the sunglasses there. We're going to go into mat lab and we are going to first of all we're going to load our network. And then what we're going to do is we're going to get our image. This is a pre-trained network done by someone else forum object detection. We have to resize it to 224x 224. This is the size of image that ResNet accept. So it has to be that size. So we've got our image and then we can classify it and it will give us two things back. But the one we're most interested in is this variable called cat, the category. Write that out. We've got some sunglasses in our image. So,

### Imagenet

[1:01] what's going on there? There is a repository of images online called ImageNet. And what this is is it's just an array of images that are annotated with an object that's in them. And you can um submit your neural network or your artificial intelligence to see how well you can classify these images. So, at the moment, the record is about 91%. Um, and there's a thousand categories. So, this is a really difficult task. So, 91% is pretty good. And looking at all of the categories as well, they're not things like um cat and dog. They're a certain breed of cat and a certain breed of dog. So actually very difficult and I imagine most people will probably get between 95 and 98% something like that. I'm not exactly sure. So ResNet that we're using um gets about 70 71% which might seem quite low but when you've got a thousand categories it's actually really good. And the reason we're using

### Data

[1:52] it as well is because it's a bit smaller than some of the other networks and because we're going to be running it a lot of times. Okay, so there is a lot of data inside ResNet. It's a 44 megabyte download I think and probably about 2/3 of that are just raw numbers. So there's millions and millions of parameters in ResNet. There's been some videos on convolutional neural networks before and this is um what we've got here. And with this amount of variables, it's very hard to understand what's going on on the inside of the network. So there are some videos with Mike where he's talked about analyzing the layers of the convolutional network to find features and so on and so forth. And this is really good. However, in the networks that are becoming very good at this type of thing, there's a lot of layers and there's a lot of numbers in there. And as human beings, we just can't make sense of that much data. It doesn't mean anything to us. So, how do we try and figure out a little bit of what's going on in here? If you give ResNet an image, we will essentially get a vector of numbers. So, we've got a thousand categories, any image could possibly be, and it will give you a value, and all these values will add up to one hopefully um specifying how likely it thinks a specific object is in that image.

[3:02] So, for instance, that picture of the sunglasses might have been.1% cat or something like that.

### Category

[3:07] Yeah, exactly that. And we can actually see it on the screen. We've got category and we've got res. And res actually is this information. So it's basically a vector of size a thousand which specifies these odds. So if we just plot this when it comes up we should see that it was a likelihood of 0.68 something like that. Now the other probability is so low you can see a little bit of a spike. So it was it thinks that something here. So that big pointy spike in the middle that's sunglasses. That's sunglasses. And if we look at 766. So mat lab counts from one but this list is zero. So, we're looking for 765. A rocking chair. Close enough. Should we check another one? It thinks there's a little bit of rocking chair. Is that spike 422? So, 421 banister. I suppose with the wood a little bit of a chance, but it's pretty sure that is just a pair of sunglasses. So, you're right.

[3:55] Sometimes it's really not sure and you get a lot more peaks and it just happens to be the highest one and that's what it classifies um as the object in the image. Okay. So, ResNet gives you a

### Number

[4:07] thousand numbers. So, if we just do a small one, we got 0.1, 0.3, and 0.6. So, this could be cat, dog, giraffe. So, it'll think that 0.6 being the highest value for this class. If it was only outputting three classes, you would say it's this one, which corresponds to a giraffe. These numbers are actually very precise. So, they have um quite a few numbers after the decimal point. So what we can do is we can have an image which we're going to give to ResNet and we can focus on one of these classes. So this number here 0.3 could be 0.317 928. Okay. [snorts] So very precise. So small changes in the image will affect this. If a giraffe is in our picture and it is 0.6 what we can do is we can just change one pixel in the image just one. and we can see how this number changes. Okay?

[5:03] So, if it goes ever so slightly up, what we could do is we could keep that change. And if it goes ever so slightly down or or doesn't change at all, we can reject that change. And if we do this over time, we'll be able to make small changes which will change this number and hopefully increase it until that is the category that is seen in the image and not the giraffe. So, this this number will go down and this one will go up by only changing one pixel at a time. And we can keep on doing this and incrementally move more towards a different classification. So, we're going to do this with a picture of the remote control. This is something that we all know what this is. Uh, this is my remote control um from home that I took a photo of. What we're going to do is we're going to use this image and we are going to try and trick ResNet into mclassifying it. Let's say we're going to turn this remote control into

### Classes

[5:50] something else. So the classes I chose are coffee mug, computer keyboard, envelope, golf ball, and photocopier. So we're trying to change the original image here of the remote control into another image according to ResNet by just making these small incremental changes. So we've got our remote control and then we can look and see what um the changes that were made to turn this into a coffee mug. And here we go. So that's it. For all the changes that it's made to the image, it now thinks that that is over 99% likelihood of being a coffee mug. Can you see a coffee mug there? If it is, it's uh it's definitely by one of the more abstract artists. Exactly. Right. And then we can go computer keyboard. I mean, there's some space here surrounded by some boundaries. I mean, it it's loose.

[6:38] Similar things happen. This is an envelope. Doesn't like an envelope. This is a photocopier. And we have a golf ball here which is slightly different. It just seems to me that there might be some attempt to get the dimples on a golf ball. I mean again it's very very loose. We can categorically say that if we gave that to a person they would say there's a remote control in that image and some noise.

### Remote Control

[7:00] And I can imagine that you know that's you've cropped that remote control to be on a white background. But if that was say a carpet or something like that you wouldn't even notice a difference. Exactly. Yeah. um especially it was higher resolution as well um and you're less able to see those dots. Um yeah, that's very much the case. Um so

### Blank Slate

[7:17] something made me think after doing this maybe maybe there's something about a remote control which is just inherently confusing. Maybe I picked a class which is difficult for it to recover from and move to a different class. Not that it's ever trained to do that. So I thought I'll give it a blank slate and start with a completely blank image and then see what representations would it make if it doesn't have to change anything. it can just go from blank image to whatever it wants. So, the same thing, just making one incremental change at a time and adding it up until it's 99% sure it's a certain class. This is our coffee mug. That looks like the world at night from the ISS with just a few lights over Africa. Not a bad shout. Computer keyboard. If we're being truly optimistic, that could be a key, but it's not the best rendition of a keyboard. This is an envelope. I say there's not much there, but it's I mean these are all 99% sure.

[8:08] So it is really sure that these are certain things. So here's an interesting one actually. The golf ball. Now it's definitely not a golf ball, but it seems that there is an attempt there to make something that looks like the dimples in a golf ball if you're trying to give it the benefit of the doubt. And that's probably the feature that is most looking for. That's what it thinks a golf ball is. So not necessarily round per se, but these dimples. And the last one is the photocopier. So something's going on in ResNet in a way which we just can't rationalize. I'm pretty sure that if you edited a picture and put some pixels in certain places, we wouldn't be fooled by it. So something like ResNet could make a pretty decent attempt at a driverless car. So it could probably stay within in between the lines, do some accelerating and braking. For motorway driving, I think it would be pretty good. But when you have things like this and things you can't really interpret very well, like a little ray of sunshine reflecting off a water drop on a leaf like 20 yards over there and some other things, you could get some strange behavior. However, on aggregate, you wouldn't I think so to actually make an effort to try and sort of spoof these networks and make them mclassify something um is is like a dedicated task. For it to happen naturally, I think is exceptionally rare. However, um you just don't want it to happen at all.

[9:24] And it would be great if you could understand this. And it would be it would be great for sort of just our understanding and our happiness with this if it did draw a golf ball or something like that. So when there's lots of blank space, the envelope was quite sparse. Yeah, there's not much going on in envelope. So it looked like it made a lot more changes for a golf ball than an envelope. But I was thinking, how good can we get this? Minimum number of changes. Minimum number of changes. So, cuz you mentioned it was on a white background, so the change a bit more obvious, but can we get it close enough so that it's really there's really not much going on there. So, obviously I've shot myself in the foot there with it being a white background cuz you can notice all the changes. But what I did is I went back to my trusty friend, the genetic algorithm, which we spoke about in a previous video. So, if you're in the desert and you had one rucks sack, you'd have to fill it with the most valuable items. And the fitness function of the genetic algorithm is just to try and maximize the value um of a certain a certain category. So the number attached to a certain category so that it changes it from being a remote control. So it doesn't have to be 99% but if the highest number if it's like for example 70% sure that it's a remote control but we're going to try and change um the likelihood of it being golf ball. going to try and increase that until the golf ball is higher than the original image in remote control. And we're going to see what that looks like. And we're only going to give it 100 pixels to play with. So, we've got 224 x 224, which is about 50,000, something like that. Um, pixels and we're going to change 100 of them. So,

[10:56] can we change the um the categorization ResNet gives the remote control by just changing 100 pixels? you can, which is

### Re categorization

[11:05] good. So, we'll just go through the same five again. Um, we've got our coffee mug here. And there we go. That's with 100 pixels being changed. A lot less information there. And that does just look like noise. We can't do anything with that information. And similarly with computer keyboard, 100 pixels. Not too much of a change there compared to the others. And this is our envelope. Very similar. Golf ball now doesn't really even have the concept of a dimple in the golf ball. So, it just looks like random noise. And same with the photocopier. And I think if we push this hard enough, we could probably get it down to about 50 70 pixels or something like that. These networks are exceptionally good at um categorizing um which objects are are in images. However, they seem to be doing it in a very different way to us human beings. It doesn't quite tie in with our intuition. When we did this originally, um we didn't know what was going to happen. We didn't know if the genetic algorithm or iteratively hill climbing through the image would make something that looked like a coffee mug. That would make sense. We didn't know that, but it turns out it just makes um garbage and puts it on the image and yeah, changes it classification.

[12:14] In particular, what we are doing is uh to uh 3D print these kind of uh uh systems such that in future they can actually be manufactured together with the robot body and have integrated solution. That's going to be slow. Except it's not slow because there's hardly any ones in
