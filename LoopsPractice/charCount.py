str = "teteer"
for char in str:
    print(char)
    if str.count(char) == 1:
        print("First non repeating char is: ",char)
        break
