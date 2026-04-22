# # Tuple Unpacking
# # # t = (1,2,3,4) #a=1, b=2, rest=[3,4]
# # # c = []
# # # for num in t:
# # #     if num == 1:
# # #         a = 1
# # #     if num == 2:
# # #         b = 2
# # #     else:
# # #         c.append(num)

# # # print("a = ",a)
# # # print("b = ",b)
# # # print("c = ",c)


# #Count Elements in Tuple

# t = (1,2,3,4,2,2,2,4,5,4,6)
# charCount = {}
# for num in t:
#     if num in charCount:
#         charCount[num] +=1
#     else:
#         charCount[num] = 1
# print(charCount)