parz=0
nieparz=0
for i in range (1,51):
    if i%2==0:
        parz=parz+i
    else:
        nieparz=nieparz+i
print("Suma parzystych: ", parz)
print("Suma nieparzystych: ", nieparz)
    