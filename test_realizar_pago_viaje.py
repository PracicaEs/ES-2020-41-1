import unittest
import Bank
import User
import PaymentData

# [V1]Realizar el pago de un viaje (sin considerar errores y sin necesidad de seleccionar el método de pago)

class MyTestCase(unittest.TestCase):
    def test_realizar_pago_viaje(self):
        banco = Bank()
        usuario = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaaaaaaaaa@aaaaaaaaaaa.aaa")
        datos_pago = PaymentData()

        res = banco.do_payment(usuario, datos_pago)
        self.assertEqual(True, res)


if __name__ == '__main__':
    unittest.main()
