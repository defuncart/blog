---
layout: post
title:  "blockNect"
date:   2012-02-24 22:00:00 +0100
tags:
- iOS
- openFrameworks
- maxmsp
- mfa
---

*blockNect* is an multi-purpose interactive interface, realized using Microsoft’s Kinect camera and computer vision, developed along with Thibault Lelievre and Philo van Kemenade as the group Computer Vision assignment for Parag Mital as part of *Workshops in Creative Coding 2*. Colored blocks are placed on an arbitrary sized chess board, where the block’s can be manipulated by the user. Each color block corresponds to a separate entity, while stacked blocks merge together to form single blocks. This affords the user three separate degrees of freedom; *x*, *y*-coordinates and height. This was realized as an eight-step sequencer where different colored blocks would relate to different instrumentation (such as drums, keyboard, bass), and the height to volume.

{% include vimeo.html id="48721613" %}

Using *OSC*, *openFrameworks* communicates bi-directionally to *Max/MSP*. Each beat of an adjustable metronome in *Max/MSP* requests the current board’s arrangement. The current beat sequenced for each instrument is then analyzed, and corresponding *MIDI* messages are outputted to a Sampler. However, an interface for sample playback is nothing new, and thus to better showcase the possibilities offered by *blockNect*, a Soundscape sound synthesis engine was also created. This engine consisted of three simple instruments; an additive synthesizer, a wavetable synthesizer, and a subtractive synthesizer. Following from the homogenous mapping explored for the sequencer, for the Soundscape engine, the *y*-direction corresponds to pitch, the *x*-direction to unique properties, and the height to volume.

![]({{site.url}}/assets/images/posts/2012/12-02-24/01.png)
<p style="text-align: center;"><b>Figure 1:</b> Snapshot of the program showing register blocks in <i>Max/MSP</i>.</p>

To improve the efficiency of OSC communication, instead of periodic data requesting from *Max/MSP*, and then sending this data to the correct location, a more one-to-one connection was conceived, in which when a new item is placed on board, a new instrument is created in *Max/MSP*. Dynamic instrument addition and removal was achieved using *Javascript*. To further improve the usability for the end user, one is able to switch at any stage between either the Sequencer or the Soundscape engine, while an onscreen chessboard is presented for visual feedback of the mapped block’s location. I built the sequencer in *Max/MSP*, and took care of the OSC communication from *openFrameworks* to *Max/MSP*, while my group mates Thibault and Philo concentrated on the computer vision.

![]({{site.url}}/assets/images/posts/2012/12-02-24/02.png)
<p style="text-align: center;"><b>Figure 2:</b> Elegant UI for <i>blockNect</i>.</p>

[Personal Report](https://www.dropbox.com/s/2ccw4azb3h0axr5/BlocknectJamesLeahyWriteUp.pdf){:target="_blank"}. [Group Report](https://www.dropbox.com/s/3yoz1e433rnljx5/BlockNect%20report%20Group.pdf){:target="_blank"}. [Source Code](https://www.dropbox.com/s/skck3ylb2qzgnjj/blocknect.zip){:target="_blank"}.
