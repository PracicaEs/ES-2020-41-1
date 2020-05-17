import unittest
from Flights import *


class MyTestCase(unittest.TestCase):
    def test_manage_passengers(self):
        expected_number = 6
        flight = Flight("1", "A", expected_number, 200.0)
        f1 = Flights([flight])
        returned_number = f1.get_passengers(0)
        self.assertEqual(expected_number, returned_number)


if __name__ == '__main__':
    unittest.main()


