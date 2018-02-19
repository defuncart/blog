---
layout: post
title: DJ Using Only a Launchpad
date: 2014-07-24 22:00:00 +02:00
tags:
- LiAMP
- dj
- NovationLaunchpad
- AbletonLive
- Max
- MaxForLive
---
Today I started to prepare a new DJ set in *Ableton* and I began to think, can a traditional DJ set be solely performed using a *Launchpad*?

Considering a standard two-deck DJ setup, the most important components are:
1. Deck volume control
2. Deck spatilization
3. Crossfade between these two decks
4. Knobs for the Bass, Middle and Treble for each deck
5. Kill switch for the Bass, Middle and Treble for each deck
6. Cue points
7. Tempo sync button
8. Deck scratch knob

In the mixer section on the launchpad, volume and spatilization are already accounted for, and once your tracks are warped, there is no need to sync the tempo between the decks. *Ableton* doesn’t support cue points, but by splicing your track into sections, you can easily skip between track sections in session mode. So what I began to think about, is how can User 2 mode be utilized to implement # 3, 4, and 5.

As you know, the launchpad is an 8x8 matrix with 8 side buttons, thus giving a total of 72 possible MIDI events in User 2 mode. If we take one of those rows, say the last one, four cells could be assigned to the left channel of the Master’s crossfader, and the other four to the right channel, with the special side button in the center.

![]({{site.url}}/assets/images/posts/2014/14-07-24/01.png)

As the Master’s crossfader is a fader and hence a single MIDI widget, to map these nine cells, we need to use a little programming and *Max for Live*.

![]({{site.url}}/assets/images/posts/2014/14-07-24/02.png)

Now this patch is a lot simpler than it looks. Basically there are nine **[live.toggle]**s which are MIDI mappable to our nine cells on the *Launchpad*. Each toggle triggers a specific value to be sent to the Master’s crossfader referenced via a **[live.object]**. As these toggles can be toggled on and off, and I only want one to be active at a time (as the crossfader has only one value at any given time), a little bit of scripting is used to toggle off any toggle other than the activated one. This could be achieved other (and maybe easier) ways, but this is what came to me, so I decided to go with it!

This *LiAMP.AudioEffect.xFader* module can be placed on the Master track (in fact it is irrelevant which audio track it is place on, but on the Master makes logical sense), and the cells assigned in MIDI assignment mode. And viola, a simple to use crossfader on the launchpad.

Of course the obvious downfall is that there are only 9 discrete steps between L and R, clearly less afforded than by a slider. But in some quick testing I’ve found it to work quite well. Tomorrow I am going to implement # 3 and 4 in a similar fashion, and introduce another novel feature for crossfading on the *Launchpad*!
