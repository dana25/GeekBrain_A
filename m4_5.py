from functools import reduce

def list5 (n1, n2):
    return n1*n2

new_list= [n for n in range(100, 1001,2)]
print(new_list, reduce(list5, new_list))