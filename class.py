# class Animal:
#     pass

# type("Animal",(),{})


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


myCar = Car("Totya", "Prado")
print("My car brand is: ",myCar.brand)
print("My car model is: ",myCar.model)