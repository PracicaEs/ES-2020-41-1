import unittest.mock
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        self.destinations = ["BCN", "ROM", "MAD"]
        self.passengers = 3
        self.t = Travel(self.destinations, self.user, self.passengers)
        self.hotel1 = Hotel("1234", "Vela", self.passengers, 2, 2, 1)
        self.hotel2 = Hotel("1235", "Vela1", self.passengers, 2, 2, 2)
        self.hotel3 = Hotel("1236", "Vela2", self.passengers, 2, 2, 3)
        self.t.add_hotel(self.hotel1)
        self.t.add_hotel(self.hotel2)
        self.t.add_hotel(self.hotel3)

    def test_add_hotels(self):
        expected = [self.hotel1, self.hotel2, self.hotel3]
        self.assertEqual(expected, self.t.hotels.hotels)

    def test_remove_hotels(self):
        self.t.remove_hotel(self.hotel3.codi)
        expected = [self.hotel1, self.hotel2]
        self.assertEqual(expected, self.t.hotels.hotels)

    def test_confirm_reserve(self):
        expected = "La reserva de los alojamientos se ha efectuado correctamente"
        returned = self.t.confirm_reserve_hotels()
        self.assertEqual(expected, returned)

    @unittest.mock.patch('src.Travel.Booking')
    def test_error_confirm_reserve(self, m):
        expected = "No se ha podido realizar la reserva"
        m.return_value.confirm_reserve.return_value = False
        returned = self.t.confirm_reserve_hotels()
        self.assertEqual(expected, returned)

    def test_retry_confirm_reserve_hotels_correct(self):
        expected = "La reserva de los alojamientos se ha efectuado correctamente"
        returned = self.t.confirm_reserve_hotels()
        self.assertEqual(expected, returned)

    @unittest.mock.patch('src.Travel.Booking')
    def test_retry_confirm_reserve_limit_of_retries_overcomed(self, m):
        expected = "No se ha podido realizar la reserva"
        m.return_value.confirm_reserve.return_value = False
        returned = self.t.confirm_reserve_hotels()
        self.assertEqual(expected, returned)
