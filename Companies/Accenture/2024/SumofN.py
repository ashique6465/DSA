def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5)+ 1):
        if n %i == 0:
            return False
    return True
def sumOfPrime(n):
    sum = 0
    for i in range(2,n):
        if isPrime(i):
            sum +=i
    return sum
        
     

n = 10
print(sumOfPrime(n))