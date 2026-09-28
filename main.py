import requests_cache
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

FlightSearch = FlightSearch()
DataManager = DataManager()

pprint(DataManager.data())
flight_search = FlightSearch.check_flights(origin_city_code="CDG", destination_city_code="FRA")
print(flight_search)

