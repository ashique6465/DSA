def findFibonacci(n):
    if n <= 0:
        return []
    elif n ==1:
        return [1]
    fib = [0,1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# n = int(input("Enter the number: "))
print(findFibonacci(5))