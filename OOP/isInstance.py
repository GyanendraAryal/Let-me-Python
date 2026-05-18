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


my_tesla = ElectricCar("Tesla", "Cyber", "85kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
