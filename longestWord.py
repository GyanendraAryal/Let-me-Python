# word = "I love full stack development"
# longest_word = max(word.split(), key=len)
# print(longest_word)



words = "I love full stack development".split()
longest = ""
    
for word in words:
    if len(word) > len(longest):
        longest = word

print(longest) 