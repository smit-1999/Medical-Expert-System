import networkx as nx
import matplotlib.pyplot as plt # For drawing
from networkx.algorithms import bipartite


G=nx.Graph() # Create a graph
G.add_nodes_from(['A','B','C'], bipartite = 0)
G.add_nodes_from(['e','f'], bipartite=1)
G.add_edges_from([('A','e'),('A','f'),('B','e'),('C','e')])
# for target in dictionary.keys():
#     G.add_edge(target, dictionary[target]) # Add an edge for each dictionary entry
#                                            # Nodes are automatically created

X, Y = bipartite.sets(G)
print('X: ',X)
print('Y:',Y)
pos=dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) )
pos.update( (n, (2, i)) for i, n in enumerate(Y) )

color_map=[]

for node in X:
    color_map.append('blue')

for node in Y:
    color_map.append('green')


nx.draw(G,node_color=color_map, with_labels = True,pos=pos) # Draw the graph
plt.savefig("graph.png") # Save to a PNG file
