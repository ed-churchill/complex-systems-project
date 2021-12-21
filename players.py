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

class Detective:
    """A class to model a detective"""

    def __init__(self):
        """Constructor, assigning a detective an initial location"""
        
        # Choose a random starting location for MisterX from the possible starting locations
        initial_locations = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 138, 141, 155, 174]
        initial_location = random.choice(initial_locations)

        # Initialise location using initial location
        self.location = initial_location
    

