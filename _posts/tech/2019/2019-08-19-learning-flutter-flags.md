---
layout: post
title: 'Learning Flutter: flags'
date: 2019-08-19 18:00:00 +02:00
category: tech
tags:
- Flutter
- LearningFlutter
---

A simple flags app build using Flutter.

![](https://raw.githubusercontent.com/defuncart/learning-flutter/master/flags/screenshots/01.gif)

The goals of this project were to utilize the GridView and Hero widgets by rendering flag images on screen.

## Overview

- HomeScreen contains a GridView of clickable flag images.
- DetailsScreen contains info on a clicked flag.

## Remarks

- Originally I had planned on using SVGs and the [flutter_svg](https://pub.dev/packages/flutter_svg) by Dan Field, however many of the *country-flags* SVG files did not render correctly, perhaps due to some file export incompatibilities.
- Åland Islands is sorted last on the list, probably because *compareTo* considers a < z < å.

## Resources

[GridView](https://api.flutter.dev/flutter/widgets/GridView-class.html)

[Hero](https://api.flutter.dev/flutter/widgets/Hero-class.html)

## Assets Utilized

[countries.json](https://gist.github.com/erdem/8c7d26765831d0f9a8c62f02782ae00d)

[country-flags](https://github.com/hjnilsson/country-flags/)


<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="https://github.com/defuncart/learning-flutter/tree/master/flags">GitHub repository</a>.</font></p>
