import pydotplus as pdp
import os
import ast
from players import Detective, MisterX

def add_nodes(graph, mister_x_location, detective_locations):
    """Adds nodes to the given graph, taking into account the provided location of mister_x
    (an int between 1 and 200), as well as the location of the detectives (provided as a list of 3 
    integers, each between 1 and 200)"""

    # Add graph nodes
    for i in range(1, 200):
        node_i = pdp.graphviz.Node(name=str(i))
        node_i.set('penwidth', 3)
        node_i.set('fontsize', 40)
        graph.add_node(node_i)

def add_edges(graph):
    """Adds edges to the graph of London"""

    # Read edges from text file
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
        graph.add_edge(edge)
    for edge in bus_edges:
        edge = pdp.graphviz.Edge(src=str(edge[0]), dst=str(edge[1]))
        edge.set('color', 'blue')
        edge.set('penwidth', 4)
        graph.add_edge(edge)
    for edge in taxi_edges:
        edge = pdp.graphviz.Edge(src=str(edge[0]), dst=str(edge[1]))
        edge.set('color', 'green')
        edge.set('penwidth', 4)
        graph.add_edge(edge)


def generate_initial_graph():
    """Function that returns a pdp.graphviz.Graph object of the initial graph of London, with 
    Mister X and the detectives at their initial locations"""

    # Initialise graph
    london_graph = pdp.graphviz.Graph(graph_name='london_graph',
                                            graph_type='graph',
                                            simplify=False)

    # Add nodes and edges
    add_nodes(london_graph, mister_x_location=45, detective_locations=[1, 2, 3])
    add_edges(london_graph)

    return london_graph

def draw_graph(graph, graph_name):
    """Function that writes the given pydotplus.graphviz.Graph object to a .gv file and .png
    file. The name of both the files will be decided by the argument 'graph_name' of type string"""

    # Write graph to .gv file
    with open(f"{graph_name}.gv", 'w') as f:
        f.write(graph.to_string())

    # Write graph to .png file, using the already created .gv file
    os.system(f'dot -Tpng {graph_name}.gv -o {graph_name}.png')

london_graph = generate_initial_graph()
draw_graph(london_graph, 'london_graph')