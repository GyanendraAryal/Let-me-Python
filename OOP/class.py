# class Car:
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "LandCrusiur")
# print(my_car.brand)
# print(my_car.model)
# self is a reference to the current object.
# Every method in a class must have self as its first parameter.
# Inside a method, use self.attribute to access class attributes.
# Equivalent to this in JavaScript.

# Class vs Instance Storage
# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand #self.brand = brand, - adding tailing comma makes the object tuple
#         self.model = model
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#     def car_price(self,price):
#         return f"{self.brand}{self.model}'s price is {price:,}"
#         # :, is a format specifier(50_00_000)-50,00,000

# my_car = Car("Tata", "Safari")
# print(my_car.full_name())
# print(my_car.car_price(50_00_000))

# Attribute Lookup


# class Bus:
#     wheels = 4


# b1 = Bus()
# b1.wheels = 9 - but when we define it has!!
# print(b1.wheels)

# Bus.wheels = 6
# print(b1.wheels)
# So here wheel changes for b1 because it does not have its whee Look (Up chain rule)


# Proof of look up chain
# b2 = Bus()

# print(b1.__dict__)
# print(Bus.__dict__)
# print(Bus.__bases__)


# Modify class at Runtime
# class Motor:
#     def drive(self):
#         return "normal driving"


# m = Motor()
# print(m.drive())

# Motor.drive = lambda self: "new driving style"

# print(m.drive())


# Encapsulation_
# -Modify the Car class to encapsulate the brand attribute,
# -make it private and provide a getter method for it

# When we add __ in field that becomes private and it is only access inside the class only

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand,model)
        self.batterysize = batterysize
myteslaCar = ElectricCar("Tesla", "Model S", "85KWH")
# print(myteslaCar.__brand)
print(myteslaCar.get_brand())