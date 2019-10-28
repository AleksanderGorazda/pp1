prod = input("Dodaj produkt:")
with open('shoppinglist.txt','a') as file:
    file.write(prod)
    file.write("\n")