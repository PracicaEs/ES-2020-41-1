import unittest.mock
from src.Skyscanner import *
from src.Travel import *


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        self.destinations = ["BCN", "ROM", "PEK"]
        self.passengers = 3
        self.t = Travel(self.destinations, self.user, self.passengers)

    def test_confirm_reserve(self):
        expected = "La reserva de los vuelos se ha efectuado correctamente"
        answer = self.t.confirm_reserve_flights()
        self.assertEqual(answer, expected)

    @unittest.mock.patch('src.Travel.Skyscanner')
    def test_error_confirm_reserve(self, m):
        expected = "No se ha podido realizar la reserva"
        m.return_value.confirm_reserve.return_value = False
        answer = self.t.confirm_reserve_flights()
        self.assertEqual(answer, expected)

    def test_retry_confirm_reserve_flights_correct(self):
        expected = "La reserva de los vuelos se ha efectuado correctamente"
        answer = self.t.confirm_reserve_flights()
        self.assertEqual(answer, expected)

    @unittest.mock.patch('src.Travel.Skyscanner')
    def test_retry_confirm_reserve_flights_limit_of_retries_overcomed(self, m):
        expected = "No se ha podido realizar la reserva"
        m.return_value.confirm_reserve.return_value = False
        answer = self.t.confirm_reserve_flights()
        self.assertEqual(answer, expected)
