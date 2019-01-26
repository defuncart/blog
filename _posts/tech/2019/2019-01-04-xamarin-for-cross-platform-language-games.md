---
layout: post
title: 'Xamarin for Cross-Platform Language Learning Games'
date: 2019-01-04 18:00:00 +0100
category: tech
tags:
- Xamarin
---

Over the past two years I've prototyped, built and released numerous language learning games, for instance *Caoga caoga*, *Der Die Das* and *Konjugator*. As I professionally use Unity day-to-day, it made sense to build these Cross-Platform MVPs (Minimal Viable Products) as quickly as possible using Unity itself. However, as Unity is a games engine and these aforementioned games are all UI-based, Unity is completely overkill, as, for instance, the UI doesn't need to be rendered 30/60 times per second!

### Der Tropfen, der das Fass zum Überlaufen bringt

Although these games may be more taxing on the battery than a native solution, Unity is still a good compromise as an initial MVP can be exported using WebGL and hosted online, while beta and production version can be exported for iOS and Android, my main platforms of concern. Moreover, I have a library of custom modules which can be easily imported into a new project and help speed-up development ten-fold.

However, while developing *Konjugator*, it became clear that I was using the wrong tool for the job as, not only did I need to create a custom keyboard for mobile devices, I also needed to create a custom input field too. Thus I was trying to create a UI application in a gaming engine with the end result not only not as efficient as a native solution, but also not as fully-functioning (in the sense of what players would expect from UI controls) as a native solution.

### Go Native?

Of course I could create a native iOS app using Xcode and Swift, and a native Android app using Android Studio and Java, however then I'd double my initial workload while needing to maintain two code-bases going forward.

Another option would be creating the app once using Javascript, and then building a native app using PhoneGap/Cordova or React Native. However, I honestly don't like Javascript, and I don't know if React Native would (professionally) be worth the time investment to learn.

### Xamarin

Being already proficient in C# and using Visual Studio daily, Xamarin seems to be a promising solution as it allows one to build native apps using a shared C# codebase. In the case of Xamarin.Forms, I expect that 99% of my codebase will be shared, while being able to export simple, native (in the sense of performance and UI) language games.

### Not saying goodbye, just saying...

I do not expect that I'll stop prototyping or creating language learning apps with Unity, however in the case of *Konjugator* it makes sense to explore other options.

My goal is to learn enough of Xamarin.Forms so that I can write a cross-platform MVP for *Konjugator*. To this end, I will try and create a simple project each weekend, starting with *Hello World* tomorrow!
