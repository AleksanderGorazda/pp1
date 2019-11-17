tab=[32,16,5,8,24,7]
with open('tablenumbers.txt','a') as file:
    for i in range(len(tab)):
        file.write(str(tab[i]))
        file.write("\n")