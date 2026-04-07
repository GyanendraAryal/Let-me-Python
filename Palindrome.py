value = "Madam In Eden Im Adam".strip().replace(" ", "").lower()

rev_val = value[::-1]
if rev_val == value:
    print("String is palindrome")
else:
    print("String is not palindrome!!")