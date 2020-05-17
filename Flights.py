from Flight import *


class Flights:
    def __init__(self, flights: list):
        self.flights = flights
        self.total_price = 0.0
        self.recalculate_price()

    def get_passengers(self, flight_num: int) -> int:
        return self.flights[flight_num].get_passengers()

    def recalculate_price(self) -> None:
        price = 0.0
        for flight in self.flights:
            price += flight.get_price() * flight.get_passengers()
        self.total_price = price

    def get_total_price(self) -> float:
        return self.total_price

    def add_destination(self, destination: Flight):
        self.flights.append(destination)
        self.recalculate_price()

    def remove_destination(self, destination: Flight):
        self.flights.remove(destination)
        self.recalculate_price()
