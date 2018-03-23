---
layout: post
title:  'Unity or SpriteKit for 2D iOS Game Development?'
date:   2017-11-09 20:00:00 +0100
tags:
- iOS
- Unity
- SpriteKit
- article
---

{% include figure.html imagePath="2017/17-11-09/LinkedInCoverImage.png" caption="Images courtesy of Apple, Microsoft and Unity respectively." %}

Are you thinking of exploring 2D Game Development for iOS but not sure which tools you should invest your time into learning? In this article I will talk about my experience with Unity and SpriteKit, two of the leading options available to iOS developers. In a nutshell here are what I consider the pros and cons of each engines.

[Unity](https://unity3d.com/) is a proprietary, cross-platform 3D gaming engine first released in 2005. Since 2013 Unity has natively supported 2D.
* (+) Used extensively by both indie and major studios
* (+) Low learning curve
* (+) Rapid prototyping
* (+) Asset Store
* (+) Live debugging
* (+) Can export to every major platform
* (+) Built in Analytics, Cloud Build, Remote Settings
* (-) Quite large apps
* (-) Non-optimized 2d performance
* (-) Coded using C# as opposed to Swift or Objective-C which most iOS developers will be familiar with.
* (-) Collection of player data

[SpriteKit](https://developer.apple.com/spritekit/) is a 2D gaming framework developed by Apple, first introduced in iOS 7.
* (+) Developed by Apple
* (+) Optimized for iOS (and macOS, tvOS, watchOS)
* (+) Completely free
* (+) GameKit, GameplayKit
* (-) Locked into Apple's ecosystem
* (-) Very code heavy - basic objects like buttons do not exists
* (-) Yearly update process
* (-) Supporting older iOS versions can be tedious
* (-) Apple's commitment to SpriteKit isn't abundantly clear
* (-) Visual editor is still quite basic compared to Unity

The remainder of this article will contrasts these points more rigorously.

**Game Development or iOS Development? Existing iOS Development Knowledge?**

The most important question to ask is, do I wish to make mobile games or iOS apps? If one wishes to design iOS apps and games, then SpriteKit's integration within Xcode will feel natural along with Interface Builder. Moreover, SpriteKit can be written in Swift (or Objective-C), as opposed to C#. If one wishes to make games, and has no prior iOS development experience (or possibly even a Mac to develop on), then Unity and C# would probably be faster to get up and running with, especially if they don't come from a programming background.

**Cross-platform?**

As this article is centered on games for iOS, cross platform is clearly not a consideration, however if one is hoping to target multiple platforms, then realistically Unity, or the open source framework [Cocos2d](http://www.cocos2d-x.org/), are the only viable options as there is no plugin that can magically port SpriteKit to Android.

**Budget?**

SpriteKit is part of Xcode and completely free to use, while Unity has Personal (free), Plus and Pro versions. One can freely release apps created using Unity Personal (as long as revenue and funds do not exceed $100k annually), but cannot, for instance, remove the initial "Made with Unity" splash screen. Unity Plus costs $35 a month and allows custom splash screens.

**Supporting Older Versions of iOS?**

Unity targets iOS7+, while SpriteKit is iOS8+. Now this mightn't seem like a big deal as most iOS users are on the latest two OS releases, but when one considers the iPad in isolation, the level of upgrading is specifically lower - popular models like the iPad2 and the original iPad mini are capped at iOS9.3.

Like most new APIs from Apple, SpriteKit upgrades are limited to the OS they were announced alongside with, thus if one wishes to utilize them, then they must forsake supporting older OS versions. Certain target markets are more likely to use certain devices and iOS version so one needs to plan accordingly.

**Performance, Install Size**

SpriteKit is a framework add-on, while Unity is a full blown 3D game engine, thus Unity's performance is not as optimized as a dedicated 2D engine or framework. Moreover, a blank project has an install size of 35.8MB, compared to SpriteKit's leaner 25.3MB.

**Prototyping**

A project developed with Unity will be prototyped MUCH FASTER than SpriteKit due to the advanced visual editor, tons of features available out of the box and the approach of adding script components to control an object as opposed to writing classes. Once a prototype is deemed viable, it is not unheard of for it to be re-written for SpriteKit or Cocos2d.

**Asset Store**

For indie developers whose budget cannot stretch to employing an artist, or for non-programmers looking to enter the world of game development, the [Unity Asset Store](https://www.assetstore.unity3d.com/) contains a wide range of free and paid assets from code snippets to music and art to complete game packages.

**Deploying to Device**

SpriteKit projects can be easily deployed to a physical device or simulator via Xcode, while Unity projects have the additional step that they must first be built to an Xcode project, which in turn can then be deployed to devices. This can take a LOT of time, depending on the scale of your Unity project, and personally I tend to do a lot of quick testing on my Android phone, and major testing less frequently on an iPad.

**Live Debugging**

When a Unity project is running inside the Unity Editor, all variables can be adjusted, even components added or removed from game objects, thus facilitating a live debugging environment where gaming ideas can be easily tested. Conversely, when one wants to test any new gaming variables or ideas in SpriteKit, the project must be built and ran on a device (or the simulator).

**Analytics, Cloud Build, Remote Settings**

Unity has built-in [Analytics](https://unity3d.com/unity/features/analytics]), [Cloud Build](https://unity3d.com/unity/features/cloud-build) (the automatic building of a project from a source control repository) and [Remote Settings](https://blogs.unity3d.com/2017/06/02/introducing-remote-settings-update-your-game-in-an-instant/) (the ability to change variables online). Although these could be achieved using external tools, built-in is really convenient.

**Stability, Updates, Future**

SpriteKit is updated yearly along with a new version of iOS, with bug fixes throughout the year. Over the last three years Apple has included Reference Nodes and Tile Map support but for instance there is still no simple UI, causing a lot of 'rolling-your-own' due to the performance trade off of mixing SpriteKit and UIKit. With their new 2017 release model, Unity will have weekly updates with new features released as they are finished, as opposed to major updates every few months.

iOS9 shipped with a buggy version of SpriteKit that took a few months to somewhat fix. The lack of communication from Apple enraged many developers, while others (myself included) began to look at other options. Although Apple clearly values games for their ecosystems, their commitment to SpriteKit isn't abundantly clear. Other than integration with ARKit, iOS11 had no new features for SpriteKit.

### Conclusion

In this article I have presented some of the main contrasts between SpriteKit and Unity that I have experienced from using both within a professional environment. Which will you be utilizing for your next project?
