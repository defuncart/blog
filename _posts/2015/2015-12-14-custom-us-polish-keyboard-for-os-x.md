---
layout: post
title: Custom US-Polish Keyboard (for OS X)
date: 2015-12-14 22:00:00 +01:00
tags:
- macOS
---
If you wish to write in different languages on OS X, one approach is to add as many keyboards as you need in System Preferences and then swap between them using **⌥⌘Space**. One setback is that cycling between keyboards is time consuming, a larger problem is that punctuation and symbol keys can be remapped to completely different keys - just compare the U.S. and German keyboards!

![]({{site.url}}/assets/images/posts/2015/15-12-14/01.png)

![]({{site.url}}/assets/images/posts/2015/15-12-14/02.png)

A little known fact is that the **⌥** key can actually be used with ‘hot keys’ to enter a dead state from which special characters can be created, for instance **⌥u** is the the combination to create umlauts. Once in this state, **¨** flashes on the screen, and if an **a**, **e**, **i**, **o**, **u** or **y** is subsequently pressed, then that letter with an umlaut will be produced. If any other key is pressed, the **¨** and other character are instead produced.

![]({{site.url}}/assets/images/posts/2015/15-12-14/03.png)

**⌥e** works similarly for producing accents, while for those who write in Cyrillic, the phonetic Russian keyboard can be used to write special Ukrainian or Belarusian letters by producing an optional value of a key: **⌥у**(u) = **ў**, **⌥и**(i) = **і**, **⌥а**(а) = **ї** and **⌥э**(\) = **є** (note that **⌥ш** = **щ**, **⌥е** = **ё**).

So between the standard U.S. keyboard and Phonetic Russian keyboard, one can easily write in English, Russian, German, Ukrainian, Irish… but what about Polish?

Polish contains both accented characters (**ć**, **ń**, **ó**, **ś** and **ź**) and special characters (**ą**, **ę**, **ł** and **ż**), most of which are not produceable by the standard U.S. keyboard. One can, however, easily edit a keyboard layout (using, for instance, [*Ukelele*](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele){:target="_blank"}) and install this modified keyboard to their computer. Thus, **⌥e** can be extended to include all accented letters

![]({{site.url}}/assets/images/posts/2015/15-12-14/04.png)

while **⌥z** and **⌥l** seem like natural choices for **ż** and **ł** respectively.

For **ą** and **ę**, a custom dead state with terminator **,** can be created such **⌥a** triggers this state, a **,** (comma) is displayed,

![]({{site.url}}/assets/images/posts/2015/15-12-14/05.png)

and if either **a** or **e** are pressed, then **ą** or **ę** result.

![]({{site.url}}/assets/images/posts/2015/15-12-14/06.png)

Adding capitals, one now has a fully functional U.S. keyboard that can write Polish letters. To install, simply go to **File -> Install** in *Ukelele* and the keyboard will be installed to the System.

**NOTE** that if you modified your default keyboard, then the following terminal commands are the easiest approach to remove it. More info [here](https://apple.stackexchange.com/questions/44921/how-to-remove-or-disable-a-default-keyboard-layout/60521#60521){:target="_blank"}.
1. Change the current input source to your custom keyboard layout.
2. Open *~/Library/Preferences/com.apple.HIToolbox.plist* (in 10.9+). You can convert the plist to XML with ```plutil -convert xml1```.
3. Remove the input source or input sources you want to disable from the *AppleEnabledInputSources* dictionary. If there is an *AppleDefaultAsciiInputSource* key, remove it.
4. Restart.

If you are looking to extend your current standard keyboard to write some additional characters, then this approach is a solid solution as opposed to opening **Show Emoji & Symbols** or installing another keyboard. The above U.S.-Polish keyboard can be downloaded [here](https://github.com/defuncart/custom-osx-us-polish-keyboard){:target="_blank"}.
