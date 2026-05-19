class A:
    x = 10


class B(A):
    pass


b = B()

print(b.x)  # 10

b.x = 50  # x = 50

print(b.x)  # 50
print(A.x)  # 10
