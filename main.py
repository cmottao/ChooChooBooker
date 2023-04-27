from data import ReservationReader

if __name__ == '__main__':
    for r in ReservationReader.ReservationReader.read_reservations():
        print(r)