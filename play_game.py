from generate_graphs import get_edges, add_edges, add_nodes, generate_graph, draw_graph
from players import MisterX, Detective
import random

def initialise_game():
    """Function that sets up the initial graph with MisterX and the Detectives in
    randomly chosen unique locations. It returns the class objects as a tuple of the form
    (MisterX(), detectives)"""

    # Create Mister X and Detectives
    mister_x = MisterX()
    detectives = [Detective(), Detective(), Detective(), Detective()]

    # Ensure Detectives have unique starting locations
    possible_locations = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 138, 141, 155, 174]
    initial_locations = [detective.location for detective in detectives]
    if len(initial_locations) > len(set(initial_locations)):
        for i in range(0, 4):
            detectives[i].location = random.choice(possible_locations)
            possible_locations.remove(detectives[i].location)
    initial_locations = [detective.location for detective in detectives]

    # Generate graph, including initial locations of players
    intiial_graph = generate_graph(mister_x.location, initial_locations)

    # Draw the graph and write it to a file "initial_graph.png"
    draw_graph(intiial_graph, 'initial_graph')

    # Return class objects for use in the game
    return (mister_x, detectives)


def play_random_game(mister_x, detectives):
    """Function that carries out one game of Scotland Yard using the random walk
    strategy specified in the write up. It takes class objects as paramaters (which
    have been obtained from the 'initialise_game()' function"""

    tube_edges, bus_edges, taxi_edges = get_edges()

    # Calculate Mister X's possible nodes TODO: IF LIST IS EMPTY THEN GAME OVER
    misterx_moves = mister_x.possible_moves(tube_edges, bus_edges, taxi_edges)
    for detective in detectives:
        if detective.location in misterx_moves:
            misterx_moves.remove(detective.location)
        
    # Move to a random node out of the possible nodes
    mister_x.location = random.choice(misterx_moves)

if __name__ == "__main__":
    mister_x, detectives = initialise_game()
    play_random_game(mister_x, detectives)