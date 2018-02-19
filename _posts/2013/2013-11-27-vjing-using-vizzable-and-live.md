---
layout: post
title: VJing using VIZZable and Live
date: 2013-11-27 22:00:00 +01:00
tags:
- Max
- Jitter
- MaxForLive
- VIZZable
- VIZZIE
- vj
---
[*VIZZable*](http://vizzable.zeal.co/){:target="_blank"} is a [*Max for Live*](https://www.ableton.com/en/live/max-for-live/){:target="_blank"} suite for video manipulation and live performance in *Ableton Live* 9. Originally based on Cycling ‘74’s [*VIZZIE*](https://cycling74.com/2010/11/19/introducing-vizzie/){:target="_blank"} package, in it’s latest version, *VIZZable* has been rebuilt from the ground up to take advantage of Cycling '74’s new environment *Gen*, facilitating very fast and efficient video processing on the GPU.

{% include youtube.html id="I9WJr0nvCiQ" %}

The beauty in *VIZZable* is it’s simplicity. As demonstrated by the developer in the video above, all one needs to do is download *VIZZable*, add the folder to *Live*, and can then one can easily drag and drop players and effects onto *Live*’s tracks. *VIZZable* is a great tool for VJing, and in version 2.1 has some really exciting features!

Firstly, you might not be aware that videos can not only be played in Live, but also edited and warped.

{% include youtube.html id="KKd6rVLUrwI" %}

These videos can be arranged in the *Arrangement view*, however currently (as of *Live* 9.1) cannot be triggered in the *Session view*. Luckily, *VIZZable* now supports the playing of video clips in *Session view* via the *clipPlayer(audio)* module.

{% include youtube.html id="JA2IMKTSBeo" %}

[*Syphon*](http://syphon.v002.info/){:target="_blank"} support is also included, so input from another source (*VDMX*, *Mad Mapper*, *Resolume*, *openFrameworks*, *Quarz Composer*, *Processing*, *Pd* etc.) can be routed through *VIZZable* and *Live*, or *VIZZable* can be outputted to one of these applications.

*VIZZable* v2.1 requires *Ableton Live* 9 (32 bit only) and *Max for Live* 6.13.  Windows users also need the 32 bit version of *Quicktime*. To keep up-to-date with developments in *VIZZable*, and in general *Jitter* within *Max for Live*, join the [*Jitter in Max 4 Live* forum](https://groups.google.com/forum/#!forum/jitterinmax4live-){:target="_blank"}.
