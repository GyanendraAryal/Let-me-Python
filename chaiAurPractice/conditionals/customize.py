yes_choices = {'yes', 'y', 'true', '1'}
order_size = input("Enter order size(Large,Medium,Small): ").strip().capitalize()
user_inpt = input("Enter value: ").lower()
is_ExtraShot = user_inpt in yes_choices
if is_ExtraShot == True:
    coffee = order_size + " Coffee with an extra shot"
else:
    coffee = order_size + " Coffee"
print("Order: ",coffee)