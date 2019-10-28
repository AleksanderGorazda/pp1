tab = [15, 8, 31, 47, 2, 19]
sum=0
n=0
for i in range(len(tab)):
    if tab[i]%2==1:
        sum = sum+tab[i]
        n=n+1
    else:
        continue
print(sum/n)