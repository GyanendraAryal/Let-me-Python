class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

D().show() #prints C because it looks up to its own dict first, although B doesn't has 
#its own so it goes to class C and it has its own method show() and executes that