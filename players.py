import random

class MisterX:
    """A class to model Mister X"""

    def __init__(self):
        """Constructor, assigning MisterX an initial location"""
        
        # Choose a random starting location for MisterX from the possible starting locations
        initial_locations = [45, 51, 71, 78, 104, 106, 127, 132, 146, 166, 170, 172]
        initial_location = random.choice(initial_locations)

        # Initialise location using initial location
        self.location = initial_location

    def possible_moves(self, tube_edges, bus_edges, taxi_edges):
        """Function that returns a list of possible nodes that can be travelled to 
        from the current location"""

        # List to store nodes that can be travelled to via tube
        tube_journeys = []
        for edge in tube_edges:
            if self.location in edge:
                # Get index of current location in the list (of length 2)
                index = edge.index(self.location)
                
                # Append the other node in the edge to list of possible nodes
                possible_node = edge[index - 1]
                tube_journeys.append(possible_node)

        # List to store nodes that can be travelled to via bus
        bus_journeys = []
        for edge in bus_edges:
            if self.location in edge:
                # Get index of current location in the list (of length 2)
                index = edge.index(self.location)
                
                # Append the other node in the edge to list of possible nodes
                possible_node = edge[index - 1]
                bus_journeys.append(possible_node)

        # List to store nodes that can be travelled to via taxi
        taxi_journeys = []
        for edge in taxi_edges:
            if self.location in edge:
                # Get index of current location in the list (of length 2)
                index = edge.index(self.location)
                
                # Append the other node in the edge to list of possible nodes
                possible_node = edge[index - 1]
                taxi_journeys.append(possible_node)

        # Return list
        return tube_journeys + bus_journeys + taxi_journeys

    
class Detective:
    """A class to model a detective"""

    def __init__(self):
        """Constructor, assigning a detective an initial location"""
        
        # Choose a random starting location for MisterX from the possible starting locations
        initial_locations = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 138, 141, 155, 174]
        initial_location = random.choice(initial_locations)

        # Initialise location using initial location
        self.location = initial_location
    
    def possible_moves(self, tube_edges, bus_edges, taxi_edges):
        """Function that returns a list of possible nodes that can be travelled 
        to from the current location"""

        # List to store nodes that can be travelled to via tube
        tube_journeys = []
        for edge in tube_edges:
            if self.location in edge:
                # Get index of current location in the list (of length 2)
                index = edge.index(self.location)
                
                # Append the other node in the edge to list of possible nodes
                possible_node = edge[index - 1]
                tube_journeys.append(possible_node)

        # List to store nodes that can be travelled to via bus
        bus_journeys = []
        for edge in bus_edges:
            if self.location in edge:
                # Get index of current location in the list (of length 2)
                index = edge.index(self.location)
                
                # Append the other node in the edge to list of possible nodes
                possible_node = edge[index - 1]
                bus_journeys.append(possible_node)

        # List to store nodes that can be travelled to via taxi
        taxi_journeys = []
        for edge in taxi_edges:
            if self.location in edge:
                # Get index of current location in the list (of length 2)
                index = edge.index(self.location)
                
                # Append the other node in the edge to list of possible nodes
                possible_node = edge[index - 1]
                taxi_journeys.append(possible_node)

        # Return dictionary
        return tube_journeys + bus_journeys + taxi_journeys
