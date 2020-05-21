from src.User import *
from src.Cars import *
from src.Car import *
from src.Flights import *
from src.Flight import *
from src.Hotels import *
from src.Hotel import *
from src.Skyscanner import *

class Travel:
    def __init__(self, destinations: list, user: User, passengers: int):
        self.destinations = destinations
        self.passengers = passengers
        self.flights = Flights([])
        self.cars = Cars([])
        self.hotels = Hotels([])
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

    def add_car(self, car: Car) -> None:
        self.cars.cars.append(car)
        self.recalculate_price()

    def remove_car(self, codi: str) -> None:
        pos = 0
        for i, c in enumerate(self.cars.cars):
            if c.codi == codi:
                pos = i
        self.cars.cars.pop(pos)
        self.recalculate_price()

    def add_hotel(self, hotel: Hotel) -> None:
        self.hotels.hotels.append(hotel)
        self.recalculate_price()

    def remove_hotel(self, codi: str) -> None:
        pos = 0
        for i, c in enumerate(self.hotels.hotels):
            if c.codi == codi:
                pos = i
        self.hotels.hotels.pop(pos)
        self.recalculate_price()

    def recalculate_price(self) -> None:
        price = 0.0
        for flight in self.flights.flights:
            price += (flight.get_price() * flight.get_passengers())
        for car in self.cars.cars:
            price += (car.preu_dia * car.dies_reserva)
        for hotel in self.hotels.hotels:
            price += (hotel.preu_dia * hotel.num_hab * hotel.dies_reserva)
        self.total_price = price

    def confirm_reserve(self, sky: Skyscanner) -> str:
        retries = 0
        ok = False
        message = ""
        while retries < 3 and not ok:
            retries += 1
            if sky.confirm_reserve(self.user, self.flights):
                ok = True
                message = "La reserva se ha efectuado correctamente"
        if retries == 3 and ok == False:
            message = "Error en la confirmación de la reserva"
        return message







