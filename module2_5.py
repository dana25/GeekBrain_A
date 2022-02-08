my_list = [3,3,5,6,7,7,7,8]
num= int(input('entre new number: '))

i=0
for n in my_list:
    if num >=n:
        i+=1
    else:
        break
my_list.insert(i, num)
print(my_list)