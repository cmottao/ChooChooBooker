class UserInterface:
    '''Class for user interface management.'''

    # Constructor method
    def __init__(self):
        self._is_admin = False

    # Methods
    def login(self):
        user = input("Enter username: ")
        password = input("Enter password: ")

        if user == 'admin' and password == 'password':
            self._is_admin = True
            print('Logged in as administrator.')
        # elif:

        # else:


    def show_menu(self):
        pass

    def run(self):
        pass