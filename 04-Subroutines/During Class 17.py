tab=[]
sum=0
from random import randint
def rzut():
    oczka=randint(1,6)
    return oczka
print("Wyrzucone oczka: ", end="")
for i in range(3):
    tab.append(rzut())
    sum+=tab[i]
    print(tab[i], end=" ")
print("Suma oczek: ", sum)

