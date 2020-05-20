import unittest
from src.Car import *
from src.Rentalcars import *
from src.Travel import *


class TestCase(unittest.TestCase):

    def test_confirm_reserve(self):
        cars = Rentalcars()
        user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "BCN", 2)
        car2 = Car("2222BBBB", "Lamborgini", "LON", 5)
        car3 = Car("3333CCCC", "Ferrari", "NAP", 6)
        t.cars=[car1,car2,car3]
        answer = cars.confirm_reserve(user, t.cars)
        self.assertEqual(answer, True)
        print("La reserva se ha efectuado correctamente")

    def test_error_confirm_reserve(self):
        def confirm_reserve(user: User, cars: Cars) -> bool:
            print("Error en la confirmación de la reserva")
            return False

        cars = Rentalcars()
        cars.confirm_reserve = confirm_reserve
        user = User("Guillermo Boreal", "333666999A", "08666", 666666666, "ggg@ggg.ggg")
        destinations = ["BCN", "LON", "NAP"]
        passengers = 5
        t = Travel(destinations, user, passengers)
        car1 = Car("1111AAAA", "Bugatti", "BCN", 2)
        car2 = Car("2222BBBB", "Lamborgini", "LON", 5)
        car3 = Car("3333CCCC", "Ferrari", "NAP", 6)
        t.cars = [car1, car2, car3]
        answer = cars.confirm_reserve(user, t.cars)
        self.assertEqual(answer, False)



if __name__ == '__main__':
    unittest.main()
