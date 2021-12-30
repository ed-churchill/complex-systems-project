"""File containing functions to carry out the strategy outlined in Section 4 of the write-up."""

from generate_graphs import get_edges, generate_graph, draw_graph
import random
from strategy_one import initialise_game, detectives_random_move, misterx_random_move
from graphical_distance_calculator import graphical_set_distance

def poss_x_locations(detectives, mister_x, k, last_poss_locations, tranport_mode):
    """Function that updates the possible locations of Mister X as a list of nodes, as outlined
    in section 4 of the write up."""

    # On turns 3, 8, 13, 18, the detectives get full knowledge of Mister X's location.
    if k in [3, 8, 13, 18]:
        return [mister_x.location]
    else:
        # Get edges in the subgraph of the last transport mode
        if tranport_mode == 'tube':
            sub_edges = get_edges()[0]
        elif tranport_mode == 'bus':
            sub_edges = get_edges()[1]
        elif tranport_mode == 'taxi':
            sub_edges = get_edges()[2]

        # Calculate possible vertices mister x could have moved to, given his last
        # transport mode
        temp = []
        for vertex in last_poss_locations:
            for v in range(1, 200):
                if ([vertex, v] in sub_edges) or ([v, vertex] in sub_edges):
                    if v not in temp:
                        temp.append(v)

        # Remove the detective locations from the possible Mister X locations
        detective_locations = [detective.location for detective in detectives]
        for location in detective_locations:
            if location in temp:
                temp.remove(location)

        # Return possible locations of Mister X
        return temp

def detective_rush(detectives, mister_x, k, poss_locations, tube_edges, bus_edges, taxi_edges):
    """Function that carries out the detectives' move as outlined in Section 4 of the
    write up. The parameter k is the turn number and the parameter possiblex_locations
    is a list of possible locations where Mister X could be. The function returns 0 if the
    detectives have no possible moves, otherwise it returns the list 'detectives', updated
    with new locations"""

    # Move randomly until turn 3
    if k < 3:
        detectives = detectives_random_move(detectives, tube_edges, bus_edges, taxi_edges)
    else:
        for i, detective in enumerate(detectives):
            #  Calculate detective's possible moves, ensuring no clashes with other detectives
            detective_moves = detective.possible_moves(tube_edges, bus_edges, taxi_edges)
            if detectives[i - 1].location in detective_moves:
                detective_moves.remove(detectives[i - 1].location)
            if detectives[i - 2].location in detective_moves:
                detective_moves.remove(detectives[i - 2].location)

            if not detective_moves:
                return 0

            # Calculate distance from current detective location to possible Mister X locations
            current_distance = graphical_set_distance(detective.location, poss_locations, tube_edges, bus_edges, taxi_edges)

            # Find the node which minimises the distance to possible Mister X location
            current_move = detective.location
            found_smaller = False
            for node in detective_moves:
                distance = graphical_set_distance(node, poss_locations, tube_edges, bus_edges, taxi_edges)
                if distance < current_distance:
                    found_smaller = True
                    current_move = node
                    current_distance = distance

            # Move the detective to the node minimising distance, and move randomly 
            # if no smaller path was found.
            if found_smaller:
                detective.location = current_move
            else:
                detective.location = random.choice(detective_moves)

    return detectives

def random_versus_rush(mister_x, detectives):
    """Function that carries out one game of Scotland Yard using the minimisation
    strategy specified in section 4 of the write up. It takes class objects as paramaters 
    (which have been obtained from the 'initialise_game()' function. The function returns 1 
    if the detectives win and returns 0 if MisterX wins
    
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

        # Carry out mister X's random move and check if game has terminated. If it hasn't, 
        # update Mister X to latest version
        location_before = mister_x.location
        mister_x = misterx_random_move(mister_x, detectives, tube_edges, bus_edges, taxi_edges)
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
    mister_x, detectives = initialise_game()
    random_versus_rush(mister_x, detectives)
    
    # Option 2
    misterx_wins = 0
    detective_wins = 0
    for j in range(1,1001):
        mister_x, detectives = initialise_game()
        result = random_versus_rush(mister_x, detectives)
        if result == 1:
            detective_wins += 1
        else:
            misterx_wins += 1
    print(f"Detective wins: {detective_wins}")
    print(f"Mister X wins: {misterx_wins}")