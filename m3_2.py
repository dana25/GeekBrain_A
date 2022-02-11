def pers_data(name, surname):
    #birthday, city , email, phone
    name, surname = str(name), str(surname)
    s = ' '.join([name, surname])
    return s
print (pers_data(name= str(input('enter name : ')), surname= str(input ('enter surname: '))))