pin = "0805"
for i in range(3):
    inp=input("Podaj kod PIN: ")
    if(pin==inp):
        print("Kod PIN poprawny")
        break
    else:
        print("Kod PIN niepoprawny")
