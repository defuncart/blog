---
layout: post
title: Willkommen bei DPNT!!
date: 2013-12-12 22:00:00 +01:00
tags:
- GermanLangauge
- HTML
- CSS
- javascript
---
Today I merged the writing and button-pressing versions of the German plural app into a single DPNT (Deutsch Plural Nomen Test) application. Firstly, the main page (index.html) allows the player to play either game, or to get information on the app

![]({{site.url}}/assets/images/posts/2013/13-12-12/01.png)

The application follows the style derived yesterday, utilizing *New Rockstar* from [*Google Fonts*](https://fonts.google.com/) as the main font. By the way, if you are unfamiliar with *Google Fonts*, basically you can select a font, incorporate it in your HTML file using

```html
<link href='http://fonts.googleapis.com/css?family=New+Rocker' rel='stylesheet' type='text/css'>
```

and then utilize it within CSS using

```css
p
{
    font-family: 'New Rocker', cursive;
    color : black;
}
```

The information page simply explains how to play the game

![]({{site.url}}/assets/images/posts/2013/13-12-12/02.png)

where *Spiel Eins* is not only an updated UI of Tuesday’s post, but also includes buttons for the umlauts incase the user doesn’t have them on their keyboard (personally I prefer to use ALT+U then A/E/O/U when typing on the Mac US keyboard than use the German keyboard).

![]({{site.url}}/assets/images/posts/2013/13-12-12/03.png)

The actual moving from Main → Spiel Eins/Spiel Zwei is done via the function call

```html
window.location.href = "MyPage.html";
```

which seems to do the job just fine. However, the user can go backwards/forwards at any time (as these are merely webpages) so some confirmation should be used during the game etc.

Finally, an array is a great way to store the words, but having to manually type them in

```javascript
//array of words (in their singular form)
var singularWords = ["Das Buch", "Der Mann", "Die Frau", "Das Kind"];
//and an array of their plural forms
var pluralWords = ["Bücher", "Männer", "Frauen", "Kinder"];
```

isn’t the most efficient way, nor flexible if I wish to add another pair. Instead, this can be stored in text files, and then grabbed using *jQuery*

```html
<script language="JavaScript" type="text/javascript" src="/js/jquery-1.10.2.js"></script>
<script type="text/javascript">
  $.get("/lists/singular.txt", function(data)
  {
    //global array of words (in their singular form)
    singularWords = data.split('\n');
  });
  $.get("/lists/plural.txt", function(data)
  {
    //global and an array of their plural forms
    pluralWords = data.split('\n');
    //initialize the game by setting up the next question
    setUpNextQuestion();
  });
</script>
```

where the words here are separated in the text file by newlines. These global variables can then be references in *GameOne.js* or *GameTwo.js* with

```html
window.singularWords and window.pluralWords
```

Now that a basic implementation is achieved, the main priority is Facebook integration. Some other nice additions would be:
1. A time limit on each question, for instance 5 seconds.
2. A points system which is inversely proportional to the time spent answering the question.
3. Categories and a favorites list for the different nouns.
