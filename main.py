from business.TourOrganizer import TourOrganizer

if __name__ == '__main__':
    t = TourOrganizer()
    t.organize()

    for r in t.get_reservations():
        print(r)