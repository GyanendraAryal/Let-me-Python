class LivingBeing:
    def __init__(self):
        pass

    def breath(self):
        return f"Breathing"


class Animal(LivingBeing):
    def __init__(self):
        super().__init__()

    def eat(self):
        return f"I'm eating!!"


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        return f"You are barking!!"


myPet = Dog()
print(myPet.breath())
print(myPet.eat())
print(myPet.bark())
