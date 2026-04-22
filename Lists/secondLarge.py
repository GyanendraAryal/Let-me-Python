words = "I love full stack development".split()
largest = ""
second = ""

for word in words:
    if len(word) > len(largest):
        second = largest
        largest = word
    elif len(word) > len(second) and word != largest:
        second = word
print(second)