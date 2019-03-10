import subprocess
import argparse

resultList = list()
tally = 0
numfiles = 1275

parser = argparse.ArgumentParser(description='''Checks links for link''')
parser.add_argument('searchterm', metavar='F', nargs=1,
                    help='term to search for')
parser.add_argument('-s', '--silent', action='store_true', help='suppress status reports')
args = parser.parse_args()

searchWord = args.searchterm[0]
silent = args.silent

for i in range(numfiles):
    filename = "results/text/result" + str(i) + ".html"
    command = "grep -li " + searchWord + " " + filename
    result = subprocess.run(command, capture_output=True, text=True, errors='ignore')

    if(len(result.stdout)) > 0:
        resultList.append(filename)
    if(i%100 == 0):
        print("Searching - found in " + str(len(resultList)) + " pages.", flush=True) 

if (len(resultList) < 10):
    print("term '" + searchWord + "' found in less than 10 pages.")
else:
    
    for file in resultList:
        with open(file) as inf:
            content = inf.read()
        newname = file.replace("results/text/", "results/found/")
        with open(newname, 'w') as of:
            of.write(content)
