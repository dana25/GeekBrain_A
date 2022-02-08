my_list = [2, 3.4, (1+3j), "строка", None, (4,5), [1,2,3], {6,7,8}, set("asd"), frozenset("qwe"),
           {'book':5, 'cup':7}, b'ten', range(30)]
for el in my_list:
    print (f"{el} - {type(el)}")