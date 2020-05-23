import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_do_payment(self):
        bank = Bank()
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        payment_data = PaymentData("Visa", "Agapito Pelaez Sanchez", 123, 999)
        res = bank.do_payment(user, payment_data)
        self.assertEqual(True, res)

    def test_error_payment(self):
        def do_payment(a: User, b: PaymentData):
            print("Error al realizar el pago")
            return False

        bank = Bank()
        bank.do_payment = do_payment
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        payment_data = PaymentData("Visa", "Agapito Pelaez Sanchez", 123, 999)
        res = bank.do_payment(user, payment_data)
        self.assertEqual(False, res)

    def test_gestionar_metodo_pago(self):
        def do_payment(a: User, b: PaymentData):
            print ("Pago realizado con ", b.tipo_tarjeta)
            return b.tipo_tarjeta

        passengers = 2
        destinations = ["BCN", "PEK", "ROM"]
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        bank = Bank()
        bank.do_payment = do_payment
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        payment_data = PaymentData("Visa", "Agapito Pelaez Sanchez", 123, 999)
        res = bank.do_payment(user, payment_data)
        self.assertEqual("Visa", res)


if __name__ == '__main__':
    unittest.main()
