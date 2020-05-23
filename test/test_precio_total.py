import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("Aitor Tilla", "22222222A", "08666", 666666666, "aaa@aaa.aaa")
        self.destinations = ["BCN", "MIL", "LON"]
        self.passengers = 5
        self.t = Travel(self.destinations, self.user, self.passengers)
        self.car1 = Car("1212AAAA", "Ferrari", "BCN", 2, 30)
        self.car2 = Car("1313AAAA", "Bugatti", "MIL", 2, 50)
        self.hotel1 = Hotel("1A1A1", "BCN Resort", self.passengers, 3, 2, 100)
        self.hotel2 = Hotel("2A2A2", "MIL Resort", self.passengers, 2, 1, 85)

    def test_add_car(self):
        self.t.add_car(self.car1)
        total_price = (6*self.passengers)+(self.car1.preu_dia * self.car1.dies_reserva)
        self.assertEqual(total_price, self.t.total_price)

    def test_delete_car(self):
        self.t.add_car(self.car1)
        self.t.add_car(self.car2)
        self.t.remove_car(self.car1.codi)
        total_price = (6*self.passengers)+(self.car2.preu_dia*self.car2.dies_reserva)
        self.assertEqual(total_price, self.t.total_price)

    def test_add_hotel(self):
        self.t.add_hotel(self.hotel1)
        total_price = (6*self.passengers)+(self.hotel1.dies_reserva * self.hotel1.preu_dia * self.hotel1.num_hab)
        self.assertEqual(total_price, self.t.total_price)

    def test_delete_hotel(self):
        self.t.add_hotel(self.hotel1)
        self.t.add_hotel(self.hotel2)
        self.t.remove_hotel(self.hotel1.codi)
        total_price = (6 * self.passengers) + (self.hotel2.dies_reserva * self.hotel2.preu_dia * self.hotel2.num_hab)
        self.assertEqual(total_price, self.t.total_price)

    def test_all_together(self):
        self.t.add_hotel(self.hotel1)
        self.t.add_car(self.car1)
        self.t.add_car(self.car2)
        total_price = (6 * self.passengers) + (self.hotel1.dies_reserva * self.hotel1.preu_dia * self.hotel1.num_hab) \
                      + (self.car2.preu_dia*self.car2.dies_reserva) +(self.car1.preu_dia * self.car1.dies_reserva)
        self.assertEqual(total_price, self.t.total_price)


if __name__ == '__main__':
    unittest.main()
