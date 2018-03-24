---
layout: post
title: 'αბц for Android'
date: 2015-08-28 23:56:52 +02:00
category: tech
tags:
- Android
- AndroidStudio
- Java
- αბц
---
Yesterday I upgraded to a Nexus 5 and thus today I decided to do something I haven’t tried in a while: coding a simple Android app. Other than the significant aesthetic overall Google undertook with Lollipop, over the last two years they’ve been working hard on their own dedicated IDE *Android Studio*. Thus it seems like a good time to dabble my toes in the Android world again.

As the iOS αბц application was quite useful in learning the Georgian alphabet, I figured that an Android equivalent would be beneficial for the Armenian alphabet. However, instead of choosing a correct answer from a list, I want to reinvestigate the idea of matching pairs.

Like latin based alphabets, Armenian has both upper and lower case letters. Thus three clear game modes would be matching Armenian Lower Case and Latin Transliteration, Armenian Upper Case and Latin Transliteration and Armenian Lower Case and Armenian Upper Case, however what if we go one further and consider a triplet?

Well firstly this simple application has the four mentioned game modes (left)

<img src="{{site.baseurl}}/assets/images/posts/2015/15-08-28/01.png" width="50%"/>

In one of the pair matching modes, as the user selects a cell, it turns blue (left), and if they choose the corresponding pair, both cells are deactivated, with their color changing to green, while if they choose the wrong letter to complete the pair, both cells turn red (right). Once all cells are matched, the game proceeds to the next round, that is simply a selection of six more letters.

<table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-08-28/02.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-08-28/03.png"></td>
  </tr>
</table>
<p></p>

However what I was really interested in, is the triplet match. The mechanics work similar to the pair match, except that the lower, upper and transliteration of a letter must be correctly selected.

<img src="{{site.baseurl}}/assets/images/posts/2015/15-08-28/04.png" width="50%"/>

So overall it will be interesting to test αბц in this match mode and see how effective it will be. As ever, *αბц* is an app developed for personal use and thus functionality comes before style :)

*αბц* was built using Android 6 using *Android Studio* and testing on a Nexus 5 (running Marshmallow). This was my first time using *Android Studio* and I must admit that I am pleased to see the new interface builder and predictive typing.
