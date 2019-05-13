#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
from TagUtils import getUniqueTags

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

# get all the post tags
tags = getUniqueTags()

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
