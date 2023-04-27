import csv

from ..business.LeadPassenger import LeadPassenger
from ..business.Passenger import Passenger

class ReservationReader:
    @staticmethod
    def read_reservations():
        reservations = [] # Strores reservations
        with open('./data/reservations.csv') as f:
            reader = [r for r in csv.reader(f) if len(r)!=0]

        for i in range(0,len(reader)-1,2):
            lead_data = reader[i]
            passangers_data = reader[i+1]
            print(i)
            


if __name__ == '__main__':
    ReservationReader.read_reservations()
