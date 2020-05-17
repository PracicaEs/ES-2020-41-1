class Flight:
    def __init__(self, code: str, destination: str, passengers: int, price: float):
        self.code = code
        self.destination = destination
        self.passengers = passengers
        self.price = price

    def get_code(self) -> str:
        return self.code

    def get_destination(self) -> str:
        return self.destination

    def get_passengers(self) -> int:
        return self.passengers

    def get_price(self) -> float:
        return self.price
