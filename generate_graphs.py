import pydotplus as pdp
import os
import ast
from players import Detective, MisterX

def add_nodes(graph):
    """Adds the 199 nodes to the given graph"""

    # Add graph nodes
    for i in range(1, 200):
        node_i = pdp.graphviz.Node(name=str(i))
        node_i.set('penwidth', 3)
        node_i.set('fontsize', 40)
        graph.add_node(node_i)

def get_edges():
    """Function that reads edges from text files, and returns 3 lists (as a tuple)
    in the format (tube_edges, bus_edges, taxi_edges)"""

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

    return (tube_edges, bus_edges, taxi_edges)

def add_edges(graph):
    """Adds the edges to the graph"""

    # Read edges from text file
    edges = get_edges()
    tube_edges, bus_edges, taxi_edges = edges[0], edges[1], edges[2]

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
    """Function that returns a pdp.graphviz.Graph object of the initial graph of London"""

    # Initialise graph
    london_graph = pdp.graphviz.Graph(graph_name='london_graph',
                                            graph_type='graph',
                                            simplify=False)

    # Add nodes and edges
    add_nodes(london_graph)
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

# Main method
if __name__ == "__main__":
    london_graph = generate_initial_graph()
    draw_graph(london_graph, 'london_graph')

    tube_edges, bus_edges, taxi_edges = get_edges()
    print(possible_moves(5, tube_edges, bus_edges, taxi_edges))