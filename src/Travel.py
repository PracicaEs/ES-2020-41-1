from src.Car import *
from src.Bank import *
from src.Hotel import *
from src.Flight import *
from src.Booking import *
from src.Rentalcars import *
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
        self.total_price_destination = {}
        self.user = user
        self.IVA = 0.21
        self.total_price_no_IVA = 0.0
        self.IVA_price = 0.0

    def assign_flights(self) -> None:
        for i in range(len(self.flights.flights), len(self.destinations)):
            f1 = Flight(str(i), self.destinations[i], self.passengers, i + 1)
            self.flights.flights.append(f1)

    def add_destination(self, destination: str) -> None:
        self.destinations.append(destination)
        self.assign_flights()

    def remove_destination(self, destination: str) -> None:
        self.destinations.remove(destination)
        for i, flight in enumerate(self.flights.flights):
            if flight.destination == destination:
                self.flights.flights.pop(i)

    def add_car(self, car: Car) -> None:
        if car.ocupants <= 4:
            self.cars.cars.append(car)

    def remove_car(self, codi: str) -> None:
        pos = 0
        for i, c in enumerate(self.cars.cars):
            if c.codi == codi:
                pos = i
        self.cars.cars.pop(pos)

    def add_hotel(self, hotel: Hotel) -> None:
        if self.passengers/hotel.num_hab <= 3:
            self.hotels.hotels.append(hotel)

    def remove_hotel(self, codi: str) -> None:
        pos = 0
        for i, c in enumerate(self.hotels.hotels):
            if c.codi == codi:
                pos = i
        self.hotels.hotels.pop(pos)

    def calculate_price_flights(self, destination):
        price = 0.0
        for flight in self.flights.flights:
            if flight.destination == destination:
                price += (flight.price * flight.passengers)
        return price

    def calculate_price_cars(self, destination):
        price = 0.0
        for car in self.cars.cars:
            if car.lloc_recollida == destination:
                price += (car.preu_dia * car.dies_reserva)
        return price

    def calculate_price_hotels(self, destination):
        price = 0.0
        for hotel in self.hotels.hotels:
            if hotel.ciutat == destination:
                price += (hotel.preu_total * hotel.dies_reserva)
        return price

    def calculate_price_destination(self, destination):
        self.total_price_destination[destination] = self.calculate_price_cars(destination) + self.calculate_price_hotels(
            destination) + self.calculate_price_flights(destination)
        return self.total_price_destination[destination]

    def calculate_total_no_IVA(self):
        for destination in self.destinations:
            self.total_price_no_IVA += (self.calculate_price_destination(destination))
        return self.total_price_no_IVA

    def calculate_IVA_price(self):
        self.IVA_price = self.IVA * self.calculate_total_no_IVA()
        return self.IVA_price

    def calculate_total(self):
        self.total_price = self.calculate_IVA_price() + self.calculate_total_no_IVA()
        return self.total_price

    def confirm_reserve_flights(self) -> str:
        retries = 0
        ok = False
        message = ""
        sky = Skyscanner()
        while retries < 3 and not ok:
            retries += 1
            if sky.confirm_reserve(self.user, self.flights):
                ok = True
                message = "La reserva de los vuelos se ha efectuado correctamente"
        if retries == 3 and ok is False:
            message = "No se ha podido realizar la reserva"
        return message

    def confirm_reserve_cars(self) -> str:
        retries = 0
        ok = False
        message = ""
        r = Rentalcars()
        while retries < 3 and not ok:
            retries += 1
            if r.confirm_reserve(self.user, self.cars):
                ok = True
                message = "La reserva de los vehiculos se ha efectuado correctamente"
        if retries == 3 and ok is False:
            message = "No se ha podido realizar la reserva"
        return message

    def confirm_reserve_hotels(self) -> str:
        retries = 0
        ok = False
        message = ""
        hotel = Booking()
        while retries < 3 and not ok:
            retries += 1
            if hotel.confirm_reserve(self.user, self.hotels):
                ok = True
                message = "La reserva de los alojamientos se ha efectuado correctamente"
        if retries == 3 and ok is False:
            message = "No se ha podido realizar la reserva"
        return message

    def confirmar_pago(self, user: User, payment_data: PaymentData):
        tries = 1
        valid = False
        b = Bank()
        while (valid is False) or (tries <= 3):
            valid = b.do_payment(user, payment_data)
            tries += 1
        if valid is False:
            return "Process has failed"
        else:
            return "Process has succeed"

    def confirm_data(self, payment_data: PaymentData) -> str:
        correct = True
        if payment_data.tipo_tarjeta != "VISA" and payment_data.tipo_tarjeta != "MasterCard":
            correct = False
        elif payment_data.codigo_seg < 0 or payment_data.codigo_seg > 999:
            correct = False
        elif len(payment_data.nom_titular) < 5:
            correct = False

        if correct:
            m_correct = "Datos correctos"
        else:
            m_correct = "Datos incorrectos"
        return m_correct
