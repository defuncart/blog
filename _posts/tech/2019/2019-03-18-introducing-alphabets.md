---
layout: post
title: 'Introducing Alphabets'
date: 2019-03-18 18:00:00 +0100
category: tech
tags:
- αბц
- Xamarin
---

Four years ago, I began learning the Georgian alphabet using a *Memrise* course. One of my issues with this community-built course was that the Georgian letters were low-quality, pixelated images, while I longed for a way to practically test my knowledge of these letters in a non-intimidating manner. I thus prototyped *αბц*, a simple alphabet learning application for iOS, and although the application served its purpose, I become busy with other projects and abandoned development.

<table bgcolor="#EEEEEE" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/02.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/03.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/07.png"></td>
  </tr>
</table>
<p></p>

Fast forward to the present day. As I would like to refresh my knowledge of the Georgian alphabet, and have still not developed an app using Xamarin, I decided that *αბц* would make the perfect project. Over the last two weeks, I've been working in my spare time in developing a basic proof of concept!

The version I developed four years ago had numerous issues, notably the manner in which letters where taught to the player only through trial and error multiple choice questions. In this new iteration, a letter is first presented to the player in the form of a flashcard (left), before being later quizzed via multiple choice (right). In the next version I would like to include a transliteration exercise where the player transliterates a Georgian word into Latin letters.

<table bgcolor="#EEEEEE" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2019/19-03-18/01.png" width="260"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2019/19-03-18/02.png" width="260"></td>
  </tr>
</table>
<p></p>

These 33 letters are taught over the course of ten lessons (inspired heavily from [*Learn the Georgian alphabet*](https://www.georgian-alphabet.com/en/)), with plans for reversion exercises. At the end of each lesson there is a overview of what letters were learned and which are giving the player problems.

## Alpha

For the alpha release, I'm working towards:

- 10 full lessons (presently only one in this proof of concept)
- Revision exercises
- New game mode: transliterating a Georgian word to Latin
- Potentially localized into German and Polish
- iOS design optimizations

## Future

For the future I would love to support other alphabets, for instance Russian, Armenian and Greek, however Georgian is presently the sole focus. The code, however, already supports multiple alphabets, and alphabets with upper and lower case letters.

## Xamarin?

In a recent post I questioned the continued use of Xamarin with so much industry praise for Flutter. As I professionally use Unity day-to-day, writing apps in C# is quick and easy, however I cannot shake the nagging feeling that Xamarin is a (slowly) dying platform, and that it may be worthwhile investing more time initially in a long-term solution. Moreover, I do not like that UI elements aren't rendered consisted across platforms (Material will change this but is still in preview), while, paradoxically, it feels like Flutter has more support for simple problems (i.e. there is a package available that can autosize text, for Xamarin I needed to write my own). Once *αბц* enters Alpha, I think it would make sense to develop a simple app from scratch using Flutter, for instance *Bratacha*.
