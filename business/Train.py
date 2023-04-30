from Wagon import Wagon

# Capacities of the Train
NUMBER_OF_WAGONS = 6
WAGON_CAPACITY = 50

class Train:
    '''Represents an object of type Train.'''

    # Constructor method
    def __init__(self, number):
        self._number = number
        self._number_of_wagons = NUMBER_OF_WAGONS
        self._wagon_capacity = WAGON_CAPACITY
        self._wagons = [Wagon(i, self._wagon_capacity) for i in range(1, self._number_of_wagons + 1)]

    # Getters methods
    def get_number(self):
        return self._number
    
    def get_number_of_wagons(self):
        return self._number_of_wagons
    
    def get_wagon_capacity(self):
        return self._wagon_capacity
    
    def get_wagons(self):
        return self._wagons