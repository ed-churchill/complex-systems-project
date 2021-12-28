from generate_graphs import get_edges, generate_graph, draw_graph
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

    # Return class objects for use in the game
    return (mister_x, detectives)


def play_random_game(mister_x, detectives):
    """Function that carries out one game of Scotland Yard using the random walk
    strategy specified in the write up. It takes class objects as paramaters (which
    have been obtained from the 'initialise_game()' function. The function returns 1 
    if the detectives win and returns 0 if MisterX wins"""

    # Get graph edges
    tube_edges, bus_edges, taxi_edges = get_edges()

    for k in range(1, 25):
        # Draw graph of current situation
        current_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
        draw_graph(current_graph, f'graph_{k}')

        # Carry out mister X's move and check if game has terminated. If it hasn't, update Mister X to
        # latest version
        mister_x = misterx_random_turn(mister_x, detectives, tube_edges, bus_edges, taxi_edges)
        if mister_x == 1:
            print('Game over. Detectives win.')
            return 1

        # Carry out the detectives' move
        detectives = detectives_random_move(detectives, tube_edges, bus_edges, taxi_edges)

        # Check if any of the detectives have the same location as Mister X
        detective_locations = [detective.location for detective in detectives]
        if mister_x.location in detective_locations:
            end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
            draw_graph(end_graph, 'end_graph')
            print("Game over. Detectives win")
            return 1

    # MisterX wins if the for loop completes without returning a value
    end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
    draw_graph(end_graph, 'end_graph')
    print("Game over. Mister X wins.")
    return 0

def misterx_random_turn(mister_x, detectives, tube_edges, bus_edges, taxi_edges):
    """Function that carries out Mister X's turn using the random walk strategy. The 
    function returns 1 if Mister X has no possible moves and the detectives win, otherwise
    it return the current instance of Mister X, to be used as a parameter in the
    'detective_random_turn' function."""

    # Calculate Mister X's possible moves
    misterx_moves = mister_x.possible_moves(tube_edges, bus_edges, taxi_edges)
    for detective in detectives:
        if detective.location in misterx_moves:
            misterx_moves.remove(detective.location)
     
    # If list of possible moves is empty, then detectives win
    if not misterx_moves:
        end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
        draw_graph(end_graph, 'end_graph')
        return 1
    else:
        # Otherwise, move to a random node out of the possible nodes
        mister_x.location = random.choice(misterx_moves)
        return mister_x

def detectives_random_move(detectives, tube_edges, bus_edges, taxi_edges):
    """Function that carries out the detectives' turn using the random walk strategy. The 
    function returns 0 if any detective has no possible moves and Mister X wins, otherwise
    it return the current instances of the detectives as a list , to be used as a parameter in the
    'detective_random_turn' function."""

    # Calculate the detectives' possible moves.
    for i, detective in enumerate(detectives):
        # Ensure no clashes with other detectives
        detective_moves = detective.possible_moves(tube_edges, bus_edges, taxi_edges)
        if detectives[i - 1].location in detective_moves:
            detective_moves.remove(detectives[i - 1].location)
        if detectives[i - 2].location in detective_moves:
            detective_moves.remove(detectives[i - 2].location)
        if detectives[i - 3].location in detective_moves:
            detective_moves.remove(detectives[i - 3].location)
        
        # Move to random node unless there are no possible moves, in which case don't move
        if detective_moves:
            detective.location = random.choice(detective_moves)
    
    return detectives    

if __name__ == "__main__":
    mister_x, detectives = initialise_game()
    result = play_random_game(mister_x, detectives)
