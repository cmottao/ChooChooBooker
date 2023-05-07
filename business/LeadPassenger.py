from .Passenger import Passenger

class LeadPassenger(Passenger):
    '''Represents an object of type Lead Passenger. Inherits from Passenger.'''

    # Constructor method
    def __init__(self, name, id, phone, email):
        super().__init__(name)
        self._id = id
        self._phone = phone
        self._email = email

    # Getters methods
    def get_id(self):
        return self._id

    def get_phone(self):
        return self._phone 

    def get_email(self):
        return self._email