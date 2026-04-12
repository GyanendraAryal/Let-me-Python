fruit = "Banana"
color = input("Enter the color: ").lower().strip()

if fruit == "Banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overriped")