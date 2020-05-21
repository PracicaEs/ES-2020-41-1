import unittest
from src.Booking import *
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_gestionar_alojamientos(self):
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        hotel1 = Hotel("1234", "Vela", passengers, 2, 2, 1)
        hotel2 = Hotel("1235", "Vela1", passengers, 2, 2, 2)
        hotel3 = Hotel("1236", "Vela2", passengers, 2, 2, 3)
        t.add_hotel(hotel1)
        t.add_hotel(hotel2)
        t.add_hotel(hotel3)
        expected = [hotel1, hotel2, hotel3]
        self.assertEqual(expected, t.hotels.hotels)

    def test_confirm_reserve(self):
        hotels = Booking()
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        hotel1 = Hotel("1234", "Vela", passengers, 2, 2, 1)
        hotel2 = Hotel("1235", "Vela1", passengers, 2, 2, 2)
        hotel3 = Hotel("1236", "Vela2", passengers, 2, 2, 3)
        t.add_hotel(hotel1)
        t.add_hotel(hotel2)
        t.add_hotel(hotel3)
        x = hotels.confirm_reserve(user, t.hotels)
        self.assertEqual(x, True)
        print("La reserva se ha efectuado correctamente")

    def test_error_confirm_reserve(self):
        def confirm_reserve(user: User, cars: Cars) -> bool:
            print("Error en la confirmación de la reserva")
            return False

        hotels = Booking()
        hotels.confirm_reserve = confirm_reserve
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        hotel1 = Hotel("1234", "Vela", passengers, 2, 2, 1)
        hotel2 = Hotel("1235", "Vela1", passengers, 2, 2, 2)
        hotel3 = Hotel("1236", "Vela2", passengers, 2, 2, 3)
        t.add_hotel(hotel1)
        t.add_hotel(hotel2)
        t.add_hotel(hotel3)
        x = hotels.confirm_reserve(user, t.hotels)
        self.assertEqual(x, False)
