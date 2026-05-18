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

    @staticmethod  # These are decotators
    def general_description():
        return f"Cars are means of transport and are amaizing"
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def fuel_type(self):
        return f"Fuel type is Electric Charge"


my_car = Car("Tata", "Safari")
# my_car.__model = "City"
# print(my_car.__model)
print(my_car.model)