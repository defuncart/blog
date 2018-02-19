#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os

# directory variables
# current_dir = os.getcwd()
# posts_dir = os.path.join(current_dir, "_posts")
# tags_dir = os.path.join(current_dir, "tags")

posts_dir = '../_posts/'
tags_dir = '../tags/'

# a function which constructs the text string for a tagPage md file
def textString ( tag ):
    returnString = "---\n"
    returnString += "layout: tagPage\n"
    returnString += "title: \"" + tag + "\"\n"
    returnString += "---\n"
    return returnString

# get a list of md files in posts directory
filepaths = glob.iglob('../_posts/**/*.md', recursive=True)

#loop through all the posts and pull their tags
tags = []
for filepath in filepaths:
    f = open(filepath, 'r', encoding="utf8")

    insideFontMatter = False # where the current line is within the font matter (between set of --- marks)

    #loop through each line
    for line in f:
        #if inside font matter, determine if the first character is -
        if insideFontMatter:
            characters = line.strip().split()
            if(characters[0] == "-"):
                tags.extend(characters[1:])
        if line.strip() == "---":
            insideFontMatter = not insideFontMatter
            if not insideFontMatter:
                break

    f.close()

# determine unique list of tags by creating a set
uniqueTags = set(tags)

# print info to console
for tag in uniqueTags:
    print("{}: {}".format(tag, tags.count(tag)))
