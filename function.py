# # # # # # # # def rectange_area(length, width):
# # # # # # # #     return length * width

# # # # # # # # print(rectange_area(5,5))


# # # # # # # def is_Even(n):
# # # # # # #     if n % 2 == 0:
# # # # # # #         return True
# # # # # # #     else:
# # # # # # #         return False
# # # # # # # print(is_Even(5))

# # # # # # def greet_user(username, greet = "Good Morning"):
# # # # # #     print(f"{greet} {username}")
# # # # # # greet_user("Chut","Hallo")

# # # # # # # myList = []
# # # # # # word = ''
# # # # # # def reverse_string(string):
# # # # # #     for i in string:

# # # # # #         # print(reverse_string("hallo"))
# # # # # # reverse_string("hallo")
# # # # # # print(word)


# # # # # def reverse_string(name):
# # # # #     word = ''
# # # # #     for i in name:
# # # # #         word = i + word
# # # # #     return word


# # # # # print(reverse_string("hello"))


# # # # def sum_all(*args):
# # # #     sum = 0
# # # #     for i in args:
# # # #         sum += i
# # # #     return sum

# # # # # print(sum_all(1,2,3,4))
# # # # print(sum_all(1, 2, 3, 4))


# # # def create_profile(**info):
# # #     for item in info:
# # #         print(item)

# # # create_profile(name="acut", age="pedo")

# # nameFunction = lambda name: "Hello" + name
# # # print(nameFunction(" Gyanendra"))
# # callName = nameFunction("Hello")
# # print(callName)


# # def apply_twice(func, value):
# #     return func(func(value))

# # print(apply_twice(lambda value: value * 2, 3))


# def make_counter(anotherNum):
#     def increse_count():
#         return anotherNum + 1
#     return increse_count
# anotherFunc = make_counter(999)
# print(anotherFunc())


def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)  # 1234 // 10 == 123

print(sum_digits(1234))
