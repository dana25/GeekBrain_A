while True:
    days = 1
    a = float(input("начальный результат: "))
    b = float(input("конечный результат: "))
    if a <=0 or b<=0:
        print("введите положительное число: ")
    else:
        while a < b:
            a=a+a*0.1
            days= days+1

        print(f"результат через {days} дней")
        break