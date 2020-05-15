from Flight import *

class Flights:

    def __init__(self, flights: list):
        self.flights = flights
        self.total_price = 0.0
        self.recalculate_price()

    def get_passengers(self) -> int:
        pass

    def recalculate_price(self) -> None:
        price = 0.0
        for flight in self.flights:
            price += flight.get_price() * flight.get_passengers()
        self.total_price = price

    def get_total_price(self):
        return self.total_price
