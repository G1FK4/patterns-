from abc import ABC, abstractmethod

# Абстрактний клас для транспортних засобів
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Конкретні класи транспортних засобів
class Car(Vehicle):
    def move(self):
        return "Driving a car"

class Plane(Vehicle):
    def move(self):
        return "Flying a plane"

# Фабричний клас для створення транспортних засобів
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "plane":
            return Plane()
        else:
            raise ValueError("Unknown vehicle type")

# Приклад використання:
factory = VehicleFactory()
car = factory.create_vehicle("car")
print(car.move())  # Виведе: Driving a car

plane = factory.create_vehicle("plane")
print(plane.move())  # Виведе: Flying a plane
