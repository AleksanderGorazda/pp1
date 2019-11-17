tab=[]
tab = list()
x = int(input("Podaj liczbę: "))
y = int(input("Podaj liczbę: "))
z = int(input("Podaj liczbę: "))
if x>y and x>z:
    tab.append(x)
    if z>y:
        tab.append(z)
        tab.append(y)
    else:
        tab.append(y)
        tab.append(z)
if y>x and y>z:
    tab.append(y)
    if z>x:
        tab.append(z)
        tab.append(x)
    else:
        tab.append(x)
        tab.append(z)
if z>y and z>x:
    tab.append(z)
    if x>y:
        tab.append(x)
        tab.append(y)
    else:
        tab.append(y)
        tab.append(x)
print("Liczby w kolejności rosnącej: ",tab[2],", ",tab[1],", ",tab[0])