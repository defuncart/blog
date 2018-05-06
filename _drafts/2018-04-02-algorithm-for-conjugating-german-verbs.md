---
layout: post
title: 'Determining an Algorithm for Conjugating German Verbs (Part 1)'
date: 2018-04-02 10:00:00 +0200
category: tech
tags:
- Konjugator
---

Before I discussed about determining an algorithm to conjugate Russian verbs. Today, in the first of a two-part series, I will discuss how German verbs are conjugated in the main tenses, before putting forward an algorithm in Part 2.

German verbs are generally categorized as being either *stark* (strong), *schwach* weak or *gemischt* (mixed), depending whether the verb's *Stammvokal* (stem-vowel) is changed in any of the tenses.
1. *schwache Verben* are completely regular. They take **-te** endings in the *Präteritum*, and **-t** endings for their *Partizip II*.
2. *starke Verben* have *Stammvokal* changes. They take **-en** endings for their *Partizip II*.
3. *gemischte Verben* take *schwache Verben* endings but have *Stammvokal* changes.

### Präsens

#### Trennbare Verben

### Perfekt

The *Perfekt* tense is formed by using an auxiliary verb (**haben** or **sein**) and the **Partizip II**.

| | | |
| --- | ---- | ----- |
| ich   | habe   | gekauft |
| du   | bist   | gegngen |
| Sie   | sind   | angekommen |

**Algorithm**: For a given verb, we only need to known it's *Partizip II*, which auxiliary verb it takes, and how to conjugate that auxiliary verb.

#### Partizip II

The *Partizip II* (also know as the *Partizip Perfekt*) is formed depending on the verb type:

|
------|:------:|:------:
*schwache Verben*               | ge + Verbstamm + (e)t           | gekauft
*schwache, trennbare Verben*    | präfix + ge + Verstamm + (e)t   | eingekauft
*schwache, untrennbare Verben*  | präfix + Verstamm + (e)t        | benutzt
Verbs ending with *-ieren*      | Verstamm + t                    | studiert
*starke Verben*                 | ge + Perfektstamm + en          | gekommen
*gemischte Verben*              | ge + Perfektstamm + t           | gekannt

while there are some irregularities too (i.e. sein gewessen etc.).

**Algorithm**: Although the *Partizip II* could be determined algorithmically, due to the irregularities, *starke/gemischte* Verben which use a *Perfektstamm* and the additional e between Verbstamms ending in *t*, *d*, *n* and *m*, and the added *t*, I think it is best to include the *Partizip II* in the verb model instead of trying to compute it.

### Präteritum



### References

[Deutsch Plus - *Partizip II*](https://www.deutschplus.net/pages/Partizip_II_Partizip_Perfekt)

[Duden – *Starke und schwache Verben*](https://www.duden.de/sprachwissen/sprachratgeber/Starke-und-schwache-Verben)
