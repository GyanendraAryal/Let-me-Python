pi = 3.14
def circleArea(rad):
    area = pi * rad**2
    circumference = 2 * pi *rad
    return area, circumference
a , b = circleArea(5)
print("Area is:",a)
print("Circumference is:",b)
    