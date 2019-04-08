#!/usr/bin/python

# https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py

# -*- coding: utf-8 -*-
import feedparser
import re


def getwordcounts(url):
    '''
    Returns title and dictionary of word counts for an RSS feed
    '''
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary

        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return (d.feed.title, wc)


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


def main():
    apcount = {}
    wordcounts = {}
    feedlist = list()
    # read the contents of feedlist.txt into a list
    with open('feedlist.txt') as inf:
        for line in inf:
            feedlist.append(line)
    # for each item in the list...
    for feedurl in feedlist:
        try:
            (title, wc) = getwordcounts(feedurl)  # ...get the title and dict of wordcounts
            wordcounts[title] = wc  # add the wordcount to master dict of wordcounts
            for (word, count) in wc.items():  # for each word/count pair...
                apcount.setdefault(word, 0)   # make sure [word] is in apcount...
                if count > 1:                 # ...and add 1 to apcount[word] if count > 1.
                    apcount[word] += 1        # apcount is then a dict of "how many docs contain [word]".
        except:
            print('Failed to parse feed %s' % feedurl)

    wordlist = []
    for (w, bc) in apcount.items():  # for each word/count pair in apcount...
        frac = float(bc) / len(feedlist)   # ...frac = % of docs that contain [word].
        if frac > 0.1 and frac < 0.5:       # if 10% < frac < 50%...
            wordlist.append(w)              #... add the word to the list.

    with open('blogdata1.txt', 'w') as out:
        out.write('Blog')
        for word in wordlist:
            out.write('\t%s' % word)
        out.write('\n')
        for (blog, wc) in wordcounts.items():
            print(blog)
            out.write(blog)
            for word in wordlist:
                if word in wc:
                    out.write('\t%d' % wc[word])
                else:
                    out.write('\t0')
            out.write('\n')
    return 0
