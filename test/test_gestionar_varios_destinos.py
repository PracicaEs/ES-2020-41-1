import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.passengers = 2
        self.destinations = []
        self.user = User("A", "1", 2, 3, "a@b.c")
        self.t = Travel(self.destinations, self.user, self.passengers)

    def test_no_destinations(self):
        expected = []
        self.assertEqual(expected, self.t.destinations)

    def test_no_destinations_flights(self):
        expected = []
        self.assertEqual(expected, self.t.flights.flights)

    def test_add_destinations(self):
        expected = ["BCN"]
        self.t.add_destination("BCN")
        self.assertEqual(expected, self.t.destinations)

    def test_add_destinations_flights(self):
        expected = ["BCN"]
        self.t.add_destination("BCN")
        returned = [flight.destination for flight in self.t.flights.flights]
        self.assertEqual(expected, returned)

    def test_remove_multiples_destinations(self):
        self.t.add_destination("BCN")
        self.t.add_destination("PEK")
        self.t.add_destination("ROM")
        self.t.add_destination("ARM")

        self.t.remove_destination("BCN")
        self.t.remove_destination("ROM")

        expected = ["PEK", "ARM"]
        self.assertEqual(expected, self.t.destinations)

    def test_remove_multiples_destinations_flights(self):
        self.t.add_destination("BCN")
        self.t.add_destination("PEK")
        self.t.add_destination("ROM")
        self.t.add_destination("ARM")

        self.t.remove_destination("BCN")
        self.t.remove_destination("ROM")

        expected = ["PEK", "ARM"]
        returned = [flight.destination for flight in self.t.flights.flights]
        self.assertEqual(expected, returned)


if __name__ == '__main__':
    unittest.main()
