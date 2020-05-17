import unittest
from Travel import*


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
        num_destinations = destinations_list.get_num_destinations()
        travels = destinations_list.get_destinations()
        self.assertEqual(n, num_destinations)
        self.assertEqual(destinations, travels)

    def test_no_destinations(self):
        passengers = 2
        destinations = []
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        self.assertEqual(destinations, t1.get_destinations())

    def test_no_destinations_flights(self):
        passengers = 2
        destinations = []
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        self.assertEqual([], t1.get_flights())

    def test_add_destinations(self):
        passengers = 2
        destinations = []
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.add_destination("BCN")
        self.assertEqual(destinations, t1.get_destinations())

    def test_add_destinations_flights(self):
        passengers = 2
        destinations = []
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.add_destination("BCN")
        returned_destinations = []
        for flight in t1.get_flights():
            returned_destinations.append(flight.get_destination())
        self.assertEqual(destinations, returned_destinations)

    def test_remove_multiples_destinations(self):
        passengers = 2
        destinations = ["BCN", "PEK", "ROM"]
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.remove_destination("BCN")
        expected_destinations = ["PEK", "ROM"]
        returned_destinations = t1.get_destinations()
        self.assertEqual(expected_destinations, returned_destinations)

    def test_remove_multiples_destinations_flights(self):
        passengers = 2
        destinations = ["BCN", "PEK", "ROM"]
        user = User("A", "1", 2, 3, "a@b.c")
        t1 = Travel(destinations, user, passengers)
        t1.remove_destination("BCN")
        expected_destinations = ["PEK", "ROM"]
        returned_destinations = []
        for flight in t1.get_flights():
            returned_destinations.append(flight.get_destination())
        self.assertEqual(expected_destinations, returned_destinations)


if __name__ == '__main__':
    unittest.main()
