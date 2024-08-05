def CheckPassword(str):
    if len(str) < 4:
        return False
    if str[0].isdigit():
        return 0
    has_digit = False
    has_cap = False
    for char in str:
        if char.isdigti():
            has_digit = True
        if char.isupper():
            has_cap = True
        if char == " " or char == "/":
            return 0
    if has_cap and has_digit:
        return True
    else:
        return 0
str = input("Enter you pass")
print(CheckPassword(str))

