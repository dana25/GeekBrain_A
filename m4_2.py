my_list = [23,8,9,7,5,29,60,45,1,6]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i]>my_list[i-1]]
print(new_list)