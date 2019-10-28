import math
a = int(input("Wprowadź a: "))
b = int(input("Wprowadź b: "))
c = int(input("Wprowadź c: "))
delta=(b**2)-(4*a*c)
pier=math.sqrt(delta)
x1 = ((-b-pier)/(2*a))
x2 = ((-b+pier)/(2*a))
print(delta," ",pier," ",x1," ",x2)