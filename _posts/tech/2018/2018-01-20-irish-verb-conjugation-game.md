---
layout: post
title: 'Irish Verb Conjugation Game'
date: 2018-01-20 16:00:00 +0100
category: tech
tags:
- Konjugator
---

Today I starting sketching ideas for an Irish Verb Conjugation game. From what I've seen, nothing of the kind exists for the Irish language. There are, for instance, books such as [*Collins Easy Learning Irish Grammar*](https://www.harpercollins.co.uk/9780008207045/collins-easy-learning-irish-grammar/) and the [*Verbix*](http://www.verbix.com/languages/irish.html) online conjugator, but no game for Android or iOS where one can learn/test their knowledge of verb conjugation as Gaeilge.

My idea would be to include four tenses, An Aimsir Láithreach (präsens), An Aimsir Chaite (prätritum), An Aimsir Fháistineach (Future 1) and An Modh Coinníollach (Konditional) for a group of the most popular verbs (say 10 or 100 for the first prototype, 500 for the final version). The player could practice conjugating a single verb and a single tense or multiple tenses. A conjugation chart would be available as a popup.

![]({{site.baseurl}}/assets/images/posts/2018/18-01-20/01.png)

The conjugations could be tested by either conjugating a verb in full (top left). Other options would be multiple choice (top right), typing (bottom left) and matching (bottom right) Irish conjugations to English translations.

![]({{site.baseurl}}/assets/images/posts/2018/18-01-20/02.png)

Verbs could be organized into groups. Like in *Caoga caoga*, players would need to complete all verbs belonging to a group before they could proceed. A test option would be available for those with advanced knowledge looking to skip ahead.

![]({{site.baseurl}}/assets/images/posts/2018/18-01-20/03.png)

What is interesting about Irish is that
- there are only 11 irregular verbs
- only two conjugation types (1st conjugation, 2nd conjugation)
- no infinitive, instead uses a verbal noun

Thus the game could theoretically use an algorithm to conjugate the verbs, with a database for the irregular verbs. Audio playback would be desirable although difficult to implement.

Lets see how *Caoga caoga* fairs first (I am targeting a release for the beginning of March) - then it will be easier to gauge if there is sufficient interest for subsequent Irish Language learning games.
