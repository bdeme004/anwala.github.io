import igraph as ig

mr_hi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 17, 18, 19, 20, 22]
officers = [10, 15, 16, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

G = ig.Graph.Famous("Zachary")

G_edge = G.community_edge_betweenness(clusters=2).as_clustering().subgraphs()
G_edge[0].write_svg("graphs/ig/gedge0.svg")
G_edge[1].write_svg("graphs/ig/gedge1.svg")

G_glass = G.community_spinglass(spins=2).subgraphs()
G_glass[0].write_svg("graphs/ig/gglass0.svg")
G_glass[1].write_svg("graphs/ig/gglass1.svg")

G_fastg = G.community_fastgreedy().as_clustering().subgraphs()
G_fastg[0].write_svg("graphs/ig/gfastg0.svg")
G_fastg[1].write_svg("graphs/ig/gfastg1.svg")
