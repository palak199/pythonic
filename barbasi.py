import networkx as nx
import matplotlib.pyplot as plt
for i in range(1,6):
    g=nx.erdos_renyi_graph(5, 0.5)
    #g=nx.barabasi_albert_graph(5, 2)
    nx.draw(g)
    plt.show()
