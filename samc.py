import networkx as nx
import matplotlib.pyplot as plt
import networkx.readwrite.gml as nrg
import random
import sys

#G=nx.karate_club_graph()
G=nrg.read_gml("Italy.gml")

C=6
cent=[]
centdis=[]
preCent=[0 for i in range(C)]
cnode=[[] for i in range(C)]
nochange=False

for i in range(G.number_of_nodes()):
    G.node[i]['center']=False
    G.node[i]['clid']=-1
    G.node[i]['Sdis']=0
    G.node[i]['Cdis']=100


for i in range(C): #---------------------initialize centers
    centdis.append(sys.maxint)   #----------initialize center distance
cent=random.sample(G.nodes(),C)
    #if G.node[x]['center'] is True:
    #    i-=1
    #    continue
    #G.node[x]['center']=True
    #cent.append(x)

for i in range(C):
    print cent[i],

while nochange is False:
    cnode=[[] for i in range(C)]
    for v in G.nodes():   #-------------------cluster id set------------------
        for i in range(C):
            if G.node[v]['Cdis'] > nx.dijkstra_path_length(G,v,cent[i]): # select shortest path from centroid to each node
                G.node[v]['clid']=i
                G.node[v]['Cdis']=nx.dijkstra_path_length(G,v,cent[i])
            #elif G.node[v]['Cdis'] == nx.dijkstra_path_length(G,v,cent[i]):

            #    if len(cnode[G.node[v]['clid']]) > len(cnode[i]):
            #        G.node[v]['clid']=i
            #        G.node[v]['Cdis']=nx.dijkstra_path_length(G,v,cent[i])
            #elif nx.dijkstra_path_length(G,v,cent[i]) == nx.dijkstra_path_length(G,v,cent[j]):
            #    if v%2==0:
            #        G.node[v]['clid']=i
            #        cnode[i].append(v)
            #    else:
            #        G.node[v]['clid']=j
            #        cnode[j].append(v)
            #else:
            #    G.node[v]['clid']=j
            #    print "ID:",j,cnode[j]
        cnode[G.node[v]['clid']].append(v)

    for i in range(C):
        print cnode[i]

    for i in range(C):
        for v in G.nodes():
            if G.node[cent[i]]['clid'] == G.node[v]['clid']:
                for j in range(len(cnode[i])):
                    G.node[v]['Sdis']+=nx.dijkstra_path_length(G,v,cnode[i][j])
                if G.node[v]['Sdis'] < centdis[i]:
                    centdis[i]=G.node[v]['Sdis']
                    cent[i]=v

                    #print "id:",i,"node",v,G.node[v]['Sdis']

    h=0
    for i in range(C):  #---------center
        centdis[i]=sys.maxint #------------- initialize center distance
        if preCent[i]==cent[i]:
            h+=1

    if h==C:
        nochange=True

    print "center:",cent
    print "Precent:",preCent
    for i in range(C): #----------new center
        preCent[i]=cent[i]

    for i in G.nodes():
        G.node[i]['Sdis']=0      #--------initialize distance sum
        G.node[i]['Cdis']=100    #---------initialize distance from each node to center

print "end"

colors=["r","g","b","c","m","y"]
pos=nx.spring_layout(G)
nx.draw(G,pos,node_size=200,with_labels=True)
for i in range(C):
    nx.draw_networkx_nodes(G,pos,cnode[i],node_size=200,node_color=colors[i])
    print cnode[i]
nx.draw_networkx_nodes(G,pos,cent,node_size=300,node_shape='s',node_color='white',alpha=0.8)

print "controller node:",cent

plt.show()
