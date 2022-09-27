from json import loads
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from config_parser_api import ConfigParserApi



class Translate:

    def __init__(self):
        cf = ConfigParserApi()
        self.API_KEY = cf.get_api_key()
        self.API_SECRET_KEY = cf.get_api_secret_key()
        self.USER_NAME = cf.get_user_name()
        self.URL = "https://mt-auto-minhon-mlt.ucri.jgn-x.jp"
        self.ACCESS_TOKEN_URL = f"{self.URL}/oauth2/token.php"
        self.CLIENT_DATA = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET_KEY,
            "urlAccessToken": f"{self.URL}/oauth2/token.php"
        }
        self.DEFAULT_DATA = {
            "key": self.API_KEY,
            "name": self.USER_NAME,
            "type": "json"
        }

    def __post(self, url: str, data: dict[str, str]) -> str:
        request_object = Request(url, urlencode(data).encode("ascii"), method="POST")
        with urlopen(request_object) as response:
            result = response.read().decode("utf-8")
        return result 

    def __get_access_token(self):
        return loads(self.__post(f"{self.URL}/oauth2/token.php", data=self.CLIENT_DATA))["access_token"]

    def __translate(self, text: str, url: str) -> str:
        data = dict(**self.DEFAULT_DATA, access_token=self.__get_access_token(), text=text)
        return loads(self.__post(url, data=data))["resultset"]["result"]["text"]


    def translate_language_ja_to_en(self, text: str) -> str:
        return self.__translate(text, f"{self.URL}/api/mt/generalNT_ja_en/")


    def translate_language_en_to_ja(self, text: str) -> str:
        return self.__translate(text, f"{self.URL}/api/mt/generalNT_en_ja/")


if __name__ == "__main__":
    te = Translate()
    print(te.en_to_ja("test"))


