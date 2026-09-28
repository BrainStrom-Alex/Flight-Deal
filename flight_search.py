import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
        self.endpoint = os.getenv("FLIGHT_API_ENDPOINT")
        self.flights = []


    def check_flights(self, origin_city_code, destination_city_code):
        para = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": "2026-09-29",
            "return_date": "2026-10-30",
            "type": "1",
            "adults": "1",
            "currency": "INR",
            "api_key": self.api_key,
        }
        response = requests.get(url=self.endpoint, params=para)
        self.flights = response.json()["best_flights"]
        self.flights.append(response.json()["other_flights"][0])
        self.flights.append(response.json()["other_flights"][1])
        self.flights.append(response.json()["other_flights"][2])
        self.flights.append(response.json()["other_flights"][3])
        print(response.json())
        return self.flights

# , from_time, to_time