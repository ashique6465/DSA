def smallest_string(s):
    stack= []
    for char in s:
        if stack and stack[-1] == "1" and char =="0":
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)

s = "0000111111"
print(smallest_string(s))
