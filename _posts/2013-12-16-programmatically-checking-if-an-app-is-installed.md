---
layout: post
title: Programmatically Checking if an App is Installed on iOS + Launching Apps via
  URL Schemes
date: 2013-12-16 23:07:00 +01:00
tags:
- iOS
- Objective C
---
[Apple URL Schemes](https://developer.apple.com/library/content/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html) allow Native iOS and web apps in Safari to trigger System and installed 3rd party apps.

> For example, if your iOS app displays telephone numbers, you could use an appropriate URL to launch the Phone app whenever someone taps one of those numbers. Similarly, clicking an iTunes link, launches the iTunes app and plays the song specified in the link.

Firstly, one of the main benefits of these URL Schemes is that we can check if an application is installed on the user’s device by checking if the system can open the application’s URL scheme. Lets take *Facebook* as an example.

```objc
NSURL *url = [NSURL URLWithString:@"fb://"];
BOOL isInstalled = [[UIApplication sharedApplication] canOpenURL:url];
```

Secondly, the real benefit is that these applications can not only be opened programmatically from another iOS device, but can be triggered to a certain section of that app. Talking the Facebook example again, ```fb://``` loads up the default homepage of the Facebook app, while ```fb://profile``` opens up the user’s profile page.

```objc
if( [[UIApplication sharedApplication] canOpenURL:[NSURL URLWithString:@"fb://"]] )
{
    //open fb app on the user''s profile page
    [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"fb://profile"]];
}
else
{
    //otherwise load up the app store
    [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"itms-apps://"]];
}
```

Although there is some information on Apple’s official page, a larger-collection of URLs can be found [here](http://www.handleopenurl.com/scheme) and [here](http://wiki.akosma.com/IPhone_URL_Schemes). It seems to be quite app-specific also. *LinkedIn*, for instance, doesn’t seem to allow much more than main page, profile, and groups.
