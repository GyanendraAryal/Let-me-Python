num = int(input("Enter the table number: "))
for n in range(1,11):
    if n == 5:
        continue
    else:
        print(num ,"x" ,n ," = ",num*n)