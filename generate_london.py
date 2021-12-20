import pydotplus as pdp
import os
import ast

 # Create London graph
london_graph = pdp.graphviz.Graph(graph_name='london_graph',
                                        graph_type='graph',
                                        simplify=False)

# Create graph nodes
for i in range(1, 200):
    node_i = pdp.graphviz.Node(name=str(i))
    node_i.set('penwidth', 3)
    node_i.set('fontsize', 40)
    london_graph.add_node(node_i)
    

#######---------------------------------------------------
# Create graph edges, using the edges stored in text files
#######---------------------------------------------------

#  Read edges from text file
with open('Edges/tube_edges.txt') as f:
    tube_edges = f.readline()
with open('Edges/bus_edges.txt') as f:
    bus_edges = f.readline()
with open('Edges/taxi_edges.txt') as f:
    taxi_edges = f.readline()
    
# Convert edges from text files to lists
tube_edges = ast.literal_eval(tube_edges)
bus_edges = ast.literal_eval(bus_edges)
taxi_edges = ast.literal_eval(taxi_edges)

# Add edges to graph
for edge in tube_edges:
    edge = pdp.graphviz.Edge(src=str(edge[0]), dst=str(edge[1]))
    edge.set('color', 'red')
    edge.set('penwidth', 4)
    london_graph.add_edge(edge)
for edge in bus_edges:
    edge = pdp.graphviz.Edge(src=str(edge[0]), dst=str(edge[1]))
    edge.set('color', 'blue')
    edge.set('penwidth', 4)
    london_graph.add_edge(edge)
for edge in taxi_edges:
    edge = pdp.graphviz.Edge(src=str(edge[0]), dst=str(edge[1]))
    edge.set('color', 'green')
    edge.set('penwidth', 4)
    london_graph.add_edge(edge)

# Write graph to .gv file
with open('london_graph.gv', 'w') as f:
    f.write(london_graph.to_string())

# Write London graph to .png file
os.system('dot -Tpng london_graph.gv -o london_graph.png')

