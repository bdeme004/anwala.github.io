import requests as rq
from bs4 import BeautifulSoup as bs
import re
import json
import clusters


# modified from Programming Collective Intelligence:
# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py
# note: splits words at apostrophe, eg "she's home" -> ["she", "s", "home"]
def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


# modified from Programming Collective Intelligence:
# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py
def getWorkingList(bcdict, numBlogs):

    def numBlogsWith(e):
        return bcdict[e]

    wordlist = []
    for (w, bc) in bcdict.items():  # for each word/count pair in apcount...
        if w not in STOP:
            frac = float(bc) / numBlogs   # ...frac = % of docs that contain [word].
            if frac > 0.1 and frac < 0.5:       # if 10% < frac < 50%...
                wordlist.append(w)
    wordlist.sort(reverse=True, key=numBlogsWith)
    while len(wordlist) > 1000:
        wordlist.pop(1000)
    return wordlist


# modified from Programming Collective Intelligence:
# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py
def getWordCounts(blogs):
    blogsWithWord = dict()
    wcPerBlog = dict()

    for blog in blogs:
        wcPerBlog.setdefault(blog, dict())
        for post in blogs[blog]:
            for word in post:
                wcPerBlog[blog].setdefault(word, 0)
                wcPerBlog[blog][word] += 1
    for blog in wcPerBlog:
        for word in wcPerBlog[blog]:
            blogsWithWord.setdefault(word, 0)
            blogsWithWord[word] += 1
    return (wcPerBlog, blogsWithWord)


# from Programming Collective Intelligence:
# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py
def matrixToFile(wordlist, wcdict, path="."):
    outfile = path + '/blogdata1.txt'
    with open(outfile, 'w') as out:
        out.write('Blog')
        for word in wordlist:
            out.write('\t%s' % word)
        out.write('\n')
        for (blog, wc) in wcdict.items():
            # print(blog)
            out.write(blog)
            for word in wordlist:
                if word in wc:
                    out.write('\t%d' % wc[word])
                else:
                    out.write('\t0')
            out.write('\n')

    print("Data written to '%s'." % outfile)


# Uses Stopwords for MyISAM Search Indexes:
# https://dev.mysql.com/doc/refman/8.0/en/fulltext-stopwords.html
def loadStopwords(path="."):
    words = list()
    try:
        with open(path + "/stopwords.txt") as inf:
            for line in inf:
                words.append(line.rstrip("\n"))
    except Exception as e:
        print(e)
        print("Proceeding with no stoplist." + "\n")
    return words


def getBlogData(path="."):
    with open(path + "/blogs.txt") as inf:
        for line in inf:
            bloglist.setdefault(line.rstrip("\n"), list())

    for blog in bloglist:
        print(blog, flush=True)
        first_page = "%s/feeds/posts/default" % blog
        next_page = getPosts(blog, first_page)
        while next_page is not None:
            next_page = getPosts(blog, next_page)
        with open("blogdata.txt", 'w') as of:
            of.write(json.dumps(bloglist, indent=4))


def getPosts(blog, page):
    r = rq.get(page)
    soup = bs(r.text, features="lxml")
    entries = soup("entry")
    for entry in entries:
        bloglist[blog].append(getwords(str(entry.title.string)))
    print(len(bloglist[blog]), flush=True)
    next_page = soup.find("link", rel="next")
    try:
        next_page = next_page['href']
    except TypeError:
        pass
    return next_page


def loadBlogData(path="."):
    with open(path + "/blogdata.txt") as inf:
        return json.loads(inf.read())


def batchKClusters(kValsList):
    batchClusters = dict()
    for kVal in kValsList:
        print("\nk=%d:" % kVal)
        batchClusters.setdefault(kVal, list())
        kclust = clusters.kcluster(DATA, k=kVal)
        for i in range(len(kclust)):
            batchClusters[kVal].append([BLOGNAMES[j] for j in kclust[i]])
    return batchClusters


def kClustersToFile(kclusts, path="."):
    with open(path + "/results/kclusters.txt", 'w') as of:
        for i in KVALS:
            of.write("\nk=%d:\n" % i)
            for cluster in kclusts[i]:
                of.write("---------------" + "\n")
                for blog in cluster:
                    of.write(blog + "\n")
                of.write("---------------" + "\n")
                of.write("\n")


STOP = loadStopwords("DON'T USE")
KVALS = [5, 10, 20]

# getBlogData()  # already executed; see "blogdata.txt"
bloglist = loadBlogData()

wcDict, bcDict = getWordCounts(bloglist)
workingList = getWorkingList(bcDict, len(bloglist))

matrixToFile(workingList, wcDict)

# from wk 11 ppt, page 13-14:
# https://docs.google.com/presentation/d/11mxRBRXiwvGQdBDqosDHn5np5tnx10Pdm0L6POtx-_I/edit?usp=sharing
BLOGNAMES, WORDS, DATA = clusters.readfile('blogdata1.txt')

clust = clusters.hcluster(DATA)
clusters.printclust(clust, labels=BLOGNAMES)
clusters.drawdendrogram(clust, BLOGNAMES, jpeg='results/blogclust.jpg')

# from wk 11 ppt, page 29:
# https://docs.google.com/presentation/d/11mxRBRXiwvGQdBDqosDHn5np5tnx10Pdm0L6POtx-_I/edit?usp=sharing
coords = clusters.scaledown(DATA)
clusters.draw2d(coords, BLOGNAMES, jpeg='results/blogs2d.jpg')


kclusts = batchKClusters(KVALS)
kClustersToFile(kclusts)
