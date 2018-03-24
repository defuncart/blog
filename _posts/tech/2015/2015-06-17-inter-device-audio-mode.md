---
layout: post
title: Inter-device Audio Mode
date: 2015-06-17 16:00:00 +02:00
category: tech
tags:
- iOS
- macOS
---
For musicians and those who code iOS music apps, one interesting development for iOS9 and OSX 10.11 is the forthcoming *Inter-device Audio Mode*, discussed during the [*‘What’s New in Core Audio’*](https://developer.apple.com/videos/play/wwdc2015/507/) (from 37m20s onwards) talk at WWDC 2015.

Basically IdAM allows one to digitally record output from iOS to OSX via the lightning connector USB cable. The iOS application must be configured to output 24 bit @ 48kHz, while on the OSX side, the iOS device will shown as an input source in *Audio MIDI Setup*.

This should basically eliminate the need of recording audio from the iOS app (via cable to a sound card connected to the computer) or the need to bounce and transfer files, and thus will definitely be a feature that many musicians will embrace. Shame that it will not be support on the original iPad Mini :(
