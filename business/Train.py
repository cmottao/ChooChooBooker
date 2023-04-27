from Wagon import Wagon

#Capacities of the Train
NUMBER_OF_WAGONS = 6
WAGON_CAPACITY = 50

class Train:
    '''Represents an object of type Train.'''

    #Constructor method
    def __init__(self, number):
        '''Initializes an object of type Train.'''

        self._number = number
        self._number_of_wagons = NUMBER_OF_WAGONS
        self._wagon_capacity = WAGON_CAPACITY
        self._wagons = [Wagon(self._wagon_capacity, i) for i in range(1, self._number_of_wagons + 1)]

    #Getters methods


    #Methods 
    
    