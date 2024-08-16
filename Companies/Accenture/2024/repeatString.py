def repeatString(n,s):
    if n == 1:
        return s
    else:
        return n * s

n = int(input("Enter the Integer: "))
s = input("Enter the string: ")
print(repeatString(n,s))