from Skyscanner import *
from random import *


class Travel:
    def __init__(self, destinations: list, user: User, passengers: int):
        self.destinations = destinations
        self.passengers = passengers
        self.flights = Flights([])
        self.assign_flights()
        self.total_price = 0.0
        self.user = user

    def get_destinations(self) -> list:
        return self.destinations

    def get_passengers(self) -> int:
        return self.passengers

    def get_flights(self) -> Flights:
        return self.flights

    def get_flights_list(self) -> list:
        return [f for f in self.flights.flights]

    def get_total_price(self) -> float:
        return self.total_price

    def assign_flights(self) -> None:
        for i in range(len(self.flights.flights), len(self.destinations)):
            f1 = Flight(str(i), self.destinations[i], self.passengers, i+1)
            self.flights.flights.append(f1)

    def add_destination(self, destination: str) -> None:
        self.destinations.append(destination)
        self.assign_flights()
        self.recalculate_price()

    def remove_destination(self, destination: str) -> None:
        self.destinations.remove(destination)
        for i, flight in enumerate(self.flights.flights):
            if flight.get_destination() == destination:
                self.flights.flights.pop(i)
        self.recalculate_price()

    def recalculate_price(self) -> None:
        price = 0.0
        for flight in self.flights.flights:
            price += flight.get_price() * flight.get_passengers()
        self.total_price = price