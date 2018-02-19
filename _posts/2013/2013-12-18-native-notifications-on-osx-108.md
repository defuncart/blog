---
layout: post
title: Native Notifications on OSX 10.8+
date: 2013-12-18 23:06:11 +01:00
tags:
- macOS
- ObjectiveC
---
Since the introduction of Mountain Lion (OSX 10.8), Notification Center and Notifications are possible for native applications on OSX just like on iOS.

![]({{site.url}}/assets/images/posts/2013/13-12-18/01.png)

A [*NSUserNotification*](https://developer.apple.com/documentation/foundation/nsusernotification) can be easily created as follows:

```objc
NSUserNotification *notification = [[NSUserNotification alloc] init];
[notification setTitle:@"Title"];
[notification setSubtitle:@"Subtitle"];
[notification setInformativeText:@"Informative Text"];
[notification setDeliveryDate:[NSDate dateWithTimeInterval:0
                    sinceDate:[NSDate date]]];
[notification setSoundName:NSUserNotificationDefaultSoundName];
```

and then sent to the [*NSUserNotificationCenter*](https://developer.apple.com/documentation/foundation/nsusernotificationcenter) using

```objc
[[NSUserNotificationCenter defaultUserNotificationCenter] scheduleNotification:notification];
```

In this case our notification is scheduled for delivery - if we want to explicitly deliver it ourselves, simply use the **deliverNotification:** method. We can even **removeScheduledNotification:**, **removeDeliveredNotification:**, or **removeAllDeliveredNotifications**.

As you’d expect, you can get callbacks on these various methods by implementing the **NSUserNotificationCenterDelegate**

```objc
- (void) userNotificationCenter:(NSUserNotificationCenter *)center
        didActivateNotification:(NSUserNotification *)notification
{
}

- (void) userNotificationCenter:(NSUserNotificationCenter *)center
         didDeliverNotification:(NSUserNotification *)notification
{
}

//Sent to the delegate when the user notification center has decided not to present your notification.
- (BOOL) userNotificationCenter:(NSUserNotificationCenter *)center
      shouldPresentNotification:(NSUserNotification *)notification
{
    return YES;
}
```

**userNotificationCenter:shouldPresentNotification:** can be especially useful as you can explicitly force the display of a notification onscreen (which can be suppressed by the Notification Center if, for instance, the application is already in the foreground), while **userNotificationCenter:didActivateNotification:** is called after a user clicked on the notification.

If we wish to incorporate buttons into this notification (so that the user has the option of easily choosing between different options from the mere notification), we first need to make a [*plist*](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW1) entry for **NSUserNotificationAlertStyle** to **alert**, and then augment our code as follows

```objc
[notification setHasActionButton: YES];
[notification setActionButtonTitle: @"Action Button"];
[notification setOtherButtonTitle: @"Other Button"];
```

Note that regardless of these delegates and methods, the Notification Center WILL suppress notifications if the user has opted out of them in **System Preferences**, or repurpose ALERT notifications displayed as mere BANNERs etc. if the user has chosen so.

![]({{site.url}}/assets/images/posts/2013/13-12-18/02.png)
