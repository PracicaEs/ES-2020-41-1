import unittest
from src.Travel import *
from src.User import *
from src.Car import *


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
        t = Travel(destinations, user, passengers)
        price_car1 = 30
        dies_reserva = 2
        car1 = Car("1212AAAA", "Ferrari", "BCN", dies_reserva, price_car1)
        t.add_car(car1)
        total_price = (6*passengers)+(price_car1*dies_reserva)
        self.assertEqual(total_price, t.get_total_price())

    def test_delete_hotel(self):
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


if __name__ == '__main__':
    unittest.main()

#Dado un viaje con más de un viajero, cuando se añaden vehículos, el precio del viaje es el esperado
#Dado un viaje con más de un viajero, cuando se quitan vehículos, el precio del viaje es el esperado
#Dado un viaje con más de un viajero, cuando se añaden alojamientos, el precio del viaje es el esperado
#Dado un viaje con más de un viajero, cuando se quitan alojamientos, el precio del viaje es el esperado
