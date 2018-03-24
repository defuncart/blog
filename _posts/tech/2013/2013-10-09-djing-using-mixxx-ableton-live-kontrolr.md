---
layout: post
title: DJing using Mixxx + Ableton Live + Kontrolr
date: 2013-10-09 11:29:58 +02:00
category: tech
tags:
- Kontrolr
- MaxForLive
- AbletonLive
- dj
---
[*Mixxx*](https://www.mixxx.org/) is an awesome Open-Source DJ software, and a major rival to *Virtual DJ* and *Traktor* from what I’ve heard. So today I decided to try experimenting with it.

*Mixxx* sports a user friendly interface, and plays Mp3, WAV, OGG files. Moreover, it supports live microphone input, vinyl and MIDI controllers. When you first load the application, just point it towards your music collection, and it’ll load all these tracks in! The track has MetaData (i.e. tempo, key, composer etc.)? Great, it’ll import all that also!

![]({{site.baseurl}}/assets/images/posts/2013/13-10-09/01.png)

For MIDI controllers, it has a MIDI-learning mode (like in *Ableton Live* etc.), so all you need to do if connect your controller, go into learn mode, move a controller widget on screen (knob, slider etc.), and then a controller widget on your controller and they are paired together! I decided to try *kontrolr*, my iOS MIDI controller app, and am pleased to say it worked flawlessly and immediately!

![]({{site.baseurl}}/assets/images/posts/2013/13-10-09/02.png)

The only thing that *Mixxx* lacks at the moment is an effects unit. However, don’t fear, if you are an *Ableton* user you can easily connect *Mixxx* to *Ableton* so that all *Live*’s effects or external VSTs can be utilized. On Mac, download [*Soundflower*](https://cycling74.com/products/soundflower/) if you don’t already it. Basically this allows you to route audio between different programs. In *Mixxx*, send Deck 1 and Deck 2 out on channels 1-2, 3-4 (we want stereo don’t we?) using *Soundflower (64ch)* interface.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-09/03.png)

In *Live* select *Soundflower (64ch)* as the audio input (you may also need to select channels 3, 4 and 3-4 on in *input config*)

![]({{site.baseurl}}/assets/images/posts/2013/13-10-09/04.png)

and then create two Audio tracks whose inputs are 1-2 and 3-4 respectively. Now you can drop any effects you want onto these tracks, VSTs, *Max for Live* devices etc. The master audio then goes out from *Ableton*.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-09/05.png)

I really like using *Mixxx* for fast, DJ mixes, and they have stated that they are presently working on an effects unit. Although the *Ableton* workaround is a good solution, I wonder how practical this is as *Ableton* can do all the functionality of *Mixxx* anyway.
