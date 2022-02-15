def fact(num):
    aex = 1
    for i in range(num+1):
        yield f'{i}! = {aex}'
        aex *= i+1

for n in fact(int(input('enter num: '))):
    print(n)