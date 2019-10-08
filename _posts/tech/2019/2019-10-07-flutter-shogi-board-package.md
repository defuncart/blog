---
layout: post
title: flutter_shogi_board package
date: 2019-10-07 18:00:00 +0200
category: tech
tags:
- Flutter
- flutter_shogi_board
---

Yesterday I release my first package on pub.dev, [*flutter_shogi_board*](https://pub.dev/packages/flutter_shogi_board/), a shogi board widget for Flutter which can be used to render static game board positions, tsume problems or shogi castles.

![]({{site.baseurl}}/assets/images/posts/2019/19-10-07/01.png)

## Importing a Game Board

As the game board is presently static, a board position can be notated by `{PieceType}-{Row}{Column}`, i.e. `K-59`. If sente or gote aren't specified, then sente is chosen by default. Note that 11 is the top left board cell as per japanese notation.

```dart
final yagura = ['L-99', 'N-89', 'K-88', 'G-78', 'P-97', 'P-87', 'S-77', 'G-67', 'P-76', 'P-66', 'P-56'];

final boardPieces = ShogiUtils.stringArrayToBoardPiecesArray(yagura);
```

To import pieces for both players, use the notation `{Player}:{PieceType}-{Row}{Column}`.

```dart
final tsume1 = ['G:K-51', 'G:S-61', 'G:S-41', 'S:+P-53', 'S:+B-25'];
```

|:-------------------|:-------------------|
| ![]({{site.baseurl}}/assets/images/posts/2019/19-10-07/02.png) | ![]({{site.baseurl}}/assets/images/posts/2019/19-10-07/03.png) |

## Future Plans

This package grew out of my desired to visualize shogi castles in Flutter, and with no widget or even shogi package available, I decided to roll my own.

For the future I would like to utilize this widget not just for displaying static game boards, but also for tsume problems, thus user interaction may be considered. The models and enums may also be moved to their own package, if deemed necessary.

As the game board is static, the notation `G:K-51` is currently utilized to import game boards, however `KIF` may be more suitable for future versions:

```
1 ７六歩(77)
2 ３四歩(33)
3 ７五歩(76)
```

Finally, presently the numbers 1-9 and 一, 二, 三, 四, 五, 六, 七, 八, 九 are not displayed to mark cell positions, this is something that could be offered as an optional boolean defaulting to `true`.
