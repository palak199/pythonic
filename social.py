import networkx as nx
def neighborhood_overlap(g, u, v):
    n_common_nbrs = len(set(nx.common_neighbors(g, u, v)))
    n_join_nbrs = g.degree(u) + g.degree(v) - n_common_nbrs - 2
    return n_common_nbrs / n_join_nbrs

G=nx.Graph()
G.add_edges_from([1,i])
neighborhood_overlap(G,u,v)