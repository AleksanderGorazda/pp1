tab=[[1,2,0],[0,0,3],[5,1,1]]
print(tab)
def transpozycja(tab):
    trans=[]
    for i in range(len(tab[0])):
        trans.append([])
        for j in range(len(tab)):
            trans[i].append(tab[j][i])
    return trans
print(transpozycja(tab))

    