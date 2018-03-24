---
layout: post
title: Csound Tutorial 1
date: 2014-08-19 16:15:00 +02:00
category: tech
tags:
- Csound
- AudioProgramming
- tutorial
---
[*Csound*](http://www.csounds.com/) is an open-source C-Based Audio Programming Language which enjoyed popularity throughout the late eighties and nineties. During my MA in Electroacoustic Music Composition, I was first expose to the language, along with *Max/MSP*. Although Graphical languages like *Max* and creative coding frameworks like *Processing* and *openFrameworks* are more accessible than *Csound*, *Csound* nevertheless still enjoys active development and a solid user community.

Moreover, since the explosion of iOS and Android smart devices, *Csound* has been ported and can be incorporated into self-coded musical apps. In fact, long-time developer Richard Boulanger created [*Boulanger Labs*](http://boulangerlabs.com/) and has released some *Csound* based apps on the Apple App Store. There is also a freely downloadable *Max* object which allows *Csound* to be incorporated and performed in real-time from *Max*, and a propriety set of *Max for Live* [*Csound*-based objects](http://store.kagi.com/cgi-bin/store.cgi?storeID=6FJCL_LIVE&KagiAffiliate=Kagi_Market_Place).

So how exactly does *Csound* operate? Firstly download the relevant version of *Csound 6* for your OS [here](http://csound.com/download.html) and install it. *Csound* 'programs' comprise of two text files; an *orchestra* declaring the instruments and a *score* specifying notes and other relevant parameters. *Csound* then processes these files and renders an audio file or outputs the audio in real-time.

These *orchestra* and *score* files can be unified into a single *CSD* file, written using any standard text editor, and saved with the .csd extension. They can be compiled and executed using the *Terminal*, however for these tutorials we will utilize the included GUI *CsoundQT*. Open up the application and you should be greeted with the following screen:

![]({{site.baseurl}}/assets/images/posts/2014/14-08-19/01.png)

Type the following code

```c
<CsoundSynthesizer>

<CsInstruments>
	sr     = 44100				;sample rate
	kr     = 4410				;control signal rate
	ksmps  = 10				;samples per control signal
	nchnls = 1				;number of output channels

	instr 1
	a1	oscil 10000, 440, 1		;1 is the table number
		out a1				;output
	endin

</CsInstruments>

<CsScore>

	f1 0 4096 10 1				;table containing a sine wave

	;ins	strt	dur
	i1 	0 	5			;start playing instr 1 for
						;5 seconds at time 0
</CsScore>

</CsoundSynthesizer>
```

and then press the **'play'** button and you should be greeted with a simple sine tone playing for 5 seconds! You can even directly render this composition to an audio file using **'render'** or edit the audio file in an audio editor (i.e. [*Audacity*](http://www.audacityteam.org/download/)) directly using **'editor'**.

Our first *Csound* program is a very simple instrument containing an oscillator which has an amplitude of 10000 and frequency of 440 Hz, and utilizes function table #1. This table is defined in the score section of the file, and is defined to be a simple sine wave. The score section itself simple states that we want to start playing *instr 1* for 5 seconds at time 0. **Note** that we have specified a sample rate of 44.1 kHz, and a control rate of 4410 Hz, thus the number of samples in each control period must be 10 (ksmps = sr / kr). In general, these basic settings can be copied between different *Csound* files. 

In this first tutorial, we have set up our development environment and generated some sound. In the next tutorial we will continue with changing parameters of an oscillator.
