# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#     @property
#     def get_balance(self):
#         return self.__balance
# myAcc = BankAccount(1000)
# print(myAcc.get_balance)


class Animal:
    def __init__(self, sound):
        self.sound = sound
    def sound(self):
        return (f"Soundingggggggggggggghh")
class Dog(Animal):
    def __init__(self, size, sound):
        self.size = size
        super().__init__( sound)
    def size(self):
        print("6 inches, period!!")
        
class serviceDog(Dog):
    def __init__(self, size, sound, character):
        self.character = character
        super().__init__(size, sound)
    def character(self):
        print("Active as fucKK")
        
myServiceDog = serviceDog("Cocaine", "Bhau Bhau", "6 inches period")
print(myServiceDog.sound)
# myServiceDog.size
# myServiceDog.character