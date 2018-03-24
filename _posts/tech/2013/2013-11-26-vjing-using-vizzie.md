---
layout: post
title: VJing using VIZZIE
date: 2013-11-26 22:00:00 +01:00
category: tech
tags:
- Max
- Jitter
- VIZZIE
- vj
---
[Cycling 74’s *Vizzie*](https://cycling74.com/articles/introducing-vizzie) is a collection of interactive *Jitter* objects, in essence *bpatchers*. To use *Vizzie*, first create a new patcher and then add modules by right clicking then **Paste From -> VIZZIE-CLIPPINGS**

![]({{site.baseurl}}/assets/images/posts/2013/13-11-26/01.png)

Within two minutes one can create simple yet powerful patcher, clearly geared towards VJing, in which a video may be dragged and dropped from a browser, or the output rendered to disk.

![]({{site.baseurl}}/assets/images/posts/2013/13-11-26/02.png)

Each module contain numerous built-in presets, while various parameters (speed, loop points etc.) can be controlled by *VIZZIE GEN* modules by connecting the modifiers to circle inputs of the module. For instance, the following patch contains a video track whose magnification is being controlled by the RMS of an audio signal.

![]({{site.baseurl}}/assets/images/posts/2013/13-11-26/03.png)

As *Vizzie* is merely *Jitter bpatchers*, *Jitter* code may be added at any time. Moreover, a favorite or often used piece of code can be incorporated as a *Vizzie* module by editing *effects-example-patch.maxpat* in /Max6/examples/VIZZIE-EXAMPLES/VIZZIE-KIT and saving it as a new *maxpat* (see [here](https://cycling74.com/tutorials/vizzie-tutorial-1-creating-a-vizzie-effects-module-using-the-vizzie-kit) for a full tutorial).

![]({{site.baseurl}}/assets/images/posts/2013/13-11-26/04.png)

Cycling ‘74 have some official tutorials on their youtube page: [1. - Quickstart](https://www.youtube.com/watch?v=z4TfdPHrbgg){:target="_blank"}, [2. - Vizzie Control](https://www.youtube.com/watch?v=Q2On-3lSATE){:target="_blank"}, and [3. - Vizzie Routing](https://www.youtube.com/watch?v=c2KYmDWgr7Q){:target="_blank"}.
