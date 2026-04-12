age = int(input("Enter your age: "))
weather = input("Enter the weather: ").strip().lower()

price = 12 if age >= 18 else 8
if weather == "wednesweather":
    price -= 2
print("Ticket price for you is $",price)