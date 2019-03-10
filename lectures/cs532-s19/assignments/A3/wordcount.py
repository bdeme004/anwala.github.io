import subprocess
import argparse

foundList = list()
resultList = list()

with open("results_found.txt") as inf:
    for line in inf:
        foundList.append(line.rstrip("\n"))

for item in foundList:
    filename="results/found/" + item
    with open(filename) as inf:
        content = inf.read().upper()
    chargeCount = content.count("CHARGE")
    wordCount = (subprocess.run("wc -w " + filename, capture_output=True, text=True, errors='ignore').stdout)
    resultList.append(str(chargeCount) + "/" + wordCount.replace("results/found/", ""))
    
for item in resultList:
    print(item)
