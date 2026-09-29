import requests_cache
from data_manager import DataManager
from datetime import datetime, timedelta
from pprint import pprint
from flight_data import find_cheapest_fight
from flight_search import FlightSearch
import smtplib

msg = []
my_email = "abc@gmail.com"
password = "abcdefghijkl"

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

DataManager = DataManager()
sheety_data = DataManager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

FlightSearch = FlightSearch()

ORIGIN_CITY_IATA = "LHR"

for destination in sheety_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = FlightSearch.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today)

    cheapest_flight = find_cheapest_fight(data=flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{sheety_data[0]['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < sheety_data[0]["lowestPrice"]:
        pprint(f"Lower price flight found to {sheety_data[0]['city']}!")
        DataManager.update_lowest_price(sheety_data[0]["id"], cheapest_flight.price)

    message =(f"Subject: Flight\n\nLow price alert! Only GBP {cheapest_flight.price} "
         f"to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}")

    msg.append(message)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="xyz@gmail.com", msg=msg[0])
