---
layout: post
title: Gen Tutorial 1 - A Friendly Introduction to Digital Signal Processing
date: 2013-10-01 22:00:00 +02:00
tags:
- Max
- Gen
- dsp
- tutorial
---
Digital Signal Processing (DSP) is the mathematical manipulation of an information signal to modify it in some way. An audio waveform is represented digitally by breaking it up into a certain number of samples per second, at a certain bit resolution (i.e. 44100 samples per second at 16 bit quality). All these sampled amplitude points are stored in a floating point array, and can be manipulated accordingly. If any of this seems unfamiliar, please consult this great introduction to digital audio.

DSP facilitates more direct control over the audio processing, but is a notoriously difficult area of digital audio, and is generally conducted in *C/C++*. Luckily, in *Max 6* Cycling ‘74 created [*Gen*](https://cycling74.com/products/gen/), which allows one to visually develop low-level, platform-independent code which is compiled on the fly. Like traditional dsp, *Gen* works on the sample level, thus offering more precision than the vector level in *MSP*. It should be noted that *Gen* is not merely limited to audio processing **[gen~]**, also incorporating its Jitter equivalents **[jit.pix]**, **[jit.gl.pix]**, and **[jit.gen]**.

**NOTE:** To edit *Gen* patches, you need to purchase it. However, all *Gen* patches can be ran  with a copy of *Max 6*.

With **[gen~]** there are some key differences from MSP:
* Firstly, the flow of data inside **[gen~]** is constant, thus there are no messages, UI objects etc. Since data is always synchronous, a feedback loop isn’t possible. Instead, an **history** operator is needed to act like a single-sample delay.
* Secondly, there is no need to differentiate hot and cold inlets, or the order in which outlets ‘fire’, since all objects and outlets always fire at the same time.
* Thirdly, the usual distinction between int and float numbers does not apply to *Gen* patchers. At the *Gen* patcher level, everything is a 64-bit floating point number.
*Finally, send and receive operate locally in a *Gen* patcher, and not to another *Gen* patcher or *Max* patcher. *Gen* patchers are connected to the outside world through the **in**, **out**, and **param** operators.

So lets go about creating your first *Gen* patch. Create a new *Max* patch with the object **[gen~]**. Double click on **[gen~]**, and you should be greeted with the following default template:

![]({{site.url}}/assets/images/posts/2013/13-10-01/01.png)

This patch simply adds two incoming signals, like **[+~]**. Test it out!

![]({{site.url}}/assets/images/posts/2013/13-10-01/02.png)

In many cases, the specification of an object’s argument effectively replaces the corresponding inlet. This is possible in *Gen* because there is no messaging and all processing is synchronous. For example, the **+** operator takes two inputs, but if an argument is given only one input needs to be specified as an inlet. If no argument is given, then the default value (generally zero) is used. Finally, an inlet with multiple connections adds them all together, just as with *MSP* signal patchcords.

![]({{site.url}}/assets/images/posts/2013/13-10-01/03.png)

So far we’ve seen **in** and **out**. Lastly, lets look at **param** which defines a parameter inside *Gen*, and can be controlled from it’s parent patcher. **Mix** acts similarly to **+**, but interpolates between input 1 and input 2, depending on a given interpolation factor (from 0 to 1). This factor is declared as a parameter called *mixLevel*, and thus controllable in the parent *Max* patch.

![]({{site.url}}/assets/images/posts/2013/13-10-01/04.png)
