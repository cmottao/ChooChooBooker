class Passenger:
    '''Represents an object of type Passenger.''' 

    # Constructor method
    def __init__(self, name):
        self._name = name

    # Getters methods
    def get_name(self):
        return self._name