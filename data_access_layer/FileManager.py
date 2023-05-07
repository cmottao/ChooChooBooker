import csv

from business.LeadPassenger import LeadPassenger
from business.Passenger import Passenger
from business.Reservation import Reservation
from business.exceptions.InvalidSetupException import InvalidSetupException

class FileManager:
    '''Class for read and write files on disk.'''

    # Methods
    @staticmethod
    def read_reservations():
        '''Reads reservations data from CSV file and returns a list of the data.'''

        reservations = [] # Stores reservations
        with open('./data/reservations.csv') as f:
            reader = [r for r in csv.reader(f) if len(r) != 0]

        for i in range(0, len(reader) - 1, 2):
            lead_data = [l.strip() for l in reader[i]]
            passengers_data = [p.strip() for p in reader[i + 1]]
            lead_passenger = LeadPassenger(lead_data[0], int(lead_data[1]), int(lead_data[2]), lead_data[3])
            
            passengers = [Passenger(name) for name in passengers_data]
            passengers.insert(0, lead_passenger) # Lead passenger is also a passenger

            reservations.append(Reservation(lead_passenger, passengers))
        
        return reservations
    
    @staticmethod
    def read_setup():
        '''Reads the train setup from TXT file and returns a list of the data.'''

        setup = []
        with open('./data/setup.txt', 'r') as f:
            try:
                data = (f.read()).split(' ')
                setup.append(int(data[0]))
                setup.append(sorted(int(i) for i in data[1:]))
            except ValueError:
                raise InvalidSetupException(data)

        return setup
    
    @staticmethod
    def rewrite_setup(data):
        '''Method for rewriting the setup Train.'''
        
        with open('./data/setup.txt', 'w') as f:
            f.write(data)