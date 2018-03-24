---
layout: post
title: Csound Tutorial 3
date: 2014-08-21 13:00:00 +02:00
category: tech
tags:
- Csound
- AudioProgramming
- tutorial
---
Yesterday we learned how to incorporate parameters into our instrument such that the amplitude and frequency could be altered from our score. However this only allows us to control the loudness of a new note; what if we want to alter the loudness during the course of a given note? Also did you notice that unsettling audio-pop glitch between successive notes?

Firstly some theory. In *Csound* we have three types of variables:
- *i-rate* variables which change at the note rate,
- *k-rate* variables which change at the control signal rate, and
- *a-rate* variables which change at the audio signal rate.

Thus, *i-variables* are modifiable in the score, and *k-variables* and *a-variables* are modifiable in the orchestra, where *a-variables* produce sonic output, and *k-variables* can manipulate particulars of these audio functions.

We want to create an amplitude envelope which is controllable for each note of the score, and luckily Csound has a built-in function, **linen**

```c
kr linen kamp, irise, idur, idec
```

which produces a *k-variable* from a given amplitude, attack, duration, and decay value. We can then modify our instrument as follows:

```c
<CsoundSynthesizer>

<CsInstruments>
	sr     = 44100				;sample rate
	kr     = 4410				;control signal rate
	ksmps  = 10				;samples per control signal
	nchnls = 1				;number of output channels

		instr 1
	k1	linen 	p4, p6, p3, p7		;p3 = duration, p4 = amp p5 = freq
	a1	oscil 	k1, p5, 1		;p6 = attack time, p7 = decay time
		out 	a1			;output
		endin

</CsInstruments>

<CsScore>

	f1 0 4096 10 1				;table containing a sine wave

	;ins	strt	dur(p3)	amp(p4)	freq(p5) attack(p6)	decay(p7)
	i1   	0	1	10000 	440        0.5 		0.5
	i1   	1	1	5000 	528.64     0.75 	0.25		
	i1   	2	1	2000 	594.39     0.9 		0.5
	i1   	3	1	5000	660        0.2 		0.9
	i1   	4 	1	10000	792.86	   0.5 		0.5
</CsScore>

</CsoundSynthesizer>
```

In this case, we firstly design the amplitude envelope such that for a given maximum amplitude, attack time, decay time, and overall duration, we can calculate the instantaneous value of the line function at a control rate interval (i.e. 4410 times per second). This variable *k1* is then used as the amplitude of the oscillator *a1*. As before, *p5* is then used as the corresponding frequency.

Notice that those audio-pop glitches are gone? Using an amplitude envelope, we can avoid those instantaneous audio jumps, and thus audible glitches, an invaluable tool for all compositions (unless you purposely want them, of course :p).

In this third tutorial, we have discussed the practical use of an amplitude envelope and how to implement it. In the next tutorial we will discuss altering the timbre of our instrument.
