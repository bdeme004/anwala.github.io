import subprocess
import argparse

parser = argparse.ArgumentParser(description='''no description available''')
parser.add_argument('-c', '--csv', action='store_true', help='output results to "wordcount.csv"')
parser.add_argument('-s', '--silent', action='store_true', help='suppress output to stdout')
args = parser.parse_args()

csv_output = args.csv
silent = args.silent

foundList = list()
resultList = list()

with open("results_found.txt") as inf:
    for line in inf:
        foundList.append(line.rstrip("\n"))

for item in foundList:
    filename = "results/found/" + item
    with open(filename) as inf:
        content = inf.read().upper()
    chargeCount = content.count("CHARGE")
    wordCount = (subprocess.run("wc -w " + filename, capture_output=True, text=True, errors='ignore').stdout).split(" ")

    filename = wordCount[1].replace("results/found/", "").replace("\n", "")
    index = filename.replace("result", "").replace(".html", "")

    result = (str(chargeCount) + "," + str(wordCount[0]) + "," + filename + "," + index)
    resultList.append(result)

    if not silent:
        print(item)

if csv_output:
    with open("wordcount.csv", "w") as of:
        of.write("WCt,WC,FILENAME,INDEX\n")
        for item in resultList:
            of.write(item + "\n")
