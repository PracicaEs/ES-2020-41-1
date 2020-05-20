import unittest
from src.Hotel import *
from src.Travel import *
from src.Booking import *
from src.User import *


class MyTestCase(unittest.TestCase):

    def test_gestionar_alojamientos(self):
        hotels = Booking()
        user = User("Kerry", "12345A", 123, 123456789, "abc@abc.abc")
        destinations = ["BCN", "ROM", "MAD"]
        passengers = 3
        t = Travel(destinations, user, passengers)
        hotel1 = Hotel("1234", "Vela", passengers, 2, 2)
        hotel2 = Hotel("1235", "Vela1", passengers, 2, 2)
        hotel3 = Hotel("1236", "Vela2", passengers, 2, 2)
        t.hotels = [hotel1, hotel2, hotel3]
        self.assertEqual(hotel1, t.hotels[0])
        self.assertEqual(hotel2, t.hotels[1])
        self.assertEqual(hotel3, t.hotels[2])






