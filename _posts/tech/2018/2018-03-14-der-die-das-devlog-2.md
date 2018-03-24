---
layout: post
title: 'Der Die Das Devlog #2'
date: 2018-03-14 18:00:00 +0100
category: tech
tags:
- DerDieDas
---

Last week I uploaded an online playable version of *Der Die Das*, with posts on Duolingo and Reddit asking for feedback. Interest was larger than I expected, with 22 feedback form submissions and numerous comments on the forums. In this Devlog I will summarize this feedback and discuss the future development roadmap.

### Proof of Concept is a Success

96% of players would consider download the game for mobile, while 100% would recommend the game to German language learners. Moreover, *simplicity* was a term used often to describe what players liked most about the game. Thus I deem this basic proof of concept a success, and will now turn my attention into creating a MVP (minimal viable product).

### Translation of German nouns

Like I expected, one of the main requests was to translated the German nouns, although I had noted that this wasn't going to happen.

> Der Die Das is not designed to teach vocabulary. There are presently no plans to include English (or other language) translations for the German nouns.

I'm against including translations as
1. the game isn't designed to teach vocabulary,
2. word translations can often be incorrect or misleading and
3. localizing to other languages (Polish, Russian etc.) would be a huge undertaking.

I am firmly of the belief that *Der Die Das* should have a single goal, that is, to test the player's knowledge of articles for Goethe-Institut level nouns. There are plenty of other solutions available for learning vocabulary which would serve that purpose much better than *Der Die Das* ever could.

### Nouns Which Can Take Multiple Articles

One point that a few people latched onto was that some nouns can take multiple articles. *der See* and *der Teil* are on the A1 wordlist, with *die See* and *das Teil* introduced in A2 and B1 respectively. *die Bank* (bank) and *die Bank* (bench) is another possible issue, while *die Kunde*, for instance, is not part of A1-B1 vocabulary. As *der See*/*die See*, *der Teil*/*das Teil* and *die Bank*/*die Bank* are completely different words (compared to der/die/das Joghurt), they are considered as six separate nouns, each with a specified article.

### Hochdeutsch

Although Goethe-Institut covers German in Germany, Austria and Switzerland, *Der Die Das* will only consider Hochdeutsch. Thus *die E-Mail*, which can be written *das E-Mail* ([Duden](https://www.duden.de/rechtschreibung/E_Mail) - *die E-Mail; auch, besonders süddeutsch, österreichisch, schweizerisch: das E-Mail*), won't accept das as an answer. Moreover, *der Geldautomat* instead of *der Bankomat* and *die Fahrkarte* instead of *das Billet* etc. will be included.

### Example Sentences

Another popular request was to see the noun used in context. Now this is something that clearly would be quite useful in the case of *die Bank*/*die Bank* but not something I feel is critical for all nouns. Thus for all noun whose article may be ambiguous (See, Teil, Bank), a short example sentence is displayed underneath. Where the example sentence would explicitly denote the article, appropriate words will be masked with dots.

### Adjectival Nouns

Nouns which are derived from adjectives and represent people can take either the article der or die. In A1, there are five such nouns: *Beamte*, *Bekannte*, *Erwachsene*, *Jugendliche* and *Verwandte*. The game now accepts either der or die as a correct answer for these words. To emphasize that these nouns can take either article, they are displayed as der/die Deutsche and spoken as "der oder die Deutsche".

### Tips

One thing I quite liked about this prototype are the helpful tips. Although there is no shortcut or magic formula to predict articles for every noun in German, there are some tips which can help beginners. However, 67% of players found the tips useful, with only 33% deeming them "almost always useful". This is honestly lower than what I expected, and seems to imply that the tips aren't important for the players.

### Localization

Presently the user interface and tips are in English. As the tips don't seem to be hugely popular with the players, it doesn't make any sense to localize them into multiple languages. Lets see what feedback I receive over the next couple of prototypes, however I am presently leaning towards including the tips in German by default, with an option of viewing them in English, and having the user interface itself available in English, French, German, Italian, Polish, Russian and Spanish.

### More Nouns Coming Soon

Another popular request was more nouns. Soon I will begin adding nouns adhering to A2, thereafter B1. There seems to be a strong interest for B2, however most players surveyed are A1 students and it would be interesting to compare what B1 students would say. Personally I am skeptical about the need for such a game above B1. Lets see how A2 and B1 go first.

### Timeframe

A new version is now available to [play online](http://defuncart.com/games/derdiedas). I hope to implement A2 nouns before the end of next week when another version will be released. I am also working on a related nouns game that I hope to demo soon.

<table cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2018/18-03-14/01.png" style="width:50% height:50%"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2018/18-03-14/02.png" style="width:50% height:50%"></td>
  </tr>
</table>
<p></p>

Thanks for reading. Stay tuned for future developments!
