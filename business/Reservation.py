class Reservation:
    '''Represents an object of type Reservation.'''

    #Constructor method
    def __init__(self, lead_passenger, passengers):
        '''Initializes an object of type Reservation.'''

        self._lead_passenger = lead_passenger
        self._passengers = passengers
        self._number_of_passengers = len(passengers)
    
    def __repr__(self):
        return f'reservation of {self._number_of_passengers} made by: {self._lead_passenger.get_name()}'


    #Getters methods


    #Methods
    
    #     class Reservation:
    # '''Represents an object of type Reservation.'''

    # #Constructor method
    # def __init__(self, lead_passenger, passengers):
    #     '''Initializes an object of type Reservation.'''

    #     self._lead_passenger = lead_passenger
    #     self._lead_passenger = passengers
    #     self._number_of_passengers = len(passengers)

    # #Getters methods


    # #Methods
    
        