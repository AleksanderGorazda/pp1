def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2) + fib(n-1)
for i in range(20):
    print(fib(i))