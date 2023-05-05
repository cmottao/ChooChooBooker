
class UnableToBook(Exception):
    def __init__(self, reservation):
        super().__init__(
            f'Unable to book {reservation.get_lead_passenger().get_name()} reservation due to wagons capacities, please remove it from reservations file and execute the program again'
            )
