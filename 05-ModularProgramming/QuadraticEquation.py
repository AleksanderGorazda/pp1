import math
def wpisz():
    a=float(input('Podaj a:'))
    b=float(input('Podaj b:'))
    c=float(input('Podaj c:'))
    return a,b,c
a,b,c = wpisz()
def delta():
    delt = (b**2 -4*a*c)
    return delt
delta()
def pierw():
    if delta()<0:
        return []
    elif delta()==0:
        return [(-b/2*a)]
    else:
        return [((math.sqrt(delta())-b)/2*a),((-math.sqrt(delta())-b)/2*a)]
def napis():
    print('Równanie kwadratowe postaci: ',a,'x^2+',b,'x+',c,end='')
    print('Pierwiastki równania: x1=',pierw()[0],' x2=',pierw()[1],end='')
napis()