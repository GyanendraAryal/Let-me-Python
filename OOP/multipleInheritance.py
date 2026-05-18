class Car:
    total_car = 0  # To Track the number of cars created using this class

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return f"Brand is {self.__brand}"

    def get_model(self):
        return f"Model is {self.__model}"

    def fuel_type(self):
        return f"Fuel type is Diesel or Petrol"


class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def fuel_type(self):
        return f"Fuel type is Electric Charge"


class Battery:  # pass is just a placeholder for the codes
    def battery_info(self):
        return f"This is battery"


class Engine:
    def engine_info(self):
        return f"This is engine"


class ElectricCar(Battery, Engine, Car):
    pass

my_new_Tesla = ElectricCar("Tesla","Model S")
print(my_new_Tesla.engine_info())
print(my_new_Tesla.battery_info())