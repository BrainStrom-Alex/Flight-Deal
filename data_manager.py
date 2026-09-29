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
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=url_datasheet, auth=self.AUTH)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{url_datasheet}/{row_id}",
            json=new_data,
            auth=self.AUTH
        )