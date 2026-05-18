class Employee:
    def __init__(self):
        pass

    def work(self):
        return f"Employee work"


class Developer(Employee):
    def __init__(self):
        super().__init__()
    def work(self):
        return f"Developer writes Code!!"


myDev = Developer()
print(myDev.work())
