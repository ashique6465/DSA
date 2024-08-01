def DectoNBase(n,num):

    if n == 0:
        return "0"
    symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while num > 0:
        remainder = num % n 
        result.append(symbols[remainder])
        num //= n
    result.reverse()
    return ''.join(result)

num = 718
n = 12
print(DectoNBase(n,num))