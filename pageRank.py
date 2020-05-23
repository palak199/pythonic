import networkx as nx
import matplotlib.pyplot as plt
import random 
from fractions import Fraction
g=nx.DiGraph()
g.add_nodes_from([1,2,3,4,5])
g.add_edges_from([(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5),(5,1)])
labels=[1,2,3,4,5]
nx.draw_spring(g,with_labels=True)
#plt.show()
pr=nx.pagerank(g,weight=10)
for i,j in pr.items():
    print(i,round(j,2))