import networkx as nx
import matplotlib.pyplot as plt
import networkx.readwrite.gml as nrg
import random

C=2
G=nrg.read_gml("Italy.gml")
SG=[]
cent=[]

random.seed(0)
for i in range(10):
    x=random.randint(0,1)
    print x

print G.node[0]
print G.nodes()
for v in G.nodes():
    #print nx.dijkstra_path_length(G,v,4)
    cent.append(v)

nx.draw(G,pos=nx.spring_layout(G),with_labels=True)
#plt.show()
