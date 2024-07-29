def OperationsBinaryString(str):
    if str is None or len(str) == 0:
        return -1

    
    result = int(str[0])
    
    for i in range(1,len(str), 2):
        operation = str[i]
        next_digit = int(str[i+1])
        if operation == "A":
            result = result & next_digit
        elif operation == "B":
            result = result | next_digit
        elif operation == "C":
            result = result ^ next_digit
    return result
print(OperationsBinaryString("1C0C1C1A0B1")) 
print(OperationsBinaryString("0C1A1B1C1C1B0A0"))