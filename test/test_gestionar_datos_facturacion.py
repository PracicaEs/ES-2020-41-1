import unittest
from src.PaymentData import *
from src.Travel import *


class TestCase(unittest.TestCase):
    def test_payment_data(self):
        passengers = 2
        destinations = ["BCN", "PEK", "ROM"]
        user = User("Agapito Pelaez Snachez", "1", 2, 3, "aaaa@baaaa.caa")
        t = Travel(destinations, user, passengers)
        payment_data = PaymentData("VISA", "Elsa Patico", 123, 150)
        res = t.confirm_data(payment_data)
        self.assertEqual("Datos correctos", res)

    def test_incorrect_payment_data(self):
        passengers = 2
        destinations = ["BCN", "PEK", "ROM"]
        user = User("Agapito Pelaez Snachez", "1", 2, 3, "aaaa@baaaa.caa")
        t = Travel(destinations, user, passengers)
        payment_data = PaymentData("Randomcard", "Elsa Patico", 123, 150)
        res = t.confirm_data(payment_data)
        self.assertEqual("Datos incorrectos", res)