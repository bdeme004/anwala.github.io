import networkx as nx
import matplotlib.pyplot as plt

# MR_HI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 21]
# OFFICERS = [9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

COLOR = ["r", "r", "r", "r", "r", "r", "r", "r", "r", "g", "r", "r", "r", "r", "g", "g", "r",
         "r", "g", "r", "g", "r", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g"]
i = 1


def getHighest(betw_dict):
    betweenenness = list(betw_dict.values())
    return betweenenness.index(max(betweenenness))


def girvanNewman(graph):
    betweenness = nx.edge_betweenness_centrality(graph)
    edge = list(betweenness.keys()).pop(getHighest(betweenness))
    graph.remove_edge(edge[0], edge[1])


def plotAndSave(graph, n):
    plt.clf()
    nx.draw(graph, with_labels=True, node_color=COLOR)
    plt.savefig("graphs/nx/step%d.png" % n)


G = nx.karate_club_graph()
plotAndSave(G, 0)

while len(list(nx.connected_components(G))) < 2:
    girvanNewman(G)
    plotAndSave(G, i)
    i += 1
