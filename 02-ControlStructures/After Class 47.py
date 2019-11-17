haj = int(input("Podaj kwotę w zł: "))
reszta1 = haj%5
reszta2 = reszta1%2
five = (haj-reszta1)/5
two = (reszta1-reszta2)/2
print("Kwota ",haj, " zł w monetach:\n5 zł - ",five," szt\n2 zł - ",two," szt\n1 zł - ",reszta2," szt")