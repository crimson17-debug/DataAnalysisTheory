# #inheritance is a fundamental concept in object-oriented programming (oop) that involves creating new classes (subclasses or derived classes) based on existing classes (superclasses or base classes)

# A car is-a vehicle
# a bike is-a vehicle 

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, no_of_doors, no_of_wheels):
        super().__init__(brand,model,year)
        self.no_of_doors = no_of_doors
        self.no_of_wheels = no_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year,no_of_wheels):
        super().__init__(brand,model,year)
        self.no_of_wheels = no_of_wheels



car = Car("ford", "focus",2008,4,4)
bike = Bike("honda", "scoopy",2345, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
