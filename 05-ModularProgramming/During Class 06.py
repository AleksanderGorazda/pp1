import csv
with open('employees.csv', newline='') as f:
    i = 1
    suma=0
    reader = csv.reader(f)
    print('#     SURNAME     NAME     AGE     EMAIL\n===============================================================')
    for row in reader:
        print(i,'     ',row[0],'     ',row[1],'     ',row[2],'     ',row[3],'\n',end='')
        if i>1:
            suma += int(row[2])
        i+=1
    print(suma/(i-1))