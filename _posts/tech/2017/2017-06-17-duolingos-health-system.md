---
layout: post
title:  "Duolingo's Health System: To Discourage Binge Playing or a Blatant Paywall?"
date:   2017-06-17 18:00:00 +0100
category: tech
tags:
- article
---

Today on the train I opened up a previously updated version of *Duolingo* on my iPad and was presented with their new monetization model: ads, subscriptions and In-App purchases of in-game currency *Gems*. Although I haven't really been actively using the platform since the start of 2016, I am aware that they need to start funding themselves so that the project can become self-sustainable for the future.

### Ads

'Ads' and 'remove ads' are both stables of FTP games these days: you can play for free, but there'll be ads. Don't like ads? Pay a once-off fee and never seen them again. Ads are the main source of income for many games, and with 10 million users per day, it is clear why *Duolingo* have incorporated them.

At the end of each lesson, *Duolingo* now displays an ad (from an ad network like Google) which, although it takes up most of the screen, does not affect gameplay or intrude upon learning. Moreover, the title *This ad helps keep education free* succinctly explains the need for ads within the game. From a player's perspective, this should be agreeable, while the platform should make sufficient daily income.

<img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/01.png" width="50%"/><br/>

### Health

*Duolingo* have re-introduce the lives system, albeit where before the player needed to complete a level without using up a given number of 'lives' (3), now 'health' (max 5) is persisted between levels.

Thus if I begin with five health points and lose two in level X, then I will only have three beginning level Y. To begin a new level, or continue playing after making a mistake, the player must have health.

In a blog post, Luis states that

> Our research shows that if people do too much Duolingo in one day, it can actually negatively impact their learning because they are less likely to remember what they’ve learned. So we are introducing another new feature on iOS called Health. Health is a way of pacing the use of Duolingo to discourage binging behavior, which is shown to be ineffective for learning a new language. If you lose your Health (by answering incorrectly too many times), we encourage you to go back and practice previous lessons to restore it, or to take a break while your Health restores over time. For those who still want to binge on Duolingo without taking a break or taking the time to review lessons they missed, they can do so by refilling their Health with Gems.

Even if *Duolingo* are trying to avoid players binging, the manner in which they are restricting players seems to more of a leaf taken from F2P games than a concerned teacher. It may not be *pay to win*, but it can be argued that it is *pay to learn*.

1. The player begins with 5 health pieces.
2. Each mistake looses the player a health piece.
3. A new health piece only autogenerates every 5-6 hours.
4. 5 health pieces can be bought for 350 Gems (in-game currency). As an IAP, 400 gems cost roughly $2.
5. Although one health piece can be acquired after successfully revising an old lesson, in-game there is no option other than paying.

<table style="width:100%; height=20%; margin:0; padding:0;" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/h1.png" style="width:50% height:100%"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/h2.png" style="width:50% height:100%"></td>
  </tr>
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/h3.png" style="width:50% height:100%"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/h4.png" style="width:50% height:100%"></td>
  </tr>
</table><br/>

### Video Ads

Separate from the ads mentioned above, before a lesson begins the player has the option to start the level with more health by watching a video ad (Unity Ads). This opt-in feature is seen in many games, however I feel that a popup instead of a whole modal page would suffice. Here it is clear that they want you to watch the ad.

<table style="width:100%; height=20%; margin:0; padding:0;" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/a1.png" style="width:50% height:100%"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2017/17-06-17/a2.png" style="width:50% height:100%"></td>
  </tr>
</table><br/>

### Conclusion

I understand the predicament that *Duolingo* are in: they've created the world's most popular language learning platform and must somehow now find a way to make it self-sufficient. With over 10 million daily users, ads, and the ability to remove ads, is logical. However, I would imagine that a once-off payment ($2/3) instead of a subscription (10,99€ per month) would be more player-friendly. Moreover, I realize that there are many people who'd like to support the *Duolingo* project, but *Duolingo Plus* gives the impression that it is a premium service, when it essentially just removes ads and allows offline lessons to be played. Yes the projects supports loads of languages, but players cannot even change their language when offline.

I find the 'health' system to be both frustrating and an exaggerated form of paywalls seen in F2P games. Beginners should be encouraged to make mistakes and learn from them, not have the fear of a wrong answer ruining their chance of studying further. Yes health regenerates, but who wants to wait six hours? Yes video ads are possible, but Unity Ads limits the amount of videos per hour a player can view, so this is clearly not always a fallback. Yes I could revise old lessons but maybe I actually want to learn something new. If *Duolingo* really wanted to stop players binging, they could limit the number of new levels that a player can start per day before introducing a paywall, it honestly wouldn't be any less subtle that what they have implemented here.

### Resources

[Duolingo Discussions - State of Monetization at Duolingo](https://www.duolingo.com/comment/15695026/State-of-Monetization-at-Duolingo)

[Duolingo Discussions - State of Monetization at Duolingo II](https://www.duolingo.com/comment/22426779/State-of-Monetization-at-Duolingo-II)
