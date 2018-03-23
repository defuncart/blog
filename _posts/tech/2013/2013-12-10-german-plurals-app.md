---
layout: post
title: German Plurals App
date: 2013-12-10 22:00:00 +01:00
tags:
- GermanLanguage
- HTML
- javascript
---
Other than knowing the correct gender of a noun in German, one of the other difficulties is knowing how to form its plural! This, at least to me, seems more complicated than in English, French, or Russian. [*Der Die Das*](https://itunes.apple.com/us/app/der-die-das/id548055880?mt=8) is a great application to know the test the gender of a noun, while apps like [*Babel*](https://www.babbel.com) and (potentially) [*Memrise*](https://www.memrise.com/) state the article when studying a new noun.

However, no one seems too interested in testing one’s ability in the plural of a noun, other than this [*German Noun Quiz*](http://www.helloresolven.com/portfolio/german-nouns-quiz/). So I decided to throw together a simple proof-of-concept to determine if in fact such an application would be beneficial (to me at least) für Deutsch lernen.

As far as I can see, there are two possible implementations:

1. The application displays a word, say **Buch**, the the user needs to type in the correct answer, in this case **Bücher**.
2. The application displays a word, again **Buch**, and the user has the option of choosing the correct answer from, say, four answers, three of which are incorrect. So, **Buch**, **Buchs**, **Buchen**, and **Bücher**.

For this simple demo, I’m going to implement option one. Now, as this will be a typing-based game, I’d sooner use it on my laptop than smartphone, so I’m going to (initially) design it as a desktop application. An native application doesn’t make much sense to me, so I’m going to design it in HTML, with a possible view to, say, Facebook integration.

The HTML file is very simple, and basically displays the question in a header, lets the user answer in a text box, and displays the score below in a paragraph

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Hello World</title>
    <script defer type="application/javascript" src="js/GermanPlurals.js"></script>
  </head>
  <body>
    <h1 id="questionWord">Question Word</h1>
    <p>Enter the plural: <INPUT TYPE="TEXT" id="answer"><BR><BR>
      <INPUT TYPE="BUTTON" Value="Submit" onclick="checkAnswer(this.form)"></p>
    <p id="score>"></p>
  </body>
</html>
```

while all the computation happens in the javascript file *GermanPlurals.js*

```js
//array of words (in their singular form)
var singularWords = ["Das Buch", "Der Mann", "Die Frau", "Das Kind"];
//and an array of their plural forms
var pluralWords = ["Bücher", "Männer", "Frauen", "Kinder"];

//variables to the question word, answer, and score HTML elements
var questionWord = document.getElementById("questionWord");
var answer = document.getElementById("answer");
var scoreElement = document.getElementById("score");

//a variable to note which word we are quizzing
var questionIndex;
//and a variable to keep count of the user''s score
var userScore = 0;

//initialize the game by setting up the next question
setUpNextQuestion();

//this function sets up the next question
function setUpNextQuestion()
{
    //generate a random index from 0 to 3
    questionIndex = Math.floor( Math.random()*4 );

    //set the word at this position as the question word
    questionWord.innerHTML = singularWords[questionIndex];
    //and set the user''s current score
    scoreElement.innerHTML = "Your current score is " + userScore;
}

//this function checks the submitted answer
function checkAnswer(e)
{
    //check the supplied answer against the correct answer
    //generally we'd convert both to lower case to counteract any
    //case issues but in German nouns are always capitalized...
    if( answer.value == pluralWords[questionIndex] )
    {
        console.log("correct!");
        userScore++;
    }
    else
    {
        console.log("incorrect");
        console.log("your answer is " + answer + " but the correct
        answer is " + pluralWords[questionIndex] );
    }

    //remove previous answer and setup next question
    answer.value = "";
    setUpNextQuestion();
}
```

And our very basic game is then operational!

![]({{site.baseurl}}/assets/images/posts/2013/13-12-10/01.png)

One annoying thing is that the ENTER key doesn’t work by default to submit the answer. This can be fixed by adding the simple script

```html
<script type="text/javascript">
//check answer (or whatever was typed) when enter button is pressed
document.onkeypress = function checkIfEnterWasPressed(key)
{
  if(key.which == 13)
  {
    checkAnswer();
  }
}
</script>
```

to the HEAD of the HTML document.

So the proof of concept is operational, and, if it had a larger dictionary, I believe it would be a useful study tool. Although *German Noun’s Quiz* is already quite a fully-functioning application (singular and plural), it requires the purchase of noun packs for 99¢ each. Thus I feel that a fully-developed plurals-testing application could have its own (small) place in the market if free and fun to play.
