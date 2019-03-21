import networkx as nx

G = nx.karate_club_graph()
officers = list()
mr_hi = list()

for node in G:
    if G.node[node]['club'] == "Officer":
        officers.append(node)
    else:
        mr_hi.append(node)

print(officers)
print(mr_hi)
