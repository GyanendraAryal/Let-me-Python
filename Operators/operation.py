"""
a = int(input("Enter a number: "));

if a%2==0:
    print("A is even number")
else:
    print("A is odd number")
"""

"""b = int(input("Enter a number:"))
if b<0:
    print("B is negative number")
elif b>0:
    print("B is positive number")
else:
    print("B is zero")"""

"""mark = int(input("Enter your mark: "))

if mark>=90:
    print("You got an A")
elif mark>=70 and mark<=80:
    print("You got a B")
elif mark>=60 and mark<=70:
    print("You got a C")
else:
    print("Sorry you failed!")"""

#Loops
#For Loop
#for a limited time or until the conditio is met
#Iterates in sequences:- list, tuple, string
"""for i in range(1,11):
    print(i)"""
"""a = [1,2,3,4,5]
for i in a:
    print(i)

str = ["a","b","c","d"]
for i in str:
    print(i)
"""
#Range
"""a  = range(1,10,1)
print(a)# return a range(1,10)

b = list(range(1,11,2))#List
print(b)

c = tuple(range(1,21,4))
print(c)"""
#Nested Loop
"""for i in range(1,3):# 3 is exclusive
    for j in range(2,4):# 4 is exclusive
        print(f"{i},{j}")"""

#Breaking the loop
"""for num in range(1,11,1):
    if num == 4:
        break;
    print(num)"""

"""for n in range(1,7,1):
    if n == 2:
        continue;
    print(n)"""
#Pass
"""for num in range(1,11,1):
    if num == 5:
        pass
    print(num)"""

#While Loop
#as long as the condition is true
i = 1
"""while i <=5:
    print(i)
    print("i is incremented by 1:")
    i += 1
"""

#Even Number
a = int(input("Enter the starting number: "))
b = int(input("Enter the last number: "))
print("Even numbers are: ")
for i in range(a,b,1):
    if i%2==0:
        print(i)
    else:
        print(i)

