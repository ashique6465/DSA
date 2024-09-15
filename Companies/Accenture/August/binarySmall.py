def BinarySmall(n):
    if n == 0:
        return False
    binary_digit = bin(n).count('1')
    result = (1 << binary_digit) - 1 
    return result
    
n = int(input())
print(BinarySmall(n))