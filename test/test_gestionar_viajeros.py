import unittest
from src.Travel import *


class MyTestCase(unittest.TestCase):
    def test_manage_passengers(self):
        passengers = 2
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel([], user, passengers)
        self.assertEqual(passengers, t1.get_passengers())


if __name__ == '__main__':
    unittest.main()


