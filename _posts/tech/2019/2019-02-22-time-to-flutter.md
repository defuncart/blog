---
layout: post
title: 'Time to Flutter?'
date: 2019-02-22 18:00:00 +0100
category: tech
tags:
- Flutter
- Xamarin
---

At the start of the new year, I discussed the need to find a cross-platform solution to quickly prototype language learning games (which, for extensive purposes, are apps). I settled on Xmarain, and over the last few weeks I've been steadily learning Xamarin.Forms to the point that I can now start working on ap projet.

## Flutter

One solution which I didn't consider was Flutter. [*Flutter*](https://flutter.dev/) is an open-source mobile application development SDK created by Google, which can be used to develop applications for Android and iOS. Although the SDK was only officially released last Dec, the community is actually very vibrant as the SDK was in alpha/beta for a long time. Moreover, as Flutter is the primary method of creating applications for Google Fuchsia, Google's future super OS, it isn't some community-led SDK that may run out of active controbutors in the future.

> Flutter allows you to build beautiful native apps on iOS and Android from a single codebase.

> Fast Development: Paint your app to life in milliseconds with stateful Hot Reload. Use a rich set of fully-customizable widgets to build native interfaces in minutes.

> Expressive and Flexible UI: Quickly ship features with a focus on native end-user experiences. Layered architecture allows for full customization, which results in incredibly fast rendering and expressive and flexible designs.

> Native Performance: Flutter’s widgets incorporate all critical platform differences such as scrolling, navigation, icons and fonts to provide full native performance on both iOS and Android.

So far, so good, but is really worth using over Xamarin or React?

## Xamarin.Forms is ok but...

I really hate laying out UI in Xamarin.Forms. Maybe with more experience I'll get better at it, but honestly I hate writing UI code like it is 2010. Although there is an XAML Designer, it isn't compatible with Xamarin.Forms. I hope this is something they improve upon in the future, but with the fragmented native of the platform (Xamarin.Native and Xamarin.Forms), I'm not expecting anything soon.

## First Impressions

- Flutter's focus on UI perfectly suits my UI-centric language games.
- Hot reloading, oh fuck yeah. Code changes are automaticlly visible on device/simulator on code saving. This can only be a massive time saver.
- There are so many articles praising Flutter that it is hard to ignore, for instance [*Flutter will change everything, and is an excellent choice for iOS development*](https://medium.com/coding-with-flutter/flutter-will-change-everything-and-apple-wont-do-anything-about-it-f495e7087802), [*13 Reasons Why you should choose/ consider to move to Flutter*](https://medium.com/flutter-community/13-reasons-why-you-should-choose-consider-to-move-to-flutter-in-2019-24323ee259c1) and [*Flutter: the good, the bad and the ugly*](https://medium.com/asos-techblog/flutter-vs-react-native-for-ios-android-app-development-c41b4e038db9).
- UI Controls are consistent across platforms, which I personally prefer (as opposed to rendering as per native controls).
- Although UI code must also be written in Flutter, [*Flutter Studio*](https://flutterstudio.app/) is a web app which allows one to layout a UI visually and copy the generated code.
- Dart is honestly a language I've never heard of, but from first appearances it looks to be a mix of Swift, C# and Javascript. I don't expect it to be difficult to learn.

## Conclusion

Although Flutter is something I'd love to start working with straight away, I think it makes sense to at least develop one game using Xamarin.Forms before jumping ship.
