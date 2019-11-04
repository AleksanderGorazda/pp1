tab=[]
with open('numbers.txt','r') as file:
    for line in file:
        tab.append(line)
tab.sort()
for i in range(len(tab)):
    print(tab[i], end="")