import pydotplus as pdp
import os
import ast

from pydotplus.graphviz import Node

 # Create London graph
london_graph = pdp.graphviz.Graph(graph_name='london_graph',
                                        graph_type='graph',
                                        simplify=True)

# Create graph nodes
for i in range(1, 200):
    node_i = pdp.graphviz.Node(name=str(i))
    london_graph.add_node(node_i)

#######---------------------------------------------------
# Create graph edges, using the edges stored in text files
#######---------------------------------------------------

#  Read tube edges from text file
with open('tube_edges.txt') as f:
    # Read edges from text file and convert to list
    tube_edges = f.readline()
    
# Add tube edges to graph
tube_edges = ast.literal_eval(tube_edges)
for edge in tube_edges:
    edge = pdp.graphviz.Edge(src=str(edge[0]), dst=str(edge[1]))
    london_graph.add_edge(edge)

# Write tube graph to .gv file
with open('tube_edges.gv', 'w') as f:
    f.write(london_graph.to_string())

# Write tube graph to .png file
os.system('dot -Tpng tube_edges.gv -o london_graph.png')

