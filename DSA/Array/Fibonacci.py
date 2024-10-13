def Fib(n):
    if n == 0 or n == 1:
        return n 
    return Fib(n-1) + Fib(n-2)
print(Fib(5))