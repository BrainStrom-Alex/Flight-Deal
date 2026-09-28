from flight_search import FlightSearch

flight_search = FlightSearch()

class FlightData:
    def __init__(self):
        self.price
        self.origin_airport
        self.destination_airport
        self.out_date
        self.return_date

    def find_cheapest_fight(self, data, return_date):
        flight = flight_search.check_flights(origin_city_code="CDG", destination_city_code="FRA")
        for i in flight:
            if i["price"] < self.price:
