import requests as rq
from bs4 import BeautifulSoup as bs
import json
import getblogdata as gbd

bloglist = dict()

with open("blogs.txt") as inf:
    for line in inf:
        bloglist.setdefault(line.rstrip("\n"), " ")

for blog in bloglist:
    print("...", flush=True)
    datapage = "%s/feeds/posts/default" % blog

    r = rq.get(datapage)
    soup = bs(r.text, features="lxml")
    title = soup.find("title")
    try:
        title = title.string
    except AttributeError:
        pass
    bloglist[blog] = title

with open("thetitles.txt", 'w') as of:
    of.write(json.dumps(bloglist))

bloglist = gbd.loadBlogData()

with open("thetitles.txt") as inf:
    titlelist = json.loads(inf.read())

blogtitles = dict()

for blog in titlelist:
    title = titlelist[blog]
    blogtitles.setdefault(title, None)
    blogtitles[title] = bloglist[blog]

with open("blogtitles.txt", 'w') as of:
    of.write(json.dumps(blogtitles, indent=4))
