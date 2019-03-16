import argparse
import subprocess

parser = argparse.ArgumentParser(description='''retrieves carbondate data.''')
parser.add_argument('infile', metavar='F', nargs='?',
                    default='result_urls_limited.txt',
                    help='.txt list of links')
parser.add_argument('-s', '--silent', action='store_true', help='suppress status reports')
args = parser.parse_args()

infile = args.infile
silent = args.silent

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
        if not silent:
            print("carbondate- " + str(tally), flush=True)
    tally += 1

subprocess.run("ls results/carbondate > results_carbondate.txt")
print("\n CarbonDate collection complete.")
