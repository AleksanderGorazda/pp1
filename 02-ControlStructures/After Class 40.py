from random import randrange
o1=0
o2=0
o3=0
o4=0
o5=0
o6=0
for i in range(100):
    act=randrange(6)+1
    if act==1:
        o1=o1+1
    elif act==2:
        o2=o2+1
    elif act==3:
        o3=o3+1
    elif act==4:
        o4=o4+1
    elif act==5:
        o5=o5+1
    elif act==6:
        o6=o6+1
print("Szóstka: ", o6, "\nPiątka: ", o5, "\nCzwórka: ", o4, "\nTrójka: ", o3, "\nDwójka: ", o2, "\nJedynka: ", o1)
    
