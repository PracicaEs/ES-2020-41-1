import unittest
from src.Travel import *


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.passengers = 2
        self.destinations = ["BCN", "PEK", "ROM"]
        self.user = User("Agapito Pelaez Snachez", "1", 2, 3, "aaaa@baaaa.caa")
        self.t = Travel(self.destinations, self.user, self.passengers)

    def test_payment_data(self):
        payment_data = PaymentData("VISA", "Elsa Patico", 123, 150)
        res = self.t.confirm_data(payment_data)
        self.assertEqual("Datos correctos", res)

    def test_incorrect_payment_data(self):
        payment_data = PaymentData("Randomcard", "Elsa Patico", 123, 150)
        res = self.t.confirm_data(payment_data)
        self.assertEqual("Datos incorrectos", res)
