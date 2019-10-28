x = int(input("liczba: "))
tab=[]
tab=list()
while 0<1:
    tab.append(int(x%2))
    x = (x-(x%2))/2
    if x==0:
        break
for i in range(len(tab)):
    print(tab[len(tab)-(i+1)], end="")