import csv

from business.Passenger import Passenger
from business.Reservation import Reservation
from business.LeadPassenger import LeadPassenger

class ReservationReader:
    @staticmethod
    def read_reservations():
        reservations = [] # Strores reservations
        with open('./data/reservations.csv') as f:
            reader = [r for r in csv.reader(f) if len(r)!=0]

        for i in range(0,len(reader)-1,2):
            lead_data = [l.strip() for l in reader[i]]
            passangers_data = [p.strip() for p in reader[i+1]]
            lead_passenger = LeadPassenger(
                lead_data[0].split(' ')[0],
                lead_data[0].split(' ')[1],
                int(lead_data[1]),
                int(lead_data[2]),
                lead_data[3]
                )
            
            passengers = [Passenger(p.split(' ')[0], p.split(' ')[1]) for p in passangers_data]
            passengers.append(lead_passenger) # Lead passenger is also a passenger

            reservations.append(Reservation(lead_passenger, passengers))
        
        return reservations


