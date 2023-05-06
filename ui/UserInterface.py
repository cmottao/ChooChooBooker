import os

from business.TourOrganizer import TourOrganizer

class UserInterface:
    '''Class for user interface management.'''

    # Constructor method
    def __init__(self):
        self._is_admin = False
        self._is_lead = False
        self._id = None
        self._tour_organizer = TourOrganizer()
        self._tour_organizer.organize()

    # Methods
    def show_message(self, message):
        '''Cleans and displays the message.'''

        os.system('cls')
        print(message)
        os.system('pause')
    
    def show_reservation(self):
        '''Displays the reservation of the logged-in lead passenger.'''

        os.system('cls')
        print(self._tour_organizer.get_reservation(self._id))
        os.system('pause')
    
    def show_reservations(self):
        '''Displays all reservations.'''

        os.system('cls')
        for reservation in self._tour_organizer.get_reservations():
            print(reservation)
        os.system('pause')
    
    def resetup_train(self):
        '''Updates the train setup.'''

        os.system('cls')
        print('Enter the new setup train')
        new_setup = input('>>> ')
        self._tour_organizer.reorganize(new_setup)
        self.show_message('Updated train configuration!')
    
    def show_menu_login(self):
        '''Displays login menu.'''

        os.system('cls')
        print('Sign in \n \n1 -> As admin \n2 -> As lead passenger \n3 -> Exit')

    def show_menu_admin(self):
        '''Displays the main menu of the system for admin users.'''

        os.system('cls')
        print('Menu \n \n1 -> Resetup the train \n2 -> View reservations \n3 -> Logout')

    def show_menu_lead(self):
        '''Displays the main menu of the system for lead passenger users.'''

        os.system('cls')
        print('Menu \n \n1 -> View my reservation \n2 -> Logout')
    
    def login_as_admin(self):
        '''Sets a flag indicating that the user is an admin.'''

        os.system('cls')
        self._is_admin = True

    def login_as_lead(self):
        '''Sets a flag indicating that the user is an lead passenger.'''

        while not self._is_lead:
            os.system('cls')
            print('Enter ID')
            id = input('>>> ')
            self._id = id
            
            if id in self._tour_organizer.get_leaders_data():
                self._is_lead = True
            else:
                self.show_message('Reservation not found for this ID')
    
    def logout(self):
        '''Resets the user's flags and ID.'''

        self._is_admin = False
        self._is_lead = False
        self._id = None

        self.show_message('Logged out!')

    def run_admin(self):
        '''Runs the loop of the system for admin users.'''
        
        while True:
            self.show_menu_admin()
            option = input('>>> ')

            if option == '1':
                self.resetup_train()
            elif option == '2':
                self.show_reservations()
            elif option == '3':
                self.logout()
                break
            else:
                self.show_message('Invalid option')

    def run_lead(self):
        '''Runs the loop of the system for lead passenger users.'''
        
        while True:
            self.show_menu_lead()
            option = input('>>> ')

            if option == '1':
                self.show_reservation()
            elif option == '2':
                self.logout()
                break
            else:
                self.show_message('Invalid option')

    def run(self):
        '''Runs the main loop for User Interface'''

        while True:
            self.show_menu_login()
            option = input('>>> ')

            if option == '1':
                self.login_as_admin()
                self.run_admin()
            elif option == '2':
                self.login_as_lead()
                self.run_lead()
            elif option == '3':
                break
            else:
                self.show_message('Invalid option')