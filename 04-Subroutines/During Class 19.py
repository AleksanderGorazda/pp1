def function(n):
    if n==1:
        return 1
    if n > 1:
        suma = n + function(n-1)
        return suma
print("Suma pierwszych 500 liczb naturalnych ", function(500))
    