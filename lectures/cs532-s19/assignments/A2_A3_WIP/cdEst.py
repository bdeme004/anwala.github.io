import argparse
import subprocess

parser = argparse.ArgumentParser(description='''Checks links for link''')
parser.add_argument('infile', metavar='F',  nargs='?',
                    default='result_urls.txt',
                    help='.txt list of links')
args = parser.parse_args()

infile = args.infile
urls = list()
tally = 0

with open(infile) as inf:
    for line in inf:
        urls.append(line.rstrip("\n"))

for url in urls:
    command = "docker container run --rm -it oduwsdl/carbondate ./main.py -l" + url
    output = "results/carbondate/result" + str(tally) + ".txt"
    result = subprocess.run(command, capture_output=True, text=True, errors='ignore')
    with open(output, 'w') as of:
        of.write(result.stdout)
    tally += 1

tally = 0
for url in urls:
    command = "curl " + url
    output =  "results/curl/result" + str(tally) + ".html"
    result = subprocess.run(command, capture_output=True, text=True, errors='ignore')
    with open(output, 'w') as of:
        of.write(result.stdout)
    tally += 1

print("Extraction complete.")
