tab = []
with open('students.txt','r') as file:
    for line in file:
        tab.append(line.split(","))
for i in range(len(tab)):
    if tab[i][2]=="age":
        continue
    elif int(tab[i][2])<30:
        print(tab[i][0], "", tab[i][1], "", tab[i][4]) 
    else:
        continue