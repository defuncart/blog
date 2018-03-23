---
layout: post
title: Determining an Algorithm for Conjugating Russian Verbs (contd.)
date: 2015-07-13 15:01:21 +02:00
tags:
- Swift
- Konjugator
---
Continuing on from Friday’s discussion of a basic algorithm to conjugate Russian verbs, today let’s discover how robust it actually is. Considering the verbs **водить**, **делать**, **думать**, **ездить**, **жениться**, **жить**, **иметь**, **использовать** and **читать**, we have the following output:

![]({{site.baseurl}}/assets/images/posts/2015/15-07-13/01.png)

Bar **жить** and **использовать**, all these verbs are regular first or second conjugation verbs, and thus, as expected, produce the correct conjugations.

**использовать** belongs to the group of verbs which replace **-ова** with **-уй** for the present stem, but otherwise conjugate as normal. **жить**, like **идти**, is a Second Conjugation verb with a stressed ending. Due to the design of the algorithm, it is also able to successfully cope with these two cases.

**ждать** and **писать**, with stems **жда’** and **писа** respectively, cause some problems though. We would expect **ждать** to be a second conjugation verb, but it actually takes first conjugation endings, while the stem of **писать** undergoes mutation for all conjugations in the present. In these and similar cases, we need to supply an additional flag for which endings to takes, stem mutation for all conjugation etc.

I believe that at this point a basic model could be tested within a game scenario. Stay tuned for more info.
