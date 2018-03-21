---
layout: post
title: M4L and User 1 Mode on the Launchpad
date: 2014-07-26 22:00:00 +02:00
tags:
- LiAMP
- NovationLaunchpad
- AbletonLive
- Max
- MaxForLive
---
Last year while undertaking my MFA in Live Audiovisual performance, I developed a set of *Max for Live* modules to facilitate my final performance, one of which was a *monome*-style emulator, such that the top row would have a flashing right light through the cells to specify the current beat. In the v0.01 beta of *LiAMP*, *LiAMP.Controller.Launchpad.Monome* was released with the note “Presently over-rides any cell in the top row”, while User1 mode wasn’t functioning at all.

So basically by getting the *Button_Matrix* of the *Launchpad*, we can easily set the cells in *Session*, *User2* or *Mixer mode*, however *User 1* presumably acts differently as it is optimized for Ableton’s Drum racks. (Some discussion here on *Session Mode* and *User2 Mode*). Today I decided to look into this more as I wish to utilize both live drum playing in *User1 mode*, and also a visual metronome. This [interesting video](https://www.youtube.com/watch?v=Jkvq_6Jg6UU) from FletchMusicVideo states how you can firstly supply visual feedback to the launchpad by MIDI routing, and most importantly, how to easily create the monome effect by outputting MIDI corresponding to the MIDI value of the desired cells. It is also interesting to note that the velocity of these notes determine the output color.

Basically we have two scenarios:
1. in *Session*, *User2* or *Mixer* mode use Live’s API, and
2. in *User1* mode need to do some clever MIDI routing.

So firstly I created a simple patch to determine which Mode the user presently is in.

![]({{site.baseurl}}/assets/images/posts/2014/14-07-26/01.png)

Now for User1 mode, the notes E3 F3 F#3 G3 C6 C#6 D6 D#6 are the corresponding values for the cells of the first row, so all we need to do is output these notes with velocity 74 (gives red color) in a MIDI clip receiver **Launchpad Output** on **Ch. 5**

![]({{site.baseurl}}/assets/images/posts/2014/14-07-26/02.png)

However, instead of adding another MIDI track to the Live project, I want this is to self-contained with *LiAMP.Controller.Launchpad.Monome*. This can be easily achieved by outputting the corresponding MIDI notes from the module itself

![]({{site.baseurl}}/assets/images/posts/2014/14-07-26/03.png)

and setting the MIDI output to **‘Lauchpad’** on Channel 5.

![]({{site.baseurl}}/assets/images/posts/2014/14-07-26/04.png)

And thus we have a fully functioning Monome beat-indicator for all the four user modes. One of the main setbacks is that the top row is always overwritten, but this personally doesn’t bother me too much, and throughout the last year performing *П* I haven’t felt the need to rectify this yet.

For the Drum Pad feedback, as per the instructions in the video, create a new MIDI track which is set to IN and has the drum kit as INPUT and the Launchpad on channel 5 as OUTPUT. There is probably a fancier way to achieve this with M4L, but why fix something if it ain’t broken?!
