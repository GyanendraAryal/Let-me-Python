# num = int(input("Enter the number: "))
# numbers = []
# numbers = num
# validation = [1,2,3,4,5,6,7,8,9,10]
# while True:
#     if num in validation:
#         print("Number is validated")
#         break;
#     else:
#         num = int(input("Enter the number: "))

while True:
    number = int(input("Enter a number b/w 1 - 10: "))
    if 1<= number <=10:
        print("Number is validated")
        break
    else:
        print("Invalid number please try again!!")