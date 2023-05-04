from data_access_layer.ReservationReader import ReservationReader

from .Train import Train

class TourOrganizer:
    '''Class for organize the tour.'''

    # Constructor method
    def __init__(self):
        self._reservations = ReservationReader.read_reservations()
        self._reservations.sort(key = lambda n: n.get_number_of_passengers())
        self._trains = [Train(1)]

    # Getters methods
    def get_reservations(self):
        return self._reservations

    # Methods
    def organize(self):
        '''Assigns reservations to wagons and trains in an optimal way.'''

        i = 0 # iterator variable for reservations
        n_train = 1
        n_wagon = 1
        
        while i < len(self._reservations):
            current_train = self._trains[n_train - 1]
            current_wagon = current_train.get_wagons()[n_wagon - 1]

            if self._reservations[i].get_number_of_passengers() <= current_wagon.get_capacity(): # If there is still space in wagon
                current_wagon.assign_passengers(self._reservations[i])
                
                # Updating reservation variables
                self._reservations[i].assign_train(current_train)
                self._reservations[i].assign_wagon(current_wagon)
                i += 1

            else: # No enough space on current wagon
                if n_wagon < current_train.get_number_of_wagons():
                    n_wagon += 1
                elif n_wagon < current_train.get_number_of_wagons():
                    n_train += 1
                    self._trains.append(Train(n_train)) # Adding new train to the list of trains
                    n_wagon = 1 # Restarting current wagon variable
                continue
            
    def get_leaders_data(self):
        '''Returns a dictionary with the id and the name of the reservation leaders.'''

        data = {}
        for reservation in self._reservations:
            lead = reservation.get_lead_passenger()
            data[lead.get_id()] = lead.get_name()
        return data