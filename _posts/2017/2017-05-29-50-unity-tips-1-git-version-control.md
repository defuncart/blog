---
layout: post
title: '50 Unity Tips #1: Git Version Control'
date: 2017-05-29 10:00:00 +02:00
tags:
- unity2d
- Unity3D
- github
- 50UnityTips
---

[github_link]: https://github.com/defuncart/50-unity-tips/tree/master/%2301-GitVersionControl
[image1]: https://raw.githubusercontent.com/defuncart/50-unity-tips/master/%2301-GitVersionControl/images/gitVersionControl1.png
[image2]: https://raw.githubusercontent.com/defuncart/50-unity-tips/master/%2301-GitVersionControl/images/gitVersionControl2.png
[image3]: https://raw.githubusercontent.com/defuncart/50-unity-tips/master/%2301-GitVersionControl/images/gitVersionControl3.png
[![]({{site.url}}/assets/images/viewOnGitHub.png)][github_link]

[Version control](https://en.wikipedia.org/wiki/Version_control) is something that I’m sure most are familiar with (if not check out [this tutorial](https://try.github.io/levels/1/challenges/1) and [this course](https://www.codecademy.com/learn/learn-git)), but something that you may not be familiar with is how to optimize a Unity Project for Git version control.

One issue is that within a Unity Project there are many folders and files that can remain local and don’t need to be tracked. The Library folder, for instance, when not present is always constructed on load, while OS (Mac/Windows etc.) specific files don’t need to be synced across computers.

Firstly, in **Project Settings/Editor** insure *Version Control Mode* is set to *Visible Meta Files*

![][image1]

as this is required for version control. The benefit of this meta files is that unique settings for a file (such as import settings for a sprite etc.) are saved to an associated meta file, so syncing is easier and faster between projects.

Now we could commit only the relevant files (that is, the *Assets* and *ProjectSettings* folders)

```
git add Assets
git add ProjectSettings
```

but one issue is the annoyance of untracked files messages for files which we have no interest in tracking.

![][image2]

Luckily by writing a custom <a href="https://gist.github.com/defuncart/3cb2946c591df61e9bf1c280d0611674"><b>.gitignore</b></a> file (saved to the root project folder), we can specific the files that git should ignore tracking.

```
# Unity generated folders
Temp/
Library/

# Custom Build Folder
Builds/

# MonoDevelop generated files
obj/
*.csproj
*.unityproj
*.sln
*.userprefs

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
```

![][image3]

One last point is the *Editor* setting **Asset Serialization Mode** to being *Force Text* or *Mixed* (between Text and Binary). Most Unity Projects will have scenes, prefabs and thus a lot of binary files. Force Text works better for version control in viewing the changes between commits, but Mixed means that binary files are imported faster into the project.
