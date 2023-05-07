from data_access_layer.FileManager import FileManager

from .Wagon import Wagon

class Train:
    '''Represents an object of type Train.'''

    # Static attributes
    _NUMBER_OF_WAGONS = None
    _WAGON_CAPACITIES = None

    # Constructor method
    def __init__(self, number):
        self._number = number
        self._wagons = [Wagon(i, Train._WAGON_CAPACITIES[i-1]) for i in range(1, Train._NUMBER_OF_WAGONS + 1)]
        self._max_capacity = max(Train._WAGON_CAPACITIES)
    
    # Representation method
    def __repr__(self):
        return f'N {self._number}'

    # Getters methods
    def get_number(self): 
        return self._number
    
    def get_number_of_wagons(self):
        return self._NUMBER_OF_WAGONS  
    
    def get_wagons(self):
        return self._wagons
    
    def get_max_capacity(self):
        return self._max_capacity
    
    # Methods
    @classmethod
    def setup_trains(cls):
        '''Assigns the static variables values according to setup file. This method must be executed before 
           instaciating a train for first time, or when admin has updated the setup values.'''

        setup = FileManager.read_setup()

        cls._NUMBER_OF_WAGONS = setup[0]
        cls._WAGON_CAPACITIES = setup[1]