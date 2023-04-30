from Train import Train
from data.ReservationReader import ReservationReader

class TourOrganizer:
    '''Class for organize the tour.'''

    # Constructor method
    def __init__(self):
        self._reservations = ReservationReader.read_reservations()
        self._trains = []

    # Methods
    def sort_reservations(self):
        pass

    def organize(self):
        pass