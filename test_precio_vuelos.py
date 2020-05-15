import unittest
from Travel import *


class MyTestCase(unittest.TestCase):
    def test_zero_destinations(self):
        f1 = Flights([])
        expected_price = 0.0
        calculated_price = f1.get_total_price()
        self.assertEqual(calculated_price, expected_price)

    def test_one_passenger_price(self):
        f1 = Flight("A", "BCN", 1, 300.0)
        f2 = Flight("B", "ROM", 1, 200.0)
        f3 = Flights([f1, f2])
        expected_price = 500.0
        calculated_price = f3.get_total_price()
        self.assertEqual(calculated_price, expected_price)

    def test_multiple_passenger_price(self):
        f1 = Flight("A", "BCN", 2, 300.0)
        f2 = Flight("B", "ROM", 2, 200.0)
        f3 = Flights([f1, f2])
        expected_price = 1000.0
        calculated_price = f3.get_total_price()
        self.assertEqual(calculated_price, expected_price)


if __name__ == '__main__':
    unittest.main()
