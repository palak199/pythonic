import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
g1=nx.Graph()
g2=nx.complete_graph(5)
g1.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,6)])
g.add_edges_from([(8,4),(9,4),(4,2),(2,5),(5,10),(2,1),(1,3),(3,7),(3,6)])
nx.draw(g2)
plt.show()
print(nx.average_shortest_path_length(g2))