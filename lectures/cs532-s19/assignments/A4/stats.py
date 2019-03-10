import statistics as stat
import numpy as np
import matplotlib.pyplot as plt

fb_stats = {
    "graph":
    {
        "color": '#dc8113',
        "prefix": 'F',
        "id": 'facebook',
        "xlabel": 'Friend',
        "ylabel": 'Number of Friends'
    },
    "self":
    {
        "x": 0,
        "x2": 0,
        "y": 0,
        "name": ""
    },
    "values": list(),
    "zscores": list(),
    "twoDevValues": list(),
    "twoDevzScores": list()
}

ln_stats = {
    "graph":
    {
        "color": '#00bb08',
        "prefix": 'C',
        "id": 'linkedin',
        "xlabel": 'Connection',
        "ylabel": 'Number of Connections'
    },
    "self":
    {
        "x": 0,
        "x2": 0,
        "y": 0,
        "name": ""
    },
    "values": list(),
    "zscores": list(),
    "twoDevValues": list(),
    "twoDevzScores": list()
}

tw_fl_stats = {
    "graph":
    {
        "color": '#95549A',
        "prefix": 'F',
        "id": 'tw_follow',
        "xlabel": 'Follower',
        "ylabel": 'Number of Follower'
    },
    "self":
    {
        "x": 0,
        "x2": 0,
        "y": 0,
        "name": ""
    },
    "values": list(),
    "zscores": list(),
    "twoDevValues": list(),
    "twoDevzScores": list()
}

tw_fr_stats = {
    "graph":
    {
        "color": '#D7829F',
        "prefix": 'F',
        "id": 'tw_friend',
        "xlabel": 'Friend',
        "ylabel": 'Number of Friends'
    },
    "self":
    {
        "x": 0,
        "x2": 0,
        "y": 0,
        "name": ""
    },
    "values": list(),
    "zscores": list(),
    "twoDevValues": list(),
    "twoDevzScores": list()
}

TARGET_NAME = {

    "twitter": 'acnwala',
    "facebook": 'Alexander Nwala',
    "linkedin": 'Traci DeMerchant'
}


def allStats(datalist):
    for data in datalist:
        coreStats(data)
        twoDevStats(data)


def coreStats(data):
    data["values"].sort(reverse=True)
    data["mean"] = stat.mean(data["values"])
    data["median"] = stat.median(data["values"])
    data["stdev"] = stat.stdev(data["values"])
    data["self"]["x"] = data["values"].index(data["self"]["y"])
    data["graph"]["xSpacing"] = np.linspace(0, len(data["values"]), 6)
    data["graph"]["xticks"] = list()

    for item in data["graph"]["xSpacing"]:
        data["graph"]["xticks"].append(data["graph"]["prefix"] + str(int(item)))

    for x in data["values"]:
        data["zscores"].append((x - data["mean"]) / (data["stdev"]))


def twoDevStats(data):
    for x in data["values"]:
        if data["zscores"][data["values"].index(x)] < 2:
            data["twoDevValues"].append(x)

    data["twoDevValues"].sort(reverse=True)
    data["twoDevMean"] = stat.mean(data["twoDevValues"])
    data["twoDevMedian"] = stat.median(data["twoDevValues"])
    data["twoDevStdev"] = stat.stdev(data["twoDevValues"])
    data["self"]["x2"] = data["twoDevValues"].index(data["self"]["y"])
    data["graph"]["x2Spacing"] = np.linspace(0, len(data["twoDevValues"]), 6)
    data["graph"]["x2ticks"] = list()

    for item in data["graph"]["x2Spacing"]:
        data["graph"]["x2ticks"].append(data["graph"]["prefix"] + str(int(item)))

    for x in data["twoDevValues"]:
        data["twoDevzScores"].append((x - data["twoDevMean"]) / (data["twoDevStdev"]))


def plotAll(datalist):
    for data in datalist:
        plotCoreStats(data)
        plotCoreStatsLog(data)
        plotTwoDevStats(data)


def plotCoreStats(data):
    y = data["values"]
    x = list()
    for n in y:
        x.append(y.index(n))

    fig, ax = plt.subplots()
    ax.plot(x, y, '.', color=data["graph"]["color"])
    ax.plot(x, y, '#424441', linewidth=.5)
    ax.plot(data["self"]["x"], data["self"]["y"], 'k*',
            label=data["self"]["name"] + " (" + str(len(y)) + ")")

    ax.axhline(y=(data["mean"]), color='#022233', linewidth=.85,
               label=r'$\overline{x}\approx$' + str(int(data["mean"])))
    ax.axhline(y=(data["mean"] + data["stdev"]), color='#022233', alpha=.5, linewidth=.85,
               label=r'$\overline{x}\pm s$')
    ax.axhline(y=(data["mean"] - data["stdev"]), color='#022233', alpha=.5, linewidth=.85)

    ax.axhline(y=(data["mean"] + (2 * data["stdev"])), color='#022233', alpha=.25, linewidth=.85,
               label=r'$\overline{x} + 2s$')

    ax.legend()
    plt.xticks(data["graph"]["xSpacing"], data["graph"]["xticks"])
    ax.set(xlabel=data["graph"]["xlabel"], ylabel=data["graph"]["ylabel"])
    fig.savefig("graphs/" + data["graph"]["id"] + "_core.png")


def plotCoreStatsLog(data):
    y = data["values"]
    x = list()
    for n in y:
        x.append(y.index(n))

    fig, ax = plt.subplots()
    ax.plot(x, y, '.', color=data["graph"]["color"])
    ax.plot(x, y, '#424441', linewidth=.5)
    ax.plot(data["self"]["x"], data["self"]["y"], 'k*',
            label=data["self"]["name"] + " (" + str(len(y)) + ")")

    ax.axhline(y=(data["mean"]), color='#022233', linewidth=.85,
               label=r'$\overline{x}\approx$' + str(int(data["mean"])))
    ax.legend()
    plt.xticks(data["graph"]["xSpacing"], data["graph"]["xticks"])
    ax.set(xlabel=data["graph"]["xlabel"], ylabel=data["graph"]["ylabel"], yscale='log')
    fig.savefig("graphs/" + data["graph"]["id"] + "_log.png")


def plotTwoDevStats(data):
    y = data["twoDevValues"]
    x = list()
    for n in y:
        x.append(y.index(n))

    fig, ax = plt.subplots()
    ax.plot(x, y, '.', color=data["graph"]["color"])
    ax.plot(x, y, '#424441', linewidth=.5)
    ax.plot(data["self"]["x2"], data["self"]["y"], 'k*',
            label=data["self"]["name"] + " (" + str(len(data["values"])) + ")")

    ax.axhline(y=(data["twoDevMean"]), color='#022233', linewidth=.85,
               label=r'$\overline{x}\approx$' + str(int(data["twoDevMean"])))
    ax.axhline(y=(data["twoDevMean"] + data["twoDevStdev"]), color='#022233', alpha=.5, linewidth=.85,
               label=r'$\overline{x}\pm s$')
    ax.axhline(y=(data["twoDevMean"] - data["twoDevStdev"]), color='#022233', alpha=.5, linewidth=.85)
    ax.axhline(y=(data["twoDevMean"] + (2 * data["twoDevStdev"])), color='#022233', alpha=.25, linewidth=.85,
               label=r'$\overline{x} + 2s$')

    ax.legend()
    plt.xticks(data["graph"]["x2Spacing"], data["graph"]["x2ticks"])
    ax.set(xlabel=data["graph"]["xlabel"], ylabel=data["graph"]["ylabel"])
    fig.savefig("graphs/" + data["graph"]["id"] + "_twoDev.png")


with open("facebook.txt") as inf:
    for line in inf:
        split_line = line.split(',')
        fb_stats["values"].append(int(split_line[1].rstrip(')\n')))
        if line.find(TARGET_NAME["facebook"]) > 0:
            fb_stats["self"]["y"] = int(split_line[1].rstrip(')\n'))
            fb_stats["self"]["name"] = TARGET_NAME["facebook"]

with open("linkedin.txt") as inf:
    for line in inf:
        split_line = line.split(',')
        ln_stats["values"].append(int(split_line[1].rstrip(')\n')))
        if line.find(TARGET_NAME["linkedin"]) > 0:
            ln_stats["self"]["y"] = int(split_line[1].rstrip(')\n'))
            ln_stats["self"]["name"] = TARGET_NAME["linkedin"]

with open("tw_follows.txt") as inf:
    for line in inf:
        split_line = line.split(',')
        tw_fl_stats["values"].append(int(split_line[1].rstrip(')\n')))
        if line.find(TARGET_NAME["twitter"]) > 0:
            tw_fl_stats["self"]["y"] = int(split_line[1].rstrip(')\n'))
            tw_fl_stats["self"]["name"] = TARGET_NAME["twitter"]

with open("tw_friends.txt") as inf:
    for line in inf:
        split_line = line.split(',')
        tw_fr_stats["values"].append(int(split_line[1].rstrip(')\n')))
        if line.find(TARGET_NAME["twitter"]) > 0:
            tw_fr_stats["self"]["y"] = int(split_line[1].rstrip(')\n'))
            tw_fr_stats["self"]["name"] = TARGET_NAME["twitter"]


allData = (fb_stats, tw_fl_stats, ln_stats, tw_fr_stats)

allStats(allData)
plotAll(allData)
