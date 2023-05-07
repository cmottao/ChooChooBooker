from data_access_layer.FileManager import FileManager

from .Train import Train

class TourOrganizer:
    '''Class for organize the tour.'''

    # Constructor method
    def __init__(self):
        Train.setup_trains()
        self._reservations = FileManager.read_reservations()
        self._reservations.sort(key = lambda n: n.get_number_of_passengers(), reverse=True)
        self._unbooked_reservations = []
        self._leaders_data = self.create_leaders_data()
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
    def all_reservations_assigned(self):
        '''Checks whether all reservations have been assigned to a train and a wagon.'''

        for reservation in self._reservations:
            if not reservation.is_assigned():
                return False
            
        return True

    def create_leaders_data(self):
        '''Creates a dictionary with the id and the name of the reservation leaders.'''

        data = {}
        for reservation in self._reservations:
            lead = reservation.get_lead_passenger()
            data[str(lead.get_id())] = lead.get_name()

        return data
    
    def update_counters(self, current_train_number, current_wagon_number, current_train):
        '''Updates train and wagon counters.'''

        if current_wagon_number < current_train.get_number_of_wagons():
            current_wagon_number += 1
        elif current_wagon_number == current_train.get_number_of_wagons():
            current_train_number += 1
            self._trains.append(Train(current_train_number)) # Adding new train to the list of trains
            current_wagon_number = 1 # Restarting current wagon variable
    
        return current_train_number, current_wagon_number
    
    def unbookable_reservations(self):
        '''Marks reservations that cannot be booked due to exceeding the maximum capacity of any train 
           in the system as unbookable, and adds them to a list of unbooked reservations.'''

        for j in range(len(self._reservations)):
            if self._reservations[j].get_number_of_passengers() > self._trains[0].get_max_capacity():
                self._unbooked_reservations.append(self._reservations[j])
                self._reservations[j].unbookable()

    def select_reservation(self, reservations, wagon_capacity):
        '''Selects the optimal reservation for a given wagon capacity.'''

        reservation_selected = None
        choose = None

        for j in range(len(reservations)):
            if reservations[j].get_number_of_passengers() <= wagon_capacity and (not reservations[j].is_assigned()):
                if reservation_selected is None or reservations[j].get_number_of_passengers() > reservation_selected.get_number_of_passengers():
                    reservation_selected = reservations[j]
                    choose = j

        return choose

    def organize(self):
        '''Assigns reservations to wagons and trains in an optimal way.'''

        current_train_number = 1
        current_wagon_number = 1

        self.unbookable_reservations() # Mark unbookable reservations
        
        while not self.all_reservations_assigned(): # If there is any unassigned reservation
            current_train = self._trains[current_train_number - 1]
            current_wagon = current_train.get_wagons()[current_wagon_number - 1]

            # Select the reservation according to the optimization
            reservation_selected = self.select_reservation(self._reservations, current_wagon.get_capacity()) 

            if reservation_selected is not None: # If finds a reservation
                current_wagon.assign_passengers(self._reservations[reservation_selected])
                self._reservations[reservation_selected].assign_train(current_train)
                self._reservations[reservation_selected].assign_wagon(current_wagon)

            else: # No enough space on current wagon
                current_train_number, current_wagon_number = self.update_counters(current_train_number, current_wagon_number, current_train)
                continue

    def reorganize(self, new_setup):
        '''Reorganizes with the new train setup.'''

        FileManager.rewrite_setup(new_setup)
        Train.setup_trains()
        self._reservations = FileManager.read_reservations()
        self._reservations.sort(key = lambda n: n.get_number_of_passengers(), reverse=True)
        self._trains = [Train(1)]
        self._unbooked_reservations = []
        self.organize()