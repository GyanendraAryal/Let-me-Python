class Animal:
    def __init__(self):
        pass
    def speak(self):
        return f"Can Speak"

class Dog(Animal):
    def speak(self):
        # return super().speak()
        return "I bark!!"
class Cat(Animal):
    def speak(self):
        return "I mewow!!"
class Cow(Animal):
    def speak(self):
        return f"I Mooo!!"
    
myList = [Dog(),Cat(),Cow()]

for inst in myList:
    print(inst.speak())