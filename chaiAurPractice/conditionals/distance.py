distance = int(input("Enter distance in KM: "))

if distance < 3:
    transport = "Walk"
elif distance < 15:
    transport = "Ride Bike"
elif distance > 15:
    transport = "Ride Car"

print(transport)