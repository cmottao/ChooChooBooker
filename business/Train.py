from .Wagon import Wagon

class Train:
    '''Represents an object of type Train.'''
    _NUMBER_OF_WAGONS = 6

    # Constructor method
    def __init__(self, number):
        self._number = number
        self._wagons = [Wagon(i) for i in range(1, Train._NUMBER_OF_WAGONS + 1)]
    
    def __repr__(self):
        return f'N {self._number}'

    # Getters methods
    def get_number(self):
        return self._number
    
    def get_number_of_wagons(self):
        return Train._NUMBER_OF_WAGONS  
    
    def get_wagons(self):
        return self._wagons