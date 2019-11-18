import statistics
tab = [2,3,5,2,9,8,1,3,9,1,1,4,7,7,1,4,+]
tab.sort()
def mediana(tab):
    if len(tab)%2==0:
        med = (tab[int((len(tab)/2)-1)] + tab[int(len(tab)/2)])/2
    else:
        med = tab[int((len(tab)/2)+0.5)]
    print(med)
def dominanta(tab):
    print(statistics.mode(tab))
mediana(tab)
dominanta(tab)

    