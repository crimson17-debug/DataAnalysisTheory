
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("the vehicle is stating")
    def stop(self):
        print("vehicle is stopping")



class Car(Vehicle):
    def __init__(self,brand, model, year):
        super().__init__(brand,model,year)
        # self.brand = brand
        # self.model = model
        # self.year = year

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")




class Bike(Vehicle):
    def __init__(self,brand, model, year):
        super().__init__(brand,model,year)
        # self.brand = brand
        # self.model = model
        # self.year = year

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stoppin")



vehicles: list[Vehicle] = [
    Car("tata", "cookie", 2023),
    Bike("honda", "freeky", 2345)
]


for vehicle in vehicles:
        print(f"Inspecting {vehicle.brand} {vehicle.model}, {type(vehicle).__name__}")
        vehicle.start()
        vehicle.stop()



    