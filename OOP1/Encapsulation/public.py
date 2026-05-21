# class Student:
#     def __init__(self):
#         self.name = "Ram"
        
# s = Student()
# print(s.name)
# class Student:
#     def __init__(self):
#         self._name = "Ram" #_ block the access of name outside class but still we can access using _ whi
        
# s = Student()
# print(s.name)

class Bank:
    def __init__(self):
        self.__balance = 1000
        
b = Bank()
# print(b.__balance)
print(b._Bank__balance)