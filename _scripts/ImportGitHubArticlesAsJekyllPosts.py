import json
import os
import requests

# clear screen
os.system('clear')

# constants
FLUTTER_TIPS_TRICKS = 'GitHubArticles/FlutterTipsTricks.json'

# determines the jekyll post content in md from a git readme
def postMarkdown( json ):
    # generate YAML
    md = '---\n'
    md += 'layout: post\n'
    md += 'title: \'{}\'\n'.format(json['title'])
    md += 'date: {}\n'.format(json['date'])
    md += 'category: tech\n'
    md += 'tags:\n'
    for tag in json['tags']:
        md += '- {}\n'.format(tag)
    md += '---\n'

    # get content from github
    url = '{}/README.md'.format(json['gitUrl'].replace('github', 'raw.githubusercontent')).replace('/tree', '')
    githubMd = requests.get(url).text
    # remove title
    gitHubPageTitle = githubMd.partition('\n\n')[0]
    githubMd = githubMd.replace(gitHubPageTitle, '')
    # update relative (i.e. image) urls
    imageUrl = format(json['gitUrl'].replace('github', 'raw.githubusercontent')).replace('/tree', '')
    githubMd = githubMd.replace('![](images', '![]({}/images'.format(imageUrl))
    # finally add post body
    md += githubMd

    # add footer re-directing to github
    # md += '\n## Original Article\n\nThis post is generated from an article on GitHub. Full source code and original article can be found [here]({}).\n'.format(json['gitUrl'])
    md += '\nThis post is generated from an article on [GitHub]({}).\n'.format(json['gitUrl'])

    return md

# determines the jekyll post filename from a git readme
def postFilename( json ):
    # determine post's year and date (YYYY-MM-DD)
    year = json['date'][0:4]
    date = json['date'][0:10]
    # determine post url
    # firstly remove special characters
    title = json['title'].replace('#', '').replace(':', '').replace('/', ' ') 
    # then convert to lower characters with dashes for spaces
    title = title.replace(' ', '-').lower()

    return '../_posts/tech/{}/{}-{}.md'.format(year, date, title)

gitRepos = [FLUTTER_TIPS_TRICKS]
for repo in gitRepos:
    with open(repo) as jsonFile:
        articles = json.load(jsonFile)
        for article in articles:
            print('{}...'.format(article['title']))

            contents = postMarkdown(article)
            filepath = postFilename(article)
            with open(filepath, 'w') as postFile:
                postFile.write(contents)
