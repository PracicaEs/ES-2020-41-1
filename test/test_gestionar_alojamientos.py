import unittest
from src.Booking import *
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_add_hotels(self):
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

    def test_remove_hotels(self):
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
        t.remove_hotel(hotel3.codi)
        expected = [hotel1, hotel2]
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

    def test_retry_confirm_reserve_hotels_correct(self):
        hotels = Booking()
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        expected = "La reserva de los alojamientos se ha efectuado correctamente"
        answer = t.confirm_reserve_hotels(hotels)
        self.assertEqual(answer, expected)

    def test_retry_confirm_reserve_limit_of_retries_overcomed(self):
        def confirm_reserve(user: User, flights: Flights) -> bool:
            print("Error en la confirmación de la reserva de los hoteles")
            return False
        hotels = Booking()
        hotels.confirm_reserve = confirm_reserve
        user = User("Kerry", "12345A", "123", 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        expected = "Error en la confirmación de la reserva de los alojamientos"
        answer = t.confirm_reserve_hotels(hotels)
        self.assertEqual(answer, expected)
