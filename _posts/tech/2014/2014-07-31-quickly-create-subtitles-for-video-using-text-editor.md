---
layout: post
title: Quickly Create Subtitles for a Video using a Text Editor
date: 2014-07-31 20:00:00 +02:00
tags:
- subtitles
- SRT
- tutorial
---
Something I needed to do today was to create an *SRT* subtitle text file for a video. These *SRT* files are the simplest method of including subtitles into your video, and although the process is somewhat tedious, it is repetitive and very straight forward.

What is the benefit of **softsubbing** using these *SRT* files? Namely that no specialized software is required, and also that once the *SRT* file is placed in the same folder as the video file with the same corresponding name (say *video.mp4* and *video.srt*), the subtitles will automatically be displayed in most leading media players (I tested using *VLC*).

These *SRT* files can be created in any normal text editor (say *Notepad* on *Windows* or *Sublime* on *OSX*) with context of the form:

```
1
00:00:20,000 –> 00:00:24,400
This is Statement 1 from 20s to 24.4s

2
00:01:45,000 –> 00:01:50,000
And this is Statement 2 from 1m45s to 1m50
which actually contains two lines.
```

where each desired sentence or statement has a unique number, followed on a new line by HH:MM:SS,MS –> HH:MM:SS,MS corresponding to the start and end time of the subtitle, and finally the text for the subtitle itself. **NOTE:** that there must be an empty line between these code blocks!

Practically this is achieved by starting with a blank text file, and having the video opened alongside. By playing and pausing the video, for each dialog line take a note of the start and end time, and create blocks as shown above. To turn this text into a *SRT* file, you need to save it using *UTF-8 encoding* with the extension **.srt**, for instance

![]({{site.baseurl}}/assets/images/posts/2014/14-07-31/01.png)

using *Notepad* on *Windows*. Make sure the *SRT* file and video file are in the same folder, open the video file, and you should be greeted with your subtitles! This is a quick and dirty approach that is also useful appropriate for [creating captions and subtitles](https://support.google.com/youtube/answer/2734796?hl=en) for *Youtube*. Many prominent video editing software include some mechanism for easily creating subtitles within the software itself.
