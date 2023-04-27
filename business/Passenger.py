class Passenger:
    '''Represents an object of type Passenger.'''

    #Constructor method
    def __init__(self, name, surname):
        '''Initializes an object of type passenger.'''
        
        self._name = name
        self._surname = surname

    #Getters methods
    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    #Methods
    