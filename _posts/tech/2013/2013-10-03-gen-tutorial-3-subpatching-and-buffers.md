---
layout: post
title: Gen Tutorial 3 - Subpatching and Buffers
date: 2013-10-03 22:00:00 +02:00
tags:
- Max
- Gen
- dsp
- tutorial
---
Subpatchers and abstraction in *Gen* objects behave practically identically to standard *Max* subpatchers and abstractions. In *Gen* objects, subpatchers are created with the **Gen** operator.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-03/01.png)

However, what has happened to our parameter control? In the parent *Gen* patcher, the parameter gets converted into a constant because nothing is connected to the parameter. Since subpatcher and abstraction parameters don’t create their own inlets to connect objects to, there is a special operator called **setparam** which connects all of its inputs to a named parameter in a subpatcher or abstraction. When **setparam** is connected to a parameter, the parameter changes from being a constant to a dynamic variable equivalent to the value at the input of the **setparam** object.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-03/02.png)

Like *Max* abstractions, a *Gen* patch can be saved as a file and then loaded using the *gen filename* message, or by supplying the filename as an argument for **[gen~]**.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-03/03.png)

For persistent audio data storage, **[gen~]** offers two operators, **data** and **buffer**. Both are similar to MSP’s **[buffer~]**, main difference is that **data** is local to the *Gen* patcher, while **buffer** is a shared reference to an external *MSP* **[buffer~]**. Thus modifying a *Gen* **buffer**, is directly modifying the contents of the *MSP* **[buffer~]** it references.

In the following patch, we define an *MSP* **[buffer~]**, and send a **[phasor~]** (continuous stream of values from 0 to 1) into *Gen*. In *Gen* we set a reference to the *MSP* **[buffer~]**, and then grab the sample at the current location (input from **[phasor~]**), and output it to *Max*. So basically we have created a simple sample player.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-03/04.png)

In the next patch we create an internal *Gen* buffer using **data** and then write into it using **poke** and the current sample value via **counter**. The drum sample is continually sent into our *Gen* patch, but only recorded when we press the record button. After toggling record off, or by pressing the play button, we then play this 1 second recorded loop.

![]({{site.baseurl}}/assets/images/posts/2013/13-10-03/04.png)

All patches can be downloaded [here](https://drive.google.com/open?id=1g5iJapet5Aq4zXAOTgVzOqOIWxaRPN_V){:target="_blank"}.
