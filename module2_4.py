sent= input('enter the words with space: ').split()
#print((sent, 1))

for i, n in enumerate(sent, 1):
    print (f"{i}. {n[:10]}")