imiona=["Janek","Ania","Wojtek","Zosia"]
def jestImie(imie,imiona):
    print("Imiona: ", end="")
    com = "Rezultat: imię nie zawarte jest w wykazie imion"
    for i in range(len(imiona)):
        print(imiona[i], end=" ")
        if imie == imiona[i]:
            com = "Rezultat: imię zawarte jest w wykazie imion"
    print("")
    print(com)
jestImie(input("Imie: "),imiona)
