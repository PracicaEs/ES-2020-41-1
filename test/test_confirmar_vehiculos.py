import unittest.mock
from src.Rentalcars import *
from src.Travel import *


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        self.destinations = ["BCN", "LON", "NAP"]
        self.passengers = 4
        self.t = Travel(self.destinations, self.user, self.passengers)
        self.car1 = Car("1111AAAA", "Bugatti", "BCN", 2, 1, 4)
        self.car2 = Car("2222BBBB", "Lamborghini", "LON", 5, 4, 4)
        self.car3 = Car("3333CCCC", "Ferrari", "NAP", 6, 3, 4)
        self.t.add_car(self.car1)
        self.t.add_car(self.car2)
        self.t.add_car(self.car3)
        self.cars = Rentalcars()

    def test_add_vehicles(self):
        expected = [self.car1, self.car2, self.car3]
        self.assertEqual(self.t.cars.cars, expected)

    def test_limit_of_passengers_per_vehicle_overcomed(self):
        self.destinations = ["LON"]
        passengers = 5
        t2 = Travel(self.destinations, self.user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "LON", 2, 1, 5)
        car2 = Car("2222BBBB", "Lamborghini", "LON", 5, 2, 2)
        car3 = Car("3333CCCC", "Ferrari", "LON", 6, 3, 3)
        t2.add_car(car1)
        t2.add_car(car2)
        t2.add_car(car3)
        expected = [car2, car3]
        self.assertEqual(t2.cars.cars, expected)

    def test_remove_vehicles(self):
        self.t.remove_car(self.car2.codi)
        expected = [self.car1, self.car3]
        self.assertEqual(self.t.cars.cars, expected)

    def test_confirm_cars(self):
        expected = "La reserva de los vehiculos se ha efectuado correctamente"
        answer = self.t.confirm_reserve_cars()
        self.assertEqual(expected, answer)

    @unittest.mock.patch('src.Travel.Rentalcars')
    def test_error_confirm_cars(self, m):
        expected = "No se ha podido realizar la reserva"
        m.return_value.confirm_reserve.return_value = False
        answer = self.t.confirm_reserve_cars()
        self.assertEqual(expected, answer)

    def test_retry_confirm_cars_correct(self):
        expected = "La reserva de los vehiculos se ha efectuado correctamente"
        answer = self.t.confirm_reserve_cars()
        self.assertEqual(answer, expected)

    @unittest.mock.patch('src.Travel.Rentalcars')
    def test_retry_confirm_cars_limit_of_retries_overcomed(self, m):
        expected = "No se ha podido realizar la reserva"
        m.return_value.confirm_reserve.return_value = False
        answer = self.t.confirm_reserve_cars()
        self.assertEqual(answer, expected)
