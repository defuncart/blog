---
layout: post
title: 'A Declension Game Idea'
date: 2015-02-09 13:00:41+01:00
category: tech
tags:
- macOS
- Swift
- Deklinator
---
On Friday I spoke about *αბц*, an alphabet learning application I created to help me learn the Georgian alphabet. However, *αბц* isn’t the only application I’ve designed to aid language learning, and *Declinator* is one such other example.

<table bgcolor="#FFFFFF" border="0" bordercolor= "#FFFFFF" cellspacing="0" cellpadding="0">
  <tr>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-09/01.png"></td>
    <td><img src="{{site.baseurl}}/assets/images/posts/2015/15-02-09/02.png"></td>
  </tr>
</table>
<p></p>

*Declinator* is an OSX based application (completely written in *Swift*) which tests the user’s declination of Russian adjectives and nouns. The application presents the user with a randomly selected adjective and noun, and then instructs which case should be utilized. For instance, in the first image above, **хороший человек** should be declined in the **dative singular** case. The user types their answer, and if it is correct, then a green checkmark is displayed and a correct jingle is played, whereas if they are incorrect, then a red x is displayed and an incorrect jingle is played, along with a popup showing the correct answer.

I personally decided to create this application as declining Russian adjectives and nouns can be one of the trickier aspects for beginner and intermediate learners.

The application is implemented using a knowledge based approach where for every noun every possible declination is saved within a custom *Noun* class.

![]({{site.baseurl}}/assets/images/posts/2015/15-02-09/03.png)

Now this could be algorithmically achieved, as the declination of nouns follows a standard approach. However, because of some exceptions, человек being a perfect example, I decided to use a hard-coded knowledge approach.

Once we consider the adjectives, things get a lot more complicated as three genders, being plural or not and six cases leads to a whopping 24 possibilities, while for in accusative case, the nouns animacy must be considered.

![]({{site.baseurl}}/assets/images/posts/2015/15-02-09/04.png)

However these 24 possibilities can be halved (as the masculine and neuter singulars are generally identical, the same form for genitive, dative, instrumental, proposition feminine singular etc.). Again a hard-coded approach is fail-safe, but requires a hand-checked tabular.

Presently the application only considers 10 nouns and 10 adjectives, but I plan on substantially adding to this. Also game modes would be included such as which cases, genders to test, whether adjectives or nouns on their own or mixed as above etc., while a page with full declinations and spelling rules would be useful also. For incorrect answers, although a pop-up isn’t the best user experience, it is quite effective I feel.

Stay tuned for updates. As usual, the application will be available for download and the source code will be available on GitHub.
