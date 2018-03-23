---
layout: post
title: 'αბц - An Alphabet Learning Tool'
date: 2015-02-06 13:53:00+01:00
tags:
- iOS
- Swift
- αბц
---
Last month I started learning the Georgian alphabet using [this course](https://www.memrise.com/course/44023/georgian-alphabet-ipa-with-audio/) on *Memrise*. However, one of my issues with this community-built course was that the Georgian letters were low-quality, pixelated images, while I longed for a way to practically test my knowledge of combinations of these letters in a non-intimidating manner.

Thus last weekend I went about building **αბц** (*Alphabets*, pronounced Alphabaytz), a simple alphabet learning application for iOS. Coded entirely in *Swift*, a proof of concept with an ultra minimalistic UI presently exists.

Like all good applications, on the initial launch, the user is presented with a landing screen (left). The application itself has two game modes and a progress viewer (right). 

<table bgcolor="#EEEEEE" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/01.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/02.png"></td>
  </tr>
</table>
<p></p>

The first game mode is the learning and testing mode. Here the user is presented with letters (chosen at random) in either the Georgian or Latin scripts, with four possible answers in the opposite script. If the user answers correctly (left), the letter is highlighted and a jingle is played. If the user answers incorrectly (center), the incorrect selected letter is highlighted along with the correct one, a different jingle is played, and the user to transferred to a screen giving some information about the letter (right). Note that if the user hasn’t previously learned the selected letter, then they are initially transferred to this info screen. Each correct answer gets a point associated with that letter, while the current streak is noted (i.e. +2).

<table bgcolor="#EEEEEE" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/03.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/04.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/05.png"></td>
  </tr>
</table>
<p></p>

The second game mode is a practice mode which displays either a real Georgian word or the Latin transliteration of a real Georgian word, and the user has the option of choosing from four possible answers (three of which are random gibberish of the same word length). Answering correctly (left) or incorrectly (center) follows similarly from the first game mode, except there is no need for an info screen, and that the score for each letter of the word is affected. Note that this game mode is only available after all the letters have been learned.

<table bgcolor="#EEEEEE" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/06.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/07.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-06/08.png"></td>
  </tr>
</table>
<p></p>

Finally a progress screen (right) displays score information for learned letters from the Georgian alphabet. Tapping on a cell in the table view brings up the letter’s info screen.

**To DO:**
- Include a total score for the alphabet or someway in determining the user’s progress on the whole.
- Implement a better game AI. Presently the letters are chosen at random. Some type of ‘intelligence’ which considers the letters that the user is finding most difficult (via score and steak) is one avenue to explore. Likewise, words of smaller length could first be displayed, then steadily progressing based upon the user’s total score.
- Add pronunciation sound files of the letters
- Add the Armenian alphabet. As the Georgian alphabet doesn't distinguish between upper and lower cases, the application would need to be adapted. Logically, I feel that the user can learn both upper and lower cases at the same time (via info screen), but should be quizzed on them separately.
- One useful feature of *Memrise* courses is that instead of a correct or an incorrect jingle, they actual plays an audio file of the respective letter/word. I think this would be very useful for the Learning mode.

**For the future..**
- One idea was to include easy to identify Georgian words, for instance კატა, ბერლინი, ლონდონი (cat, Berlin, London) as opposed to the transliteration of popular words. As this app is presently primarily concerned with learning the Latin transliteration of the Georgian letters, I’m not sure how much more beneficial this would be.
- As mentioned, the Georgian alphabet doesn’t distinguish between upper and lower cases, but unlike Latin and Cyrillic alphabets which are written on the same horizontal level, Georgian varies between three different levels. It would be good to make this more explicit somehow, as presently to the unknowing user, the letters seem to be awkwardly vertically off-centered.
- UI concept. As stated presently this is a proof of concept, and once the technical elements have all been implemented, I will begin working on the UI.
- Include an option to log in with social media networks, challenging friends etc.
- Maybe make it available for free on the AppStore but as it is an open source project, the code will be hosted on my GitHub account.

BTW, while writing this post I stumbled across [*Alphi*](https://itunes.apple.com/en/app/alphi/id549527299?mt=8) by Johannes Berger. Although his app appears to be of a similar vain, there are some fundamental differences (from the information presented on the *AppStore*), most notably that it only teaches you the letter’s name, not the latin transliteration or english pronunciation, and it supports in-app purchases.

In summary, this is an application I am developing to aid in the learning of the Georgian and Armenian alphabets and so I am mainly focussing on my needs as opposed to the general public. That being said, I would of course like to receive feedback as the app and code will be eventually be released for free.

Stay turned for updates and videos! :)
