from data_access_layer.FileManager import FileManager

from .Train import Train

class TourOrganizer:
    '''Class for organize the tour.'''

    # Constructor method
    def __init__(self):
        Train.setup_trains()
        self._reservations = FileManager.read_reservations()
        self._unbooked_reservations = []
        self._reservations.sort(key = lambda n: n.get_number_of_passengers())
        self._leaders_data = self._create_leaders_data()
        self._trains = [Train(1)]

    # Getters methods
    def get_reservations(self):
        return self._reservations

    def get_unbooked_reservations(self):
        return self._unbooked_reservations
    
    def get_reservation(self, id):
        for reservation in self._reservations:
            if reservation.get_lead_passenger().get_id() == int(id):
                return reservation
    
    def get_leaders_data(self):
        return self._leaders_data

    # Methods
    def _create_leaders_data(self):
        '''Creates a dictionary with the id and the name of the reservation leaders.'''

        data = {}
        for reservation in self._reservations:
            lead = reservation.get_lead_passenger()
            data[str(lead.get_id())] = lead.get_name()
        return data
    
    def _update_counters(self, current_train_number, current_wagon_number, current_train):
        '''Updates train and wagon counters.'''

        if current_wagon_number < current_train.get_number_of_wagons():
            current_wagon_number += 1
        elif current_wagon_number == current_train.get_number_of_wagons():
            current_train_number += 1
            self._trains.append(Train(current_train_number)) # Adding new train to the list of trains
            current_wagon_number = 1 # Restarting current wagon variable
    
        return current_train_number, current_wagon_number
    
    def organize(self):
        '''Assigns reservations to wagons and trains in an optimal way.'''

        i = 0 # iterator variable for reservations
        current_train_number = 1
        current_wagon_number = 1
        
        while i < len(self._reservations):
            current_train = self._trains[current_train_number - 1]
            current_wagon = current_train.get_wagons()[current_wagon_number - 1]

            if self._reservations[i].get_number_of_passengers() > current_train.get_max_capacity():
                self._unbooked_reservations.append(self._reservations[i])
                i += 1
                continue # Skips the reservation

            elif self._reservations[i].get_number_of_passengers() <= current_wagon.get_capacity(): # If there is still space in wagon
                current_wagon.assign_passengers(self._reservations[i])
                
                # Updating reservation variables
                self._reservations[i].assign_train(current_train)
                self._reservations[i].assign_wagon(current_wagon)
                i += 1

            else: # No enough space on current wagon
                current_train_number, current_wagon_number = self._update_counters(current_train_number, current_wagon_number, current_train)
                continue

    def reorganize(self, new_setup):
        '''Reorganizes with the new train setup.'''

        FileManager.rewrite_setup(new_setup)
        Train.setup_trains()
        self._reservations = FileManager.read_reservations()
        self._trains = [Train(1)]
        self._unbooked_reservations = []
        self.organize()