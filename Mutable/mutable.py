# # # # # # # # username = "Gyanendra"
# # # # # # # # print(username)
# # # # # # # # username = "Aryal"
# # # # # # # # print(username)

# # # # # # # a = [1,2,3,4]
# # # # # # # b = a#Reference Copy
# # # # # # # b.append(5)
# # # # # # # print(a)#[1,2,3,4,5]

# # # # # # x = 10
# # # # # # y = x#creates new memory reference as strings are immutable
# # # # # # x = x + 5
# # # # # # print(y)#10

# # # # # import copy

# # # # # a = [[1,2], [3,4]]
# # # # # b = copy.copy(a)
# # # # # b[0][0] = 100
# # # # # print(b)
# # # # # print(a)#Why does a change? Fix using deep copy!!

# # # # import copy
# # # # a = [[1,2],[3,4]]
# # # # b = copy.deepcopy(a)#not connected to original values
# # # # b[0][0] = 100
# # # # print(b)
# # # # print(a)


# # # #Must pass the numbers as strings. This allows the decimal module to parse
# # # #the digits directly without the initial binary conversion error.
# # # from decimal import Decimal
# # # num1 = "0.1"
# # # num2 = "0.2"
# # # print(Decimal(num1) + Decimal(num2))

# # num = 10
# # print(bin(num))
# # print(oct(num))
# # print(hex(num))

# a = 29
# b = 15
# print(a and b)
# print(a or b)
# print(a ^ b)
# print(a << 2)

