import unittest
from Bank import*
from User import*

# [V1]Realizar el pago de un viaje (sin considerar errores y sin necesidad de seleccionar el método de pago)

class MyTestCase(unittest.TestCase):
    def test_realizar_pago_viaje(self):
        banco = Bank()
        usuario = User()


        res = banco.do_payment(usuario, datos_pago)
        self.assertEqual(True, res)


if __name__ == '__main__':
    unittest.main()
