from networkx.algorithms.shortest_paths.unweighted import bidirectional_shortest_path
from generate_graphs import get_edges
import networkx as nx

def graphical_distance(src, dest, tube_edges, bus_edges, taxi_edges):
    """Function that returns the minimum number of edges required to travel
    between vertex 'src' and vertex 'dest'"""

    # Get all edges of graph
    edges = tube_edges + bus_edges + taxi_edges

    # Create graph as networkx object
    G = nx.Graph()
    G.add_nodes_from(range(1, 200))
    for edge in edges:
        edge = tuple(edge)
        G.add_edge(*edge)

    # Compute length of shortest path
    shortest_path = bidirectional_shortest_path(G, src, dest)
    if src == dest:
        distance = 0
    else:
        distance = len(shortest_path) - 1

    return distance

def graphical_set_distance(src, dests, tube_edges, taxi_edges, bus_edges):
    """Function that calculates the minimum number of edges required to
    travel between node 'src' and every node in the list of nodes 'dests'.
    It returns the minimum distance of these distances."""

    # Calculate the distance to each node and return the minimum
    distances = [graphical_distance(src, dest, tube_edges, bus_edges, taxi_edges) for dest in dests]
    return min(distances)