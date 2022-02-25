my_file= open("text_1.txt", 'w', encoding='utf-8')

line = " "
while line:
    line = input("Please enter text: ")
    my_file.write(f"{line}\n") if line !='' else my_file.close()