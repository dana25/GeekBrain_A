def fun4 (x, y):
    try:
        x, y = float(x), int(y)
        a=1
        for i in range(abs(y)):
            a /=x
        return round(a, 7)
    except ValueError:
        return "enter number: "

print(fun4(x=input('enter integer'), y=  input('etner negative integer')))
