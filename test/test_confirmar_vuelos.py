import unittest
from src.Skyscanner import *
from src.Travel import *


class TestCase(unittest.TestCase):

    def test_confirm_reserve(self):
        sky = Skyscanner()
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        answer = sky.confirm_reserve(user, t.flights)
        self.assertEqual(answer, True)
        print("La reserva se ha efectuado correctamente")

    def test_error_confirm_reserve(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación de la reserva")
            return False

        sky = Skyscanner()
        sky.confirm_reserve = confirm_reserve
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        answer = sky.confirm_reserve(user, t.flights)
        self.assertEqual(answer, False)

    def test_retry_confirm_reserve_flights_correct(self):
        sky = Skyscanner()
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        expected = "La reserva de los vuelos se ha efectuado correctamente"
        answer = t.confirm_reserve_flights(sky)
        self.assertEqual(answer, expected)

    def test_retry_confirm_reserve_flights_limit_of_retries_overcomed(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación de la reserva")
            return False
        sky = Skyscanner()
        sky.confirm_reserve = confirm_reserve
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        expected = "Error en la confirmación de la reserva de los vuelos"
        answer = t.confirm_reserve_flights(sky)
        self.assertEqual(answer, expected)
