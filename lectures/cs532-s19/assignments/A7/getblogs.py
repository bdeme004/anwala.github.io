import requests as rq
from bs4 import BeautifulSoup as bs
import re

BLOG = "http://f-measure.blogspot.com"

blogs = dict()


# from Programming Collective Intelligence:
# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py
# note: splits words at apostrophe, eg "she's home" -> ["she", "s", "home"]
def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


blogs.setdefault(BLOG, list())
#with open("blogs.txt") as inf:
#    for line in inf:
#        blogs.setdefault(line.rstrip("\n"), list())

for blog in blogs:
    posts = "%s/feeds/posts/default" % blog
    r = rq.get(posts)
    soup = bs(r.text, features="lxml")
    entries = soup("entry")

    for entry in entries:
        blogs[blog].append(getwords(str(entry.title.string)))

print(blogs)
