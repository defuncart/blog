---
layout: post
title: Introducing LiAMP
date: 2013-09-23 22:00:00 +02:00
tags:
- LiAMP
- Max
- MaxForLive
---
*LiAMP* (Live Algorithms for Musical Performance) is a modular *Max for Live* package which deviates from solely utilizing programming environments for Live Algorithms, and instead embraces the added benefits of using a DAW (Digital Audio Workstation). The package consists of *Max for Live* modules which function as the ‘brain’ of the Live Algorithms paradigm, while *Live* acts as the listener and performer elements. The package may be subdivided into four main sections; Communication, Instruments, Composition, and External Controllers.

Communication consists of modules which send performance related data, for instance current BPM, beat, output level of individual tracks etc. over a chosen OSC connection, and locally within *Live*. Some other utilities include a console to print the value of local variables, and a listener for when a specific scene is triggered.

Instrument consists of some basic, yet sequence-able, monophonic and polyphonic synthesizers. Composer consists of a group of algorithmic music composition modules, utilizing Markov chains, genetic algorithms, and Arvo Pärt’s *Tintinnabuli* system. Finally, there are also some modules for the Novation Launchpad such that *Monome* simulation can be achieved.

![]({{ site.url}}/assets/images/posts/2013/13-09-23/01.png)

The package originates from James’ research into custom audiovisual interfaces during his MFA at Goldsmiths, and is still in development. Stay tuned for updates!
