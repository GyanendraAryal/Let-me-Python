words = ['apple','orange','apple', 'mango' ,'litchi']
unique_words = set()

for word in words:
    if word in unique_words:
        print("Unique word",word)
    else:
        print("Duplicate word is: ",word)