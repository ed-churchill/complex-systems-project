from typing import ByteString
from generate_graphs import get_edges

def get_adjacency_lists(tube_edges, bus_edges, taxi_edges):
    """Function that creates a list of length 199. Each element of the list is a 
    list of adjacent nodes to node (index + 1)"""

    # Get edges and remove duplicates
    edges = tube_edges + bus_edges + taxi_edges

    # For every node, make a list of nodes adjacent to it (remember zero indexing)
    adjacent_nodes = []
    for i in range(0, 199):
        adjacent_nodes.append([])
    for edge in edges:
        source_index = edge[0] - 1
        dest_index = edge[1] - 1
        if edge[1] not in adjacent_nodes[source_index]:
            adjacent_nodes[source_index].append(edge[1])
        if edge[0] not in adjacent_nodes[dest_index]:
            adjacent_nodes[dest_index].append(edge[0])
    
    return adjacent_nodes


if __name__ == "__main__":
    tube_edges, bus_edges, taxi_edges = get_edges()
    adjacency_list = get_adjacency_lists(tube_edges, bus_edges, taxi_edges)
    print(adjacency_list)