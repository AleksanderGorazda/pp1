from random import randrange
comp = (randrange(6) + 1)
x = input("Podaj, ile oczek kostki wyrzucił komputer: ")
print("Komputer wyrzucił", comp)
comp = int(comp)
x = int(x)
if comp==x:
    print("True")
else:
    print("False")