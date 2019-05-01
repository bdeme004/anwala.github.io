import json
import datetime
import matplotlib.pyplot as plt

CURRENT = datetime.datetime.fromisoformat("2019-03-16T04:13:24")

cd_and_map = list()
files = dict()

numMementos = list()
ages = list()
mementos = list()

bins = [0, 50, 100, 150, 200, 250, 375, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]
ticks = [0, 50, 100, 150, 200, 250, 375, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500]
label = [0, "", 100, " ", " ", 250, " ", 500, 750, 1000, "  ", 1500, "  ", 2000, "  ", 2500]

lowBins = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25]
lowTicks = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25]
lowLabel = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25]


#def ageInDays(page):
#    try:
#        creation = datetime.datetime.fromisoformat(files[page]["date"])
#        files[page]["age"] = (CURRENT - creation).days
#    except ValueError:
#        files[page]["age"] = None


def countMementos(page):
    try:
        with open("results/timemap/" + page.replace(".txt", ".html")) as timemap:
            files[page]["mementos"] = timemap.read().count("memento")
            numMementos.append(files[page]["mementos"])
    except Exception as e:
        print(e, flush=True)
#
#
#def getCarbonData(page):
#    try:
#        with open("results/carbondate/" + file) as carbondate:
#            string = str(carbondate.read()).replace(" ", "")
#            cdateobj = json.loads(string)
#            files[file]["uri"] = cdateobj["uri"]
#            files[file]["date"] = cdateobj["estimated-creation-date"].replace("'", "")
#    except json.decoder.JSONDecodeError:
#        files[file]["uri"] = cdateobj["uri"]
#        files[file]["date"] = cdateobj["estimated-creation-date"].replace("'", "")
#    except Exception as e:
#        print(e, flush=True)
#
#
#def plotMementosAges():
#    fig, ax = plt.subplots()
#    ax.plot(ages, mementos, '.')
#    ax.set(xlabel="age in days", ylabel="number of mementos", yscale='log')
#
#
#def plotMementoFreq():
#    fig, ax = plt.subplots()
#    plt.hist(numMementos, bins, log=True)
#    plt.xticks(ticks, label)
#    fig.tight_layout()
#    ax.set(xlabel="number of mementos", ylabel="frequency")
#
#
#def plotLowMementoFreq():
#    fig, ax = plt.subplots()
#    plt.hist(numMementos, lowBins, log=True)
#    plt.xticks(lowTicks, lowLabel)
#    fig.tight_layout()
#    ax.set(xlabel="number of mementos", ylabel="frequency")
#
#
#def noAgeNoMem():
#    noMem = 0
#    noAge = 0
#    for file in files:
#        if files[file]["age"] is None:
#            noAge += 1
#        if files[file]["mementos"] == 0:
#            noMem += 1
#
#    print("No Estimated Date: " + str(noAge) + "/" + str(len(files)))
#    print("No Mementos: " + str(noMem) + "/" + str(len(files)))


with open("results_carbondate.txt") as inf:
    for line in inf:
        file = line.rstrip("\n")
        files[file] = dict()

for file in files:
    countMementos(file)
#    getCarbonData(file)
#    ageInDays(file)

#    if files[file]["age"] is not None:
    if files[file]["mementos"] >= 0:
        try:
            # ages.append(files[file]["age"])
            mementos.append(files[file]["mementos"])
        except Exception:
            print(file, flush=True)

with open("results_mementos_old.txt") as old:
    mementos_old = [int(line.rstrip("\n")) for line in old]

y = []
for num_current in mementos:
    i = mementos.index(num_current)
    try:
        y.append(num_current - mementos_old[i])
    except:
        print("%d/%d" % (i, len(mementos_old)))

fig, ax = plt.subplots()
ax.plot(range(len(mementos)), y, '.')
ax.set(xlabel="TimeMap", ylabel="Change in mementos", yscale='log')

#noAgeNoMem()
#
#plotMementoFreq()
#plotLowMementoFreq()
#plotMementosAges()
#
#
plt.show()
