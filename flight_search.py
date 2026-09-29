import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
        self.endpoint = os.getenv("FLIGHT_API_ENDPOINT")

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        para = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "INR",
            "api_key": self.api_key,
        }

        response = requests.get(url=self.endpoint, params=para)

        if response.status_code != 200:
            print(f"check_flights() response.status_code: {response.status_code}")
            return None

        data = response.json()

        if "error" in data:
            print(f"API error: {data['error']}")
            return None

        return data