#Loops
"""i = 0
while i <= 10:
    print(i,end =" ")
    i += 1 #updates the count by 1"""

#Sum of 1st N numbers
"""num = int(input("Enter the 1st N num: "))
i = 0
sum = 0
while i <= num:
    sum += i
    i  += 1;
print("Sum is: ",sum)"""

#Even numbers from 1 to 20
"""num = int(input("Enter the last num: "))
i = 1
while i <num:
    if i % 2==0:
        print(i)
    i +=1"""
#Multiplication table of a number
"""num = int(input("Enter a number: "))
for i in range(1,11):
    print(num ," * ", i , " = ",num * i)"""

#Reverse a number

"""num = int(input("Enter a number: "))#1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10 
print("Reversed number: ", reverse)"""

#Counting digits in number
"""num = int(input("Enter number: "))
subCount = 0
count = 0
while num > 0:
    digit = num % 10
    subCount = subCount * 10 + digit
    num = num // 10
    count += 1 
print(count)"""
#Another way of claculating numbers of digit in a number
"""num = 1234
b = len(str(abs(num)))
print(b)"""