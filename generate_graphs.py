import pydotplus as pdp
import os
import ast

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
    """Function that adds the edges to the graph"""

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

def add_nodes(graph, misterx_location, detective_locations):
    """Adds the 199 nodes to the given graph, highlighting the locations of MisterX and the Detectives"""

    # Add Mister X node
    node_misterx = pdp.graphviz.Node(name=str(misterx_location), style='filled')
    node_misterx.set('pendwidth', 3)
    node_misterx.set('fontsize', 40)
    node_misterx.set('fillcolor', 'red')
    graph.add_node(node_misterx)

    # Add Detective nodes
    for val in detective_locations:
        node_detective = pdp.graphviz.Node(name=str(val), style='filled')
        node_detective.set('pendwidth', 3)
        node_detective.set('fontsize', 40)
        node_detective.set('fillcolor', 'green')
        graph.add_node(node_detective)

    # Add remaining graph nodes
    other_nodes = [i for i in range(1, 200) if i != misterx_location and i not in detective_locations]
    for i in other_nodes:
        node_i = pdp.graphviz.Node(name=str(i))
        node_i.set('penwidth', 3)
        node_i.set('fontsize', 40)
        graph.add_node(node_i)

def generate_graph(misterx_location, detective_locations):
    """Function that returns a pdp.graphviz.Graph object of the graph of London, together with
    Mister X's location and the Detectives' location highlighted."""

    # Initialise graph
    graph = pdp.graphviz.Graph(graph_name='london_graph',
                                            graph_type='graph',
                                            simplify=False)

    # Add nodes and edges
    add_nodes(graph, misterx_location, detective_locations)
    add_edges(graph)

    return graph

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
    graph = generate_graph(1, [2, 3, 4])
    draw_graph(graph, 'graph')