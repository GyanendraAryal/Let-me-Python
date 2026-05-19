class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Dog):
    pass

myCat = Cat()
myDog = Dog()
# print(isinstance(myDog, Animal))
# print(isinstance(myCat, Dog))
# print(isinstance(myCat, Animal))
print(issubclass(Dog, Animal))
print(issubclass(Cat, Dog))
print(issubclass(Cat, Animal))
