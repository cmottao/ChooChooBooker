class Wagon:
    '''Represents an object of type Wagon.'''

    # Constructor method
    def __init__(self, number, initial_capacity):
        self._number = number
        self._initial_capacity = initial_capacity
        self._capacity = initial_capacity

    # Representation method
    def __repr__(self):
        return  f'N {self._number}'

    # Getters methods
    def get_number(self):
        return self._number
    
    def get_capacity(self):
        return self._capacity

    # Methods
    def is_empty(self): 
        return self._initial_capacity == self._capacity
    
    def assign_passengers(self, reservation):
        self._capacity -= reservation.get_number_of_passengers()