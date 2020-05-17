import unittest
from Travel import *


# [V1] Confirmar la reserva de los vuelos seleccionados (sin considerar errores)

class TestCase(unittest.TestCase):

    def test_confirm_reserve(self):
        sky = Skyscanner()
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        respuesta = sky.confirm_reserve(user, t.get_flights())
        self.assertEqual(respuesta, True)

    def test_error_confirm_reserve(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación del pago")
            return False

        sky = Skyscanner()
        sky.confirm_reserve = confirm_reserve
        user = User("Agapito Pelaez Sanchez", "123456789A", 123456789, 123456789, "aaa@aaa.aaa")
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        respuesta = sky.confirm_reserve(user, t.get_flights())
        self.assertEqual(respuesta, False)


if __name__ == '__main__':
    unittest.main()
