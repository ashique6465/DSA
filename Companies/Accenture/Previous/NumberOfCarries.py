def NumberOfCarries(num1,num2):
    carry = 0
    carry_count = 0
    while num1 > 0 or num2 > 0 or carry > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        total = digit1 + digit2 + carry
        if total >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0

        num1 //= 10
        num2 //= 10
    return carry_count

num1 = 451
num2 = 349
print(NumberOfCarries(num1,num2))