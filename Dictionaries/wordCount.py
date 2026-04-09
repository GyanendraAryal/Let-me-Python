word = "this is a test this is".split()
countFreq = {}

for char in word:
    if char in countFreq:
        countFreq[char] += 1
    else:
        countFreq[char] = 1
print(countFreq)
