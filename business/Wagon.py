class Wagon:
    '''Represents an object of type Wagon.'''

    # Static attributes
    CAPACITY = 50

    # Constructor method
    def __init__(self, number):
        self._number = number
        self._capacity = Wagon.CAPACITY

    # Representation method
    def __repr__(self):
        return  f'N {self._number}'

    # Getters methods
    def get_number(self):
        return self._number
    
    def get_capacity(self):
        return self._capacity

    # Methods
    def assign_passengers(self, reservation):
        self._capacity -= reservation.get_number_of_passengers()