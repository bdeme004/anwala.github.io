import networkx as nx
from networkx.algorithms import community as nxcm
import matplotlib.pyplot as plt

OFFICERS = [9, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
MR_HI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 19, 21]

G = nx.karate_club_graph()

H = tuple(sorted(c) for c in next(nxcm.girvan_newman(G)))

print(type(H[0]))
