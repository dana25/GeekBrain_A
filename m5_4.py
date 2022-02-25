dict4= {"one": "один", "two":"два", "three":"три", "four":"четыре"}

with open("text_44.txt", "w", encoding='utf-8') as n_file:
    with open("text_1.txt", encoding='utf-8') as my_file:
        n_file.writelines([line.replace(line.split()[0], dict4.get(line.split()[0])) for line in my_file])