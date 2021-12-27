from generate_graphs import get_edges, generate_graph, draw_graph
from players import MisterX, Detective
import random
from random_strategy import initialise_game, detectives_random_move
from graphical_distance_calculator import graphical_distance

def detective_turn(detectives, k, possiblex_locations, tube_edges, bus_edges, taxi_edges):
    """Function that carries out the detectives' move as outlined in Section 4 of the
    write up. The parameter k is the turn number and the parameter possiblex_locations
    is a list of possible locations where Mister X could be."""

    # Move randomly until turn 3
    if k < 3:
        detectives_random_move(detectives, tube_edges, bus_edges, taxi_edges)
    else:
        for i, detective in enumerate(detectives):
            #  Calculate detective's possible moves, ensuring no clashes with other detectives
            detective_moves = detective.possible_moves(tube_edges, bus_edges, taxi_edges)
            if detectives[i - 1].location in detective_moves:
                detective_moves.remove(detectives[i - 1].location)
            if detectives[i - 2].location in detective_moves:
                detective_moves.remove(detectives[i - 2].location)
            if detectives[i - 3].location in detective_moves:
                detective_moves.remove(detectives[i - 3].location)

            # Calculate distance from current detective location to possible Mister X locations
            current_distance = graphical_distance(detective.location, possiblex_locations)

            # Find the node which minimises the distance to possible Mister X locations. If
            # the current node gives the minimum distance itself, then move randomly
            current_move = detective.location
            found_smaller = False
            for node in detective_moves:
                distance = graphical_distance(node, possiblex_locations)
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
