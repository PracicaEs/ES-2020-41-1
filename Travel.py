from Skyscanner import *
from Booking import *
from Rentalcars import *
from Bank import *
from random import *

class Travel:
    def __init__(self, destinations: list, user: User, cars: Cars, hotels: Hotels, passengers: int):
        self.destinations = destinations
        self.passengers = passengers
        self.flights = []
        self.flights_price = 0.0
        self.cars = cars
        self.cars_price = 0.0
        self.hotels = hotels
        self.hotels_price = 0.0
        self.user = user

    def add_destination(self, destination):
        self.destinations.append(destination)
        code = len(destination)
        f1 = Flight(str(code), destination, self.passengers, randint(20, 100))
        self.flights.append(f1)

    def remove_destination(self, destination):
        self.destinations.remove(destination)
