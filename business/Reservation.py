class Reservation:
    '''Represents an object of type Reservation.''' 

    # Constructor method
    def __init__(self, lead_passenger, passengers, assigned_train = None, assigned_wagon = None):
        self._lead_passenger = lead_passenger
        self._passengers = passengers
        self._assigned_train = assigned_train
        self._assigned_wagon = assigned_wagon
        self._number_of_passengers = len(passengers)
    
    # Representation method
    def __repr__(self):
        if self._assigned_train and self._assigned_wagon:
            return f'Reservation of {self._number_of_passengers} made by: {self._lead_passenger.get_name()}, Train: {self._assigned_train}, Wagon: {self._assigned_wagon}'
        else:
            return f'Reservation of {self._number_of_passengers} made by: {self._lead_passenger.get_name()}, could not be booked because it exceeds max train capacity.'
    
    # Getters methods
    def get_lead_passenger(self):
        return self._lead_passenger
    
    def get_passengers(self):
        return self._passengers
    
    def get_assigned_train(self):
        return self._assigned_train
    
    def get_assigned_wagon(self):
        return self._assigned_wagon 
    
    def get_number_of_passengers(self):
        return self._number_of_passengers
    
    # Setters methods
    def assign_train(self, train):
        self._assigned_train = train
    
    def assign_wagon(self, wagon):
        self._assigned_wagon = wagon

    # Methods
    def is_assigned(self):
        '''Returns if the reservation is assigned or not.'''
        
        return self._assigned_train != None and self._assigned_wagon != None
    
    def unbookable(self):
        '''Marks the reservation as unbookable.'''

        self._assigned_train = False
        self._assigned_wagon = False