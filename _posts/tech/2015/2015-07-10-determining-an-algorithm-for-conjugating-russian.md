---
layout: post
title: Determining an Algorithm for Conjugating Russian Verbs
date: 2015-07-10 18:00:00 +02:00
tags:
- Swift
- Konjugator
---
A few days ago I spoke about a game-application for testing the conjugation of Russian verbs, noting the need for either a large database of conjugated verbs, or an algorithm. Well today I investigated the feasibility of such an algorithm.

Firstly, Russian, like English, has regular and irregular verbs. Although comprising of far fewer irregularities, due to perfective/imperfective aspect, spelling rules, constant mutation and the need of distinct conjugative endings, this conjugation process is vastly more complicated. The logical approach would appear to divide verbs into two groups: regular, and irregular. These irregular verbs could be determined from a knowledge-based approach, while the regular verbs could be theoretically instantaneously conjugated via this magical algorithm.

The most popular theory of Russian conjugation is the single-stem approach in which conjugative endings for the present and past tense are added to a stem to form the desired conjugation. This is similar to French or Spanish, but fortunately features few fewer tenses. So for instance for the verb **знать** *to know*

**знай** + **у** = я зна<b>ю</b><br/>
**знай** + **л** = я зна<b>л</b>

Here we see the important concept of vowel-consonant/consonant/consonant-consonant/vowel-vowel combination, where opposites combine harmoniously and the second similar removes the first:

```
V + C = VC | C + V = CV | V1 + V2 = V2 | C1 + C2 = C2
```

Here we also see the concept of soft and hard vowels and consonants. **у** is a hard vowel, but **й** is a soft consonant so they combine together to make **ю**.

![]({{site.baseurl}}/assets/images/posts/2015/15-07-10/01.png)

In the present tense there are two conjugation classes. Above we see the First Conjugation, comprising of verbs generally ending in **-ать**, **-еть** or **-ять**. Second Conjugation verbs generally end in **-ить**. The conjugation endings are related but not identical to the First Conjugation.

![]({{site.baseurl}}/assets/images/posts/2015/15-07-10/02.png)

Some of these Second Conjugation verbs are subject to constant mutation in which for the first person singular, the ending consonant is changed so that it is easier to pronounce.

![]({{site.baseurl}}/assets/images/posts/2015/15-07-10/03.png)

Here the verb **видеть** has the stem **виде** and so we would expect *я видю*. However, **д** mutates to **ж**, and although **е** and **у** combine to form **ю**, **ж** is an inherently hard consonant and so can only be followed by **у**.

For stems which end stressed, this must be considered in the choice of First Conjugation verbs (here **идти** and **давать** are considered irregular verbs).

![]({{site.baseurl}}/assets/images/posts/2015/15-07-10/04.png)

The past tense is vastly simpler to conjugated, with the endings **л**, **ла**, **ло** and **ли** added for masculine, feminine, neutral or plural conjugations.

![]({{site.baseurl}}/assets/images/posts/2015/15-07-10/05.png)

Note that some seemingly irregular verbs, **пить**, **петь**, actually can be separated into two stems, which in turn behave regularly in the present and past tenses. Thus **пить** has the stems **пьй** and **пи** respectively:

**пьй** + **у** = я пь<b>ю</b><br/>
**пи** + **л** = я пи<b>л</b>

Finally, reflexive verbs in the past and present tenses are conjugated according to the above rules, with the reflexive ending appended to the conjugation.

![]({{site.baseurl}}/assets/images/posts/2015/15-07-10/06.png)

So there we have it, a proof of concept of a (very basic) algorithm for conjugating Russian verbs, realized in a *Swift* playground.

I believe that this approach could be successfully utilized with a certain subset of Russian verbs, and combined with a look-up-table for irregular verbs, a useful implementation of the most common 50 or 100 verbs could be implemented.

Some further consideration to the concept of ‘irregular’ verbs is needed, and whether the two stem approach for such verbs, if possible, makes sense, or whether a database is a better solution.

### Resources

Franke, J., The Big Silver Book of Russian Verbs, McGraw-Hill Education.

Freedel, D., Russian 101 [university course], Princeton University.
