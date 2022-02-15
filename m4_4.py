from random import randint

list4=[randint(-20, 20) for i in range(20)]
dict4 ={n: 0 for n in list4}

for n in list4:
    dict4[n]+=1

print([n for n in list4 if dict4[n] ==1])