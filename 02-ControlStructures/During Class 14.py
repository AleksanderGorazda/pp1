age=float(input('Podaj wiek psa w ludzkich latach: '))
if age>2:
    dogage = (age-2)*4 + 21
else:
    dogage = age*10.5
print('Wiek psa w psich latach to latach', dogage," lata") 