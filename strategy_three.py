"""File containing functions to carry out the strategy outlined in Section 5 of the write-up."""

from generate_graphs import get_edges, generate_graph, draw_graph
from strategy_one import initialise_game
from graphical_distance_calculator import graphical_distance, graphical_set_distance
from strategy_two import detective_rush, poss_x_locations
import numpy as np

def misterx_run(mister_x, detectives, tube_edges, bus_edges, taxi_edges):
    """Function that carries out Mister X's turn using the running strategy. The 
    function returns 1 if Mister X has no possible moves and the detectives win, otherwise
    it return the current instance of Mister X, to be used as a parameter in the
    detectives' turn function.
    
    Please note the lines generating graphs can be commented/uncommented as you desire.
    When running the game many times, comment out the lines generating graphs to improve
    performance"""

    # Calculate Mister X's possible moves
    misterx_moves = mister_x.possible_moves(tube_edges, bus_edges, taxi_edges)
    for detective in detectives:
        if detective.location in misterx_moves:
            misterx_moves.remove(detective.location)
     
    # If list of possible moves is empty, then detectives win
    if not misterx_moves:
        # end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
        # draw_graph(end_graph, 'end_graph')
        return 1
    else:
        # Calculate detective locations
        detective_locations = [d.location for d in detectives]

        # Calculate distance from Mister X location to detective locations
        current_distance = graphical_set_distance(mister_x.location, detective_locations, tube_edges, bus_edges, taxi_edges)

        # Find the node which maximises the distance to the detective locations
        current_move = mister_x.location
        found_bigger = False
        for node in misterx_moves:
            distance = graphical_set_distance(node, detective_locations, tube_edges, bus_edges, taxi_edges)
            if distance > current_distance:
                found_bigger = True
                current_move = node
                current_distance = distance

        # Move Mister X to the node maximising distance, and move randomly 
        # if no smaller path was found.
        if found_bigger:
            mister_x.location = current_move
        else:
            # mister_x.location = random.choice(misterx_moves)
            # Find ArgMin
            sums = []
            for move in misterx_moves:
                sum = 0
                for d in detectives:
                    sum += 1 / pow(3, graphical_distance(move, d.location, tube_edges, bus_edges, taxi_edges))
                sums.append(sum)
            sums = np.array(sums)            
            arg_min = np.argmin(sums, axis=0)

            # Make move to node corresponding to argmin
            mister_x.location = misterx_moves[arg_min]

    return mister_x

def run_versus_rush(mister_x, detectives):
    """Function that carries out one game of Scotland Yard using the minimisation
    strategy specified in section 4 for the detectives, and the running strategy for
    Mister X specified in section 5. It takes class objects as paramaters 
    (which have been obtained from the 'initialise_game()' function. The function returns 1 
    if the detectives win and returns 0 if MisterX wins.
    
    Please note the lines generating graphs can be commented/uncommented as you desire.
    When running the game many times, comment out the lines generating graphs to improve
    performance"""

    # Get graph edges
    tube_edges, bus_edges, taxi_edges = get_edges()

    # Set initial possible Mister X locations
    poss_locations = [i for i in range(1, 200)]

    for k in range(1, 25):
        # Draw graph of current situation
        # current_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
        # draw_graph(current_graph, f'graph_{k}')

        # Carry out mister X's running move and check if game has terminated. If it hasn't, 
        # update Mister X to latest version
        location_before = mister_x.location
        mister_x = misterx_run(mister_x, detectives, tube_edges, bus_edges, taxi_edges)
        if mister_x == 1:
            print('Game over. Detectives win.')
            return 1
        location_after = mister_x.location

        # Work out what mode of transport Mister X used
        if [location_before, location_after] in taxi_edges or [location_after, location_before] in taxi_edges:
            transport_mode = 'taxi'
        elif [location_before, location_after] in bus_edges or [location_after, location_before] in bus_edges:
            transport_mode = 'bus'
        else:
            transport_mode = 'tube'

        # Detective calculate possible Mister X locations
        poss_locations = poss_x_locations(detectives, mister_x, k, poss_locations, transport_mode)
        
        # Carry out detectives' move
        temp = detective_rush(detectives, mister_x, k, poss_locations, tube_edges, bus_edges, taxi_edges)
        if temp == 0:
            # end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
            # draw_graph(end_graph, 'end_graph')
            print("Game over. Mister X wins")
            return 0 
        detectives = temp

        # Check if any of the detectives have the same location as Mister X
        detective_locations = [detective.location for detective in detectives]
        if mister_x.location in detective_locations:
            # end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
            # draw_graph(end_graph, 'end_graph')
            print("Game over. Detectives win")
            return 1
        else:
            # Remove the detective locations from the possible Mister X locations
            detective_locations = [detective.location for detective in detectives]
            for location in detective_locations:
                if location in poss_locations:
                    poss_locations.remove(location)
            
    # MisterX wins if the for loop completes without returning a value
    # end_graph = generate_graph(mister_x.location, [detective.location for detective in detectives])
    # draw_graph(end_graph, 'end_graph')
    print("Game over. Mister X wins.")
    return 0

if __name__ == "__main__":
    """Please comment out one of the options in this method in order to run the other one.
    Option 1 runs the game once and generates graphs (assuming they are not commented out
    of the above code). Option 2 runs the game 1000 times and counts the numbers of wins for
    each player without generating graphs (assuming they are commented out of the above code)"""

    # Option 1
    # mister_x, detectives = initialise_game()
    # run_versus_rush(mister_x, detectives)
    
    # Option 2
    misterx_wins = 0
    detective_wins = 0
    for j in range(1,101):
        mister_x, detectives = initialise_game()
        result = run_versus_rush(mister_x, detectives)
        if result == 1:
            detective_wins += 1
        else:
            misterx_wins += 1
    print(f"Detective wins: {detective_wins}")
    print(f"Mister X wins: {misterx_wins}")
