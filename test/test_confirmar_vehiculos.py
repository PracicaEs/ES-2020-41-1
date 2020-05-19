import unittest
from src.Rentalcars import *


class TestCase(unittest.TestCase):

    def test_confirm_reserve(self):
        cars = Rentalcars()
        user = User("Guillermo Boreal", "333666999A", 08666, 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        answer = cars.confirm_reserve(user, t.get_flights())
        self.assertEqual(answer, True)

    def test_error_confirm_reserve(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación de la reserva")
            return False

        cars = Rentalcars()
        cars.confirm_reserve = confirm_reserve
        user = User("Guillermo Boreal", "333666999A", 08666, 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        answer = cars.confirm_reserve(user, t.get_flights())
        self.assertEqual(answer, False)


    def test_retry_confirm_reserve(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación de la reserva")
            return False

        sky = Skyscanner()
        sky.confirm_reserve = confirm_reserve
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        respuesta = sky.confirm_reserve(user, t.get_flights())



if __name__ == '__main__':
    unittest.main()
