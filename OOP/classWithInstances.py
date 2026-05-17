class Car:
    wheels:4
    def __init__(self,brand):
        self.brand = brand
        
c1 = Car("Toyota")


print(dir(Car))
# print("Car dict: ",Car.__dict__)
# print("C1: ", c1.__dict__)