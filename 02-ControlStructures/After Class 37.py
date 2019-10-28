x = input("Podaj pierwszą liczbę: ")
y = input("Podaj drugą liczbę: ")
z = input("Podaj trzecią liczbę: ")
if (y>x and z<x) or (z>x and y<x):
    print("Mediana wynosi ", x)
elif (x>y and z<y) or (z>y and x<y):
    print("Mediana wynosi ", y)
elif (y>z and x<z) or (x>z and y<z):
    print("Mediana wynosi ", z)
    