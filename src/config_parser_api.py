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

    # def wright_config(self):
    #     print('testttttttttt"""""""""""""')
    #     self.config['translate_apitest'] = {
    #       "api_key" : "95edb2ec5f760356ecd1c4315980b6fa06330e0b5"
    #     }
    #     with open('config.ini', 'w') as config_file:
    #         self.config.write(config_file)
    #     return True