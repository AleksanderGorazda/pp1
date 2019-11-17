nr=6
print("| PN | WT | SR | CZ | PT | SB | ND")
for i in range(5):
    for j in range(1,8):
        if (7*i)+j-nr<1:
            print("|    ", end="")
        elif (7*i)+j-nr<10:
            print("|  ",(7*i)+j-nr,end="")
        elif (7*i)+j-nr>30:
            continue
        else:
            print("| ",(7*i)+j-nr,end="")
    print("")