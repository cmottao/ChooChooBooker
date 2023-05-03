from business.TourOrganizer import TourOrganizer

class UserInterface:
    '''Class for user interface management.'''

    # Constructor method
    def __init__(self):
        self._is_lead = False
        self._id = None
        self._tour_organizer = TourOrganizer()
        self._tour_organizer.organize()
        self._leaders_data = self._tour_organizer.get_leaders_data()

    # Methods
    def login(self):
        '''...'''

        print('Welcome!')

        while not self._is_lead:
            id = input("Enter id: ")
            self._id = id

            if int(id) in self._leaders_data:
                self._is_lead = True
                print('Logged in!')

    def show_menu(self):
        '''...'''

        print('1 -> My reservation \n2 -> Exit')

    def run(self):
        '''...'''
        
        self.login()

        while True:
            self.show_menu()
            option = input('>>> ')

            if option == '1':
                for reservation in self._tour_organizer.get_reservations():
                    if reservation.get_lead_passenger().get_id() == int(self._id):
                        print(reservation)
                input('Press enter to continue')
                continue 
            elif option == '2':
                break
            else:
                print('Invalid option.')