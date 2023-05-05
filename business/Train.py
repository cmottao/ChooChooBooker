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
    
    # Representation method
    def __repr__(self):
        return f'N {self._number}'

    # Getters methods
    def get_number(self):
        return self._number
    
    def get_number_of_wagons(self):
        return Train._NUMBER_OF_WAGONS  
    
    def get_wagons(self):
        return self._wagons
    
    @classmethod
    def setup_trains(cls):
        '''Reads setup.txt and assign the static variables values according to that file
           This method must be executed before instaciating a train for first time, or when admin has updated
           the setup values
        '''
        with open('./data/setup.txt', 'r') as f:
            data = (f.read()).split(' ')
            cls._NUMBER_OF_WAGONS = int(data[0])
            cls._WAGON_CAPACITIES = sorted(int(i) for i in data[1:])
            