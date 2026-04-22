# #Merge the dictionaries
# # d1 = {'a':1, 'b':2}
# # d2 = {'b':3, 'c':4}
# # merge = d1 | d2
# # print(merge)

# #Invert the dictionary
# a = {'a':1, 'b':2}
# inverted = {v: k for k, v in a.items()}
# print(inverted)

#Nested Dictionary Access

data = {
  "user": {
    "profile": {
      "name": "Ram"
    }
  }
}
print(data["user"]["profile"]["name"])