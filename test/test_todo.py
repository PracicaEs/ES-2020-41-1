import unittest.mock
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        self.destinations = ["BCN", "ROM", "MAD"]
        self.passengers = 3
        self.t = Travel(self.destinations, self.user, self.passengers)
        self.hotel1 = Hotel("1234", "Vela", "BCN", self.passengers, 2, 2, 1)
        self.hotel2 = Hotel("1235", "Vela1", "ROM", self.passengers, 2, 2, 2)
        self.hotel3 = Hotel("1236", "Vela2", "MAD", self.passengers, 2, 2, 3)
        self.t.add_hotel(self.hotel1)
        self.t.add_hotel(self.hotel2)
        self.t.add_hotel(self.hotel3)
        self.car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1)
        self.car2 = Car("2222BBBB", "Lamborghini", "ROM", 5, 2)
        self.car3 = Car("3333CCCC", "Ferrari", "MAD", 6, 3)
        self.t.add_car(self.car1)
        self.t.add_car(self.car2)
        self.t.add_car(self.car3)
        self.cars = Rentalcars()

    def test_prueba(self):
        preu_coche1 = 0.0
        preu_coche2 = 0.0
        preu_coche3 = 0.0
        preu_coche1 = self.t.calculate_price_cars(self.destinations[0])
        preu_coche2 = self.t.calculate_price_cars(self.destinations[1])
        preu_coche3 = self.t.calculate_price_cars(self.destinations[2])
        self.assertEqual((self.car1.preu_dia*self.car1.dies_reserva), preu_coche1)
        self.assertEqual((self.car2.preu_dia*self.car2.dies_reserva), preu_coche2)
        self.assertEqual((self.car3.preu_dia*self.car3.dies_reserva), preu_coche3)
        preu_hotel1 = 0.0
        preu_hotel2 = 0.0
        preu_hotel3 = 0.0
        preu_hotel1 = self.t.calculate_price_hotels(self.destinations[0])
        preu_hotel2 = self.t.calculate_price_hotels(self.destinations[1])
        preu_hotel3 = self.t.calculate_price_hotels(self.destinations[2])
        self.assertEqual((self.hotel1.preu_total * self.hotel1.dies_reserva), preu_hotel1)
        self.assertEqual((self.hotel2.preu_total * self.hotel2.dies_reserva), preu_hotel2)
        self.assertEqual((self.hotel3.preu_total * self.hotel3.dies_reserva), preu_hotel3)
        preu_vol1 = 0.0
        preu_vol2 = 0.0
        preu_vol3 = 0.0
        preu_vol1 = self.t.calculate_price_flights(self.destinations[0])
        preu_vol2 = self.t.calculate_price_flights(self.destinations[1])
        preu_vol3 = self.t.calculate_price_flights(self.destinations[2])
        self.assertEqual(self.t.flights.flights[0].price * self.t.flights.flights[0].passengers, preu_vol1)
        self.assertEqual(self.t.flights.flights[1].price * self.t.flights.flights[1].passengers, preu_vol2)
        self.assertEqual(self.t.flights.flights[2].price * self.t.flights.flights[2].passengers, preu_vol3)
        iva = 0.21
        self.assertEqual(iva, self.t.IVA_percent())
        preu_destination_BCN = 0.0
        preu_destination_MAD = 0.0
        preu_destination_ROM = 0.0
        preu_destination_BCN = self.t.calculate_price_destination(self.destinations[0])
        preu_destination_ROM = self.t.calculate_price_destination(self.destinations[1])
        preu_destination_MAD = self.t.calculate_price_destination(self.destinations[2])
        self.assertEqual(preu_hotel1 + preu_coche1 + preu_vol1, preu_destination_BCN)
        self.assertEqual(preu_hotel2 + preu_coche2 + preu_vol2, preu_destination_ROM)
        self.assertEqual(preu_hotel3 + preu_coche3 + preu_vol3, preu_destination_MAD)
        total_no_iva = self.t.calculate_total_no_IVA()
        self.assertEqual(preu_destination_BCN + preu_destination_ROM + preu_destination_MAD, total_no_iva)
        porcentage_del_total_iva = self.t.calculate_IVA_price()
        self.assertEqual(total_no_iva * iva, porcentage_del_total_iva)
        total = self.t.calculate_total()
        self.assertEqual(total_no_iva * iva + total_no_iva, total)


