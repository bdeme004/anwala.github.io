import networkx as nx
import json

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


G = nx.karate_club_graph()

for node in G:
    if G.nodes[node]['club'] == "Officer":
        G.nodes[node]['color'] == 'green'
    else:
        G.nodes[node]['color'] == 'red'
