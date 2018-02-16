---
layout: post
title: Designing SpriteKit Scenes Visually in Xcode 7 (but keeping support for iOS8)
date: 2015-11-03 12:39:29 +01:00
tags:
- Swift
- SpriteKit
- ios
---
The new and improved *SpriteKit* Editor in Xcode 7 brings a whole host of new features that greatly aid the development project of visually designing games and projects that use *SpriteKit*. This post will consider three of these key features, and approaches to keep support for iOS8.

# Reference Nodes

One great new feature in Xcode 7 and iOS9 is the ability to split up an *.sks* file into multiple *.sks* files and reference them via the **Reference Node** object. Thus any GUI components, main characters, repeated backgrounds etc. can be refactored out to their own unique files and then referenced in the main level file, thus promoting code re-use, and the added benefit and any changes to the main character will be reflected throughout all your scenes.

So we can create our character once (here in *Ref.sks*)

![]({{site.url}}/assets/images/posts/2015/15-11-03/01.png)

and reuse as many times as we like (in *GameScene.sks*)

![]({{site.url}}/assets/images/posts/2015/15-11-03/02.png)

Great! There is, however, one major issue: what do you do if you want to support iOS8? As the API is iOS9+, the application will crash when **NSCoder** tries to decode the referenced node.

One approach that works is to create a separate SceneKit file (*GameScene_iOS8*) and replace the reference nodes with empty nodes.

![]({{site.url}}/assets/images/posts/2015/15-11-03/03.png)

Now when we wish to load the Scene, we check what system the device is running.

```swift
let scene: GameScene!
if #available(iOS 9, *)
{
  scene = GameScene(fileNamed:"GameScene")
}
else
{
  scene = GameScene(fileNamed:"GameScene_iOS8")
}

let skView = self.view as! SKView
skView.showsFPS = true
skView.showsNodeCount = true
skView.ignoresSiblingOrder = true
scene.scaleMode = .AspectFill
skView.presentScene(scene)
```

and when we load the scene, for devices running iOS 8, we explicitly get a reference to *Ref.sks*, load the target node into our scene at the same point where the empty node is, and then delete this empty node.

```swift
override func didMoveToView(view: SKView)
{
  if #available(iOS 9, *)
  {
    //do nothing
  }
  else
  {
    let ref = SKScene(fileNamed:"Ref")
    let targetNode = ref!.childNodeWithName("target")
    let emptyNode = self.childNodeWithName("empty")
    targetNode!.removeFromParent()
    targetNode!.position = emptyNode!.position
    emptyNode!.removeFromParent()
    self.addChild(targetNode!)
  }
}
```
This isn’t pretty, but it works.

# Named Actions

Xcode 7 and iOS 9 also introduce the ability to save an action, or a group of actions, to a file and then reference this action by name in code, or drag and drop from the actions panel in the editor itself. Below is a simple sequence of actions in which we move, scale, rotate and then fade out a sprite, saved with the name action. This, however, is once again an iOS9 only feature and will crash when **NSCoder** tries to load the *.sks* file.

![]({{site.url}}/assets/images/posts/2015/15-11-03/04.gif)

One approach is to remove the action from our *.sks* and instead manually load it in code, either by a simple reference in iOS9, or for iOS8 actually coding the actions by hand.

```swift
override func didMoveToView(view: SKView)
{
  let node = self.childNodeWithName("SKSpriteNode_0") as! SKSpriteNode

  if #available(iOS 9.0, *)
  {
    let action = SKAction(named: "action")
    node.runAction(action!)
  }
  else
  {
    //manually code for iOS8
    let action1 = SKAction.moveByX(250.0, y: 0, duration: 1.0)
    let action2 = SKAction.scaleBy(2.0, duration: 1.0)
    let action3 = SKAction.rotateByAngle((90.0/180.0)*CGFloat(M_PI), duration: 1.0) //expects radians, not degrees
    let action4 = SKAction.fadeOutWithDuration(1.0)
    let sequence = SKAction.sequence([action1, action2, action3, action4])
    node.runAction( sequence )
  }
}
```
Again, not pretty, but functional.

# Custom Classes

Lastly, another great feature is the ability to now assign nodes in *.sks* files as custom classes. Consider we wish to implement a simple **Button** class which extends **SKSpriteNode**.

In *GameScene.sks* we can create a colored sprite, set the name and its class to be **Button**.

![]({{site.url}}/assets/images/posts/2015/15-11-03/05.png)

Now in *GameScene.swift* we can easily get a reference to this button, cast it as a **Button**, and then do whatever we like (add callbacks etc.).

```swift
let button = self.childNodeWithName("button") as! Button
```

The catch, as you suspect, is that this will crash on iOS 8 as the sprite is a **SKSpriteNode** and cannot be cast to another class. One approach is to use this sprite as a placeholder for creating another Button, setting the new button’s texture, size and position identical to the graphical button, and then removing the graphical button from the scene.

```swift
let button: Button!  
if #available(iOS 9, *)  
{  
  button = self.childNodeWithName("button") as! Button  
}  
else  
{  
  let node = self.childNodeWithName("button") as! SKSpriteNode  
  button = Button(texture: node.texture!, size: node.size)
  button.position = node.position  
  node.removeFromParent()  
  addChild(button)  
}
```

This is one thing I actually expected to work on iOS 8 (the casting of a **SKSpriteNode** to a subclass) but apparently does now. More discussion on the [Apple forums](https://forums.developer.apple.com/thread/24996){:target=_"blank"}.

# Conclusion

Since the introduction of *SpriteKit* in iOS7, the framework has continued to grow from strength to strength, while the new updates to the *SpriteKit* editor drastically sped up development time. With the launch of tvOS and Apple’s growing focus on mobile gaming, I’m sure we’ll see even more innovations within the next year. 

However, making your App iOS9 only isn’t necessarily possible at this early stage and although I would love to utilize these new features, I also need to keep support for iOS 8. Above are some workarounds that I’ve been testing. I’d love to hear of any tips and tricks or alternative ideas!
