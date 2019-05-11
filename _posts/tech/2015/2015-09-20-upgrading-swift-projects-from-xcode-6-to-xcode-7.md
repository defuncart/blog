---
layout: post
title: Upgrading Swift Projects from Xcode 6 to Xcode 7
date: 2015-09-20 14:00:00 +02:00
category: tech
tags:
- Swift
- Xcode
---
With the official release of Xcode 7 and Swift 2 along with iOS9 last week comes the process of needing to upgrade Xcode 6 projects to Xcode 7, but more importantly, changes in the Swift language.

One of the biggest changes in Swift is the new approach to [error handling](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/ErrorHandling.html). Take for instance setting up a shared audio session for backgrounding. Before we would have simply typed

```swift
AVAudioSession.sharedInstance().setCategory(AVAudioSessionCategoryPlayback, error: nil)
```

and could ignore any errors, but now we are forced to deal with them

```swift
do {
  try AVAudioSession.sharedInstance().setCategory(AVAudioSessionCategoryPlayback)
} catch {
  print( "There was an error \(error)" )
}
```

Although it might seem like a pain typing this extra code, it is clearly much safer and should help debugging.

Another change is that certain **NSString** methods are no longer automatically bridged to **String** it seems, for instance **stringByDeletingPathExtension** returns an error that **NSURL** should be used instead. Although Apple has been directing developers to embrace **NSURL** over strings for dealing with paths, the truth is that some major method calls like

```swift
NSBundle.mainBundle().pathForResource()
```

and

```swift
NSFileManager.defaultManager().fileExistsAtPath()
```

still require paths as strings. These **NSString** functions can be manually extended to **String**

```swift
extension String
{
  var stringByDeletingPathExtension: String {
    get { return (self as NSString).stringByDeletingPathExtension }
}
```

Another major change is that of App Transport Security which, although makes complete sense to implement, seems to have a bug for certain HTTPS domains and so (in the case of download from Soundcloud), this needs to be [disabled](https://forums.developer.apple.com/thread/3544) by adding the following entry to **info.plist**

```
<key>NSTransportSecurity</key>
  <dict>
    <key>NSAllowsArbitraryLoads</key><true />
  </dict>
```

Otherwise **println** has been replaced by **print** and some **!** and **?** will have changed due to changes in casting. BTW if you wish to get hands-on with tvOS, you need to download the newest Xcode beta. This also included iOS 9.1.
