from .Train import Train
from .Reservation import Reservation

from data.ReservationReader import ReservationReader

class TourOrganizer:
    '''Class for organize the tour.'''

    # Constructor method
    def __init__(self):
        self._reservations = ReservationReader.read_reservations()
        self._trains = []

    # Methods
    # def sort_reservations(self):
    #     pass

    def organize(self):
        pass

    def leaders_data(self): # Esto creo que deberia ir mejor en el constructor
        '''...'''

        data = {}
        for reservation in self._reservations:
            lead = reservation.get_lead_passenger()
            data[lead.get_name()] = lead.get_id()
        return data