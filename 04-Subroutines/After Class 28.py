progLang = ['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
demand = [61,47,37,32,26,18,14,14,9,7]
def function(progLang,demand):
    for i in range(len(progLang)):
        print(progLang[i],':',demand[i]*'#', end="")
        print("")
function(progLang,demand)
        
