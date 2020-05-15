from User import *
from Flights import *


class Skyscanner():
    def __init__(self, x):
        self.num_destinos = x
        self.Destinos = []

    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return True