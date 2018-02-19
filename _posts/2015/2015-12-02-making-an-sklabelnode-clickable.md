---
layout: post
title: Making an SKLabelNode Clickable
date: 2015-12-02 13:00:00 +01:00
tags:
- SpriteKit
- iOS
- macOS
- Swift
---
One of the limitations of *SpriteKit* over other Game Engines and Frameworks is that it comes without any User Interaction elements built in, while it is expensive (and potentially dangerous - but more on that in the future) in mixing UIKit and presenting different views.

Luckily it is quite simply to add an extension to SKLabelNode to enable a callback mechanism on touch. We would assume it’d be something like

```swift
extension SKLabelNode
{
  var callback: (()->Void)?
  override public func touchesEnded(touches: Set, withEvent   event: UIEvent?)
  {
    callback?()
  }
}
```

However stored properties aren’t possible (yet) in extensions, so we need to use an ‘Associated Object’ to emulate this behavior. First create an **SKLabelNodeCallback** class

```swift
class SKLabelNodeCallback
{
  var onTouch: (() -> Void)?
  init(onTouch: (() -> Void)?)
  {
    self.onTouch = onTouch
  }
}
```

and then a reference key for our object

```swift
private var callbackKey: UInt8 = 0
extension SKLabelNode
{
  var callback: SKLabelNodeCallback {
    get {
      return objc_getAssociatedObject(self, &callbackKey) as! SKLabelNodeCallback
    }
    set(newValue) {
      objc_setAssociatedObject(self, &callbackKey, newValue, objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN)
      self.userInteractionEnabled = true //there is a callback so respond to UI input
    }
  }
}
```

So altogether it would be

```swift
class SKLabelNodeCallback
{
  var onTouch: (() -> Void)?
  init(onTouch: (() -> Void)?)
  {
    self.onTouch = onTouch
  }
}

//stored properties aren''t possible (yet) in extensions, so use an ''Associated Object'' to emulate this behavior
private var callbackKey: UInt8 = 0
extension SKLabelNode
{
  var callback: SKLabelNodeCallback {
    get {
      return objc_getAssociatedObject(self, &callbackKey) as! SKLabelNodeCallback
    }
    set(newValue) {
      objc_setAssociatedObject(self, &callbackKey, newValue, objc_AssociationPolicy.OBJC_ASSOCIATION_RETAIN)
      self.userInteractionEnabled = true //there is a callback so respond to UI input
    }
  }

  override public func touchesEnded(touches: Set, withEvent event: UIEvent?)
  {
    if let callback = callback.onTouch
    {
      callback()
    }
  }
}
```

Stay tuned for more *SpriteKit* tips!
