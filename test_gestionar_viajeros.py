import unittest
from Flights import*


class MyTestCase(unittest.TestCase):
    def test_gestionar_viajeros(self):
        n=6
        vuelo = Flights(n)
        s = vuelo.get_pasajeros()
        self.assertEqual(n, s)


if __name__ == '__main__':
    unittest.main()


