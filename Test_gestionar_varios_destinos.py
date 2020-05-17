import unittest
from Skyscanner import*


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n = 3
        x = 3
        flight1 = Flight("1", "A", n, 200.0)
        flight2 = Flight("1", "B", n, 200.0)
        flight3 = Flight("1", "C", n, 200.0)
        s1 = flight1.get_destination()
        s2 = flight2.get_destination()
        s3 = flight3.get_destination()
        destinations = list({s1, s2, s3})
        destinations_list = Skyscanner(destinations, n)
        num_destinations = destinations_list.get_num_destinnations()
        travels = destinations_list.get_destinnations()
        self.assertEqual(n, num_destinations)
        self.assertEqual(destinations, travels)


if __name__ == '__main__':
    unittest.main()
