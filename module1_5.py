revenue = float(input("выручка: "))
coast = float(input("издержки: "))

profit = revenue - coast
if profit >0:
    print (f"прибыль: {profit} ")
    print (f"рентабильность {100*profit/revenue:.1f}%")
    pers_num = int(input("количество сотрудников:"))
    print (f"прибыль на кол-во сотрудников {profit/pers_num:.3f}")
elif profit < 0:
    print (f"убыток:{-profit}")
else:
    print ("ноль")