import os
import requests
from dotenv import load_dotenv

load_dotenv()

url_dataemail_get = "abc"
url_datasheet = "abc"

class DataManager:
    def __init__(self):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.AUTH = (self.username, self.password)
        self.destination_data = {}
        self.customer_email = {}

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

    def get_customer_email(self):
        respond = requests.get(url=url_dataemail_get, auth=self.AUTH)
        email_data = respond.json()
        self.customer_email = email_data["users"]
        return self.customer_email


