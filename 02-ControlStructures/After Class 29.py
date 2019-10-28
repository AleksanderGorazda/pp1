tab = [15,8,31,47,2,19]
print("tab: ", end="")
for i in range(len(tab)):
    print(tab[i], end=" ")
print("")
print("tab in reverse: ", end="")
for i in range(len(tab)):
    print(tab[len(tab)-(i+1)], end=" ")