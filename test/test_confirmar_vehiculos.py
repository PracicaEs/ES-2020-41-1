import unittest
from src.Rentalcars import *
from src.Travel import *


class TestCase(unittest.TestCase):
    def test_add_vehicles(self):
        cars = Rentalcars()
        user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1)
        car2 = Car("2222BBBB", "Lamborgini", "LON", 5, 2)
        car3 = Car("3333CCCC", "Ferrari", "NAP", 6, 3)
        t.add_car(car1)
        t.add_car(car2)
        t.add_car(car3)
        expected = [car1, car2, car3]
        self.assertEqual(t.cars.cars, expected)

    def test_remove_vehicles(self):
        cars = Rentalcars()
        user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1)
        car2 = Car("2222BBBB", "Lamborgini", "LON", 5, 2)
        car3 = Car("3333CCCC", "Ferrari", "NAP", 6, 3)
        t.cars.cars = [car1, car2, car3]
        t.remove_car(car2.codi)
        expected = [car1, car3]
        self.assertEqual(t.cars.cars, expected)

    def test_confirm_reserve(self):
        cars = Rentalcars()
        user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1)
        car2 = Car("2222BBBB", "Lamborgini", "LON", 5, 2)
        car3 = Car("3333CCCC", "Ferrari", "NAP", 6, 3)
        t.add_car(car1)
        t.add_car(car2)
        t.add_car(car3)
        answer = cars.confirm_reserve(user, t.cars)
        self.assertEqual(answer, True)
        print("La reserva se ha efectuado correctamente")

    def test_error_confirm_reserve(self):
        def confirm_reserve(user: User, cars: Cars) -> bool:
            print("Error en la confirmación de la reserva de los vuelos")
            return False

        cars = Rentalcars()
        cars.confirm_reserve = confirm_reserve
        user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1)
        car2 = Car("2222BBBB", "Lamborgini", "LON", 5, 2)
        car3 = Car("3333CCCC", "Ferrari", "NAP", 6, 3)
        t.add_car(car1)
        t.add_car(car2)
        t.add_car(car3)
        answer = cars.confirm_reserve(user, t.cars)
        self.assertEqual(answer, False)

    def test_retry_confirm_reserve_hotels_correct(self):
        cars = Rentalcars()
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        expected = "La reserva de los alojamientos se ha efectuado correctamente"
        answer = t.confirm_reserve_hotels(cars)
        self.assertEqual(answer, expected)

    def test_retry_confirm_reserve_limit_of_retries_overcomed(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación de la reserva de los hoteles")
            return False
        cars = Rentalcars()
        cars.confirm_reserve = confirm_reserve
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        expected = "Error en la confirmación de la reserva de los alojamientos"
        answer = t.confirm_reserve_hotels(cars)
        self.assertEqual(answer, expected)

