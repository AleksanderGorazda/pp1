def podatek(dochod):
    if dochod<=5000:
        pod = (dochod*17)/100
    else:
        pod = ((5000*17)/100) + (((dochod-5000)*32)/100)
    print("Podatek należny:", pod)
podatek(int(input("Podaj dochód: ")))