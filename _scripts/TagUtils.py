#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob

# the post's tags
tags = []

# Returns a non-unique array of all the different post tags
def getAllPostTags():
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
    
    return tags

# Returns a unique array of all the different post tags
def getUniqueTags():
    return set(getAllPostTags()) if len(tags) == 0 else set(tags)
