from User import *
from Flights import *


class Skyscanner():
    def __init__(self, destination: list, num_destination: int):
        self.num_destination = num_destination
        self.destination = destination

    def get_num_destinnations(self) -> int:
        return self.num_destination

    def get_destinnations(self) -> list:
        return self.destination

    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return True