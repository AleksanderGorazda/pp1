tab=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
tab.insert(0,['Imie','Nazwisko','Email'])
print(tab)
with open('dane.csv','w+') as file:
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            file.write(tab[i][j])
            file.write(",")
        file.write("\n")