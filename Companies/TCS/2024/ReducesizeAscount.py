def reduceSize(s):
    if not s:
        return ""
    current_char = s[0]
    result = []
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1 
        else:
            result.append(current_char) 
            if count > 1:
                result.append(str(count))
            current_char = char
            count = 1
            
    result.append(current_char)
    if count > 1:
        result.append(str(count))
    return ''.join(result)
    
    
s = input("Enter the string to be reduce: ")
print(reduceSize(s))