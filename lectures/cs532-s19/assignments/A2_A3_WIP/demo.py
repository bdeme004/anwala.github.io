import argparse
import requests

parser = argparse.ArgumentParser(description='''Checks links for link''')
parser.add_argument('infile', metavar='F',  nargs='?', default='result_urls.txt',
                    help='.txt list of links')
parser.add_argument('output', metavar='O',  nargs='?',
                    default="result_urls_limited.txt",
                    help=""".txt name for output file.
                     (default: "result_urls_limited.txt")""")
args = parser.parse_args()

infile = args.infile
outfile = args.output

links_out = set()

with open(infile) as infile:
    for link in infile:
        try:
            r = requests.head(link, allow_redirects=True)
            if(r.status_code == 200):
                links_out.add(r.url)
                print(r.url)
        except:
            pass
'''
with open(outfile, 'w') as of:
    for link in links_out:
        of.write(link + '\n')
'''        
print ("URLs written to '" + outfile +"'.")