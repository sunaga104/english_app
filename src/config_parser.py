import configparser

class ConfigParser():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        print(self.config)

