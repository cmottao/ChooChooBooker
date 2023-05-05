import os

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
    
    def rewrite_setup(self, data):
        '''Method for rewriting the setup file uwu'''
        with open('./data/setup.txt', 'w') as f:
            for i in data:
                f.write(data[i])


    # Methods
    def login(self):
        '''Allows the user to log in to the system using their id.'''

        print('Welcome!')

        while not self._is_lead:
            id = input("Enter id: ")
            self._id = id

            if int(id) in self._leaders_data:
                self._is_lead = True
                print('Logged in!')
            else:
                print('No reservations found for the entered ID.')
            os.system('pause')
            os.system('cls')

    def show_menu(self):
        '''Displays the main menu of the system.'''

        os.system('cls')
        print('Menu \n \n1 -> View my reservation \n2 -> Exit')

    def run(self):
        '''Runs the main loop of the system.'''
        
        self.login()

        while True:
            self.show_menu()
            option = input('>>> ')

            if option == '1':
                print([reservation for reservation in self._tour_organizer.get_reservations() if reservation.get_lead_passenger().get_id() == int(self._id)])
                os.system('pause')
            elif option == '2':
                break
            else:
                print('Invalid option.')