---
layout: post
title: Csound Tutorial 5
date: 2014-10-14 13:00:00 +02:00
tags:
- Csound
- AudioProgramming
- tutorial
---
After our first four tutorials, we can now create our own personal synthesizer where the pitch, amplitude envelope, and timbre can be altered in the *score*. Now I know what you are thinking, “Sequencing a melody is kool and all, but what if I was able to play it in real time, with a real MIDI controller…”.

Well, luckily for us, this is quite easy to achieve! Firstly, with your MIDI keyboard connected, in *CsoundQT* go to **Configure** and select your MIDI input interface (for a comprehensive introduction to MIDI see [here](https://www.midi.org/articles/tutorials)). 

![]({{site.url}}/assets/images/posts/2014/14-10-14/01.png)

If you do not have a MIDI keyboard, then you can instead use the Virtual Keyboard by enabling it via **Configure** as follows

![]({{site.url}}/assets/images/posts/2014/14-10-14/01.png)

or using the CSOption **-+rtmidi=virtual -Ma**

Now taking our previous patch from Tutorial 4, we can modify it as follows to thus create a real-time playable synth.

```
<CsoundSynthesizer>

<CsOptions>
-Ma						;accept MIDI input on all channels
;-+rtmidi=virtual -Ma				;use if virtual unstable through GUI
</CsOptions>

<CsInstruments>
	sr     = 44100				;sample rate
	kr     = 4410				;control signal rate
	ksmps  = 10				;samples per control signal
	nchnls = 1				;number of output channels

	instr 1
iFreq	cpsmidi					;convert input MIDI frequency
iAmp 	ampmidi 10000				;scale input MIDI amplitude
a1	oscil	iAmp, iFreq, 1			;uses function table 1
a2	oscil	iAmp, iFreq, 2 			;uses function table 2
	out 0.6*a1 + 0.4*a2			;summed output
	endin

</CsInstruments>

<CsScore>

	;fn 	time 	size 	gen 	parameters
	f1 	0 	4096 	10 	1                                               ;sine
	f2 	0 	4096 	10 	1 0.5 0.3 0.25 0.2 0.167 0.14 0.125 .111 	;sawtooth
	f3 	0 	4096 	10 	1 0   0.3 0    0.2 0     0.14 0     .111 	;square
	f4 	0 	4096	10 	1 1   1   1    0.7 0.5   0.3  0.1 		;pulse

	e 30   ;score lasts for 30 seconds
</CsScore>

</CsoundSynthesizer>
```

So basically here instead of using variables *p4* and *p5* from the *score* as amplitude and frequency for the synth, we are using the input MIDI note’s velocity and pitch. **NOTE:** Our real-time synth is still dependent upon a score, i.e. execution time. Here we have selected 30s. This could also be archived by calling *instr 1* for a certain period of time as follows:

```c
;ins  strt  dur(p3)
i1    0     3600
```

In this fifth tutorial, we have learned how to break free from the static store and implement a real-time synthesizer. In the next tutorial we will investigate implementing audio effects for our synth.
