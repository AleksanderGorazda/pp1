x = 0
tab = []
tab1 = []
tab2 = []
with open('numbersinrows.txt','r') as file:
    for line in file:
        tab.append(line.rstrip('\n') )
for i in range(len(tab)):
    tab1.append(tab[i].split(","))
    for j in range(len(tab1[i])):
        tab2.append(tab1[i][j])
print(len(tab2))
for z in range(len(tab2)):
    x = x + int(tab2[z])
print(x)