i=0
with open('C:/Users/s-115-23/Desktop/pp1/03-FileHandling/numbers.txt','r') as file:
    for line in file:
        i = i+int(line)
print(i)