from itertools import count, cycle

a = count(7)
b = cycle("ABC")

for i in range(5):
    print(('{}, {}').format(next(a),next(b)))