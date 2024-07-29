def CheckPassword(str,n):
    if n  < 4:
        return 0
    if str[0].isdigit():
        return 0
    
    has_digit = False
    has_capital = False

    for char in str:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_capital = True
        if char == ' ' or char == "/":
            return 0
        
    if has_capital and has_digit:
        return 1
    else:
        return 0
password = input("Enter the password: ")
length = len(password)

result = CheckPassword(password,length)
if result:
    print("passwordd is valid")

else:
    print("password is invalid")