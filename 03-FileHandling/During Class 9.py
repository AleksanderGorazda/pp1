i=1
with open('C:/Users/s-115-23/Desktop/pp1/03-FileHandling/NoEducation.txt','r') as file:
    for line in file:
        print(i," ",line, end="")
        i = i+1