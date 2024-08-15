def OperationChoices(c,a,b):
    if c == 1:
        return a + b
    elif c ==2:
        return a-b
    elif c == 3:
        return a * b
    elif c == 4:
        if b != 0:
            return a/b
        else:
            return "Error"

a = int(input("Enter the Value of a: "))
c = int(input("Enter the value of c: "))
b = int (input("Enter the value of b: "))
print(OperationChoices(c,a,b))


