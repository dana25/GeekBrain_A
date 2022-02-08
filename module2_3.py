month = int(input('введите номер месяца: '))

season_dict = {'winter':[12, 1, 2], 'spring':[3, 4, 5], 'summer':[6, 7, 8],'autumn':[9, 10, 11]}
#print(sum(season_dict.values(), []))
#print (season_dict.items())
#print(season_dict.values())
#print(season_dict.keys())

#if month in season_dict.values():
   # print(f" {season_dict.keys()}")
#else:
   # print('wrong number')

for i in season_dict.items():
    if month in i[1]:
        print (i[0])
        break