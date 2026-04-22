#Using Set
# a = [1,2,2,3,4,4,5]
# uniq = set(a)
# print(list(uniq))

# #Using NOSET
# a = [1,2,2,3,4,5,5,6,6,7,8]
# uniqueList = []
# for num in a:
#     if num not in uniqueList:
#         uniqueList.append(num)
# print(uniqueList)

#Using fromkeys
a = [1,2,2,3,4,5,5,6,6,7,8]
uniqueList = list(dict.fromkeys(a))
print(uniqueList)