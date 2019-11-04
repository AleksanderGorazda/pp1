for j in range(216):
    tab=[]
    sum=0
    from random import randint
    def rzut():
        oczka=randint(1,6)
        return oczka
    for i in range(3):
        tab.append(rzut())
        sum+=tab[i]
    if sum == 18:
        print("Matematyka się zgadza")
    else:
        continue