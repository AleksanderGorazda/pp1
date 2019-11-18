tab=[2,5,4,1,8,7,4,0,9]
def reverse(tab):
    for i in range(len(tab)):
        x = tab.pop(len(tab)-1)
        tab.insert(i,x)
    return tab
print(tab)
print(reverse(tab))