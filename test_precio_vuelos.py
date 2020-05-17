import unittest
from Travel import *


class MyTestCase(unittest.TestCase):
    def test_zero_destinations(self):
        destinations = []
        passengers = 1
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)

        expected_price = 0.0
        calculated_price = t1.get_total_price()
        self.assertEqual(calculated_price, expected_price)

    def test_one_passenger_price(self):
        destinations = []
        passengers = 1
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.add_destination("BCN")
        t1.add_destination("ROM")
        # 1*1 + 1*2
        expected_price = 3.0
        calculated_price = t1.get_total_price()
        self.assertEqual(expected_price, calculated_price)

    def test_add_destination_price(self):
        destinations = []
        passengers = 2
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.add_destination("BCN")
        t1.add_destination("ROM")
        # 2*1 + 2*2
        expected_price = 6.0
        calculated_price = t1.get_total_price()
        self.assertEqual(expected_price, calculated_price)

    def test_remove_destination_price(self):
        destinations = ["BCN", "ROM", "PEK"]
        passengers = 2
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.remove_destination("ROM")
        # 2*1 + 3*2
        expected_price = 8.0
        calculated_price = t1.get_total_price()
        self.assertEqual(expected_price, calculated_price)


if __name__ == '__main__':
    unittest.main()
