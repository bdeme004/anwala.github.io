import networkx as nx
import matplotlib.pyplot as plt

OFFICERS = [9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
MR_HI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 21]


def getHighest(betw_dict):
    betweenenness = list(betw_dict.values())
    return betweenenness.index(max(betweenenness))


def girvanNewman(graph):
    betweenness = nx.edge_betweenness_centrality(graph)
    edges = list(betweenness.keys())
    edges.pop(getHighest(betweenness))
    graph.clear()
    graph.add_edges_from(edges)


G = nx.karate_club_graph()

# I counted and 11 is how many runs it takes.
# but the drawing is done before the math
# so we need to do an extra run.
for i in range(12):
    plt.clf()
    nx.draw(G, with_labels=True)
    plt.savefig("graphs/nx/step%d.png" % i)
    girvanNewman(G)
