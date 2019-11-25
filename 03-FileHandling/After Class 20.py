tab=[]
with open('numbers.txt','r') as file:
    for line in file:
        if int(line)%2==0:
            tab.append(line)
        else:
            continue
with open('evennumbers.txt','w') as file:
    for i in range(len(tab)):
        file.write(tab[i])