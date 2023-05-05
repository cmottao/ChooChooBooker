class Wagon:
    '''Represents an object of type Wagon.'''

    # Static attributes

    # Constructor method
    def __init__(self, number, capacity):
        self._number = number
        self._intial_capacity = capacity
        self._capacity = capacity

    # Representation method
    def __repr__(self):
        return  f'N {self._number}'

    # Getters methods
    def get_number(self):
        return self._number
    
    def get_capacity(self):
        return self._capacity

    def is_empty(self):
        return self._intial_capacity == self._capacity

    # Methods
    def assign_passengers(self, reservation):
        self._capacity -= reservation.get_number_of_passengers()