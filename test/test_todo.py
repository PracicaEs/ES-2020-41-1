import unittest.mock
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        self.destinations = ["BCN", "ROM", "MAD"]
        self.passengers = 5
        self.t = Travel(self.destinations, self.user, self.passengers)
        self.hotel1 = Hotel("1234", "Vela", "BCN", self.passengers, 3, 2, 1)
        self.hotel2 = Hotel("1235", "Vela1", "ROM", self.passengers, 2, 2, 2)
        self.hotel3 = Hotel("1236", "Vela2", "MAD", self.passengers, 1, 1, 3)
        self.t.add_hotel(self.hotel1)
        self.t.add_hotel(self.hotel2)
        self.t.add_hotel(self.hotel3)
        self.car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1, 4)
        self.car2 = Car("2222AAAA", "Bugatti", "BCN", 2, 1, 1)
        self.car3 = Car("2222BBBB", "Lamborghini", "ROM", 5, 2, self.passengers)
        self.car4 = Car("3333CCCC", "Ferrari", "MAD", 6, 3, self.passengers)
        self.t.add_car(self.car1)
        self.t.add_car(self.car2)
        self.t.add_car(self.car3)
        self.t.add_car(self.car4)

    def test_prueba(self):
        expected = (6 * self.passengers) + \
                   (self.hotel1.preu_total * self.hotel1.dies_reserva) + \
                   (self.hotel2.preu_total * self.hotel2.dies_reserva) + \
                   (self.car1.dies_reserva * self.car1.preu_dia) + \
                   (self.car2.dies_reserva * self.car2.preu_dia)

        returned = self.t.calculate_total_no_IVA()

        self.assertEqual(expected, returned)
