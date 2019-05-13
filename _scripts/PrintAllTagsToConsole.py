#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from TagUtils import getAllPostTags, getUniqueTags

# determine all the different post tags
tags = getAllPostTags()
uniqueTags = getUniqueTags()

# print info to console
for tag in uniqueTags:
    print("{}: {}".format(tag, tags.count(tag)))
