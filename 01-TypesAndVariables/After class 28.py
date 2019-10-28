from random import randrange
i=0
sum=0
while i <3:
    x = (randrange(6) + 1)
    print(x)
    i+=1
    sum = sum+x
print(sum)