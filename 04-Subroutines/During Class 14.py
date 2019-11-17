num = 23
tab =[15,38,7,23,14]
def function(num,tab):
    print("Liczba ", num)
    print("Tablica: ", end="")
    for i in range(len(tab)):
        print(tab[i], end=" ")
        if num == tab[i]:
            print("podana liczba wystepuje")
        else:
            print("nie wystepuje")
function(num,tab)