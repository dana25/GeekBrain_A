def fun1(num1=int(input('enter num1: ')), num2= int(input('enter num2: '))):
    try:
        #num1 =int(input('enternum1: '))
        #num2 = int(input('enter num2: '))
        div = num1 / num2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "ZeroDivisionError"
    return round(div,2)
print(fun1())
