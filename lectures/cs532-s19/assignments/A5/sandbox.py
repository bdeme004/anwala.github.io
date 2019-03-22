import networkx as nx
import matplotlib.pyplot as plt

NODES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
EDGES = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (10, 9), (10, 8), (10, 7), (10, 6), (9, 8), (9, 7), (9, 6), (8, 7), (8, 6), (7, 6),
         ]

G = nx.Graph()

G.add_nodes_from(NODES)
G.add_edges_from(EDGES)

cc = sorted(nx.connected_components(G), key=len, reverse=True)

for n in cc:
    print(n)

nx.draw(G, with_labels=True, node_color=range(10), cmap=plt.cm.coolwarm)
plt.show()
