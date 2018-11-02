---
layout: post
title: 'Fifty-Fifty Devlog'
date: 2018-08-31 18:00:00 +0200
category: tech
tags:
- FiftyFifty
- CaogaCaoga
- Półnapół
- FünfzigFünfzig
---

It is almost seven months since I released an early-access version of *Pół na pół* for testing, while *Caoga caoga* has been out on the App Store and Google Play for almost six months. Since then, *Caoga caoga* has been downloaded much more than I imagined (over 3000 times on Google Play and 1000 times on the AppStore) and I've received a lot of feedback. Although *Der Die Das*, *Konjugator* etc. have been the priority the last couple of months, I've implemented some new features in *Fifty-Fifty* which I'll discuss in this long overdue devlog.

#### Changelog

Firstly, the game is now optimized for taller phone screens (i.e. those with an 18:9 aspect ratio, iPhoneX, Galaxy S8 etc.).

Secondly, the setting's screen has been improved. Game modes (Fifty-Fifty, Spelling, Multiple Choice and Matching) and listening exercises can be toggled here directly, while "Pause after each answer" seems to be more understandable than "Go automatically to next question". The Spelling game mode is the most divisive, with many loving it and others hating it (even to the point of writing detailed emails how demotivating it is). With these settings more clearly visible, players can now easily turn off a game mode or listening exercises. Note that vocabulary is still initially taught using Fifty-Fifty, while Tests will always use the four modes and listening exercises.

<img src="{{site.baseurl}}/assets/images/posts/2018/18-08-31/01.png" width="300px" height="600px"/>
<p></p>

The results screen has been overhauled to display more relevant information. Coins are no-more! As the game will never utilize any monetization system, it is pointless that players can earn coins without the option of being able to buy anything. Instead, a perfect score is rewarded with a trophy while any incorrect answers will be displayed as difficult words.

<table cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2018/18-08-31/02.png" style="width:50% height:50%"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2018/18-08-31/03.png" style="width:50% height:50%"></td>
  </tr>
</table>
<p></p>

Each game mode now has a listening equivalent (initially this was just Spelling and Multiple Choice). In Fifty-Fifty, a word is spoken and the player has to choose between two images, while in Match there are four audio voices and four images which the player must match correctly together. These listening exercises occur roughly 25% of the time.

<table cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2018/18-08-31/04.png" style="width:50% height:50%"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2018/18-08-31/05.png" style="width:50% height:50%"></td>
  </tr>
</table>
<p></p>

#### Roadmap

Although I don't envisage having much time for *Fifty-Fifty* over the coming months, there are some ideas I would like to implement:
1. Speaking exercises. This would involve recording the player and performing a FFT analysis to determine how close it is to the actual word's pronunciation. This is doable (*Duolingo*'s speaking exercises aren't that accurate) but would require time and a lot of trial and error on the FFT settings I reckon.
2. A favorite's list.
3. Add some new vocabulary, about four more topics so that the total word count would be over 500.

#### Releases

On Monday *Pół na pół* will be released in open beta for Android. Although fully-functional, *Fifty-Fifty* has seen neither an alpha nor beta release yet, while I plan on launching *Fünfzig-Fünfzig* within open beta soon. Finally, *Caoga caoga* could really do with an update but I may explore whether speaking exercises are possible first.
