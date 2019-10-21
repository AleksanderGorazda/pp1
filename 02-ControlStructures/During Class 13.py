x =0
y =0
if x>0 and y>0:
    print('Punkt P(',x, "," ,y,') znajduje się w pierwszej ćwiartce układu współrzędnych')
elif x>0 and y<0:
    print('Punkt P(',x, "," ,y,') znajduje się w drugiej ćwiartce układu współrzędnych')
elif x<0 and y<0:
    print('Punkt P(',x,',',y,') znajduje się w trzeciej ćwiartce układu współrzędnych')
elif x<0 and y>0:
    print('Punkt P(',x,',',y,') znajduje się w czwartej ćwiartce układu współrzędnych')
elif x==0 and y!=0:
    print('Punkt P(',x,',',y,') znajduje się na osi Y')
elif y==0 and x!=0:
    print('Punkt P(',x,',',y,') znajduje się na osi X')
elif y==0 and x==0:
    print('Punkt P(',x,',',y,') w środku układu')