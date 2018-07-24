---
layout: post
title: 'Unity Continues to Steadily Improve'
date: 2018-07-06 18:00:00 +02:00
category: tech
tags:
- Unity
---

I know I may have mention this a few times before, but *SpriteKit* for iOS9 was a disaster. Although it included some really cool features (SKAudioNode) and the addition of GameplayKit, it seemed broken, supporting older versions of iOS (7 and 8) was a pain and there was little to no feedback from Apple. Eventually, the release was stabilized and the company I worked for released their educational game. I then started to cheat on SpriteKit by learning Unity, before pivoting to using it solely professionally.

Since then, I've written about the differences between SpriteKit and Unity, and how I feel that SpriteKit is dead. Unity, on the other hand, has released a ton of new features over the last two years including built-in analytics, Cloud Build, and Remote Settings, while 2017 show massive 2D improvements

Unity has also adopted a more modular approach by separating their engine out into packages. Although there are three main releases per year, weekly incremental updates are

Packages can be easily

Moreover, Unite's keynote

The underluying message is that Unity is co


#### New Editor UI

The Unity Editor UI isn't pretty, and hasn't been updated since I remember trying it first back in 2008. Version 2018.3 will sport a minor redesign with flat icons and a modern font, while there will a future 'opt-in' full redesign that I am looking forward to try out next year.

#### Unity for Small Things

*Unity for Small Things* is a closed-alpha solution for creating *smaller, faster, lighter experiences* that is targeted towards Playable Ads and Games in Messaging Apps but also relevant for entry-level mobile devices too. Based on a small ECS (Entity Component System) core, it is modular based which an advanced compression pipeline. In short, builds will be smaller and faster than WebGL. Interestingly, code can be 'written' visually by defining components in the Editor. As the runtime supports Web, Android and iOS, it'll be interesting to test *Unity for Small Things* once it is available in open beta.

#### SVG Importer

Released with 2018.2, *SVG Importer* (presently a preview package) imports SVG files into Unity projects.

> The SVG Importer allows you to create sprite assets with a very small file size that will retain their quality at any resolution.

Presently the importer only supports the 2D system (i.e. not the Canvas UI), while generated sprites cannot be colored like regular sprites. In a quick test, an imported SVG was almost 10x smaller in size than a 256x256 PNG. Hopefully we'll soon see Canvas support, if the generated sprites are performant which such a reduction in asset size, I will probably solely utilize SVGs within my projects.

#### Memory Profiler

#### Pixel Perfect Camera

Not something I needed yet, but good to know that a Pixel Perfect Camera is now available as a preview package. Pixel Art isn't going anywhere anytime soon, and this feature has been long requested by the community.

Support for using .java and .cpp source files as plugins in a Unity project
You now have the ability to add .java (as well as .cpp and .a) source files to Unity project plugin folders. These files will be recognized as Unity plugins and compiled into the APK without requiring the user to build libraries separately in Android Studio. The plugin code remains a part of the Unity project, eliminating the need to create a separate Android Studio project.

#### Android

ARM64 is now an Android Target Architecture (when using IL2CPP). Gone are the Android Device Filters (FAT, x86 or ARMv7), with a more understandable Target Architecture (ARMv7, ARM64, x86) which can be automatically split into multiple APKs on build.

*Google Play Instant* allows players to try a 10MB version of a game without having to install it first. The new [plugin](https://github.com/google/play-instant-unity-plugin) builds Instant projects and can run them on connected Android devices.

*Java* (along with *cpp* and *a*) source files are now recognized as Unity plugins and compiled into the APK. The plugin code remains a part of the Unity project, eliminating the need to create a separate Android Studio project to build a library.

#### Improved Prefab Workflow

After years of shying away from the issue, its hard to believe that "nested prefabs" are almost here. In the *Improved Prefab Workflow* talk by Ciro Continisio, it is clear that the new prefabs are so much more than simply nested, and will be a potential game changer for designers. Cannot wait to try them out.

#### Entity Component System, Jobs, Burst Compiler

--

#### TextMesh Pro

Unity bought TextMesh Pro in 2017, and now includes it by default in 2018 version. Unity's UGUI Text solution is quite limited, not very performant and will be eventually deprecated in favor of TextMesh Pro. TextMesh Pro uses an advanced rendering technique (Signal Distance Field) which requires only one asset to be generated per font, as opposed to bitmap fonts which require a font table for each font size. As a somewhat simplified view, it's almost like SVGs and PNGs where SVGs can be scaled to any size and remain crisp, while PNGs need to be rendered for each specific size. Moreover, TextMesh Pro offers more advanced options. I haven't actually used TextMesh Pro before, but will be utilizing it in all my future projects.

#### Unity's Evolving Best Practices

> Let me dispel a rumor right now, you should not be afraid of using the Animation component, we have no plans at this time to deprecate or remove it.

Although this flies in the face of the Unity documentation which had (doesn't seem to anymore) listed this component as legacy and shouldn't be used.

For simple UI animations, use a script instead of either animation systems.

## Resources

[Unity at GDC - ECS for Small Things](https://www.youtube.com/watch?v=EWVU6cFdmr0)

[*Unity for Small Things*](https://unity.com/unity/features/unity-for-small-things)

[2018.2 is now available](https://blogs.unity3d.com/2018/07/10/2018-2-is-now-available/)
