n = input("enter an integer: ")
while n < '0':
    print("Please enter number greater than 0 ")
    n = input("Enter the number: ")

print(f"{n} + {n+n} + {n+n+n}= {int(n)+int(n+n)+int(n+n+n)}")

