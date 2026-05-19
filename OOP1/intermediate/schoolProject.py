class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Person name is {self.name} and is {self.age} years old")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(
            f"Person name is {self.name} and is {self.age} years old and teaches {self.subject}"
        )


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        print(
            f"Person name is {self.name} and is {self.age} years old and studies in grade{self.grade}"
        )


class Principal(Teacher):
    def __init__(self, name, age, subject):
        super().__init__(name, age, subject)

    def manage_school(self):
        return f"Who manages school!!"

    def introduce(self):
        print(
            f"Person name is {self.name} and is {self.age} years old {self.manage_school()} and also teaches {self.subject}"
        )


collegeMembers = [
    Person("Gyanendra", 19),
    Teacher("Gyanendra", 19, "Python"),
    Student("Dumb", 17, 10),
    Principal("Headmaster", 50,"Math"),
]

for member in collegeMembers:
    member.introduce()

# # Person
# myPerson = Person("Gyanendra", 19)
# print(f"Person is {myPerson.name} and is {myPerson.age} years old")

# # Teacher
# myTeacher = Teacher("Gyanendra", 19, "Python")
# print(
#     f"Teacher is {myTeacher.name} and is {myTeacher.age} years old and he teaches {myTeacher.subject}"
# )

# # Student
# myStudent = Student("Dumb", 17, 10)
# print(
#     f"Student is {myStudent.name} and is {myStudent.age} years old and he studies in grade {myStudent.grade}"
# )

# # Principal
# myPrincipal = Principal("Headmaster", 50)
# print(
#     f"Principal is {myPrincipal.name} and is {myPrincipal.age} years old and {myPrincipal.manage_school()}"
# )
