---
layout: post
title: Code Signing OSX Applications using the Terminal
date: 2014-02-25 23:59:00 +01:00
category: tech
tags:
- macOS
- ObjectiveC
- Xcode
- terminal
---
*Xcode* easily allows one to sign (using an Apple Developers Account) an application or installer by selecting the relevant certificate in the Project’s general settings. However, what if you are building the project outside *Xcode*? Luckily there is the [*codesign*](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/codesign.1.html) terminal command

```
codesign -f -s "Developer ID Application" MyApp.app
```

where **Developer ID Application** is a 40-digit string unique to a specific developer’s certificate, and **MyApp.app** is the full path to *MyApp*, for instance */Applications/MyApp.app*. If this certificate is already download on your Mac, then go to Keychain Access and locate it. If not, log into the Apple Developer’s portal, and download the certificate.

![]({{site.baseurl}}/assets/images/posts/2014/14-02-25/01.png)

Double click to open it, and then find at the very bottom under *Fingerprints* locate SHA1.

![]({{site.baseurl}}/assets/images/posts/2014/14-02-25/02.png)

Copy this string and remove all the spaces. This is then the unique 40-digit string.

Afterwards, the signed application can be verified using ```codesign -vvv MyApp.app``` where **MyApp.app** is again the full path to *MyApp*.
