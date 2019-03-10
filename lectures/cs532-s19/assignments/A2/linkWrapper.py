import subprocess
import argparse

parser = argparse.ArgumentParser(description='''Wrapper to collect and check links from Twitter''')
parser.add_argument('-s', '--silent', action='store_true', help='suppress status reports')
args = parser.parse_args()

silent = args.silent

if silent:
    getLinks = "python getLinks.py -s"
    confirmLinks = "python checkLinks.py -s"
else:
    getLinks = "python getLinks.py"
    confirmLinks = "python checkLinks.py"

# collect links from Twitter
subprocess.run(getLinks)

# remove links that do not result in status code 200
# remove duplicate items
subprocess.run(confirmLinks)
