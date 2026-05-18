# Polymorphism - that can have multiple faces or uses


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

    @staticmethod #These are decotators
    def general_description():
        return f"Cars are means of transport and are amaizing"


class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize

    def fuel_type(self):
        return f"Fuel type is Electric Charge"


# myCar = Car("Toyota", "Prado")
# print(myCar.get_brand())
# print(myCar.fuel_type())

# safari = Car("Tata", "safari")
# print(safari.get_brand())
# print(safari.fuel_type())
# print(safari.total_car) #Why is this worng?

# myTesla = ElectricCar("Tesla", "CyberTruckk", "85KWH")
# print(myTesla.fuel_type())


# Static Methods
myCar = Car("Tata", "Nexon")
print(myCar.general_description())
# print(Car.general_description())
