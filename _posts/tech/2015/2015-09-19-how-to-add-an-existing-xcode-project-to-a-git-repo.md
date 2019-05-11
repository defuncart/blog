---
layout: post
title: How to add an existing Xcode project to a Git Repo
date: 2015-09-19 12:00:00 +02:00
category: tech
tags:
- Xcode
- GitHub
---
Although Xcode already has git version control built in, what if you have an existing Xcode project that you’d like to add to a Git repo? Well here is a simple solution!

If a Git Repo doesn’t already exist, log into Git and create one. Next, open the terminal and navigate to the directory containing the **[PROJECT_NAME].xcodeproj** file and type the following series of commands:

```
git init
git add .
git commit -m "initial commit"
git remote add origin git@github.com:[USER_NAME]/[REPOSITORY_NAME].git
git pull origin master
git push origin master
```
