import random
class Vehicle:
    max_speed = 120
    def __init__(self, lisence_plate):
        self.lisence_plate = lisence_plate
    @classmethod
    def create_with_random_plate(cls):
        cls.random_license_plate = random.randint(11111,99999)
        return cls(cls.random_license_plate)

class Truck(Vehicle):
    max_speed = 80
    def __init__(self, lisence_plate, capacity):
        super().__init__(lisence_plate)
        self.capacity = capacity
    @classmethod
    def create_with_random_plate(cls, capacity= 1000):
        cls.capacity = capacity
        return super().create_with_random_plate(capacity)

v1 = Vehicle.create_with_random_plate()
t1 = Truck.create_with_random_plate()
print(v1.max_speed)
print(t1.max_speed)
print(t1.capacity)