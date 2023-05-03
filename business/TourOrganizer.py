from .Train import Train
from .Reservation import Reservation

from data_access_layer.ReservationReader import ReservationReader

class TourOrganizer:
    '''Class for organize the tour.'''

    # Constructor method
    def __init__(self):
        self._reservations = ReservationReader.read_reservations()
        self._reservations.sort(
            key = lambda n: n.get_number_of_passengers()
        )
        print(len(self._reservations))
        self._trains = []

    def organize(self):
        i = 0 # iterator variable for reservations
        n_train = 1
        n_wagon = 1
        self._trains.append(Train(1))
        
        while i < len(self._reservations):
            print(i)
            reservation = self._reservations[i]
            current_train = self._trains[n_train - 1]
            current_wagon = current_train.get_wagons()[n_wagon - 1]

            if reservation.get_number_of_passengers() <= current_wagon.get_capacity(): #if there is still space in wagon
                current_wagon.assign_passengers(reservation.get_passengers())
                
                # Updating reservation variables
                reservation.assign_train(current_train)
                reservation.assign_wagon(current_wagon)
                i+=1

            else: # No enough space on current wagon
                if current_train.get_number_of_wagons() > n_wagon:
                    n_wagon += 1
                elif current_train.get_number_of_wagons() == n_wagon:
                    n_train += 1
                    self._trains.append(Train(n_train)) # Adding new train to the list of trains
                    n_wagon = 1 # Restarting current wagon variable
                
                continue
            
    def get_reservations(self):
        return self._reservations
                
    def leaders_data(self): # Esto creo que deberia ir mejor en el constructor
        '''...'''

        data = {}
        for reservation in self._reservations:
            lead = reservation.get_lead_passenger()
            data[lead.get_name()] = lead.get_id()
        return data