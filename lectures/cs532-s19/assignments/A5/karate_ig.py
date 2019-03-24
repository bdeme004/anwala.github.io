import igraph as ig

mr_hi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 17, 18, 19, 20, 22]
officers = [10, 15, 16, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

G = ig.Graph.Famous("Zachary")

print(G.community_edge_betweenness())
