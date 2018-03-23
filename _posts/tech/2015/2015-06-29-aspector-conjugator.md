---
layout: post
title: 'Aspector / Conjugator'
date: 2015-06-29 22:35:25 +02:00
tags:
- macOS
- Swift
- Konjugator
- Deklinator
---
A few months back I spoke about *Declinator*, an application game for testing one’s command of the various noun and adjective declinations for Russian. Today I want to introduce *Aspector* and *Conjugator*, two impromptu applications I have just created.

In Russian, a verb may have an imperfect or a perfect aspect, for instance *делать*/*сделать*, *знать*/*узнать*, *идти*/*пойти* etc. Following on from the ‘drilling into memory’ approach, I created the very simple application will displays a verb, and asks the user to select the correct aspect (by click or using LEFT and RIGHT arrows).

![]({{site.baseurl}}/assets/images/posts/2015/15-06-29/01.png)

Like many European languages, Russian verbs are conjugated, that is with different verbal endings for different pronouns: *я делаю*, *он делает*. So I created another simple application which presents a verb and asks the user to supply the correct conjugation for a specific pronoun (I, you, he etc.) and a specific tense (past, present, future, imperative).

![]({{site.baseurl}}/assets/images/posts/2015/15-06-29/02.png)

![]({{site.baseurl}}/assets/images/posts/2015/15-06-29/03.png)

Although quite useful tools, I’ve never really seen an ‘aspector’ game before, and only stumbled across [*Practice Russian*’s verb conjugation](http://www.practicerussian.com/Tests/TestVerbs.aspx) via google.

*Aspector* features pairs of 400 verbs, while *Conjugator* is presently a proof of concept utilizing a single verb. As per *Declinator*, this follows a coded knowledge approach in which the conjugations are stored in memory. Both games are written in *Swift*. 

This coded knowledge approach, however, requires a large number of verb or noun forms before the application could be considered useful. By considering grammatical rules and noting exceptions, a algorithm could potentially be derived.

Interestingly, these conjugations and declinations are well documented throughout the internet. [*Wiktionary*](https://ru.wiktionary.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0), for instance, contains thousands of pages on different verbs, nouns, adjectives, all of which sport the relevant conjugation or declination table. One approach could be to ‘scrape’ online pages for these tables or, as the compete wiki database is available to publicly download, create a custom database.

Although conjugation may be relatively easy to achieve via an algorithm, due to many declension exceptions (especially genitive plural), a coded knowledge approach seems to be a potentially better approach for *Declinator*. For *Conjugator* and *Aspector*, the manual creation of databases simply isn’t feasible or logical. If I am to continue with these games, then I need to consider extracting info from a pre-existing database, or coding an algorithm.
