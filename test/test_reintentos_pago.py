import unittest
from src.User import *
from src.PaymentData import *
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_pay_succed(self):
        resposta = "Process has succed"
        user = User("A", "1", 2, 3, "a@b.c")
        payment_data = PaymentData("Visa", "A", "123", 150)
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        devolucion = t.confirmar_pago(user, payment_data)
        self.assertEqual(devolucion, resposta)


if __name__ == '__main__':
    unittest.main()
