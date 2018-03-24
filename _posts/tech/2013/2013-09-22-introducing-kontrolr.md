---
layout: post
title: Introducing kontrolr
date: 2013-09-22 22:00:00 +02:00
category: tech
tags:
- Kontrolr
- iOS
- openFrameworks
---
*kontrolr* (stylized with a lower case ‘k’) is an iOS MIDI controller application. Physically, kontrolr sends MIDI data to a device via the Lightning-USB Camera Adapter<sup>**1**</sup> and a USB-MIDI cable<sup>**2**</sup>. MIDI data has the benefit over OSC that firstly no network connection is needed, hence no router and dependency on wireless transmissions, and secondly, that no OSC to MIDI program (i.e. *OSCulator*<sup>**3**</sup>) is necessary for controlling DAWs (Digital Audio Workstations), again removing a potential layer of error.

*kontrolr* is built using *openFrameworks*, and the external addons *ofxUI* and *ofxMidi*. The application’s key functionality is as follows:
1. Six different controller objects; a knob (or dial), vertical slider, horizontal slider, toggle box, XY pad, and matrix, all outputting MIDI on different controller numbers.
2. Ability to dynamically populate the canvas with controller objects.
3. Ability to change the size or remove a controller object from the canvas.
4. Ability to save and load presets. This is achieved by utilized XML files.
5. Four different canvases, each outputting on a different MIDI channel, and unique savable preset.

![]({{ site.baseurl}}/assets/images/posts/2013/13-09-22/01.png)

As the application was developed as an additional controller to perform *П*, only the relevant necessities were implemented. However, we are presently working towards a public release, and thus are investigating implementing OSC support also, and potentially some additional controller objects.

The following quick video demonstrates how the various components, kontrolr, *LiAMP*, and *LiVid.m4l*, communicate and thus how *П* is performed live.

<iframe src="https://player.vimeo.com/video/73566979" width="640" height="480" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<p></p>

**Notes**

<sup><b>1</b></sup>
Apple’s [Camera Connection kit](https://www.apple.com/uk/shop/product/MC531ZM/A/apple-ipad-camera-connection-kit) (and the updated [Lightning Connector](https://www.apple.com/uk/shop/product/MD821ZM/A/lightning-to-usb-camera-adapter)) allows one to connect their camera with USB to import photos and videos. However, it has the added hidden functionality of allowing any class compliant (a device that doesn’t require extra drivers when connected to Windows/Macintosh computers) USB audio interface or MIDI controller/keyboard to be connected to an iOS device. More info can be found in [this post](http://ma101jl.tumblr.com/post/38412006721/the-ipad-as-a-mobile-audio-studio).<br />
<sup><b>2</b></sup>
A cable with a USB plug on one end, and an IN/OUT 6-pin MIDI connectors on the other end.<br />
<sup><b>3</b></sup>
[*OSCulator*](https://osculator.net/) is an application which connecots to OSC devices (such as wiimote etc) and converts their input data into another type of data suitable for other applications, for instance MIDI and Ableton Live.
