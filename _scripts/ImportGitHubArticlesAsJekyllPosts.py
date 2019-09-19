#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import requests

# clear screen
os.system('clear')

# constants
LEARNING_FLUTTER = 'GitHubArticles/LearningFlutter.json'
FLUTTER_TIPS_TRICKS = 'GitHubArticles/FlutterTipsTricks.json'
UNITY_TIPS = 'GitHubArticles/50UnityTips.json'
LEARNING_XAMARIN = 'GitHubArticles/LearningXamarin.json'

# determines the jekyll post content in md from a git readme
def postMarkdown( url, title, date, tags ):
    # generate YAML
    md = '---\n'
    md += 'layout: post\n'
    md += 'title: \'{}\'\n'.format(title)
    md += 'date: {}\n'.format(date)
    md += 'category: tech\n'
    md += 'tags:\n'
    for tag in tags:
        md += '- {}\n'.format(tag)
    md += '---\n'

    # get content from github
    textUrl = '{}/README.md'.format(url.replace('github', 'raw.githubusercontent')).replace('/tree', '')
    githubMd = requests.get(textUrl).text
    # remove title
    gitHubPageTitle = githubMd.partition('\n\n')[0]
    githubMd = githubMd.replace(gitHubPageTitle, '')
    githubMd = githubMd[1:]
    # update relative (i.e. image) urls
    imageUrl = format(url.replace('github', 'raw.githubusercontent')).replace('/tree', '')
    githubMd = githubMd.replace('![](images', '![]({}/images'.format(imageUrl))
    githubMd = githubMd.replace('<img src="Images', '<img src="{}/Images'.format(imageUrl))
    githubMd = githubMd.replace('<img src="images', '<img src="{}/images'.format(imageUrl))
    githubMd = githubMd.replace('<img src="screenshots', '<img src="{}/screenshots'.format(imageUrl))
    githubMd = githubMd.replace('![](screenshots', '![]({}/screenshots'.format(imageUrl))
    githubMd = githubMd.replace('![](_screenshots', '![]({}/_screenshots'.format(imageUrl))
    # finally add post body
    md += githubMd

    # add footer re-directing to github
    md += '\n\n<p align="center"><font size="-1" color="#828282">This post was generated from a <a href="{}">GitHub repository</a>.</font></p>\n'.format(url)

    return md

# determines the jekyll post filename from a git readme
def postFilename( url, title, date ):
    # determine post's year and date (YYYY-MM-DD)
    year = date[0:4]
    date = date[0:10]
    # determine post url
    # firstly remove special characters
    title = title.replace('#', '').replace(':', '').replace('/', ' ') .replace('_', ' ')
    # then convert to lower characters with dashes for spaces
    title = title.replace(' ', '-').lower()

    return '../_posts/tech/{}/{}-{}.md'.format(year, date, title)

gitRepos = [LEARNING_FLUTTER]
for repo in gitRepos:
    with open(repo) as jsonFile:
        data = json.load(jsonFile)
        for article in data['articles']:
            print('{}...'.format(article['folder']))

            # determine article variables
            url = data['baseUrl'] + article['folder']
            title = data['baseTitle'] + article['folder']
            date = article['date']
            tags = data['baseTags'] + article['tags'] if 'tags' in article else data['baseTags']
            titlePost = data['postUrl'] if 'postUrl' in article else title

            # determine post content, filepath and save
            contents = postMarkdown(url, title, date, tags)
            filepath = postFilename(url, titlePost, date)
            with open(filepath, 'w') as postFile:
                postFile.write(contents)
