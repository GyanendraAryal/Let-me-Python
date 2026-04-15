number = int(input("Enter a number: "))
is_Prime = True

if number >1:
    for i in range(2,number):
        if (number % 2 == 0):
            is_Prime = False
            break
print(is_Prime)