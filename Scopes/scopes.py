# username = "gyanendra"
# def myName():
#     # username = 'aryal'
#     print(username)
# print(username)
# myName()

# x = 99
# def funTwo(y):
#     z = x + y
#     return z
# result = funTwo(1)
# print(result)


# x = 99
# def funThree():
#     global x
#     x = 88
#     return x

# print(funThree())

# x = 99

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# result = f1()
# result()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

# g = f(3)
# print(g)

f = chaicoder(3)
g = chaicoder(3)
print(f(3))
print(g(2))
