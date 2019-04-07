from bs4 import BeautifulSoup
import requests
import argparse
from urllib.parse import urlparse


# base structure taken from CS532 Slack:
# https://cs532s19.slack.com/messages/CFNQTJRGW/
def derefURI(uri):

    uri = uri.strip()
    if(len(uri) == 0):
        return ''

    html = ''
    try:
        response = requests.get(uri, timeout=10)
        html = response.text
    except Exception as e:
        # generic exception catch
        print('\tError:', str(e))
        return

    return html


def checkhref(href):

    if href.startswith('#'):
        return args.uri[0] + href
    elif href.startswith('/'):
        return mainPage + href
    else:
        return href


parser = argparse.ArgumentParser(description='''Lists all the links on a page that result in PDF files, and prints out
                                 the bytes for each link.''')
parser.add_argument('uri', metavar='U', nargs=1,
                    help='uri for the web page to be searched for links')
args = parser.parse_args()

# taken from CS532 Slack:
# https://cs532s19.slack.com/messages/CFNQTJRGW/
uri = args.uri[0]  # e.g., uri = 'https://www.cs.odu.edu/~mln/pubs/all.html'
scheme, netloc, path, params, query, fragment = urlparse(uri)
mainPage = scheme + '://' + netloc  # mainPage = 'https://www.cs.odu.edu'

html = derefURI(uri)
if (html):
    soup = BeautifulSoup(html, 'lxml')

    allLinks = list()
    pdfLinks = list()

    print("Searching page for links...\n", flush=True)

    for link in soup('a'):
        ref = link.get('href')
        allLinks.append(ref)


#    print("Checking links for PDF files...\n", flush=True)
#
#    for link in allLinks:
#        if(link):
#            r = requests.head(checkhref(link), allow_redirects=True)
#            if r.headers.get('Content-Type') == 'application/pdf':
#                pdfLinks.append([link, r.headers.get('Content-Length')])
#
#    print("Links resulting in PDF files:")
#    for link in pdfLinks:
#        print(link[0] + "\n\t(" + link[1] + " bytes)\n")

for link in allLinks:
    try:
        r = requests.head(link, allow_redirects=True)
        if r.status_code == 200:
            pdfLinks.append(r.url)
    except:
        pass

with open("blogs.txt", 'w') as of:
    for item in pdfLinks:
        of.write(item + "\n")
