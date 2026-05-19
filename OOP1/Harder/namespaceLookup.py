class A:
    x = 100

class B(A):
    x = 200

b = B()

print(b.x)#200

del B.x

print(b.x)#100