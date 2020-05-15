import unittest
from Flights import *


class MyTestCase(unittest.TestCase):
    def test_gestionar_viajeros(self):
        n = 6
        flight = Flight("1", "A", n, 200.0)
        s = flight.get_passengers()
        self.assertEqual(n, s)


if __name__ == '__main__':
    unittest.main()


