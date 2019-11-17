tab=[]
sum = 0
tab = list()
while 0<1:
    x = int(input("Podaj liczbę: "))
    if x == 0:
        break
    else:
        tab.append(x)
for i in range(len(tab)):
    sum = sum+tab[i]
print("REZULTAT: Liczb=", len(tab),", Suma=",sum,", Średnia=",sum/len(tab))    
    
    