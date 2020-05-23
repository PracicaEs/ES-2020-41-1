import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.destinations = []
        self.user = User("A", "1", 2, 3, "a@b.c")
        self.passengers = 2
        self.t = Travel(self.destinations, self.user, self.passengers)

    def test_zero_destinations(self):
        expected = 0.0
        returned = self.t.calculate_total_no_IVA()
        self.assertEqual(expected, returned)

    def test_add_destination_price(self):
        self.t.add_destination("BCN")
        self.t.add_destination("ROM")
        # 1*1 + 1*2
        expected_price = 6.0
        calculated_price = self.t.calculate_total_no_IVA()
        self.assertEqual(expected_price, calculated_price)

    def test_remove_destination_price(self):
        self.t.add_destination("BCN")
        self.t.add_destination("ROM")
        self.t.add_destination("PEK")

        self.t.remove_destination("ROM")
        # 2*1 + 3*2
        expected_price = 8.0
        calculated_price = self.t.calculate_total_no_IVA()
        self.assertEqual(expected_price, calculated_price)


if __name__ == '__main__':
    unittest.main()
