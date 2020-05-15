import unittest
from Skyscanner import*


#[V1] Confirmar la reserva de los vuelos seleccionados (sin considerar errores)

class TestCase(unittest.TestCase):
    def setupClass(self):
        self.confirm = Skyscanner()

    def test_confirm_reserve(self):
        user = User
        flight = Flights
        respuesta = self.confirm.confirm_reserve(user, flight)

        self.assertEqual(respuesta, False)


if __name__ == '__main__':
    unittest.main()
