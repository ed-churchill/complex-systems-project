class MisterX:
    """A class to model Mister X"""

    # Constructor, where 'initial_location' is an integer between 1 and 200
    def __init__(self, initial_location):
        # First check if initial location is valid
        if initial_location > 200 or initial_location < 1:
            raise Exception("Invalid initial location.")
        else:
            self.location = initial_location

class Detective:
    """A class to model a detective"""

    # Constructor, where 'initial_location' is an integer between 1 and 200
    def __init__(self, initial_location):
        # First check if initial location is valid
        if initial_location > 200 or initial_location < 1: 
            raise Exception("Invalid initial location.")
        else:
            self.location = initial_location
    

