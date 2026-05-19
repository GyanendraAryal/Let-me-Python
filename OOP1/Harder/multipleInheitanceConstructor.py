class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(A):
    def __init__(self):
        print("C")

class D(B, C):
    pass

d = D() #B gets printed because it finds the B classes method first