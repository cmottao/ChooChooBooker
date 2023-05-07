class InvalidSetupException(Exception):
    def __init__(self, setup):
        super().__init__(f'"{setup}" is not a valid format of setup file, please rewrite it.')