#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os

# directory variables
posts_dir = '../_posts/'
tags_dir = '../tags/'

# a function which returns the string contents of a Tag page
def textString ( tag ):
    returnString = "---\n"
    returnString += "layout: tagPage\n"
    returnString += "title: \"Tag: " + tag + "\"\n"
    returnString += "tag: \"" + tag + "\"\n"
    returnString += "---\n"
    return returnString

# get a list of md files in posts directory
filepaths = glob.iglob('../_posts/**/*.md', recursive=True)

#loop through all the posts and pull their tags
tags = []
for filepath in filepaths:
    f = open(filepath, 'r', encoding="utf8")

    insideFontMatter = False #between two sets of ---, the font matter defines post variables and tags
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

# remove duplicates by creating a set
tags = set(tags)

# determine an array of the existing tag pages
existingTagPages = glob.iglob("../tags/*.md")

updatedFilepaths = []
# creating tag pages
for tag in tags:
    filepath = "../tags/" + tag + ".md"
    updatedFilepaths.append(filepath)

    if not filepath in existingTagPages:
        print("Creating {}".format(tag))
        f = open(filepath, 'w')
        f.write(textString(tag))
        f.close()

# remove any other tag pages that aren't relevant
for existingTagPage in existingTagPages:
    if not existingTagPage in updatedFilepaths:
        print("Deleting {}".format(existingTagPage))
        unlink(existingTagPage)
