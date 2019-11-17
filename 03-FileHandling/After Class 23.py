suma=0
import re
with open('land.txt', 'r') as file:
    r = file.read()
    x = re.findall('\d', r)

for i in range(len(x)):
    suma = suma + int(x[i])
print(suma)