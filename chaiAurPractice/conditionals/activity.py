weather = input("Enter the weather climate: ").strip().capitalize()

if weather == "Sunny":
    activity = ("Go for a walk!!")
elif weather == "Rainy":
    activity = ("Read a book!!")
elif weather == "Snowy":
    activity = ("Build a snowman!!")
print(activity)