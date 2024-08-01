def MaxExponents(a,b):
    def exponent_of_2(n):
        count = 0
        while n % 2 == 0 and n != 0:
            n //=2
            count +=1
        return count
    max_number = a
    max_exponent = exponent_of_2(a)
    for i in range(a+1,b+1):
        current_exponent = exponent_of_2(i)
        if current_exponent > max_exponent:
            max_exponent = current_exponent
            max_number = i
        elif current_exponent == max_exponent and i < max_number:
            max_number = i

    return max_number

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print(MaxExponents(a,b))

       