def Fact(num):
    facto = 1
    if num < 1:
        return 1
    else:
        for i in range(1,num+1):
            facto *= i
        return facto
result = Fact(5)
print(result)