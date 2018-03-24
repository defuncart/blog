---
layout: post
title: MIDI over Bluetooth LE between iOS 8 and OSX 10.10
date: 2015-02-20 23:13:00 +01:00
category: tech
tags:
- iOS
- macOS
- Swift
- Kontrolr
---
While studying my MFA, I designed the application **kontrolr** so that I could control *Ableton Live* and *Max for Live* modules directly using MIDI from my iPad and a MIDI-USB cable. Although this functions perfectly fine, and is better than OSC and a wireless router or WAP, the cable is somewhat inconvenient I must admit. Since the announcement of Bluetooth LE and iOS 7, I’ve been meaning to add MIDI over Bluetooth support, but never got the chance. Today I was browsing through WWDC 2014 topics and discovered Core Audio updates which actually effortless allow MIDI over Bluetooth LE between iOS 8 and OSX 10.10 devices.

I won’t go into any specifics here, but basically Bluetooth LE is a low-energy, low data transfer protocol which has already been around for a few years, but really came to prominence after iOS 7 and Apple’s iBeacons. For iOS 8, there now exists dedicated Peripheral (sending) and Central (receiving) view controllers which basically do all the hard work for you. Consider the following code

```swift
import UIKit
import CoreAudioKit
import CoreMIDI

class ViewController: UIViewController
{
  var localPeripheralViewController:CABTMIDILocalPeripheralViewController?

  override func viewDidLoad()
  {
    super.viewDidLoad()

    localPeripheralViewController = CABTMIDILocalPeripheralViewController()
  }

  @IBAction func yesIWantToAdvertise(sender: AnyObject)
  {
    self.navigationController?.pushViewController(localPeripheralViewController!, animated: true)
  }
}
```

which creates such a peripheral view controller. When the user presses a button (a simple single-view, single button demo application in my case), this peripheral view controller is pushed into view and they are presented with the following screen in which you can start advertising. 

![]({{site.baseurl}}/assets/images/posts/2015/15-02-20/01.png)

Now on the OSX side, all that needs to be done is to go to Audio MIDI Setup

![]({{site.baseurl}}/assets/images/posts/2015/15-02-20/02.png)

and click on the Bluetooth configuration option

![]({{site.baseurl}}/assets/images/posts/2015/15-02-20/03.png)

and connect to the iPad. Now the iPad will be connected, and in fact ALL output MIDI will be routed to the computer. Thus, by firing up the now-outdated iOS 7 incarnation of *kontrolr*, 

![]({{site.baseurl}}/assets/images/posts/2015/15-02-20/04.png)

all output MIDI will be automatically passed directly, promptly and securely to the OSX, as exemplified by a Max patch below (value 93 on control channel 11)

![]({{site.baseurl}}/assets/images/posts/2015/15-02-20/05.png)

This MIDI can then be routed to Ableton by selecting the “ ” device.

So in short
- MIDI can now be effortless sent over Bluetooth LE between iOS to iOS, OSX to OSX, iOS to OSX and OSX to iOS devices.
- In the case of iOS to OSX, this now does not require the use of a  Bluetooth LE receiver OSX app which then forwards on the received messages.
- In the case of iOS, you don’t even need to code a Bluetooth LE peripheral or central - there are already pre-build view controllers good to go.
- For use with DAWs, while the hardwired USB MIDI approach was already better IMO, this approach is UNDOUBTEDLY better than OSC which requires an internet connection or wireless network adapter and an OSX application to convert these messages to MIDI.
- It takes less than 5 minutes. Although the idea is clearly to adapt these controllers within your apps, by having a ‘helper’ iOS app like the one created here, all current apps on your device can already send and receive. I’ve literally done nothing to *kontrolr* and it can already send MIDI over Bluetooth to my laptop for a performance.

As *kontrolr* is written in *openFrameworks*, lets see what oF 0.9 brings in terms of *Swift* integration!
