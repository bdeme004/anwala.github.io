import json

files = dict()

with open("results_carbondate.txt") as inf:
    for line in inf:
        files[line.rstrip("\n")] = dict()

for file in files:
    try:
        with open("results/carbondate/" + file) as carbondate:
            string = str(carbondate.read()).replace(" ", "")
            cdateobj = json.loads(string)
            files[file]["uri"] = cdateobj["uri"]
            files[file]["date"] = cdateobj["estimated-creation-date"].replace("'", "")
    except json.decoder.JSONDecodeError:
        print(file)
