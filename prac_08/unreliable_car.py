from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, fuel, name, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0

        distance_driven = super().drive(distance)
        return distance_driven

# Remember they inherit down and the __init__ must be in the same ord eg: name, fuel, distance
