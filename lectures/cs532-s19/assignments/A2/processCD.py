import json

files = list()
has_map = list()
has_cd = list()
output = dict()
nomap = 0
nocd = 0

with open("results_carbondate.txt") as inf:
    for line in inf:
        files.append(line.rstrip("\n"))

for file in files:
    try:
        with open("results/timemap/" + file) as timemap:
            line = timemap.readline()
            if line.find("404 page not found") < 0:
                has_map.append(file)
    except Exception as e:
        print("timemap error:")
        print(e)

for file in files:
    try:
        with open("results/carbondate/" + file) as carbondate:
            string = str(carbondate.read()).replace(" ", "")
            cdateobj = json.loads(string)
            if cdateobj["estimated-creation-date"] != "":
                outline = "uri: " + cdateobj["uri"] + " || " + "est date: " + cdateobj["estimated-creation-date"] + "\n"
                has_cd.append(file)
                output[file] = outline
    except Exception as e:
        print("carbondate error:")
        print(e)

with open("cd_and_map.txt", 'w') as of3:
    for line in has_map:
        if line in has_cd:
            of3.write(line + "\n")
    of3.write("\n")
    of3.write("no timemap: " + str(len(files) - len(has_map)))
    of3.write(" || no carbondate: " + str(len(files) - len(has_cd)))
