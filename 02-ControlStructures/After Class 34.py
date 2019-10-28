pesel = input("Podaj PESEL: ")
if pesel[9]=="0" or pesel[9]=="2" or pesel[9]=="4" or pesel[9]=="6" or pesel[9]=="8":
    print("Płeć: kobieta")
else:
    print("Płeć: mężczyzna")
if int(pesel[3:5])>12:
    print("Wiek: ", 18-int(pesel[0:2]))
else:
    print("Wiek: ", 118-int(pesel[0:2]))