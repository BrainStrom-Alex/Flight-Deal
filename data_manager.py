import os
import requests
from dotenv import load_dotenv

load_dotenv()


url_datasheet = "https://api.sheety.co/fbaf84ba19e1c64ba14c243fb02101aa/myFlightDeals/prices"

class DataManager:
    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.AUTH = (self.username, self.password)
        self.response = requests.get(url=url_datasheet, auth=self.AUTH)

    def data(self):
        return self.response.json()["prices"]