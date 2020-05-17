import unittest
from Bank import *
from User import *
from PaymentData import *

# [V1]Realizar el pago de un viaje (sin considerar errores y sin necesidad de seleccionar el método de pago)


class MyTestCase(unittest.TestCase):
    def test_do_payment(self):

        bank = Bank()
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        payment_data = PaymentData()
        res = bank.do_payment(user, payment_data)
        self.assertEqual(True, res)
        print("Pago realizado con éxito")


    def test_error_payment(self):
        def do_payment(a: User, b: PaymentData):
            return False

        bank = Bank()
        bank.do_payment = do_payment
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        payment_data = PaymentData()
        res = bank.do_payment(user, payment_data)
        self.assertEqual(False, res)
        print("Error al realizar el pago")


if __name__ == '__main__':
    unittest.main()
