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
        return f'reservation of {self._number_of_passengers} made by: {self._lead_passenger.get_name()}'
    
    # Getters methods
    def get_lead_passenger(self):
        return self._lead_passenger
    
    def get_passengers(self):
        return self._passengers
    
    def get_assigned_train(self):
        return self._assigned_train
    
    def get_assigned_wagon(self):
        return self.get_assigned_wagon
    
    def get_number_of_passengers(self):
        return self._number_of_passengers