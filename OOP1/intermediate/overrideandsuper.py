class Shape:
    def __init__(self):
        print(f"Shape Created!!")


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        print(
            f"Rectangle Created!!",
        )


myShape = Rectangle()
