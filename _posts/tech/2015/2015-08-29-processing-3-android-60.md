---
layout: post
title: Processing 3 + Android 6.0
date: 2015-08-29 09:37:30 +02:00
category: tech
tags:
- Android
- Processing
---
So continuing some Android adventures, this morning I wanted to test the new Processing 3 with Android Marshmallow. As Processing is written in Java, Processing and Android have always been good friends, but I was surprised to find out that they seem to work better now than ever before!

Processing has been busy developing 3.0 for a while (full changelog can be found [here](https://github.com/processing/processing/wiki/Changes-in-3.0)), and the new editor is a real game changer. FINALLY there is autocomplete and an actual debugger. This was one of the main stumbling blocks, especially when teaching beginners. Now that there is actually some intelligible feedback to your mistakes, it should greatly help the learning process for those new to programming.

Anyway, to run a Processing sketch on your Android device, you simply:
1. Download Android Mode (for Processing)
2. Download the Android SDK (or link to it if you already have previously downloaded it, i.e. Android Studio)
3. Connect your Android device and press ‘Play’

I tested this on a Nexus 5 running Android 6.0 (in developer preview) and the simplest of all sketches :)

![]({{site.baseurl}}/assets/images/posts/2015/15-08-29/01.png)

And everything works instantly! Note that Processing Android requires at least version 20 (or higher) - more info here.

After what seems like a few years of stagnation, it is great to see that Processing is not only becoming even more accessible, but is become more efficient too. Also the ease at which one can run an application on their device (compared to the loops which one needs to jump through with Apple), cannot be underestimated. Looking forward to see what the future holds for the new Processing.
