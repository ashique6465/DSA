def ReplaceCharacter(str,char1,char2):
    if str is None:
        return None
    if char1 == char2 or char1 not in str and char2 not in str:
        return str
    s_list = list(str)
    for i in range(len(s_list)):
        if s_list[i] == char1:
            s_list[i] = char2
        elif s_list[i] == char2:
            s_list[i] = char1
    return "".join(s_list)
str = "apples"
char1 = 'a'
char2 = 'p'
print(ReplaceCharacter(str,char1,char2))


    