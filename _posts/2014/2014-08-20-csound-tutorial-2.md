---
layout: post
title: Csound Tutorial 2
date: 2014-08-20 13:00:00 +02:00
tags:
- Csound
- AudioProgramming
- tutorial
---
Yesterday we created our first *Csound* file and performed it live within *CsoundQT*. Recall that this instrument could only play a sine tone at 440 Hz with Amplitude of 10000. Clearly this is quite limited musically, and as you’d expect, this can be solved by introducing variables.

Numbered from left to right, each column in the score constitutes a parameter field. The first three parameter fields (*p1*, *p2*, *p3*) are reserved for the instrument number, start time, and duration respectively, but all other parameter fields are determined within the actual sound design of the instrument.

For instance, consider the following *Csound* file:

```c
<CsoundSynthesizer>

<CsInstruments>
	sr     = 44100				;sample rate
	kr     = 4410				;control signal rate
	ksmps  = 10				;samples per control signal
	nchnls = 1				;number of output channels

	instr 1
	a1	oscil 10000, p4, 1		;using function table 1
		out a1				;output
	endin

</CsInstruments>

<CsScore>

	f1 0 4096 10 1				;table containing a sine wave

	;ins	strt	dur	freq(p4)
	i1 	0 	1	440		;ascending Yu scale (Huang Zhong base)
	i1 	1 	1	528.64		
	i1 	2	1	594.39
	i1 	3 	1	660
	i1 	4 	1	792.86		
</CsScore>

</CsoundSynthesizer>
```

Here we can now alter the frequency of our instrument using the variable *p4*, and thus can construct a simple melody in which five successive notes are played at one second intervals. In fact, we can go one further, and even alter the amplitude of the notes themselves!

```c
<CsoundSynthesizer>

<CsInstruments>
	sr     = 44100					;sample rate
	kr     = 4410					;control signal rate
	ksmps  = 10					;samples per control signal
	nchnls = 1					;number of output channels

	instr 1
	a1	oscil p4, p5, 1				;using function table 1
		out a1					;output
	endin

</CsInstruments>

<CsScore>

	f1 0 4096 10 1					;table containing a sine wave

	;ins	strt	dur	amp(p4)	freq(p5)
	i1 	0 	1	10000	440		;ascending Yu scale (Huang Zhong base)
	i1 	1 	1	5000	528.64		
	i1 	2	1	2500	594.39
	i1 	3 	1	5000	660
	i1 	4 	1	10000	792.86		
</CsScore>

</CsoundSynthesizer>
```

Play around with these amplitude and frequency values, and introduce more notes to compose your first *Csound* masterpiece!

In this second tutorial, we have learned how to alter the amplitude and frequency of our instrument. In the next tutorial we will investigate amplitude envelopes.
