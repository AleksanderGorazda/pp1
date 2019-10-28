x = int(input("Podaj limit prędkości (km/h): "))
y = int(input("Podaj prędkość pojazdu (km/h): "))
mandat=0
if (y-x)<10:
    mandat = (y-x)*5
else:
    mandat = ((y-10)-x)*15
    mandat = mandat +50
print("Mandat (zł): ",mandat)