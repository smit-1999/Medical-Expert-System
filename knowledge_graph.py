import networkx as nx
import matplotlib.pyplot as plt # For drawing
from networkx.algorithms import bipartite
import ast

print('Reading disease and its symptoms.')
file = open("disease_symptoms.txt", "r")
contents = file.read()
dictionary = ast.literal_eval(contents)
file.close()

print('Now reading all distinct symptoms.')
file = open("symptoms.txt","r")
symptoms = file.read().split("\n")
file.close()

symptoms=symptoms[0:-2]
G=nx.Graph()                    # Create a graph
G.add_nodes_from(dictionary.keys(), bipartite = 0)
G.add_nodes_from(symptoms, bipartite=1)
for key in dictionary.keys():
    u = key
    val = dictionary[key]
    val = val.split(",")

    for v in val:
        G.add_edge(u,v)

print('Graph nodes and edges created.')
X, Y = bipartite.sets(G)

pos=dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) )
pos.update( (n, (2, i)) for i, n in enumerate(Y) )

color_map=[]

for node in X:
    color_map.append('blue')

for node in Y:
    color_map.append('green')

print(X)
print(Y)
plt.title("Bipartite Knowledge Base")
nx.draw(G,node_color=color_map, with_labels = True,pos=pos) # Draw the graph
plt.savefig("graph.png") # Save to a PNG file
