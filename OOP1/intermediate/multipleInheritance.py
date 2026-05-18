class Father:
    def __init__(self):
        pass

    def driving(self):
        return f"Dad is driving!!"


class Mother:
    def __init__(self):
        pass

    def dishing(self):
        return f"She is cooking!!"


class Child(Father, Mother):
    def __init__(self):
        super().__init__()


myChild = Child()
print(myChild.driving())
print(myChild.dishing())
