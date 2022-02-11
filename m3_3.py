def fun3(num1, num2, num3):
    list= [num1, num2, num3]
    list.remove(min(list))
    return sum(list)
print(fun3(num1=int(input("input 1: ")), num2=int(input('input 2:')), num3=int(input('input 3: '))))
