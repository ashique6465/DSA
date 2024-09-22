def Max(a,b):
    def exponent_of(n):
        count = 0
        while n % 2 == 0:
            n //=2
            count +=1 
        return count
    max_count = 0
    max_n = a 
    for i in range(a,b+1):
        exponent_of_two = exponent_of(i)
        if exponent_of_two > max_count:
            max_count = exponent_of_two
            max_n = i 
        elif exponent_of_two == max_count:
            max_n = min(max_n,i)
            
    return max_n
    
a = int(input())
b = int(input())
print(Max(a,b))