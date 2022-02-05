T = int(input("enter the time: "))
h = T // 3600
m = T //60 - h * 60
s = T % 60
print(f"{h:02}:{m:02}:{s:02}")
