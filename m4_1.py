from sys import argv

def sal_cal():
    time, rate, bonus = map(float, argv[1:])
    return time*rate+bonus

print (sal_cal ())

# python m4_1.py 2 50 10