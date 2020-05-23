import networkx as nx
from networkx import edge_betweenness_centrality
import matplotlib.pyplot as plt
from networkx.algorithms import community
import random
def most_central_edge(G):
        centrality = edge_betweenness_centrality(G)
       
        return max(centrality, key=centrality.get)
G=nx.Graph()
G.add_edges_from([("m","n")])
G.add_edges_from([("a","b"),("a","c"),("a","d"),("a","e"),("a","f")])
G.add_edges_from([("b","h"),("b","l"),("b","m"),("b","n")])
G.add_edges_from([("c","d"),("c","e"),("c","f")])
G.add_edges_from([("d","e")])
G.add_edges_from([("f","g"),("f","j")])
G.add_edges_from([("g","h"),("g","k"),("g","j")])
G.add_edges_from([("h","k"),("h","l")])
G.add_edges_from([("l","m"),("l","n")])
m=most_central_edge(G)
print(m)
x=community.girvan_newman(G, most_valuable_edge=m)
print (x)

