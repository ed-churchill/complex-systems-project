from generate_graphs import get_edges, add_edges, add_nodes, generate_graph, draw_graph
from players import MisterX, Detective
import random

def initialise_game():
    """Function that sets up the initial graph with MisterX and the Detectives in
    randomly chosen unique locations"""

    # Create Mister X and Detectives
    mister_x = MisterX()
    detectives = [Detective(), Detective(), Detective(), Detective()]

    # Ensure Detectives have unique starting locations
    initial_locations = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 138, 141, 155, 174]
    detective_locations = [detective.location for detective in detectives]
    if len(detective_locations) > len(set(detective_locations)):
        for i in range(0, 4):
            detectives[i].location = random.choice(initial_locations)
            initial_locations.remove(detectives[i].location)

    


if __name__ == "__main__":
    initialise_game()