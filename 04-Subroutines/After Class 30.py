from random import randrange
tab=[]
par=0
nie=0
def function():
    x = randrange(1,51)
    return x
for i in range(1000):
    if function()%2==0:
        par+=1
    else:
        nie+=1
print("Liczby parzyste: ", par/10,"%", sep='')
print("Liczby nieparzyste: ", nie/10,"%", sep='')