oopslist = list()

with open("results-curl.txt") as inf:
    for line in inf:
        oopslist.append(line.rstrip("\n"))

for line in oopslist:
    oldname = "results/curl/" + line
    newname = oldname.replace(".txt", ".html")
    with open(oldname) as inf2:
        content = inf2.read()
    with open(newname, 'w') as of:
        of.write(content)