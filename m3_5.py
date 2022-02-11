def sum ():
    s=0
    while True:
        list = input('enter number').split()
        for i in list:
            if i.lower() == "q":
                return s
            else:
                try:
                    s+=int(i)
                except ValueError:
                    print("to exit enter - 'q'")
        print(s)

print(sum())