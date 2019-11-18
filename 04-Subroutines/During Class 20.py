def function(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    if n > 1:
        power = x * function(x,n-1)
        return power
print("5 do potęgi 3 wynosi:",function(5,3))