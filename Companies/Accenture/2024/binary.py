def decimal_to_binary(num):
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary if binary else "0"
num = int(input("Enter the number: "))
print(decimal_to_binary(num))