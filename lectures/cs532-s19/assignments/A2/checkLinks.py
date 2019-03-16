import argparse
import requests

parser = argparse.ArgumentParser(description='''Checks links for link''')
parser.add_argument('infile', metavar='F', nargs='?', default='result_urls_2.txt',
                    help='.txt list of links')
parser.add_argument('output', metavar='O', nargs='?',
                    default="result_urls_limited.txt",
                    help=""".txt name for output file.
                     (default: "result_urls_limited.txt")""")
parser.add_argument('-s', '--silent', action='store_true', help='suppress status reports')

args = parser.parse_args()

infile = args.infile
outfile = args.output
silent = args.silent

links = list()

with open(infile) as infile:
    tally = 1
    for link in infile:
        try:
            r = requests.head(link, allow_redirects=True)
            if(r.status_code == 200):
                if not silent:
                    print("confirmed-" + str(tally), flush=True)
                links.append(r.url)
                tally += 1
        # "if anything goes wrong, just forget about it."
        # sloppy, but it'll do for these purposes.
        # --BJD
        except:
            pass

links_out = list(dict.fromkeys(links))

with open(outfile, 'w') as of:
    for link in links_out:
        of.write(link + '\n')

print("URLs written to '" + outfile + "'.")
