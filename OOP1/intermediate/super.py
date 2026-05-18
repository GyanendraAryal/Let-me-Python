class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

newStudent = Student("Ram", "Python")
print(newStudent.name)
print(newStudent.course)