list = [1,2,3,4,5]
k = 2

k = k % len(list)
rotated = list[-k:] + list[-k:]
print(rotated)