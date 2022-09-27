from config_parser import ConfigParser

class ConfigParserApi(ConfigParser):
    
    def get_api_key(self):
        return self.config['translate_api']['api_key']

    def get_api_secret_key(self):
        return self.config['translate_api']['api_secret_key']
        
    def get_user_name(self):
        return self.config['translate_api']['user_name']
    
    def get_url(self):
        return self.config['translate_api']['url']
