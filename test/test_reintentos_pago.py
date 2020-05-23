import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_pay_succeed(self):
        user = User("A", "1", 2, 3, "a@b.c")
        payment_data = PaymentData("Visa", "A", "123", 150)
        destinations = ["BCN", "MIL", "LON"]
        passengers = 5
        t = Travel(destinations, user, passengers)

        returned = t.confirmar_pago(user, payment_data)
        expected = "Process has succeed"
        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()
