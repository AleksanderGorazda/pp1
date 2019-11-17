from itertools import count
n = int(input("Wprowadź ilość liczb pierwszych: "))
tab=[]
tab=list()
print("Liczby pierwsze: ", end=" ")
for i in count(0):
    x=i
    for j in count(0):
        if (j+1)<=x:
            if x%(j+1)==0 and (j+1)<x:
                if x==(j+1) or (j+1)==1:
                    tab.append(x)
                else:
                    del tab[-1]
                    break
            else:
                continue
        else:
            break
    if len(tab)==n:
        break
    else:
        if not tab:
            continue
        else:
            continue
for h in range(len(tab)):
    print(tab[h], end=" ")
    