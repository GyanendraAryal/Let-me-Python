lang = "programming"
charFreq = {}
for char in lang:
    if char in charFreq:
        charFreq[char]+=1
    else:
        charFreq[char]=1
print(charFreq)