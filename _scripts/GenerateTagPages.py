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

# get a list of md files in posts directory
# filenames = glob.glob(posts_dir + '*md')

# a function which determines if the required filename has already been exported
def textString ( tag ):
    returnString = "---\n"
    returnString += "layout: tagPage\n"
    returnString += "title: \"Tag: " + tag + "\"\n"
    returnString += "tag: \"" + tag + "\"\n"
    returnString += "---\n"
    return returnString

filepaths = glob.iglob('../_posts/**/*.md', recursive=True)
# filepaths = glob.iglob('post_dir + '/**/*.md', recursive=True)
# filepaths = glob.iglob(post_dir + "**/*.md", recursive=True)

# for filepath in filepaths:
#     print  (filepath)

#loop through all the posts and pull their tags
tags = []
for filepath in filepaths:
    f = open(filepath, 'r', encoding="utf8")

    insideFontMatter = False #between two sets of ---, the font matter defines post variables and tags
    for line in f:
        #print (line)

        #if inside font matter, determine if the first character is -
        if insideFontMatter:
            characters = line.strip().split()
            if(characters[0] == "-"):
                tags.extend(characters[1:])
        if line.strip() == "---":
            insideFontMatter = not insideFontMatter
            if not insideFontMatter:
                break
    # break

    f.close()

# remove duplicates by creating a set
tags = set(tags)

#print (tags)

# determine an array of the existing tag pages
existingTagPages = filepaths = glob.iglob("../tags/*.md")

# for page in existingTagPages:
    # print(page)



# creating tag pages
for tag in tags:
    filepath = "../tags/" + tag + ".md"

    if not filepath in existingTagPages:
        print("Creating {}".format(tag))
        f = open(filepath, 'a')
        f.write(textString(tag))
        f.close()
