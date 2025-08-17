


class Car:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")




class Bike:
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_bike(self):
        print("Car is starting")

    def stop_bike(self):
        print("Car is stoppin")



vehicles = [
    Car("tata", "cookie", 2023),
    Bike("honda", "freeky", 2345)
]


for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model}, {type(vehicle).__name__}")
        vehicle.start()
        vehicle.stop()

    elif isinstance(vehicle,Bike):
        print(f"Inspecting {vehicle.brand} {vehicle.model}, {type(vehicle).__name__}")
        vehicle.start_bike()
        vehicle.stop_bike()

    else:
        raise Exception("objecti is not a valid vehicle")
        


        