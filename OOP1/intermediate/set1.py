class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        return f"Starts with key"
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(self)
        self.brand = brand
        
myCar = Car("Tata")
print(myCar.brand)
print(myCar.start())