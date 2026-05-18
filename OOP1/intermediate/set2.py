class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, color, legs):
        super().__init__(name, age)
        self.color = color
        self.legs = legs

    def color(self):
        return f"Color is: {self.color}"

    def legs(self):
        return f"Number of legs are: {self.legs}"


myDog = Dog("Doggy", 23, "Black", 4)
# print(myDog.name)
# print(myDog.age)
# print(myDog.color)
# print(myDog.legs)

myCat = Animal("Katze",5)
print(f"My cat name is {myCat.name} and he is {myCat.age} years old!!")