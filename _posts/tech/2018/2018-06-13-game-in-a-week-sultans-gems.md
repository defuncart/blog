---
layout: post
title:  "#GameInAWeek: Sultan's Gems"
date:   2018-06-13 20:00:00 +0100
category: tech
tags:
- GameInAWeek
- SultansGems
- Unity
---

*Sultan’s Gems* is a simple Match 3 game in which the player tries to achieve a high score within a certain number of moves by matching similar pieces. The project was created for educational purposes as part of James’ **#GameInAWeek** challenge and is released freely under an MIT license. It may be of interest to those looking for a starting point in creating a Match 3 game in Unity for mobile. [Source](https://github.com/defuncart/game-in-a-week/tree/master/SultansGems)

## Screenshots

<table style="width:100%" height="20%" cellspacing="5" cellpadding="5">
  <tr>
    <th><img src="https://raw.githubusercontent.com/defuncart/game-in-a-week/master/docs/assets/images/SultansGems/screenshot1.png" style="width:25% height:100%"></th>
    <th><img src="https://raw.githubusercontent.com/defuncart/game-in-a-week/master/docs/assets/images/SultansGems/screenshot2.png" style="width:25% height:100%"></th>
    <th><img src="https://raw.githubusercontent.com/defuncart/game-in-a-week/master/docs/assets/images/SultansGems/screenshot3.png" style="width:25% height:100%"></th>
    <th><img src="https://raw.githubusercontent.com/defuncart/game-in-a-week/master/docs/assets/images/SultansGems/screenshot4.png" style="width:25% height:100%"></th>
  </tr>
</table>
<p></p>

## What's Included

* Level data is stored as customs assets. Board shape, pieces to initially place, points per stone and which stones are valid can all be assigned in the editor.
* Modular approach in which new levels can easily be added.
* Player data is saved to disk (via Binary Serialization).
* Localization is incorporated throughout.
* Optimized assets (Sprite Packer).
* iOS Launch Screen.
* A complete write-up of the game design can be found in [GameDesignDocument.pdf](https://github.com/defuncart/game-in-a-week/blob/master/SultansGems/GameDesignDocument.pdf).

## Play Online

The game can be played in the browser [here](http://defuncart.github.io/game-in-a-week/SultansGems/).

## Conclusion

Although the match 3 market is over saturated and these games require considerable amount of game balancing, from an implementation point of view, *Sultan's Gems* is is a simple yet functioning match 3 game. This prototype could easily be extended to form a full game.

## Further Reading

* A full list of credits can be found in [Credits.txt](https://github.com/defuncart/game-in-a-week/blob/master/SultansGems/Credits.txt).
* A number of principles utilized in this project are explained in more detail in various [#50-Unity-Tips](https://github.com/defuncart/50-unity-tips) articles.
