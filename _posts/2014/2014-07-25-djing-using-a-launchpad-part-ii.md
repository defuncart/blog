---
layout: post
title: DJing using a Launchpad Part II
date: 2014-07-25 20:46:50 +02:00
tags:
- LiAMP
- dj
- novation launchpad
- ableton live
- Max MSP
- Max for Live
---
Continuing on from yesterdays discussion about DJing using *Live* and a *Launchpad*, after some inspiration from the Cycling ‘74 forums I implemented the radio buttons using simple max objects as opposed to scripting.

![]({{site.url}}/assets/images/posts/2014/14-07-25/01.png)

This subpatch can be easily incorporated into a LiAMP module via a **[bpatcher]** such that the UI elements of the subpatch can be modified (and most importantly for us, MIDI assigned). Presently the utility subpatch only outputs 1, 2, 3, or 4 when a button is pressed, but we potentially may wish to use a different scaling. Instead of mapping the patch’s output, we can in fact use the **#** argument symbol and supply them as arguments into the **[bpatcher]**.

![]({{site.url}}/assets/images/posts/2014/14-07-25/02.png)

Another issue is that these toggle boxes are going to be given a generic name, say *toggleBox[2]* etc. which aren’t intuitive when you are browsing the list of MIDI Mappings. This is a little hacky, but can be solved by passing names into the subpatch, toggle on **“Link to Scripting Name”**, and then update the *varname* of the **[live.togglebox]**. As there appear to be no attributes for the *longName* or *shortName*, this is the only approach I can think of.

But now onto what I really want to implement, something which I’ve been wishing for a long, long time; automatic volume automation, that is, the fade-in or fade-out of a track over a certain bar duration at the touch of a button. As I wish to have multiple decks, and hence will use this module on each deck, it makes sense to give the toggle’s their own unique name, derived from the track number the module is placed on.

![]({{site.url}}/assets/images/posts/2014/14-07-25/03.png)

Now to create the automatic fading in and out, all that needs to be done is to:
- determine the time in ms for the selected bar duration,
- wait until the start of the next bar (quantization), and then
- trigger a **[line]** object for [-∞, 0]dB etc. to control a **[live.object]** referencing the track’s volume slider.

The implemented patch is then as follows:

![]({{site.url}}/assets/images/posts/2014/14-07-25/04.png)

Here I decided to use *M4L.api.GetSelectedTrackIndex* but could have easily also used *LiAMP.utility.PathFinder* with the variable *—trackNum*. I did however use the variables *bpm* from *LiAMP.Send.BPM* and *bar* from *LiAMP.Send.Beat*. Although it should be possible to use **[transport ms]** and the variable *1n*, the BPM was always 125, and not synced to Live’s actual transport. I’m sure there is some easy way of solving this, but my own previously created objects work just fine!

With Deck A at the left side of the launchpad, and Deck B at the right, and with a separate *LiAMP.AudioEffect.VolumeAutomator* on each Deck, the mapping works really well on two rows. I’m not sure what to do with the two side buttons though, maybe toggle between volume kill?
