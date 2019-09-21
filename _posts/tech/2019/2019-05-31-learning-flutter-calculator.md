---
layout: post
title: 'Learning Flutter: calculator'
date: 2019-05-31 18:00:00 +02:00
category: tech
tags:
- Flutter
- LearningFlutter
---

A simple calculator build in Flutter.

![](https://raw.githubusercontent.com/defuncart/learning-flutter/master/calculator/screenshots/01.gif)

## Overview

- *lib/services/calculator.dart* evaluates expressions using the package *math_expressions*.
- *lib/widgets/calculator_button* is a simple widget which acts as a calculator button (for operands and operators).
- *lib/widget/home_screen* is a **StatefulWidget** which deals with button presses and updating output display.
- On iOS, the launch screen is the same color as *scaffoldBackgroundColor*.

# Remarks

- On each button press, the **HomeScreen**'s whole widget tree is rebuilt.
- The [*Align*](https://api.flutter.dev/flutter/widgets/Align-class.html) widget is really useful and isn't something I've stumbled across before.

## Resources

[math_expressions](https://pub.dev/packages/math_expressions)


<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="https://github.com/defuncart/learning-flutter/tree/master/calculator">GitHub repository</a>.</font></p>
