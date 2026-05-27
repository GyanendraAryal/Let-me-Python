# # # # # # x = 1

# # # # # # while x <= 10:
# # # # # #     print(x)
# # # # # #     x = x + 1

# # # # # # myList = []
# # # # # # for i in range(1,10):
# # # # # #     # print(i)
# # # # # #     myList.append(i)

# # # # # # print(myList)

# # # # # # sum = 0
# # # # # # numbers = [4, 8, 15, 16, 23, 42]

# # # # # # for i in numbers:
# # # # # #     sum += i

# # # # # # # print(sum)


# # # # # # names = ['Alice', 'Bob', 'Charlie', 'Diana']

# # # # # # for i in names:
# # # # # #     print("Hello,",i,"!")


# # # # # # x = 2

# # # # # # while x <= 20:
# # # # # #     print(f"{x} is even number" if x % 2 == 0 else f"{x} is not an even number")
# # # # # #     x = x + 1


# # # # # # for i in range(20, 2,-2):
# # # # # #     print(i)


# # # # # # for i in range(10, 0,-1):
# # # # # #     print(i)

# # # # # # print("Blast of!!")


# # # # # # for i in range(1,9):
# # # # # #     print(f"{i} X {i} = {i * i}")


# # # # # word = input("Enter a string/word: ")

# # # # # i = 0
# # # # # for letter in word:
# # # # #     i += 1

# # # # # print(i)

# # # # scores = [34, 67, 23, 89, 45, 12, 90, 56]

# # # # max = scores[0]
# # # # for i in scores:
# # # #     if i > max:
# # # #         max = i
# # # # # print(max)


# # # # for i in range(1, 31):
# # # #     if i % 3 == 0 and i % 5 == 0:
# # # #         print("FizzBuzzz")
# # # #     elif i % 5 == 0:
# # # #         print("Buzz")
# # # #     elif i % 3 == 0:
# # # #         print("Fizz")
# # # # #     else:
# # # # #         print(i)


# # # # num = int(input("Enter Number: "))

# # # # for i in range(1, 11):
# # # #     print(f"{num} X {i} = {num * i}")


# # # vowels = ['a', 'e', 'i', 'o', 'u']

# # # word = input("Enter th word: ")

# # # for letter in word:
# # #     if letter.lower() in vowels:
# # #         continue
# # #     else:
# # #         print(letter)


# # # sqrList = []

# # # # count = 0
# # # for i in range(1,11):
# # #     sqrList.append(i * i)
# # # print(sqrList)


# # pasword = "python123"

# # for i in range(1, 4):
# #     userPass = input("Enter pass: ")
# #     if userPass == pasword:
# #         print("Access granted!!")
# #         break
# #     else:
# #         if i == 3:
# #             print("Account locked!!")
# #             break
# #         print("Wrong pass, enter again")
# #         continue

# # # print("Account Locked!!")


# sentence = 'the cat sat on the mat the cat'
# lst = sentence.split()

# # print(lst)
# # print(type(sentence))
# count = 0
# for word in lst:
#     if word == "the":
#         count = count + 1
        
# print(count)


for i in range(1,6):
    print(f"{i * "*"}")