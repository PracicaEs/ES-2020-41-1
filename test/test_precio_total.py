import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_add_car(self):
        user = User("Aitor Tilla", "22222222A", "08666", 666666666, "aaa@aaa.aaa")
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        price_car1 = 30
        dies_reserva = 2
        car1 = Car("1212AAAA", "Ferrari", "BCN", dies_reserva, price_car1)
        t.add_car(car1)
        total_price = (6*passengers)+(price_car1*dies_reserva)
        self.assertEqual(total_price, t.get_total_price())

    def test_delete_car(self):
        user = User("Aitor Tilla", "22222222A", "08666", 666666666, "aaa@aaa.aaa")
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        price_car1 = 30
        price_car2 = 50
        dies_reserva = 2
        car1 = Car("1212AAAA", "Ferrari", "BCN", dies_reserva, price_car1)
        car2 = Car("1313AAAA", "Bugatti", "MIL", dies_reserva, price_car2)
        t.add_car(car1)
        t.add_car(car2)
        t.remove_car("1212AAAA")
        total_price = (6*passengers)+(price_car2*dies_reserva)
        self.assertEqual(total_price, t.get_total_price())

    def test_add_hotel(self):
        user = User("Aitor Tilla", "22222222A", "08666", 666666666, "aaa@aaa.aaa")
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        habs = 3
        dias = 2
        hotel = Hotel("1A1A1","BCN Resort",passengers,habs,dias,100)
        t = Travel(destinations, user, passengers)
        t.add_hotel(hotel)
        total_price = (6*passengers)+(100*habs*dias)
        self.assertEqual(total_price, t.get_total_price())

    def test_delete_hotel(self):
        user = User("Aitor Tilla", "22222222A", "08666", 666666666, "aaa@aaa.aaa")
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        hotel1 = Hotel("1A1A1", "BCN Resort", passengers, 3, 2, 100)
        hotel2 = Hotel("2A2A2", "MIL Resort", passengers, 2, 1, 85)
        t = Travel(destinations, user, passengers)
        t.add_hotel(hotel1)
        t.add_hotel(hotel2)
        t.remove_hotel(hotel1.codi)
        total_price = (6 * passengers) + (85 * 2 * 1)
        self.assertEqual(total_price, t.get_total_price())

    def test_all_together(self):
        user = User("Aitor Tilla", "22222222A", "08666", 666666666, "aaa@aaa.aaa")
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        habs = 3
        dias = 2
        hotel = Hotel("1A1A1", "BCN Resort", passengers, habs, dias, 100)
        t = Travel(destinations, user, passengers)
        t.add_hotel(hotel)
        price_car1 = 30
        price_car2 = 50
        dies_reserva = 2
        car1 = Car("1212AAAA", "Ferrari", "BCN", dies_reserva, price_car1)
        car2 = Car("1313AAAA", "Bugatti", "MIL", dies_reserva, price_car2)
        t.add_car(car1)
        t.add_car(car2)
        total_price = (6 * passengers) + (100 * habs * dias)+(price_car1*dies_reserva)+(price_car2*dies_reserva)
        self.assertEqual(total_price, t.get_total_price())


if __name__ == '__main__':
    unittest.main()
