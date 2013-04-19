import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# In this representation i'm considering that all the graphs have nodes between 0 an 11
#                                           0    1    2    3    4    5    6    7    8    9    10   11
connection_one =                 np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])     #0
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)   #1
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)   #2
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0]],0)   #3
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)   #4
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]],0)   #5
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)   #6
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0]],0)   #7
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]],0)   #8
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)   #8
connection_one = np.append(connection_one,[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],0)   #10
connection_one = np.append(connection_one,[[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0]],0)   #11


#                                           0    1    2    3    4     5    6   
connection_two =                 np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])     #0
connection_two = np.append(connection_two,[[0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0]],0)   #1
connection_two = np.append(connection_two,[[0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]],0)   #2
connection_two = np.append(connection_two,[[0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0]],0)   #3
connection_two = np.append(connection_two,[[0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0]],0)   #4
connection_two = np.append(connection_two,[[0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0]],0)   #5
connection_two = np.append(connection_two,[[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]],0)   #6


#This is just to check my representations...

conn_one = [None]*12
conn_one[2] = []
conn_one[3] = [10,8]
conn_one[5] = [11]
conn_one[7] = [11,8]
conn_one[8] = [9]
conn_one[9] = []
conn_one[10] = []
conn_one[11] = [2,9,10]

conn_two =  [None]*7
conn_two[1] = [5,2]
conn_two[2] = [1,3,5]
conn_two[3] = [4,2]
conn_two[4] = [3,5,6]
conn_two[5] = [1,2,4]
conn_two[6] = [4]

plt.subplots_adjust(left=0,right=1,bottom=0,top=0.95,wspace=0.01,hspace=0.01)
G = nx.DiGraph()
for x in range(0,12):
    for y in range(0,12):
        if connection_one[x][y] == 1:
            G.add_node(x)
            G.add_node(y)
            G.add_edge(x, y)

plt.subplot(221)
plt.title("Graph 1 matrix")
pos = nx.shell_layout(G)
nx.draw(G,pos,with_labels=False,node_size=00)

G2 = nx.Graph()
for x in range(0,7):
    for y in range(0,7):
        if connection_two[x][y] == 1:
            G2.add_node(x)
            G2.add_node(y)
            G2.add_edge(x, y)
plt.subplot(222)
plt.title("Graph 2 matrix")
pos = nx.shell_layout(G2)
nx.draw(G2,pos,with_labels=False,node_size=20)

G3 = nx.DiGraph()
for idx, x in enumerate(conn_one):
    if x is not None:
        G3.add_node(idx)
        for y in x:
            G3.add_node(y)
            G3.add_edge(idx,y)
plt.subplot(223)
plt.title("Graph 1 list")
pos = nx.shell_layout(G3)
nx.draw(G3,pos,with_labels=False,node_size=20)

G4 = nx.Graph()
for idx, x in enumerate(conn_two):
    if x is not None:
        G4.add_node(idx)
        for y in x:
            G4.add_node(y)
            G4.add_edge(idx,y)

plt.subplot(224)
plt.title("Graph 2 list")
pos = nx.shell_layout(G4)
nx.draw(G4,pos,with_labels=False,node_size=20)

plt.show()

print("radius: %d" % nx.radius(G2))
print("diameter: %d" % nx.diameter(G2))
print("eccentricity: %s" % nx.eccentricity(G2))
print("center: %s" % nx.center(G2))
print("periphery: %s" % nx.periphery(G2))
print("density: %s" % nx.density(G2))


print("density graph1: %s" % nx.density(G)) 

