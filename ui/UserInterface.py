from business.TourOrganizer import TourOrganizer

class UserInterface:
    '''Class for user interface management.'''

    # Constructor method
    def __init__(self):
        self._is_admin = False
        self._is_lead = False
        self._user = None
        self._tour_organizer = TourOrganizer()
        self._reservations = self._tour_organizer.organize()
        self._leaders_data = self._tour_organizer.leaders_data()

    # Methods
    def login(self):
        '''...'''

        print('Welcome!')
        user = input("Enter username: ")
        password = input("Enter password: ")
        self._user = user

        if user == 'admin' and password == 'password':
            self._is_admin = True
            print('Logged in as administrator.')
        elif user in self._leaders_data and password == self._leaders_data[user]:
            self._is_lead = True
            print('Logged in as lead passenger.')
        else:
            print('Please check the username and password.')

    def show_menu(self):
        '''...'''

        if self._is_admin:
            print('1 -> Show all reservations \n2 -> Exit')
        else:
            print('1 -> Show my reservation \n2 -> Exit')

    def run(self):
        '''...'''
        
        self.login()

        while True:
            self.show_menu()
            option = input('>>> ')

            if option == '1':
                if self.is_admin:
                    for reservation in self._reservations:
                        print(reservation)
                else:
                    for reservation in self._reservations:
                        if reservation.get_lead_passenger().get_name() == self._user:
                            print(reservation)
            elif option == '2':
                break
            else:
                print('Invalid option.')