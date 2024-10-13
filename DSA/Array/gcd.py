def Gcd(a,b):
    while b!=0:
        a,b = b ,a % b
    return a
print(Gcd(10,15))
