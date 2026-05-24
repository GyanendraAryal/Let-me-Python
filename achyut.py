# # # # # a = 5 + 5 # a-----> certain memory
# # # # # a = 10 + 5 #a-----> next memory

# # # # # a = [1,2,3]
# # # # # # b = a
# # # # # print(b)

# # # # # a = [1, 2, 3]
# # # # # b = a[:]
# # # # # print(b)  # [1,2,3]
# # # # a = [4, 5, 6, 7]
# # # # # print(a)
# # # # # print(b)
 
# # # # c = a[1:]
# # # # print(c)


# # # # mylist = [1,2,3,5,4,4,3,1]

# # # # # for i in mylist:
# # # # #     print(mylist.index(i), i)

# # # # mylist.append("apple")
# # # # print(mylist)
# # # # mylist.remove("apple")
# # # # print(mylist)

# # # # mylist.pop()
# # # # print(mylist)


# # # # mylist = [1,2,3,5,4,4,3,1]
# # # # mylist.insert(1, "apple")
# # # # print(mylist)

# # # # mylist.remove("apple")
# # # # mylist.sort()
# # # # print(mylist)
# # # # mylist.reverse()
# # # # print(mylist)

# # # mylist = [1,2,3,5,4,4,3,1]
# # # # mylist.remove(4)
# # # # print(mylist)

# # # del mylist[3]
# # # print(mylist)

# # # res = mylist.pop(0)
# # # print(res)


# # myTuple = (1,2,3,4,4)
# # myTupleOne = (7,8,9,0)
# # # print(myTuple.count(4))

# # newTupple = myTuple + myTupleOne + ("ram",)
# # print(newTupple)



# mySet = {2,"ram",6,5,"sita"}
# mySetTow = {8,7,"hari"}
# # mySet.add(0)

# # mySet.remove("ram")
# # newSet = mySet.union(mySetTow)
# # print(mySetTow.union)
# # print(newSet)

# newSetTwo = mySetTow.intersection(mySet)
# print(newSetTwo)

# Dictionaries - those who stores data in key value pairs

myDic = {
    "name": "chut",
    "age": 20,
    "college":"kanti"
}

# print(myDic["name"])
# print(myDic["age"])
# print(myDic["college"])

# for i in myDic:

print(myDic)
    