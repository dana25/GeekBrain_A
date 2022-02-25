with open('text_1.txt', "r", encoding='utf-8') as f:
    emp = {line.split()[0]:float(line.split()[1]) for line in f}
    print(f'Salary ={round(sum(emp.values())/len(emp), 3)}\n' 
          f'Salary <20k {[e[0] for e in emp.items() if e[1] < 20000]}')