---
layout: post
title: Introducing LiVid.m4l
date: '2013-09-24T22:00:00+02:00'
tags:
- LiVid
- MaxForLive
- Max
- Jitter
- VIZZIE
- VIZZable
---
*LiVid.m4l* is a *Max for Live* package for live video performance, constructed in a similar manner to *LiAMP*. Although [*VIZZable*](http://vizzable.zeal.co/) exists which is a great kool for live DVJ sets, for Live Video Art I wished to use *LiVid*, a live video performance system developed for Max, which had been been robust during a tour of *П*. Thus *LiVid.m4l* is a converted and improved version of LiVid.

First of all is *LiAlg.m4l.SEQUENCR*, a module which plays a folder of videos one after another, where each video is beat-synced to four-bar measures of the current *Live* set. This has since spawned *LiVid.m4l.VIDEOSEQUENCRSIMPLE*, which just plays the videos without any tempo syncing, and *LiVid.m4l.LIVECINEMA* in which the videos aren’t automatically played, instead chosen by automation in Live.

![]({{site.url}}/assets/images/posts/2013/13-09-24/01.png)

Unlike m4l audio and MIDI modules which can pass data in a chain via **[plugin~]**/**[plugout~]** and **[midin]**/**[midiout]**, as *Live* wasn’t designed for passing *[jit.matrix]* between devices, how should we go about creating a chain? Jitter matrices are mere references to a block of memory, and so any matrix can be loaded on any device once the name is known. As I plan on keeping all my videos on the same Track, using the Device number as a unique matrix name seems like a logical choice.

Consider a simple BRCOSA (brightness, contrast, saturation) effect. Typically we’d have an input matrix, do some effects, and then have an output matrix. In this case the input will be a named matrix (say from *LiAlg.m4l.SEQUENCR*), but what about the output matrix? We cannot write to the same matrix as we’ll clearly mess up the input/output process, so instead we write to another matrix. This is the simple principle of *LiVid.m4l*. We write to the matrix of our device number, and we read from the matrix of the previous device number.

![]({{site.url}}/assets/images/posts/2013/13-09-24/02.png)

So *LiAlg.m4l.SEQUENCR* outputs 1mat, *LiVid.m4l.BRCOSA *inputs 1mat, does some effects, and then outputs 2mat. Then, say, *LiVid.m4l.GLITCH* inputs 2mat, does some effects, and outputs 3mat etc. *LiVid.m4l.GLITCH*, *LiVid.m4l.DEBRIS*, and *LiVid.m4l.FADR* work in the exact same fashion as *LiVid.m4l.BRCOSA*.

![]({{site.url}}/assets/images/posts/2013/13-09-24/03.png)

![]({{site.url}}/assets/images/posts/2013/13-09-24/04.png)

![]({{site.url}}/assets/images/posts/2013/13-09-24/05.png)

while *LiVid.m4l.VIEWR* is a simple **[jit.window]**, with a bypass and fullscreen option, but also a second viewer option if the main window is used as an external screen (for projecting) and you need to monitor the video when performing.

![]({{site.url}}/assets/images/posts/2013/13-09-24/06.png)

Now you might be thinking, what if I remove a device, add a device, or swap positions in the chain, how will the named matrices be updated? This can be done manually by clicking on a module’s sync button, or automatically via *LiVid.m4l.Utility.Sync*. It should be noted that *LiVid.m4l* assumes that all devices are enabled at all times, otherwise the chain is broken. As this is how I use the software, and I’ve designed it for myself, I’ve no intention of changing this small little fact.

![]({{site.url}}/assets/images/posts/2013/13-09-24/07.png)

Both *LiVid* and *LiVid.m4l* were designed during my MFA at Goldsmiths. Initially I had reservations about burdening *Live* with both the Audio and Visual elements, but so far the system has been robust during my final degree performances, but ultimately offering much more functionality, and a better audiovisual performance. For now *LiVid* is depreciated, but *LiVid.m4l* is still in development - stay tuned for updates!
