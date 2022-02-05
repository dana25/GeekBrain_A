num = int(input("введите целое положительное число: "))
greatest_num = 0
num0 = num

while num0>0:
    digit = num0 % 10
    if digit > greatest_num:
        greatest_num = digit
        if greatest_num ==9:
            break

    num0 = num0 // 10

print(f"наибольшая цифра {num} это {greatest_num}")