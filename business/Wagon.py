class Wagon:
    '''Represents an object of type Wagon.'''

    # Constructor method
    def __init__(self, number, capacity):
        self._number = number
        self._capacity = capacity
        
    # Getters methods
    def get_number(self):
        return self._number
    
    def get_capacity(self):
        return self._capacity

    # Methods
    def assign_passengers(self):
        pass