import subprocess

inlist = list()

with open("results_timemap.txt") as inf:
    for line in inf:
        inlist.append(line.rstrip("\n"))

for line in inlist:
    with open("results/timemap/" + line) as file:
        content = file.read()
    with open("results/timemap/" + line.replace("timemap", "result"), 'w') as of:
        of.write(content)

for line in inlist:
    subprocess.run("rm results/timemap/" + line)
